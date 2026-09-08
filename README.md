# ApexPlanet Task 4 — Advanced Data Analytics

## 📌 Project Overview

This project is completed as part of the **ApexPlanet Data Analytics Internship – Task 4**.

The objective of this task is to perform advanced data analysis on a retail **Superstore Sales Dataset** using Python. The project covers descriptive statistics, hypothesis testing, confidence intervals, time-series analysis, customer segmentation, and predictive modeling.

The dataset contains **10,194 records and 21 columns**, including customer details, order information, product categories, sales, quantity, discount, and profit.

---

## 🎯 Objectives

The main objectives of this project are:

* Perform descriptive statistical analysis.
* Calculate mean, median, mode, standard deviation, variance, and skewness.
* Perform hypothesis testing using T-Test.
* Perform Chi-Square testing between categorical variables.
* Calculate 95% confidence intervals.
* Analyze sales trends over time.
* Perform simple moving-average analysis.
* Decompose the time series into trend, seasonality, and residuals.
* Segment customers using K-Means clustering.
* Determine the optimal number of clusters using the Elbow Method.
* Visualize clusters using PCA.
* Profile and interpret customer segments.
* Build a predictive model for Profit.
* Evaluate the model using R², MAE, and RMSE.
* Identify the top 3 important features.
* Generate business insights and recommendations.

---

## 📊 Dataset

The project uses a Superstore retail sales dataset.

### Dataset Dimensions

```text
Rows:       10,194
Columns:       21
```

### Columns

```text
Row ID
Order ID
Order Date
Ship Date
Ship Mode
Customer ID
Customer Name
Segment
Country/Region
City
State/Province
Postal Code
Region
Product ID
Category
Sub-Category
Product Name
Sales
Quantity
Discount
Profit
```

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Statsmodels
* Scikit-learn
* Jupyter Notebook

---

# 🔎 Task 1 — Data Understanding & Preparation

The dataset was first loaded and examined using Pandas.

The following activities were performed:

* Dataset shape inspection
* Column identification
* Data type analysis
* Missing-value checking
* Duplicate-value checking
* Date conversion
* Feature creation

The `Order Date` and `Ship Date` columns were converted from strings into datetime format.

A new feature called `Shipping Days` was created:

```text
Shipping Days = Ship Date - Order Date
```

---

# 📈 Task 2 — Descriptive Statistical Analysis

Descriptive statistics were calculated for:

```text
Sales
Quantity
Discount
Profit
Shipping Days
```

The following statistical measures were calculated:

* Mean
* Median
* Mode
* Standard Deviation
* Variance
* Minimum
* Maximum
* Skewness

Visualizations such as histograms and boxplots were also created to understand the distribution of the numerical variables.

---

# 🧪 Task 3 — Hypothesis Testing

## Independent T-Test

An independent T-Test was performed to compare the profit of:

```text
Consumer
vs
Corporate
```

### Hypotheses

**H₀:** There is no significant difference in the mean profit between Consumer and Corporate customers.

**H₁:** There is a significant difference in the mean profit between Consumer and Corporate customers.

A significance level of:

```text
α = 0.05
```

was used.

The resulting p-value was compared with 0.05 to make the statistical decision.

---

## Chi-Square Test

A Chi-Square test was performed between:

```text
Category
and
Region
```

The purpose was to determine whether product category and geographical region are statistically associated.

A contingency table was created using:

```python
pd.crosstab()
```

### Hypotheses

**H₀:** Category and Region are independent.

**H₁:** Category and Region are significantly associated.

---

# 📐 Task 4 — Confidence Intervals

95% confidence intervals were calculated for:

* Sales
* Profit
* Quantity

The confidence intervals provide an estimated range for the population mean based on the sample data.

---

# 📅 Task 5 — Time Series Analysis

The `Order Date` column was used for time-series analysis.

Monthly sales were calculated by aggregating sales based on the order date.

### Analysis Performed

* Monthly sales trend
* 3-month moving average
* Trend analysis
* Seasonal analysis
* Residual analysis

---

## 📊 Monthly Sales

A line chart was created to visualize monthly sales over time.

This helps identify:

* Increasing or decreasing sales trends
* High-sales periods
* Low-sales periods
* Possible seasonal patterns

---

## 📉 Simple Moving Average

A **3-month moving average** was calculated to smooth short-term fluctuations in monthly sales.

The moving average makes the underlying sales trend easier to understand.

---

## 🔬 Time Series Decomposition

The monthly sales series was decomposed into:

```text
Observed
Trend
Seasonal
Residual
```

An additive decomposition model was used with a 12-month period.

This helps understand long-term trends, recurring seasonal patterns, and unexplained fluctuations.

---

# 👥 Task 6 — Customer Segmentation

Customer segmentation was performed using **K-Means clustering**.

Customer-level information was aggregated using:

```text
Customer ID
```

The following features were used:

