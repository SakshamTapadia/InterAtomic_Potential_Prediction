import pandas as pd
import numpy as np
from models.interatomic_nn import InteratomicPotentialNN
import torch
import matplotlib.pyplot as plt

df = pd.read_csv('data/dataset.csv')
print("Data Loaded Successfully")

x_test = torch.tensor(df.iloc[:,3:9].values, dtype=torch.float32)

input_dim = 6
model = InteratomicPotentialNN(input_dim)

model.load_state_dict(torch.load('results/model_weights.pth'))
print("Model Loaded Successfully")

predictions = model(x_test).detach().numpy()

print("Predictions Generated Successfully")

plt.figure(figsize=(10, 6))
plt.scatter(range(len(predictions)), predictions, color='blue', label='Predictions')
plt.xlabel('Sample Data')
plt.ylabel('Predicted Values')
plt.title('Interatomic Potential Predictions')
plt.legend()
plt.savefig('results/predictions_plot.png')
print("Predictions Plot Saved Successfully")