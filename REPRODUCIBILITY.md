# Reproducibility Guide

This document explains how the diabetic retinopathy decision strategy experiments are intended to be reproduced.

## 1. Environment Setup

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Recommended environment:

- Python 3.10+
- PyTorch
- torchvision
- scikit-learn
- pandas
- NumPy
- matplotlib

## 2. Dataset Preparation

This project is designed for retinal fundus image classification using an EyePACS-style dataset.

Expected structure:

```text
data/
  images/
    image_001.jpeg
    image_002.jpeg
    ...
  labels.csv
```

The CSV file should include:

```text
image,label,patient_id
```

Where:

- `image` is the image filename
- `label` is the diabetic retinopathy label
- `patient_id` is used for patient-level splitting

## 3. Binary Label Conversion

The original diabetic retinopathy severity labels are converted into a binary screening task:

| Original Label | Binary Label | Meaning |
|---|---:|---|
| 0 | 0 | No referable diabetic retinopathy |
| 1–4 | 1 | Referable diabetic retinopathy |

## 4. Patient-Level Splitting

To avoid leakage, images from the same patient should not appear in multiple splits.

Recommended split:

- Training set
- Calibration set
- Test set

The calibration set is used for threshold selection and probability calibration. The test set is only used for final evaluation.

## 5. Model Training

Train each base model separately:

- ResNet50
- ViT-B/16
- Supervised convolutional encoder

Each model should output a probability score for referable diabetic retinopathy.

## 6. Probability Calibration

Apply temperature scaling to model logits before threshold selection.

Calibration helps make probability scores more reliable for clinical decision strategies.

## 7. Threshold Selection

Thresholds are selected on the calibration set.

For each sensitivity target, select the highest threshold that still meets the required sensitivity.

Main targets:

- 95% sensitivity
- 90% sensitivity

## 8. Decision Strategy Evaluation

Evaluate each strategy on the held-out test set:

- Single-model thresholding
- Majority consensus
- Weighted probability averaging
- Stacking
- Two-stage pipeline

## 9. Metrics

Report clinically meaningful metrics:

- Sensitivity
- Specificity
- AUC
- Referrals
- False positives
- Referral rate

## 10. Important Note

This repository is intended for research and educational use only. It is not a clinical diagnostic system or medical device.
