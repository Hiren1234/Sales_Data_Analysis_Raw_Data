# Sales Data Analysis Project

## Project Overview

This project is a complete end-to-end Sales Data Analysis pipeline developed using Python, Pandas, MySQL, and data visualization libraries.

The project demonstrates:
- Data Cleaning
- Data Transformation
- KPI Analysis
- Revenue & Growth Analysis
- Visualization
- CSV Export
- MySQL Migration
- Automated Reporting

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- MySQL
- SQLAlchemy
- PyMySQL
- Jupyter Notebook
- PyCharm

---

# Project Workflow

```text
CSV / MySQL
      ↓
Data Loading
      ↓
Data Cleaning
      ↓
Data Transformation
      ↓
KPI Analysis
      ↓
Visualization
      ↓
Report Generation
      ↓
MySQL Upload
```

---

# Project Structure

```text
Sales_Data_Analysis/
│
├── data/
│   └── Sales.csv
│
├── notebooks/
│   └── sales_analysis.ipynb
│
├── outputs/
│   ├── charts/
│   └── reports/
│
├── scripts/
│   ├── data_loading.py
│   ├── data_cleaning.py
│   ├── transformation.py
│   ├── analysis.py
│   ├── visualization.py
│   ├── mysql_upload.py
│   └── report_generator.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

# Features

## Data Cleaning
- Remove duplicates
- Handle missing values
- Convert date formats

## Data Transformation
- Month extraction
- Year extraction
- Revenue calculation
- Profit Margin %

## KPI Analysis
- Total Sales
- Total Profit
- Total Revenue
- Monthly Growth %
- Region-wise Sales
- Month-wise sales

## Visualization
- Month-wise Revenue Chart
- Year-wise Revenue Chart
- Growth Trend Chart
- Profit Margin Chart

## Database Integration
- CSV to MySQL migration
- Automated table creation

---

# Business KPIs

## Revenue Formula

Revenue = Sales × Quantity

## Profit Margin Formula

Profit Margin % = (Profit / Sales) × 100

## Growth Formula

Growth % = ((Current - Previous) / Previous) × 100

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Sales_Data_Analysis.git
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main.py
```

---

# Output

The project generates:
- Processed CSV reports
- PNG charts
- Word reports
- MySQL tables

---

# Future Improvements

- Power BI Dashboard
- Streamlit Web App
- Machine Learning Forecasting
- Automated ETL Pipeline
- Cloud Deployment

---

# Author

Hiren Patel

---

# License

This project is developed for learning and portfolio purposes.
