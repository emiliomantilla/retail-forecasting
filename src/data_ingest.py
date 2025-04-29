# src/data_ingest.py
import os
import subprocess
import pandas as pd
import glob

BASE_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, os.pardir, "data", "raw"))

def download_kaggle_dataset():
    """Use Kaggle CLI to pull the retail-store dataset."""
    os.makedirs(DATA_DIR, exist_ok=True)
    cmd = [
        "kaggle", "datasets", "download",
        "-d", "anirudhchauhan/retail-store-inventory-forecasting-dataset",
        "-p", DATA_DIR,
        "--unzip"
    ]
    subprocess.run(cmd, check=True)
    print("Dataset downloaded to", DATA_DIR)

def list_raw_csvs():
    """Print all CSV files in data/raw/ for you to choose from."""
    files = glob.glob(os.path.join(DATA_DIR, "*.csv"))
    print("Found these CSVs in data/raw/:")
    for f in files:
        print("   -", os.path.basename(f))
    return files

def load_sales(filename):
    """Load the chosen sales CSV into a DataFrame."""
    path = os.path.join(DATA_DIR, filename)
    # adjust parse_dates=[…] as needed once you see the column names
    df = pd.read_csv(path, parse_dates=["Date"])  
    return df

if __name__ == "__main__":
    download_kaggle_dataset()
    raw_files = list_raw_csvs()

    # pick one of these filenames from the printed list!
    chosen = raw_files[0].split(os.sep)[-1]
    print(f"\nLoading {chosen!r}…")
    df = load_sales(chosen)
    print("Loaded shape:", df.shape)
