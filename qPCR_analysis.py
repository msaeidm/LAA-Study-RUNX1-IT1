import pandas as pd
import numpy as np

# Load qPCR data
data = pd.read_csv("data/clinical_data.csv")

# Calculate fold change (2^-ΔΔCt)
data['fold_change'] = 2 ** -(data['ΔCt_LAA'] - data['ΔCt_control'])

# Save results
data.to_csv("results/qPCR_results.csv")
