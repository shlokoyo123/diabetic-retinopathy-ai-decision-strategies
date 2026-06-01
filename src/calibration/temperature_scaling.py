import torch
import torch.nn as nn


class TemperatureScaler(nn.Module):
    """Temperature scaling module for probability calibration."""

    def __init__(self, temperature: float = 1.0):
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(1) * temperature)

    def forward(self, logits: torch.Tensor) -> torch.Tensor:
        return logits / self.temperature.clamp(min=1e-6)
