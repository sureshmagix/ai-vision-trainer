import json
import logging

from worker.tasks.health import run_worker_diagnostic

logging.basicConfig(level=logging.INFO, format="%(asctime)s [WORKER] %(message)s")
logger = logging.getLogger("worker")


def main():
    logger.info("Initializing AI Vision Trainer background worker...")
    diagnostic = run_worker_diagnostic()
    logger.info("Worker diagnostic report:\n" + json.dumps(diagnostic, indent=2))
    logger.info("Worker standby for queued training & evaluation jobs.")


if __name__ == "__main__":
    main()
