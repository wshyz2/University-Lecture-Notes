#Physics-Informed GAN for Anomaly Detection in Structural Health Monitoring of Dams

This repository contains a script for detecting anomalies in structural health monitoring (SHM) of dams using a combination of Generative Adversarial Networks (GANs) and Physics-Informed Neural Networks (PINNs). The aim is to generate realistic acoustic anomalies for detecting potential issues in dams.

#Key Components
1. CUDA Setup: Ensures the script runs efficiently on a GPU if available.
2. mseed Data Processing: 
   -Loads mseed files containing seismic/acoustic data.
   -Segments the data into 1-second intervals.
   -Extracts features using Hjorth parameters (activity, mobility, complexity).
3. Autoencoder: 
   -Trains autoencoders to reconstruct normal seismic data.
   -Detects anomalies based on reconstruction error.
4. GAN + PINN: 
   -Generates synthetic seismic anomalies using GANs.
   -PINN enforces physical constraints (acceleration-displacement relation).
5. CUSUM: 
   -Applies the Cumulative Sum (CUSUM) algorithm for anomaly detection.
6. Fuzzy Logic: 
   -Classifies health status of the dam based on detected anomalies.

Requirements

- Python 3.x
- PyTorch
- ObsPy
- NumPy
- SciKit-Learn
- Matplotlib

#Setup

1. Install the required libraries:
   bash
   pip install obspy numpy scipy scikit-learn matplotlib torch tqdm
