from stellar import linearRegression
import pandas as pd 

dataset = pd.read_csv("Summary of Weather.csv",low_memory=False)

linearRegression(dataset["MaxTemp"], dataset["MinTemp"])
