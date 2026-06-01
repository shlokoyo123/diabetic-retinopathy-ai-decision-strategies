import torch.nn as nn
import torchvision.models as models


def build_model(model_name: str, num_classes: int = 2) -> nn.Module:
    """Build a classification model by name."""

    model_name = model_name.lower()

    if model_name == "resnet50":
        model = models.resnet50(weights=None)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
        return model

    if model_name == "resnet18_encoder":
        model = models.resnet18(weights=None)
        model.fc = nn.Linear(model.fc.in_features, num_classes)
        return model

    raise ValueError(f"Unsupported model name: {model_name}")
