from worker.adapters.ultralytics_adapter import UltralyticsYOLOAdapter


def run_worker_diagnostic() -> dict:
    adapter = UltralyticsYOLOAdapter()
    return {
        "status": "ready",
        "supported_models": adapter.get_supported_architectures(),
        "hardware": adapter.inspect_hardware_capabilities(),
    }
