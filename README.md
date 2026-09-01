\# 📱 Smartphone Price Prediction

<p align="center">

&#x20; <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python\&logoColor=white" alt="Python">

&#x20; <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas\&logoColor=white" alt="Pandas">

&#x20; <img src="https://img.shields.io/badge/Scikit--learn-Machine%20Learning-F7931E?logo=scikit-learn\&logoColor=white" alt="Scikit-learn">

&#x20; <img src="https://img.shields.io/badge/XGBoost-Regression-189AB4?logo=xgboost\&logoColor=white" alt="XGBoost">

</p>

<p align="center">

&#x20; <b>Machine Learning regression project for predicting smartphone prices from technical specifications.</b>

</p>

\---

\## 📌 Project Overview

This project develops a machine learning regression system to estimate smartphone prices using product specifications such as:

\- 📱 Brand

\- ⭐ Rating

\- 💾 RAM

\- 💽 Storage

\- 🔋 Battery capacity

\- 🖥️ Platform

The project follows an end-to-end machine learning workflow:

\*\*Data Exploration → Data Cleaning → Feature Engineering → Model Training → Model Evaluation → Model Comparison\*\*

\---

\## 🎯 Objective

The primary objective is to build a regression model capable of predicting smartphone prices from available technical specifications.

The project compares three regression algorithms:

1\. Linear Regression

2\. Random Forest

3\. XGBoost

\---

\## 📊 Dataset

The dataset contains \*\*32,000 smartphone listings\*\* with \*\*10 original columns\*\*.

\### Original Features

| Feature | Description |

|---|---|

| `platform` | Smartphone platform |

| `brand` | Smartphone manufacturer |

| `product\_name` | Product name |

| `category` | Product category |

| `price` | Target price in INR |

| `rating` | Product rating |

| `ram` | RAM specification |

| `storage` | Storage specification |

| `battery` | Battery capacity |

| `url` | Product listing URL |

\### Dataset Quality

\- Rows: \*\*32,000\*\*

\- Columns: \*\*10\*\*

\- Missing values: \*\*0\*\*

\- Duplicate rows: \*\*0\*\*

\---

\## 🔎 Exploratory Data Analysis

The analysis investigates:

\- Price distribution

\- Rating distribution

\- Smartphone listings by brand

\- Average price by brand

\- Average price by RAM

\- Average price by storage

\- Feature correlations

\- Price outliers

\- Repeated specifications with different prices

### 📊 EDA Visualizations

<table>
<tr>

<td width="50%">

#### 📊 EDA Overview

<img src="images/eda_overview.png" alt="EDA Overview" width="100%">

</td>

<td width="50%">

#### 🔥 Correlation Heatmap

<img src="images/correlation_heatmap.png" alt="Correlation Heatmap" width="100%">

</td>

</tr>
</table>

---

## 🤖 Model Analysis

### 📈 Model Comparison

<img src="images/model_comparison.png" alt="Model Comparison" width="850">

<table>
<tr>

<td width="50%">

#### 🌲 Random Forest

<img src="images/random_forest.png" alt="Random Forest Feature Importance" width="100%">

</td>

<td width="50%">

#### 🚀 XGBoost

<img src="images/xgboost.png" alt="XGBoost Feature Importance" width="100%">

</td>

</tr>

<tr>

<td width="50%">

#### 📉 Linear Regression

<img src="images/linear_regression.png" alt="Linear Regression Feature Importance" width="100%">

</td>

<td width="50%">

#### 🏷️ Brand Premiumness

<img src="images/brand_premiumness.png" alt="Brand Premiumness" width="100%">

</td>

</tr>
</table>
