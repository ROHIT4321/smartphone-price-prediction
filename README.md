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



\### Example EDA Visualizations



Add your generated plots to an `images/` folder and display them here:



```text

images/

├── eda\_overview.png

├── correlation\_heatmap.png

├── price\_distribution.png

└── model\_comparison.png

