# ADR 0001: Model Framework Integration and Ultralytics Licensing Strategy

## Context
AI Vision Trainer requires a robust, state-of-the-art engine for training and evaluating supervised object detection models. Ultralytics YOLO (specifically YOLO11 and YOLO26 detection architectures) provides industry-leading performance and ecosystem maturity.

However, Ultralytics YOLO is distributed under the GNU Affero General Public License v3.0 (AGPL-3.0), with an alternative commercial enterprise licensing option provided by Ultralytics LLC. AGPL-3.0 contains stringent copyleft obligations when accessed over a network.

## Decision
1. **Model Adapter Isolation**: We architect the training runner behind a decoupled `BaseModelAdapter` interface in an isolated worker process.
2. **Clear Licensing Gate**: The platform's application code (FastAPI, React, database migrations, configuration) is released under the Apache 2.0 license. We explicitly document in the `LICENSE`, documentation, and system settings that deploying Ultralytics models for commercial proprietary purposes requires either adhering to AGPL-3.0 or obtaining an Enterprise Commercial License from Ultralytics LLC.
3. **No Hidden Claims**: We will never claim or imply that AGPL-3.0 components can be redistributed without legal obligations.
4. **Pluggable Architecture**: The adapter pattern ensures that alternative non-AGPL vision backends (e.g. PyTorch torchvision Faster R-CNN, RT-DETR, or Apache-2.0 object detection backends) can be plugged in without changing the core platform or database schema.

## Status
Accepted.

## Consequences
- Clean separation between core platform services and training execution workers.
- Clear legal transparency for self-hosted enterprise users and commercial deployments.
