import pytest

from worker.adapters.ultralytics_adapter import UltralyticsYOLOAdapter


def test_supported_architectures_list():
    adapter = UltralyticsYOLOAdapter()
    supported = adapter.get_supported_architectures()

    assert "yolo11n" in supported
    assert "yolo11x" in supported
    assert "yolo26n" in supported
    assert "yolo26x" in supported
    assert len(supported) == 10  # 2 families x 5 variants


def test_hardware_inspection_cpu_safety():
    adapter = UltralyticsYOLOAdapter()
    hw = adapter.inspect_hardware_capabilities()

    assert "device" in hw
    assert hw["device"] in ["cpu", "cuda", "mps"]
    assert "python_version" in hw
    assert "ultralytics_installed" in hw


def test_configuration_validation():
    adapter = UltralyticsYOLOAdapter()

    # Valid configurations
    assert adapter.validate_configuration({"model_name": "yolo11n"}) is True
    assert adapter.validate_configuration({"model_name": "yolo26s.pt"}) is True

    # Invalid configuration
    with pytest.raises(ValueError) as exc_info:
        adapter.validate_configuration({"model_name": "unsupported_v99"})
    assert "Unsupported model architecture" in str(exc_info.value)
