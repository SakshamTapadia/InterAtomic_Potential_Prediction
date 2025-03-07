# InterAtomic Potential Prediction

This repository contains code and resources for predicting interatomic potentials using machine learning techniques. The project focuses on developing and training neural network models to estimate atomic interactions based on input data.

## Table of Contents

- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Models](#models)
- [Results](#results)
- [Utilities](#utilities)
- [License](#license)

## Directory Structure

```
INTERATOMIC_POTENTIAL_PREDICTION/
├── data/
│   └── dataset.csv
├── models/
│   ├── __pycache__/
│   ├── interatomic_nn.py
│   └── train.py
├── results/
│   ├── model_weights.pth
│   └── predictions_plot.png
└── utils/
    ├── feature_extraction.py
    ├── main.py
    ├── requirements.txt
    └── run_ase.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SakshamTapadia/InterAtomic_Potential_Prediction.git
   ```
2. Navigate into the directory:
   ```bash
   cd InterAtomic_Potential_Prediction
   ```
3. Install the required packages:
   ```bash
   pip install -r utils/requirements.txt
   ```

## Usage

- The main entry point of the application is `main.py`. You can run the script as follows:
   ```bash
   python utils/main.py
   ```

## Data

- The dataset for training and testing the models is located in the `data` directory, specifically in the `dataset.csv` file.
- The dataset contains the features and labels required for training the interatomic potential prediction models.

## Models

- The `models` directory contains the implementation of the neural network model and training scripts:
  - `interatomic_nn.py`: Defines the neural network architecture.
  - `train.py`: Contains the training loop and model evaluation procedures.

## Results

- The trained model weights are saved in `model_weights.pth` located in the `results` directory.
- `predictions_plot.png`: A visual representation of the model's predictions compared to the ground truth.

## Utilities

- The `utils` directory includes helper functions for feature extraction and running the models:
  - `feature_extraction.py`: Functions for preparing input data.
  - `run_ase.py`: Interfaces with the Atomic Simulation Environment (ASE).
  - `requirements.txt`: Lists dependencies that need to be installed.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
