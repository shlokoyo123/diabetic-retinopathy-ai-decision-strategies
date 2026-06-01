import numpy as np


def single_model_threshold(probabilities: np.ndarray, threshold: float) -> np.ndarray:
    """Convert single-model probabilities into binary predictions."""
    return (probabilities >= threshold).astype(int)


def majority_vote(binary_predictions: np.ndarray) -> np.ndarray:
    """Return positive if at least two out of three models predict positive."""
    return (binary_predictions.sum(axis=1) >= 2).astype(int)


def weighted_average(prob_matrix: np.ndarray, weights: np.ndarray, threshold: float) -> np.ndarray:
    """Weighted probability ensemble followed by thresholding."""
    weights = weights / weights.sum()
    combined = np.dot(prob_matrix, weights)
    return (combined >= threshold).astype(int)


def two_stage_pipeline(
    primary_probs: np.ndarray,
    secondary_binary_predictions: np.ndarray,
    primary_threshold: float,
    veto_required_votes: int = 2,
) -> np.ndarray:
    """Two-stage strategy using a primary model and agreement-based veto."""
    stage_one = (primary_probs >= primary_threshold).astype(int)
    veto = secondary_binary_predictions.sum(axis=1) < veto_required_votes
    final = stage_one.copy()
    final[(stage_one == 1) & veto] = 0
    return final
