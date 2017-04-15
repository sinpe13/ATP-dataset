import pandas as pd

df = pd.read_csv('ATP.csv')

df.to_csv('ATP_processed.csv')