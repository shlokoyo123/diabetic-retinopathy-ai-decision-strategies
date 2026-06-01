import numpy as np
from sklearn.metrics import roc_auc_score, confusion_matrix


def evaluate_binary_predictions(y_true: np.ndarray, y_pred: np.ndarray) -> dict:
    """Compute screening-focused binary classification metrics."""
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    sensitivity = tp / (tp + fn) if (tp + fn) else 0.0
    specificity = tn / (tn + fp) if (tn + fp) else 0.0

    return {
        "true_positives": int(tp),
        "true_negatives": int(tn),
        "false_positives": int(fp),
        "false_negatives": int(fn),
        "sensitivity": sensitivity,
        "specificity": specificity,
    }


def evaluate_probabilities(y_true: np.ndarray, probabilities: np.ndarray) -> dict:
    """Compute probability-based metrics."""
    return {
        "auc": roc_auc_score(y_true, probabilities)
    }


def find_threshold_for_sensitivity(
    y_true: np.ndarray,
    probabilities: np.ndarray,
    target_sensitivity: float,
) -> float:
    """Find the highest threshold that still meets the target sensitivity."""
    thresholds = np.linspace(0, 1, 1001)
    valid_thresholds = []

    for threshold in thresholds:
        preds = (probabilities >= threshold).astype(int)
        metrics = evaluate_binary_predictions(y_true, preds)

        if metrics["sensitivity"] >= target_sensitivity:
            valid_thresholds.append(threshold)

    if not valid_thresholds:
        return 0.0

    return max(valid_thresholds)
