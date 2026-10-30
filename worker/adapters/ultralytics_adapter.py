import sys
from typing import Any, ClassVar

from worker.adapters.base import BaseModelAdapter


class UltralyticsYOLOAdapter(BaseModelAdapter):
    """
    Ultralytics YOLO Detection Adapter (supporting YOLO11 & YOLO26 detection).
    Provides strict device detection, model architecture verification, and execution abstraction.
    """

    SUPPORTED_FAMILIES: ClassVar[list[str]] = ["yolo11", "yolo26"]
    SUPPORTED_VARIANTS: ClassVar[list[str]] = ["n", "s", "m", "l", "x"]

    def __init__(self):
        self._ultralytics_available = self._check_ultralytics()

    def _check_ultralytics(self) -> bool:
        try:
            import ultralytics  # noqa: F401
            return True
        except ImportError:
            return False

    def get_supported_architectures(self) -> list[str]:
        architectures = []
        for family in self.SUPPORTED_FAMILIES:
            for variant in self.SUPPORTED_VARIANTS:
                architectures.append(f"{family}{variant}")
        return architectures

    def inspect_hardware_capabilities(self) -> dict[str, Any]:
        """
        Inspect compute hardware without fabricated numbers.
        Returns true state of PyTorch CUDA, Apple Silicon MPS, or CPU fallback.
        """
        device = "cpu"
        device_name = "CPU"
        device_count = 0
        vram_total_gb = 0.0

        try:
            import torch
            if torch.cuda.is_available():
                device = "cuda"
                device_count = torch.cuda.device_count()
                device_name = torch.cuda.get_device_name(0)
                vram_total_gb = round(torch.cuda.get_device_properties(0).total_memory / (1024 ** 3), 2)
            elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
                device = "mps"
                device_count = 1
                device_name = "Apple Silicon MPS"
        except ImportError:
            pass

        return {
            "device": device,
            "device_name": device_name,
            "device_count": device_count,
            "vram_total_gb": vram_total_gb,
            "ultralytics_installed": self._ultralytics_available,
            "python_version": sys.version.split()[0],
        }

    def validate_configuration(self, config: dict[str, Any]) -> bool:
        """Ensure model architecture is in the supported YOLO11/YOLO26 detection registry."""
        model_name = config.get("model_name", "").lower()
        # Strip extension if provided
        model_name = model_name.removesuffix(".pt")

        if model_name not in self.get_supported_architectures():
            raise ValueError(
                f"Unsupported model architecture '{model_name}'. "
                f"Supported models: {', '.join(self.get_supported_architectures())}"
            )
        return True
