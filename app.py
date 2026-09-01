import streamlit as st
import pandas as pd
import numpy as np
import joblib
from pathlib import Path

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(page_title="Mobile Price Prediction", page_icon="📱", layout="wide")


# ============================================================
# PATHS
# ============================================================

PROJECT_DIR = Path(__file__).resolve().parent
ARTIFACTS_DIR = PROJECT_DIR / "artifacts"


# ============================================================
# LOAD ARTIFACTS
# ============================================================


@st.cache_resource
def load_artifacts():

    X_train = joblib.load(ARTIFACTS_DIR / "X_train.pkl")

    scaler = joblib.load(ARTIFACTS_DIR / "scaler.pkl")

    encoders = joblib.load(ARTIFACTS_DIR / "encoders.pkl")

    lin_model = joblib.load(ARTIFACTS_DIR / "lin_model.pkl")

    rf_model = joblib.load(ARTIFACTS_DIR / "rf_model.pkl")

    xgb_model = joblib.load(ARTIFACTS_DIR / "xgb_model.pkl")

    comparison = pd.read_csv(ARTIFACTS_DIR / "model_comparison.csv")

    return (X_train, scaler, encoders, lin_model, rf_model, xgb_model, comparison)


X_train, scaler, encoders, lin_model, rf_model, xgb_model, comparison = load_artifacts()


# ============================================================
# SELECT BEST MODEL
# ============================================================

best_model_name = comparison.sort_values("R2 Score", ascending=False).iloc[0]["Model"]


if best_model_name == "Linear Regression":

    best_model = lin_model

else:

    best_model = {"Random Forest": rf_model, "XGBoost": xgb_model}[best_model_name]


# ============================================================
# FEATURE ENGINEERING
# Same logic as training notebook
# ============================================================


def recompute_features(X):

    X = X.copy()

    X["total_memory"] = X["ram"] + X["storage"]

    X["ram_storage"] = X["ram"] * X["storage"]

    X["battery_per_ram"] = X["battery"] / X["ram"]

    X["storage_per_ram"] = X["storage"] / X["ram"]

    X["rating_ram"] = X["rating"] * X["ram"]

    X["rating_storage"] = X["rating"] * X["storage"]

    X["rating_battery"] = X["rating"] * X["battery"]

    return X


# ============================================================
# ENCODING
# ============================================================


def encode_input(df):

    df = df.copy()

    for column, encoder in encoders.items():

        if column in df.columns:

            df[column] = encoder.transform(df[column])

    return df


# ============================================================
# HEADER
# ============================================================

st.title("📱 Mobile Price Prediction")

st.caption("Enter smartphone specifications to estimate its price.")

st.divider()


# ============================================================
# INPUT FEATURES
# ============================================================

ENGINEERED_FEATURES = [
    "total_memory",
    "ram_storage",
    "battery_per_ram",
    "storage_per_ram",
    "rating_ram",
    "rating_storage",
    "rating_battery",
]


input_features = [col for col in X_train.columns if col not in ENGINEERED_FEATURES]


categorical_features = [col for col in input_features if col in encoders]


numeric_features = [col for col in input_features if col not in categorical_features]


user_input = {}


# ============================================================
# COMPACT INPUT FORM
# ============================================================

st.subheader("📋 Smartphone Specifications")

# Six columns for a single-row layout
cols = st.columns(6)


# ------------------------------------------------------------
# CATEGORICAL FEATURES
# ------------------------------------------------------------

column_index = 0

for feature in categorical_features:

    if column_index >= 6:
        break

    with cols[column_index]:

        encoder = encoders[feature]

        options = list(encoder.classes_)

        user_input[feature] = st.selectbox(feature.replace("_", " ").title(), options)

    column_index += 1


# ------------------------------------------------------------
# RATING
# ------------------------------------------------------------

if "rating" in numeric_features:

    with cols[column_index]:

        user_input["rating"] = st.number_input(
            "Rating ⭐",
            min_value=0.0,
            max_value=5.0,
            value=4.5,
            step=0.1,
            format="%.1f",
            help="Rating between 0 and 5.",
        )

    column_index += 1


# ------------------------------------------------------------
# RAM
# ------------------------------------------------------------

if "ram" in numeric_features:

    with cols[column_index]:

        user_input["ram"] = st.selectbox(
            "RAM 💾",
            options=[2, 4, 8, 12, 16, 32],
            index=2,
            format_func=lambda x: f"{x} GB",
            help="Select RAM capacity.",
        )

    column_index += 1


# ------------------------------------------------------------
# STORAGE
# ------------------------------------------------------------

