# Decision Strategy Comparison Results

This page summarizes the held-out test-set performance of each diabetic retinopathy screening decision strategy.

Thresholds were selected on the calibration set and then evaluated on the test set. Because thresholds were calibration-tuned, actual test sensitivity may differ slightly from the target.

## 95% Sensitivity Target

| Method | Sensitivity % | Specificity % | AUC | Referrals | False Positives | Referral Rate % |
|---|---:|---:|---:|---:|---:|---:|
| ResNet50 | 94.9 | 14.9 | 0.746 | 4,618 | 3,321 | 87.6 |
| ViT-B/16 | 93.7 | 15.2 | 0.750 | 4,592 | 3,312 | 87.1 |
| Supervised Encoder | 94.1 | 17.5 | 0.748 | 4,506 | 3,220 | 85.5 |
| Majority Consensus | 95.9 | 12.6 | N/A | 4,723 | 3,413 | 89.6 |
| Weighted Ensemble | 94.7 | 16.2 | 0.768 | 4,565 | 3,272 | 86.6 |
| Stacking | 94.7 | 16.2 | 0.769 | 4,566 | 3,273 | 86.6 |
| Two-Stage Pipeline | 94.7 | 15.3 | 0.768 | 4,602 | 3,308 | 87.3 |

## 90% Sensitivity Target

| Method | Sensitivity % | Specificity % | AUC | Referrals | False Positives | Referral Rate % |
|---|---:|---:|---:|---:|---:|---:|
| ResNet50 | 89.3 | 29.2 | 0.746 | 3,983 | 2,763 | 75.6 |
| ViT-B/16 | 88.9 | 29.1 | 0.750 | 3,983 | 2,768 | 75.6 |
| Supervised Encoder | 89.2 | 30.9 | 0.748 | 3,915 | 2,696 | 74.3 |
| Majority Consensus | 91.3 | 26.8 | N/A | 4,105 | 2,858 | 77.9 |
| Weighted Ensemble | 88.4 | 35.1 | 0.768 | 3,742 | 2,534 | 71.0 |
| Stacking | 88.1 | 34.9 | 0.769 | 3,747 | 2,543 | 71.1 |
| Two-Stage Pipeline | 89.9 | 30.8 | 0.768 | 3,928 | 2,700 | 74.5 |

## Key Findings

At the 95% sensitivity target, the supervised encoder had the strongest single-model specificity and lowest false-positive count among individual models.

Majority consensus had the highest sensitivity, but it also produced the largest false-positive burden, showing that simple voting is not automatically better for clinical screening.

At the 90% sensitivity target, weighted ensemble and stacking strategies achieved the strongest specificity and lowest referral rates.

The main result is that the clinical operating point matters as much as the model architecture. Lowering the sensitivity target from 95% to 90% substantially reduced false positives, and combining a 90% target with an ensemble strategy reduced unnecessary referrals even further.

## Interpretation

This project shows that diabetic retinopathy AI should be evaluated as a deployment decision system, not just as a classifier. In clinical screening, threshold selection, calibration, and decision strategy directly affect how many patients are referred for follow-up.
