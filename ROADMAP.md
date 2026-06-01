# Project Roadmap

This roadmap outlines planned improvements for the diabetic retinopathy AI decision strategy repository.

## Current Status

The repository currently includes:

- Project overview and research framing
- Methodology documentation
- Decision strategy comparison results
- Result visualizations
- Starter source code structure
- Citation metadata

## Planned Improvements

### 1. Reproducible Training Pipeline

Add a complete training script for base models, including:

- Dataset loading
- Image preprocessing
- Train/calibration/test split
- Model checkpoint saving
- Training logs

### 2. Calibration and Thresholding Notebook

Add a notebook showing how thresholds are selected on the calibration set for fixed sensitivity targets.

This will include:

- Temperature scaling
- Calibration probability plots
- Sensitivity-specificity tradeoff analysis
- Threshold selection logic

### 3. Decision Strategy Evaluation Notebook

Add a notebook comparing:

- Single-model thresholding
- Majority consensus
- Weighted probability averaging
- Stacking
- Two-stage pipeline

### 4. Fairness and Subgroup Analysis

Add future evaluation across patient subgroups if demographic metadata is available.

Potential subgroup checks include:

- Age group
- Sex
- Image quality
- Disease severity distribution

### 5. Explainability Visualizations

Add explainability tools such as Grad-CAM to show which retinal regions influence model predictions.

### 6. Clinical Deployment Simulation

Extend the project from classification metrics to clinical workflow impact.

Possible additions include:

- Referral volume simulation
- Specialist capacity constraints
- False-positive burden analysis
- Cost-sensitive decision thresholds

## Long-Term Goal

The long-term goal is to make this repository a clear, reproducible research framework for evaluating healthcare AI systems under real clinical decision constraints.
