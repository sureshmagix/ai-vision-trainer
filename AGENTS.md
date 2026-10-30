# AI Vision Trainer — Agent Operating Manual & Architecture Ledger

## Project Identity & Product Baseline
- **Product Name**: **AI Vision Trainer** (strict casing, never "trainner")
- **Purpose**: Production-grade, self-hosted web platform for supervised YOLO object detection training, evaluation, dataset curation, experiment tracking, and GPU/edge deployment.
- **Scope (V1)**: Supervised **object detection** with labelled image datasets. Future tasks (segmentation, classification, pose, OBB, OCR) must be interfaced via model adapters without partial premature implementations.
- **Core Architecture**:
  - **Frontend**: React (Vite) with JavaScript, Tailwind CSS, shadcn/ui component styling, Motion animations, Plotly/Recharts.
  - **Backend**: FastAPI (Python 3.11+), Pydantic v2, SQLAlchemy 2.0 (asyncio-ready), Alembic migrations, PostgreSQL, Redis durable queue (RQ/Celery).
  - **Workers**: Isolated GPU/CPU worker processes decoupled from the FastAPI request cycle. Web server must never run long training jobs directly.
  - **Model Adapters**: PyTorch & Ultralytics (detection models: initial support YOLO11 and YOLO26 detection). Real API inspection and version-pinned dependencies.
  - **Experiment & Dataset Tracking**: MLflow tracking, optional FiftyOne visualization, local storage with S3-compatible future abstraction, Docker Compose, Nginx reverse proxy.
  - **Security & Data Integrity**: All external files (images, archives, config) are treated as untrusted. Strict MIME/magic validation, path traversal defense, archive bombs protection. No arbitrary shell command execution.
  - **Truthful Metrics Guarantee**: Hardware readings, live metrics, loss curves, FPS, and mAP must originate from verified execution on named hardware and datasets. Never invent or fabricate mock metrics or training states.

---

## Non-Negotiable Operational Protocol (Every Phase)
For every phase submitted by the user:
1. **Inspect**: Check `AGENTS.md`, existing migrations, OpenAPI schemas, and previous test suites.
2. **Plan**: Produce a concise implementation plan with explicit file paths before modifying code.
3. **Implement**: Deliver complete backend, frontend, worker, schema, and database changes. No TODO placeholders or fake flows.
4. **Test**: Write automated unit, integration, failure, and security tests. Run CPU-friendly test fixtures.
5. **Migrate & Document**: Create Alembic migrations, update OpenAPI contracts, update user docs and `docs/architecture.md`.
6. **Lint & Verify**: Run linters, type checks, and automated test commands; report honest outputs.
7. **Manual QA**: Provide copy-pasteable local run commands and step-by-step UI verification checks.
8. **Limitations**: Document factual environment boundaries (e.g., CPU fallback vs. real GPU requirement) and known issues.
9. **Git Guidance**: Use branch `phase-NN-short-slug`. Provide git commit and PR commands; never merge into `main` without explicit user confirmation.

---

## Monorepo Directory Structure Target
```
ai-vision-trainer/
├── frontend/             # React/Vite JavaScript application
│   ├── src/
│   │   ├── components/   # UI components (shadcn/ui style, accessible)
│   │   ├── pages/        # Route views
│   │   ├── api/          # API client & WebSocket handlers
│   │   └── hooks/        # State & lifecycle hooks
├── backend/              # FastAPI Python backend application
│   ├── app/
│   │   ├── api/          # Versioned REST endpoints (/api/v1/...)
│   │   ├── core/         # Config, logging, security, database session
│   │   ├── models/       # SQLAlchemy ORM models
│   │   ├── schemas/      # Pydantic v2 request/response schemas
│   │   └── services/     # Business logic & repository layers
│   ├── alembic/          # Database migrations
│   └── tests/            # Pytest suite (unit, integration, security)
├── worker/               # Background task workers (isolated training/eval)
│   ├── tasks/            # Job handlers
│   └── adapters/         # Model execution adapters (Ultralytics YOLO)
├── shared/               # Shared constants, contracts, and schema definitions
├── infrastructure/       # Dockerfile, docker-compose.yml, Nginx configs
├── docs/                 # Architecture, ADRs, user guides, API specs
├── tests/                # End-to-end and cross-cutting integration fixtures
├── Makefile              # Unified development and build commands
├── .env.example          # Environment variable reference template
└── AGENTS.md             # This document & phase tracking ledger
```

