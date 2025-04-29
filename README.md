# Retail Forecasting & Inventory Optimization

This repository provides an end-to-end pipeline to forecast SKU-level demand for a retail store dataset, then compute optimal \((Q, R)\) inventory policies to balance stock-outs and holding costs.

## 📁 Repository Structure

retail-forecasting/ 
├── data/ 
│ ├── raw/ # original Kaggle CSVs 
│ └── processed/ # cleaned & feature-engineered tables 
├── notebooks/ 
│ ├── 00_Profiling_Raw_Data.ipynb
│ ├── 01_EDA.ipynb
│ ├── 02_Modeling.ipynb
│ └── 03_Evaluation.ipynb
├── src/ 
│ ├── data_ingest.py
│ ├── data_clean.py
│ ├── features.py
│ ├── models.py
│ └── optimize.py
├── reports/ 
│ └── figures/ # output plots 
├── requirements.txt
├── README.md
└── LICENSE


## 🚀 Getting Started

1. **Clone & enter**  
   git clone git@github.com:YOUR_USERNAME/retail-forecasting.git
   cd retail-forecasting

### Create & activate virtual environment

python3 -m venv .venv
source .venv/bin/activate    # (macOS/Linux)

### Install dependencies

pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

## 🛠️ Pipeline Overview
1. Data Ingestion
- Download and unzip the Kaggle dataset into data/raw/.
- Load CSVs with src/data_ingest.py.

2. Raw Data Profiling
- Open notebooks/00_Profiling_Raw_Data.ipynb.
- Generate HTML reports with YData Profiling.
- Record missing-value patterns, duplicates, outliers, etc.

3. Targeted Data Cleaning
- Run python src/data_clean.py to apply cleaning steps informed by profiling.
- Outputs go to data/processed/.

4. Exploratory Data Analysis
- Open notebooks/01_EDA.ipynb.
- Visualize distributions, trends, seasonality, and correlations.

5. Feature Engineering
- Generate calendar, lag, rolling, and encoding features via src/features.py.
- Saves a “model ready” table in data/processed/features.csv.

6. Forecasting Models
- Open notebooks/02_Modeling.ipynb.
- Use wrappers in src/models.py for Naïve, SARIMA, ETS, Prophet, and LSTM/TCN.
- Produce out-of-sample forecasts.

7. Backtesting & Evaluation
- Open notebooks/03_Evaluation.ipynb.
- Perform rolling-window CV and compute MAPE, RMSE, MAE, plus service-level metrics.
- Compare model performance and visualize results.

8. Replenishment Optimization
- Run python src/optimize.py.
- Define (𝑄,𝑅) policy parameters (lead time, costs, service level).
- Simulate inventory over the test period and output cost vs. service-level curves.

9. Reporting & Visualization
- Figures (forecast vs. actual, cost curves) in reports/figures/.
- Summarize findings in this README and in notebook markdown cells.


## 📋 Usage Examples
- Profile raw data
jupyter notebook notebooks/00_Profiling_Raw_Data.ipynb

- Clean data
python src/data_clean.py

- Explore data
jupyter notebook notebooks/01_EDA.ipynb

- Model forecasting
jupyter notebook notebooks/02_Modeling.ipynb

- Evaluate and optimize
jupyter notebook notebooks/03_Evaluation.ipynb
python src/optimize.py

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for details.