if "storage" in numeric_features:

    with cols[column_index]:

        storage_options = {
            "64 GB": 64,
            "128 GB": 128,
            "256 GB": 256,
            "512 GB": 512,
            "1 TB": 1024,
        }

        selected_storage = st.selectbox(
            "Storage 💽",
            options=list(storage_options.keys()),
            index=2,
            help="1 TB is passed to the model as 1024 GB.",
        )

        user_input["storage"] = storage_options[selected_storage]

    column_index += 1


# ------------------------------------------------------------
# BATTERY
# ------------------------------------------------------------

if "battery" in numeric_features:

    with cols[column_index]:

        user_input["battery"] = st.number_input(
            "Battery 🔋",
            min_value=300,
            max_value=10000,
            value=5000,
            step=100,
            format="%d",
            help="Battery capacity from 300 to 10,000 mAh.",
        )

    column_index += 1


st.divider()


# ============================================================
# PREDICTION BUTTON
# ============================================================

if st.button("🔮 Predict Mobile Price", type="primary", use_container_width=True):

    try:

        # ----------------------------------------------------
        # Create dataframe
        # ----------------------------------------------------

        input_df = pd.DataFrame([user_input])

        # ----------------------------------------------------
        # Encode categorical variables
        # ----------------------------------------------------

        input_df = encode_input(input_df)

        # ----------------------------------------------------
        # Recompute engineered features
        # ----------------------------------------------------

        input_df = recompute_features(input_df)

        # ----------------------------------------------------
        # Match training feature order
        # ----------------------------------------------------

        input_df = input_df[X_train.columns]

        # ----------------------------------------------------
        # Prediction
        # ----------------------------------------------------

        if best_model_name == "Linear Regression":

            input_scaled = scaler.transform(input_df)

            prediction = best_model.predict(input_scaled)[0]

        else:

            prediction = best_model.predict(input_df)[0]

        # ----------------------------------------------------
        # Prevent negative price
        # ----------------------------------------------------

        prediction = max(0, prediction)

        # ====================================================
        # RESULT
        # ====================================================

        st.success("Prediction completed!")

        result_col1, result_col2 = st.columns([2, 1])

        with result_col1:

            st.subheader("🎯 Estimated Mobile Price")

            st.markdown(f"# ₹{prediction:,.0f}")

        with result_col2:

            st.subheader("🤖 Model")

            st.markdown(f"### {best_model_name}")

            # Show R²
            best_r2 = comparison[comparison["Model"] == best_model_name][
                "R2 Score"
            ].iloc[0]

            st.caption(f"R² Score: {best_r2:.4f}")

        # ====================================================
        # SELECTED SPECIFICATIONS
        # ====================================================

        st.subheader("📱 Selected Specifications")

        spec_cols = st.columns(6)

        # ----------------------------------------------------
        # Platform
        # ----------------------------------------------------

        if "platform" in user_input:

            with spec_cols[0]:

                st.metric("Platform", user_input["platform"])

        # ----------------------------------------------------
        # Brand
        # ----------------------------------------------------

        if "brand" in user_input:

            with spec_cols[1]:

                st.metric("Brand", user_input["brand"])

        # ----------------------------------------------------
        # Rating
        # ----------------------------------------------------

        if "rating" in user_input:

            with spec_cols[2]:

                st.metric("⭐ Rating", f"{user_input['rating']:.1f} / 5")

        # ----------------------------------------------------
        # RAM
        # ----------------------------------------------------

        if "ram" in user_input:

            with spec_cols[3]:

                st.metric("💾 RAM", f"{user_input['ram']} GB")

        # ----------------------------------------------------
        # Storage
        # ----------------------------------------------------

        if "storage" in user_input:

            with spec_cols[4]:

                storage_value = user_input["storage"]

                if storage_value == 1024:

                    storage_display = "1 TB"

                else:

                    storage_display = f"{storage_value} GB"

                st.metric("💽 Storage", storage_display)

        # ----------------------------------------------------
        # Battery
        # ----------------------------------------------------

        if "battery" in user_input:

            with spec_cols[5]:

                st.metric("🔋 Battery", f"{user_input['battery']:,} mAh")

    except Exception as e:

        st.error(f"Prediction failed: {e}")

        st.info(
            "Please check that the input values "
            "and encoders match the preprocessing "
            "used during training."
        )


# ============================================================
# MODEL INFORMATION
# ============================================================

with st.expander("📊 Model Information"):

    st.write(
        "The best-performing model is selected " "automatically using the R² score."
    )

    st.dataframe(comparison, use_container_width=True)
