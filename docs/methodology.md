# Methodology

## Overview

This project evaluates diabetic retinopathy screening models under realistic clinical deployment constraints. Instead of focusing only on model accuracy, the project studies how different AI decision strategies affect referral burden when sensitivity requirements are fixed.

The central goal is to determine which strategy can preserve patient safety while reducing unnecessary false-positive referrals.

## Clinical Screening Problem

Diabetic retinopathy screening is safety-sensitive because missed cases can delay treatment and increase the risk of preventable vision loss. For that reason, screening systems often prioritize high sensitivity.

However, increasing sensitivity usually lowers specificity, meaning more patients without referable disease may still be sent for follow-up. This creates unnecessary burden for clinics, specialists, and patients.

This project frames diabetic retinopathy AI as a clinical decision problem, not just an image classification problem.

## Dataset Setup

The project is designed for retinal fundus image classification using the EyePACS diabetic retinopathy dataset.

Original severity labels are converted into a binary screening task:

- `0`: No referable diabetic retinopathy
- `1`: Referable diabetic retinopathy

A patient-level split is used to reduce leakage between training, calibration, and test sets.

The recommended split structure is:

1. Training set for model learning
2. Calibration set for threshold selection and probability calibration
3. Test set for final held-out evaluation

## Model Training

The project supports multiple model families, including:

- ResNet50
- Vision Transformer
- Supervised convolutional encoder

Each model outputs a probability estimate for referable diabetic retinopathy.

Training uses standard deep learning procedures such as weighted cross-entropy, AdamW optimization, cosine learning rate scheduling, mixed precision, and early stopping.

## Probability Calibration

Raw neural network probabilities are often poorly calibrated. Because clinical thresholding depends on probability scores, calibration is important.

Temperature scaling is used to adjust model logits before converting them into probabilities. This helps make the predicted probabilities more reliable for downstream decision strategies.

## Threshold Selection

Thresholds are selected on the calibration set, not the test set.

For each target sensitivity, the system searches for the highest threshold that still meets the required sensitivity. This approach attempts to maximize specificity while preserving the clinical safety target.

The main sensitivity targets are:

- 95% sensitivity: high-safety operating point
- 90% sensitivity: balanced operating point

## Decision Strategies

### 1. Single-Model Thresholding

Each model is evaluated independently. A model predicts referable diabetic retinopathy if its probability exceeds a selected threshold.

### 2. Majority Consensus

Multiple models vote on the final classification. A case is classified as referable if at least two models predict positive.

### 3. Weighted Probability Averaging

Model probabilities are combined using weighted averaging. Stronger models can receive higher weights based on validation performance.

### 4. Stacking

A logistic regression meta-classifier combines model outputs and learns how to make final predictions from multiple base models.

### 5. Two-Stage Pipeline

A primary model first identifies possible referable cases. Then, secondary model agreement is used as a veto mechanism to reduce unnecessary referrals.

## Evaluation Metrics

The project focuses on clinically meaningful metrics:

- Sensitivity
- Specificity
- False positives
- False negatives
- AUC
- Referral burden

False positives are especially important because they represent patients who may be unnecessarily referred for specialist follow-up.

## Main Research Insight

The project shows that model architecture alone does not determine clinical usefulness. The decision strategy and operating threshold can strongly affect real-world outcomes.

A slightly different threshold or ensemble rule can change how many patients are referred, even when the underlying model performance is similar.

## Limitations

This repository is a research framework and should not be used as a medical device or clinical diagnostic system.

Important limitations include:

- Dataset-specific performance
- Potential demographic bias
- Need for external validation
- Need for prospective clinical testing
- Dependence on image quality and labeling consistency

## Future Work

Possible future improvements include:

- External validation on additional retinal imaging datasets
- Fairness analysis across demographic subgroups
- Image quality filtering before model prediction
- Explainability visualizations such as Grad-CAM
- Cost-sensitive referral optimization
- Deployment-focused evaluation under clinic capacity constraints
