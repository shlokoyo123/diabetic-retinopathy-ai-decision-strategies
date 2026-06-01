# Project Summary

## Title

Beyond the Model: Evaluating AI Decision Strategies for Diabetic Retinopathy Screening Under Clinical Constraints

## Research Question

How do different AI decision strategies affect false positive burden when diabetic retinopathy screening systems are required to maintain fixed clinical sensitivity targets?

## Why This Matters

In clinical screening, missing disease can be dangerous, so AI systems are often tuned for high sensitivity. However, high sensitivity can increase false positives and unnecessary referrals. This project studies how decision strategies can reduce that burden while preserving patient safety.

## Strategies Compared

1. Single-model thresholding
2. Majority consensus voting
3. Weighted probability averaging
4. Stacking with a logistic regression meta-classifier
5. Two-stage pipeline with agreement-based veto

## Main Takeaway

The project shows that deployment strategy matters. A model with a strong AUC may still perform poorly clinically if the thresholding or referral strategy is not tuned to the real safety constraint.
