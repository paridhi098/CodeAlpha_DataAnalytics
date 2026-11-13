import numpy as np
import pandas as pd
import seaborn as sns


def perform_eda():
  print("--- Loading Dataset ---")
  df = sns.load_dataset("titanic")

  print("\n--- 1. Data Structure & Data Types ---")
  print(df.info())

  print("\n--- 2. First 5 Rows ---")
  print(df.head())

  print("\n--- 3. Summary Statistics ---")
  print(df.describe(include="all"))

  print("\n--- 4. Missing Values Check ---")
  print(df.isnull().sum())

  print("\n--- 5. Correlation Matrix (Numerical Features) ---")
  numeric_df = df.select_dtypes(include=[np.number])
  print(numeric_df.corr())


if __name__ == "__main__":
  perform_eda()