---

## Phase Execution Ledger (34 Phases)

| Phase | Branch Name | Name / Focus | Status |
|---|---|---|---|
| **01** | `phase-01-repository-architecture-bootstrap` | Repository Architecture and Bootstrap | Completed |
| **02** | `phase-02-fastapi-api-react-design-system` | FastAPI API and React Design System | Pending |
| **03** | `phase-03-project-management` | Project Management | Pending |
| **04** | `phase-04-resumable-dataset-upload-import` | Resumable Dataset Upload and Import | Pending |
| **05** | `phase-05-dataset-validation-integrity-audit` | Dataset Validation & Integrity Audit | Pending |
| **06** | `phase-06-dataset-versioning-snapshot-engine` | Dataset Versioning & Snapshot Engine | Pending |
| **07** | `phase-07-dataset-explorer-curation-studio` | Dataset Explorer & Curation Studio | Pending |
| **08** | `phase-08-annotation-editor-review-workflow` | Annotation Editor & Review Workflow | Pending |
| **09** | `phase-09-augmentation-pipeline-builder` | Augmentation Pipeline Builder | Pending |
| **10** | `phase-10-dataset-export-format-transpiler` | Dataset Export & Format Transpiler | Pending |
| **11** | `phase-11-model-registry-yolo-adapter-foundation` | Model Registry & YOLO Adapter Foundation | Pending |
| **12** | `phase-12-training-job-configuration-wizard` | Training Job Configuration Wizard | Pending |
| **13** | `phase-13-redis-queue-worker-orchestration` | Redis Queue & Worker Orchestration | Pending |
| **14** | `phase-14-ultralytics-training-runner-cpu-gpu` | Ultralytics Training Runner (CPU/GPU) | Pending |
| **15** | `phase-15-real-time-metrics-telemetry-engine` | Real-Time Metrics & Telemetry Engine | Pending |
| **16** | `phase-16-training-observability-dashboard` | Training Observability Dashboard | Pending |
| **17** | `phase-17-experiment-tracking-mlflow-integration` | Experiment Tracking & MLflow Integration | Pending |
| **18** | `phase-18-checkpoint-artifact-management` | Checkpoint & Artifact Management | Pending |
| **19** | `phase-19-model-evaluation-benchmark-suite` | Model Evaluation & Benchmark Suite | Pending |
| **20** | `phase-20-confusion-matrix-error-analysis` | Confusion Matrix & Error Analysis | Pending |
| **21** | `phase-21-fiftyone-visual-diagnostics-bridge` | FiftyOne Visual Diagnostics Bridge | Pending |
| **22** | `phase-22-hyperparameter-tuning-sweeps` | Hyperparameter Tuning & Sweeps | Pending |
| **23** | `phase-23-model-comparison-champion-selection` | Model Comparison & Champion Selection | Pending |
| **24** | `phase-24-export-quantization-engine` | Export & Quantization Engine | Pending |
| **25** | `phase-25-model-deployment-serving-runtime` | Model Deployment & Serving Runtime | Pending |
| **26** | `phase-26-live-inference-playground` | Live Inference Playground | Pending |
| **27** | `phase-27-active-learning-sample-mining` | Active Learning & Sample Mining | Pending |
| **28** | `phase-28-multi-gpu-worker-cluster-management` | Multi-GPU & Worker Cluster Management | Pending |
| **29** | `phase-29-role-based-access-control-audit-log` | Role-Based Access Control & Audit Log | Pending |
| **30** | `phase-30-backup-restore-disaster-recovery` | Backup, Restore & Disaster Recovery | Pending |
| **31** | `phase-31-system-settings-hardware-diagnostics` | System Settings & Hardware Diagnostics | Pending |
| **32** | `phase-32-end-to-end-integration-smoke-test` | End-to-End Integration & Smoke Test | Pending |
| **33** | `phase-33-production-docker-compose-nginx` | Production Docker Compose & Nginx | Pending |
| **34** | `phase-34-user-documentation-final-acceptance` | User Documentation & Final Acceptance | Pending |
