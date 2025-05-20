# src/data_clean.py
import os
import pandas as pd
from data_ingest import download_kaggle_dataset, list_raw_csvs, load_sales

# where to write your cleaned data
BASE_DIR = os.path.dirname(__file__)
PROC_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir, "data", "processed"))
os.makedirs(PROC_DIR, exist_ok=True)

def clean_sales(filename=None):
    # 1) Download & pick file if needed
    download_kaggle_dataset()
    files = list_raw_csvs()  # e.g. ['retail_store_inventory.csv']
    if filename is None:
        filename = os.path.basename(files[0])
    print(f"Cleaning ⟶ {filename}")

    # 2) Load raw data
    df = load_sales(filename)  # assumes parse_dates in loader

    # 3) Transform percent & binary fields BEFORE dtype casts
    if "Discount" in df.columns:
        # convert percent values to decimals
        df["Discount"] = df["Discount"] / 100.0

    if "Holiday/Promotion" in df.columns:
        # keep as numeric 1/0 for modeling
        df["Holiday/Promotion"] = df["Holiday/Promotion"].astype(int)

    # 4) Sanity checks: no missing, drop duplicates
    assert df.isna().sum().sum() == 0, "Unexpected missing values!"
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        print(f"Dropping {dup_count} duplicate rows")
        df = df.drop_duplicates()

    # 5) Cast true categoricals
    cat_cols = [
        "Store ID", "Product ID", "Category", "Region",
        "Weather Condition", "Seasonality"
    ]
    for c in cat_cols:
        if c in df.columns:
            df[c] = df[c].astype("category")

    # 6) Convert numerics & filter negatives (except baseline)
    numeric_cols = [
        "Inventory Level", "Units Sold", "Units Ordered",
        "Demand Forecast", "Price", "Competitor Pricing",
        "Discount", "Holiday/Promotion"
    ]
    for c in numeric_cols:
        if c in df.columns:
            # only filter negatives on true sales/demand inputs
            if c not in ("Demand Forecast",) and (df[c] < 0).any():
                bad = (df[c] < 0).sum()
                print(f"Filtering out {bad} negative values in '{c}'")
                df = df[df[c] >= 0]
            # enforce numeric dtype
            df[c] = pd.to_numeric(df[c], errors="raise")

    # 7) Filter to complete years (2022 & 2023 only)
    if "Date" in df.columns:
        df = df[df["Date"].dt.year.isin([2022, 2023])]

    return df

if __name__ == "__main__":
    clean_df = clean_sales()
    out_path = os.path.join(PROC_DIR, "sales_clean.csv")
    clean_df.to_csv(out_path, index=False)
    print(f"Cleaned data written to {out_path}")