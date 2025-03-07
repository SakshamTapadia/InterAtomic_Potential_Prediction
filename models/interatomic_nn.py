import torch
import torch.nn as nn

class InteratomicPotentialNN(nn.Module): 
    def __init__(self, input_dim):   #Initializes entire model on its own
        super(InteratomicPotentialNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 1)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))  #ReLU activation function - Rectified Linear Unit
        x = torch.relu(self.fc2(x))
        return self.fc3(x)
    
