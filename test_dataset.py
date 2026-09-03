import pandas as pd

df = pd.read_csv(
    "datasets/aiops_logs/processed_events_analysis.csv"
)

print(df.head())