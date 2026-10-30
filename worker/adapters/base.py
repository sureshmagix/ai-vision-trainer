from abc import ABC, abstractmethod
from typing import Any


class BaseModelAdapter(ABC):
    """
    Abstract Model Adapter Contract.
    All detection model backends must implement this interface to decouple
    the platform, worker queues, and REST/WebSocket APIs from third-party ML frameworks.
    """

    @abstractmethod
    def get_supported_architectures(self) -> list[str]:
        """Return list of supported model architectures (e.g. yolo11n, yolo26s)."""

    @abstractmethod
    def inspect_hardware_capabilities(self) -> dict[str, Any]:
        """Return available hardware accelerators, device names, and VRAM availability."""

    @abstractmethod
    def validate_configuration(self, config: dict[str, Any]) -> bool:
        """Validate hyperparameter dictionary and data configuration before launching execution."""