```text
Total Sales
Total Quantity
Average Discount
Total Profit
Number of Orders
```

These features were standardized using:

```python
StandardScaler()
```

---

# 📉 Elbow Method

The Elbow Method was used to determine a suitable number of customer clusters.

K-Means models were evaluated for:

```text
K = 2 to 10
```

The inertia values were plotted to identify the elbow point.

---

# 🤖 K-Means Clustering

K-Means clustering was applied to divide customers into groups with similar purchasing behavior.

Each customer was assigned to a cluster.

The resulting customer segments were then analyzed based on their:

* Sales
* Quantity
* Discount
* Profit
* Number of Orders

---

# 🧩 PCA Visualization

Principal Component Analysis (PCA) was used to reduce the customer segmentation features to two dimensions.

The first two principal components were plotted to visualize the customer clusters.

This provides a clear visual representation of the customer segments.

---

# 📋 Cluster Profiling

Each cluster was profiled using average values of:

```text
Sales
Quantity
Discount
Profit
Number of Orders
```

Based on these values, clusters can be interpreted as different types of customers, such as:

* High-value customers
* Low-value customers
* Frequent customers
* Discount-oriented customers
* Highly profitable customers

The actual cluster interpretation is based on the calculated cluster profiles.

---

# 🤖 Task 7 — Predictive Modeling

A **Linear Regression** model was developed to predict:

```text
Profit
```

### Features Used

Numerical features:

```text
Sales
Quantity
Discount
Shipping Days
```

Categorical features:

```text
Ship Mode
Segment
Region
Category
Sub-Category
```

Categorical variables were encoded using One-Hot Encoding.

Numerical features were scaled using StandardScaler.

---

# ✂️ Train-Test Split

The dataset was divided into:

```text
80% → Training Data
20% → Testing Data
```

A random state of 42 was used to ensure reproducibility.

---

# 📊 Model Evaluation

The Linear Regression model was evaluated using:

### R² Score

Measures how much variation in the target variable is explained by the model.

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted profit.

### RMSE

Root Mean Squared Error measures prediction error while giving more weight to larger errors.

---

# ⭐ Feature Importance

The regression coefficients were analyzed to identify the most influential features.

The **Top 3 Important Features** were selected based on the absolute magnitude of their coefficients.

The final feature importance results are stored in:

```text
outputs/feature_importance.csv
```

---

# 📁 Project Structure

```text
ApexPlanet-Task4/
│
├── data/
│   └── superstore.csv
│
├── notebooks/
│   └── ApexPlanet_Task4.ipynb
│
├── outputs/
│   ├── descriptive_statistics.csv
│   ├── confidence_intervals.csv
│   ├── customer_segments.csv
│   ├── cluster_profile.csv
│   ├── model_metrics.csv
│   ├── feature_importance.csv
│   ├── elbow_method.png
│   ├── customer_segments_pca.png
│   ├── monthly_sales.png
│   ├── time_series_decomposition.png
│   ├── moving_average_forecast.png
│   ├── actual_vs_predicted.png
│   └── feature_importance.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# ▶️ How to Run the Project

## 1. Clone the Repository

```bash
git clone <your-repository-url>
```

## 2. Navigate to the Project

```bash
cd ApexPlanet-Task4
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Start Jupyter Notebook

```bash
jupyter notebook
```

## 5. Open the Notebook

Open:

```text
notebooks/ApexPlanet_Task4.ipynb
```

Run the cells from top to bottom.

---

# 📦 Python Libraries

```text
pandas
numpy
matplotlib
seaborn
scipy
scikit-learn
statsmodels
jupyter
openpyxl
```

---

# 💡 Key Business Insights

The analysis provides several useful business insights:

* Sales trends can help identify high-performing and low-performing periods.
* Seasonal patterns can support inventory and marketing planning.
* Customer segmentation helps identify different customer groups based on purchasing behavior.
* High-value customers can be targeted with loyalty programs.
* Customers with high discounts but low profitability should be evaluated carefully.
* Profit analysis can help optimize pricing and discount strategies.
* Regional and category analysis can support better product distribution.
* Predictive modeling can help identify factors associated with profitability.

---

# 🎯 Conclusion

This project demonstrates an end-to-end advanced analytics workflow using a retail sales dataset.

The analysis combines:

```text
Statistical Analysis
        ↓
Hypothesis Testing
        ↓
Confidence Intervals
        ↓
Time Series Analysis
        ↓
Customer Segmentation
        ↓
K-Means Clustering
        ↓
PCA
        ↓
Predictive Modeling
        ↓
Business Insights
```

The project provides practical experience in applying Python-based statistical analysis, machine learning, visualization, and business analytics to a real-world retail dataset.

---

## 👨‍💻 Author

**Sriram**

### ApexPlanet Internship — Task 4

```text
Advanced Data Analytics & Statistical Modeling
```
