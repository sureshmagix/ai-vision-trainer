"""
AI Vision Trainer — Shared System Constants & Specifications
"""

TASK_TYPE_DETECTION = "detection"
SUPPORTED_TASKS = [TASK_TYPE_DETECTION]

# Target detection architectures supported
SUPPORTED_YOLO_MODELS = {
    "yolo11": ["yolo11n", "yolo11s", "yolo11m", "yolo11l", "yolo11x"],
    "yolo26": ["yolo26n", "yolo26s", "yolo26m", "yolo26l", "yolo26x"]
}

# Standard Training Job Lifecycle
class JobStatus:
    PENDING = "pending"
    QUEUED = "queued"
    PREPARING = "preparing"
    RUNNING = "running"
    EVALUATING = "evaluating"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"

# Default File Storage Layout
STORAGE_SUBDIRS = [
    "datasets",
    "annotations",
    "checkpoints",
    "exports",
    "temp_uploads",
    "metrics",
    "evaluations"
]

DEFAULT_API_V1_PREFIX = "/api/v1"
