# AI Vision Trainer — Master Codex / Cursor Prompt Pack

Version: 1.0 | Date: 2026-10-16 | Product: **AI Vision Trainer**

## How to use

1. Create a private GitHub repository named `ai-vision-trainer` (change if desired).
2. Paste **Master Prompt** into your coding agent first and request it to save AGENTS.md and docs/architecture.md.
3. Paste **Phase 01**. Finish tests, review diffs and merge only after acceptance checks pass.
4. Repeat phases sequentially. Never paste all 34 at once as a single implementation instruction.
5. If an earlier phase is unfinished, instruct the agent to fix the earlier phase instead of accumulating technical debt.
6. On low-spec local machines, start backend without GPU; GPU training belongs on a compatible Linux/NVIDIA worker.

## Product baseline and non-negotiable engineering rules

- Brand, heading, UI metadata: **AI Vision Trainer** (not 'trainner').
- Version 1 scope: supervised **object detection** with labelled image datasets; future segmentation, classification, pose, OBB and OCR modules must fit adapters, not be partially implemented prematurely.
- Stack: React/Vite **JavaScript**, Tailwind, shadcn/ui, Motion animations, Plotly/Recharts; FastAPI Python 3.11+; Pydantic v2; SQLAlchemy/Alembic; PostgreSQL; Redis+RQ/Celery; PyTorch/Ultralytics; MLflow; FiftyOne optional; local storage with S3-compatible future abstraction; Docker Compose; Nginx.
- Architecture: frontend -> REST/WebSocket API -> durable queue -> isolated worker -> YOLO adapter -> GPU. Webserver must never execute long training in its request process.
- Use known-supported installed Ultralytics models (initial support YOLO11 and YOLO26 **detection**). Use real API inspection/version-pinned dependencies, not guessed model flags or data. Source documentation: https://docs.ultralytics.com/models/yolo26/ and https://docs.ultralytics.com/modes/ .
- Performance/accuracy metrics must come from actual runs on named datasets and named hardware. **Never fabricate FPS, mAP, confidence, losses, training examples, device state or progress.** Demo/mock data must be prominently labelled and be limited to demo/test fixtures.
- User-supplied images and videos are untrusted inputs: control file types and size, sanitize archives and paths, protect content routes, isolate data, avoid arbitrary shell concatenation, and audit authorization. Don't execute data-derived commands.
- Preserve immutable datasets and trained artifacts with checksums; log dependency versions, model name, dataset hash, seed, run ID, git SHA and hardware for reproducibility.
- CI must run on CPU; GPU integration tests are optional/marked and runnable on a real GPU host.
- Design quality: premium technical visual design, dark/light themes, accessible keyboard interaction and reduced-motion support. Animation must represent real events, and must not block the workflow.
- Every unit is independently functional with migration, tests, docs and API contract. No TODO-only endpoints masquerading as complete work. When dependencies are absent, provide honest disabled states and setup instructions.
- **Licensing gate:** Assess Ultralytics and dataset/commercial-use licensing before shipping or monetizing. Do not claim AGPL components may be redistributed without obligations.

## MASTER PROMPT (send once)

You are the principal software architect and lead engineer building **AI Vision Trainer**, a production-quality, self-hosted web platform for supervised YOLO object detection training, evaluation, dataset curation, experiment tracking and GPU/edge deployment. Work in the existing repository; inspect current code before changing anything. Respect the product baseline above and this document. Use React/Vite with JavaScript frontend, FastAPI Python backend, PostgreSQL, Redis queue, isolated GPU workers, model adapters, WebSocket updates, MLflow tracking, optional FiftyOne, reproducible Docker deployment. Treat all external files as untrusted. Never invent live training metrics, hardware readings or benchmark results. Keep all model and data provenance. Keep UI modern, elegant, animated, accurate and responsive. The first functional vertical slice should work without a GPU using CPU and a tiny labelled test fixture; only gate genuinely GPU-specific features. Do not rewrite completed modules to satisfy new requests without migration and compatibility tests.

For every phase I submit: (1) inspect repository/AGENTS.md and list what already exists, (2) produce a concise implementation plan and explicit files to be changed, (3) implement complete backend/frontend/worker/database changes needed for this phase, (4) add robust tests including failure/security cases, (5) update migrations, OpenAPI, architecture and user docs, (6) run lint/type/static checks and tests, (7) provide exact local commands and manual UI verification, (8) list any factual environment limitations and remaining known issues, (9) provide git commands for branch/commit/merge/PR but do not merge without my approval. Avoid placeholders and fabricated test success. Use branch `phase-NN-short-slug`. When tests fail, fix or report them honestly; never hide failures.

### Definition of done applicable to every phase
- Working feature, not a mocked pretend flow; if the feature needs a GPU/large dataset, use a fixture for automated tests and explicitly document real-world verification.
- Alembic migration, API validation, frontend states, access control interfaces and auditability as applicable.
- Failure handling: broken upload, bad config, worker crash, network loss, cancellation and reload as applicable.
- Automated tests + manual QA checklist; docs and sample `.env.example` updated; no secret committed.
- Branch remains reviewable with changes scoped to the requested phase.

---

## PHASE 01 — Repository Architecture and Bootstrap

**Git branch:** `phase-01-repository-architecture-bootstrap`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 01: **Repository Architecture and Bootstrap**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-01-repository-architecture-bootstrap`.
>
> **Implementation scope:** Define monorepo folders frontend/, backend/, worker/, shared/schemas/, infrastructure/, docs/, tests/; choose JavaScript React/Vite, Python FastAPI, SQLAlchemy/Alembic, PostgreSQL, Redis, Ultralytics adapter; create README, LICENSE decision note, .env.example, gitignore, Makefile, architecture diagrams in Mermaid, ADRs, GitHub Actions lint smoke and CI; health endpoints and project branding.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Clean setup starts backend and frontend; tests pass; no hardcoded secrets; API contract versioned /api/v1; repository follows documented layout.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 02 without my instruction. Do not silently merge into `main`.

---

## PHASE 02 — FastAPI API and React Design System

**Git branch:** `phase-02-fastapi-api-react-design-system`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 02: **FastAPI API and React Design System**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-02-fastapi-api-react-design-system`.
>
> **Implementation scope:** Implement FastAPI application factory, typed Pydantic request/response DTOs, exception handler, routers, CORS allowlist, structured logs, pagination, DB migrations, OpenAPI; implement React app shell, routing, dark-first accessible dashboard, sidebar, breadcrumb, motion transitions, notification system, forms and API client; create status view with real API health.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Navigation and backend health work together; accessibility keyboard checks; stable API errors; frontend/backend test suites.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 03 without my instruction. Do not silently merge into `main`.

---

## PHASE 03 — Project Management

**Git branch:** `phase-03-project-management`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 03: **Project Management**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-03-project-management`.
>
> **Implementation scope:** Create Project, ProjectMember-ready owner relationships, descriptions, task type detect, lifecycle statuses, tags, timestamps; CRUD, archive/restore, search/sort/pagination, summary cards; project wizard with sample projects ANPR and helmet detection but no fake training scores; project folders and permission interfaces.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Create/edit/archive/restore persisted across refresh; invalid input rejected; project scope enforced and tested.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 04 without my instruction. Do not silently merge into `main`.

---

## PHASE 04 — Resumable Dataset Upload and Import

**Git branch:** `phase-04-resumable-dataset-upload-import`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 04: **Resumable Dataset Upload and Import**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-04-resumable-dataset-upload-import`.
>
> **Implementation scope:** Implement streaming/chunked resumable uploads, progress, retry, cancel, upload sessions and size limits; import YOLO image/label folders and ZIP, validate archives against zip-slip, decompression bombs, symlinks, traversal; staged immutable raw files, cryptographic hashes, manifest, atomic finalize; check disk quota and errors; set framework hooks for COCO/VOC adapters, implement converters if feasible.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Upload 10k+ images without loading into RAM; restarts recover sessions; bad ZIP rejected safely; correct images/labels count and hashes.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 05 without my instruction. Do not silently merge into `main`.

---

## PHASE 05 — Dataset Image and Annotation Browser

**Git branch:** `phase-05-dataset-image-annotation-browser`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 05: **Dataset Image and Annotation Browser**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-05-dataset-image-annotation-browser`.
>
> **Implementation scope:** Build scalable paginated thumbnail API and React virtualized grid, image details with resolution/class labels, zoom/pan, responsive overlays, filters by class/split/label status, safe image streaming, background thumbnail workers, pagination; expose ground-truth bbox coordinates overlay and metadata; keyboard navigation.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Thousands of images navigate smoothly; bounding boxes align despite scaling; nonexistent/media traversal blocked; integration and UI tests.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 06 without my instruction. Do not silently merge into `main`.

---

## PHASE 06 — Human Annotation Editor

**Git branch:** `phase-06-human-annotation-editor`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 06: **Human Annotation Editor**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-06-human-annotation-editor`.
>
> **Implementation scope:** Build bounding-box drawing/move/resize/delete and class picker, keyboard shortcuts, undo/redo, autosave with revision conflicts, bulk relabel, normalized YOLO xywh mapping and precise pixel coordinate conversion; image orientation handling, read-only dataset versions, working drafts; export labels; do not implement segmentation yet.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Boxes persist/reload exactly; no out-of-range coordinates; concurrent edit conflict handled; undo/redo and keyboard tests.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 07 without my instruction. Do not silently merge into `main`.

---

## PHASE 07 — Dataset Integrity and Health Checks

**Git branch:** `phase-07-dataset-integrity-health-checks`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 07: **Dataset Integrity and Health Checks**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-07-dataset-integrity-health-checks`.
>
> **Implementation scope:** Asynchronous dataset audit checking unsupported/corrupt images, annotation syntax, invalid class index, bounding boxes clipped/out of range, zero size, missing/empty labels distinction, duplicate annotations, exact and perceptual near duplicates, dimensions, tiny objects, leakage across splits; severity and remediation hints, CSV/JSON audit exports, non-arbitrary score methodology.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Deterministic fixture dataset triggers each warning; no unsafe silent deletion; block critical errors before training.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 08 without my instruction. Do not silently merge into `main`.

---

## PHASE 08 — Dataset Statistics Dashboard

**Git branch:** `phase-08-dataset-statistics-dashboard`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 08: **Dataset Statistics Dashboard**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-08-dataset-statistics-dashboard`.
>
> **Implementation scope:** Compute counts per class and split, image/box dimensions, objects per image, relative object area, aspect ratios, class imbalance, duplicate clusters, label status; interactive Plotly/Recharts plots and sample drill downs; clarify statistics are empirical and metrics are not model accuracy; export summary data.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Plots correctly reconcile to dataset manifest; filters sync with API; large datasets computed incrementally; clear zero-data state.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 09 without my instruction. Do not silently merge into `main`.

---

## PHASE 09 — Immutable Dataset Versions and Splits

**Git branch:** `phase-09-immutable-dataset-versions-splits`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 09: **Immutable Dataset Versions and Splits**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-09-immutable-dataset-versions-splits`.
>
> **Implementation scope:** Design immutable dataset versions, draft-to-publish workflow, lineage, checksum manifests, content-addressed reuse, diff between versions, per-version train/val/test split with reproducible seed and class-aware options, group by video/source to prevent leakage, no test reuse for tuning; generate verified data.yaml; no destructive overwrites.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Same seed yields same splits; published version cannot mutate; no sample overlap; training consumes exact manifest.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 10 without my instruction. Do not silently merge into `main`.

---

## PHASE 10 — YOLO Model Registry and Adapter

**Git branch:** `phase-10-yolo-model-registry-adapter`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 10: **YOLO Model Registry and Adapter**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-10-yolo-model-registry-adapter`.
>
> **Implementation scope:** Build capability-driven adapter interface list_models/train/validate/predict/export/benchmark; populate officially supported YOLO11/YOLO26 detection weights with correct filenames from installed dependency, checksum/cache downloads, licensing notice for Ultralytics AGPL/commercial implications; UI model cards n/s/m/l/x and hardware suitability hints; avoid fabricated speed/accuracy values.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Adapter tests use mocks; one small public dataset inference smoke test; versions pinned and unsupported combinations disabled.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 11 without my instruction. Do not silently merge into `main`.

---

## PHASE 11 — Basic and Expert Training Configuration

**Git branch:** `phase-11-basic-expert-training-configuration`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 11: **Basic and Expert Training Configuration**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-11-basic-expert-training-configuration`.
>
> **Implementation scope:** Wizard basic/expert mode; fields epochs, imgsz, batch/auto, device, workers, seed, optimizer, lr0, lrf, momentum, weight decay, patience, cache, AMP, cos_lr, augmentations (mosaic, mixup, HSV, flips etc) constrained by installed model; validate data/version/hardware and show estimated disk budget only when derivable; presets save/clone.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Validated config roundtrips exactly to worker; invalid and unsupported parameters rejected; presets covered by tests.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 12 without my instruction. Do not silently merge into `main`.

---

## PHASE 12 — GPU and Host Hardware Inventory

**Git branch:** `phase-12-gpu-host-hardware-inventory`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 12: **GPU and Host Hardware Inventory**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-12-gpu-host-hardware-inventory`.
>
> **Implementation scope:** Worker capability probe using torch.cuda/torch.backends with optional nvidia-smi, GPU name, VRAM, CUDA availability, torch/driver/runtime versions, disk and RAM; CPU-only fallback; worker heartbeat; distinguish remote worker specs, never assume CUDA if unavailable; batch recommendation conservative and adjustable.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Dashboard differentiates CPU vs GPU; probe errors do not crash; no training assigned to incompatible worker.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 13 without my instruction. Do not silently merge into `main`.

---

## PHASE 13 — Durable Training Queue and Process Supervisor

**Git branch:** `phase-13-durable-training-queue-process-supervisor`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 13: **Durable Training Queue and Process Supervisor**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-13-durable-training-queue-process-supervisor`.
>
> **Implementation scope:** Create Postgres job records and Redis-backed queue; isolated training subprocess per assigned GPU, durable status transitions QUEUED/RUNNING/COMPLETED/FAILED/CANCELLED/INTERRUPTED; idempotent dispatch, concurrency/VRAM policy, log capture, stop signal escalation, checkpoint recovery semantics, retries where safe, cleanup, worker heartbeats, queue UI; prevent duplicate runs and GPU oversubscription.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Queue survives API restart; cancel and worker failure accurately reflected; isolation tested; retry never silently creates duplicate model.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 14 without my instruction. Do not silently merge into `main`.

---

## PHASE 14 — Live Training Events over WebSockets

**Git branch:** `phase-14-live-training-events-over-websockets`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 14: **Live Training Events over WebSockets**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-14-live-training-events-over-websockets`.
>
> **Implementation scope:** Capture training callbacks for epoch start/end and metrics, separate batch-level lightweight progress; versioned schema event with run_id, seq, timestamp, epoch, metric keys, GPU stats; persist events, replay from seq cursor, WebSocket auth-ready endpoint, throttling and reconnect backoff, polling fallback; never invent metrics between actual validation intervals.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Browser reconnect catches up without duplication; stable ordered event stream; multiple observers; bounded event history.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 15 without my instruction. Do not silently merge into `main`.

---

## PHASE 15 — Premium Animated Live Training Dashboard

**Git branch:** `phase-15-premium-animated-live-training-dashboard`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 15: **Premium Animated Live Training Dashboard**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-15-premium-animated-live-training-dashboard`.
>
> **Implementation scope:** Implement polished live training workstation with epoch gauge, ETA sourced from measured throughput and marked estimate, CPU/GPU/VRAM sparklines, animation timeline, real samples (with permissions), live augmentation previews generated from actual pipeline, optional checkpoint prediction gallery labeled with the checkpoint/epoch; UI motion respects prefers-reduced-motion; no fake demonstrations presented as true inference.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Responsive GPU dashboard works with replay fixture; screenshots, no layout shifts; animations disabled for reduced motion; numeric values match event stream.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 16 without my instruction. Do not silently merge into `main`.

---

## PHASE 16 — Training Graphs, Metrics and Artifacts

**Git branch:** `phase-16-training-graphs,-metrics-artifacts`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 16: **Training Graphs, Metrics and Artifacts**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-16-training-graphs,-metrics-artifacts`.
>
> **Implementation scope:** Graph train/validation box, cls, DFL losses when exposed, precision, recall, mAP@.50/.50:.95 by epoch, confidence intervals only when justified; toggle series, compare runs, hover metadata, CSV export, checkpoint tags best.pt/last.pt and artifact index; metric missingness and varying validation intervals handled honestly.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** All curves source exact artifacts and events; missing metrics show gaps; unit/API/integration tests for parsers.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 17 without my instruction. Do not silently merge into `main`.

---

## PHASE 17 — Post-Training Validation Engine

**Git branch:** `phase-17-post-training-validation-engine`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 17: **Post-Training Validation Engine**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-17-post-training-validation-engine`.
>
> **Implementation scope:** Create validation jobs for frozen version and checkpoint; select validation/test split separately; compute per-class precision, recall, AP50, AP50:95, speed with methodology and confidence/IoU settings; persist evaluation versions with environmental metadata; prohibit selecting final holdout/test as default during iteration; record error/unsupported states.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Known fixture evaluation reproducible; no data leakage; validation artifacts and split provenance available via API.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 18 without my instruction. Do not silently merge into `main`.

---

## PHASE 18 — Evaluation Metrics Dashboard

**Git branch:** `phase-18-evaluation-metrics-dashboard`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 18: **Evaluation Metrics Dashboard**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-18-evaluation-metrics-dashboard`.
>
> **Implementation scope:** Build metric cards, per-class tables with sample counts, sorted weak classes, filter by score/IoU/class/split, confidence and PR metrics; explicitly label AP vs accuracy, absent data vs zero, threshold-dependent vs integral metrics; link charts to image drill-down.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Numbers reconcile to backend evaluation and no made-up composite quality score; keyboard-accessible filters.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 19 without my instruction. Do not silently merge into `main`.

---

## PHASE 19 — Confusion Matrices and PR/F1 Curves

**Git branch:** `phase-19-confusion-matrices-pr-f1-curves`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 19: **Confusion Matrices and PR/F1 Curves**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-19-confusion-matrices-pr-f1-curves`.
>
> **Implementation scope:** Generate class-wise confusion matrix including background FP/FN interpretation, normalized/raw switch, precision-recall curve, F1-vs-confidence, precision-vs-confidence, recall-vs-confidence, AP-vs-IoU where available, correct axis scales, downloadable SVG/PNG; use actual Ultralytics artifacts or reproducible evaluator.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Fixtures verify sums and interpolation; charts explain axes/matching criteria, confidence thresholds and IoU.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 20 without my instruction. Do not silently merge into `main`.

---

## PHASE 20 — False Positive / False Negative Explorer

**Git branch:** `phase-20-false-positive---false-negative-explorer`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 20: **False Positive / False Negative Explorer**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-20-false-positive---false-negative-explorer`.
>
> **Implementation scope:** Store sample-level prediction vs GT match assignments under explicit class/IoU/confidence rules; filter FP/FN/TP, low IoU, low confidence, worst class, size, lighting metadata if provided; gallery boxes in distinct styles, side-by-side GT/prediction, annotation feedback draft only; integrate FiftyOne via service adapter when installed, avoid hard requirement for training core.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Each thumbnail has traceable match status; FP/FN counts reconcile to evaluator; reviewer corrections never silently change immutable version.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 21 without my instruction. Do not silently merge into `main`.

---

## PHASE 21 — MLflow Experiment Tracking

**Git branch:** `phase-21-mlflow-experiment-tracking`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 21: **MLflow Experiment Tracking**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-21-mlflow-experiment-tracking`.
>
> **Implementation scope:** Integrate MLflow experiment/run for config, dataset hash, git SHA, framework version, training metrics, artifacts/checkpoint pointers; local MLflow backend in compose, graceful degradation with spool/retry, synchronized run status, deep-link from UI; avoid logging secrets or large datasets as raw tracking artifacts.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Run traceable from UI to MLflow, same training job cannot duplicate registered metadata; retry tested.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 22 without my instruction. Do not silently merge into `main`.

---

## PHASE 22 — Experiment Comparison and Pareto Analysis

**Git branch:** `phase-22-experiment-comparison-pareto-analysis`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 22: **Experiment Comparison and Pareto Analysis**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-22-experiment-comparison-pareto-analysis`.
>
> **Implementation scope:** Allow compare 2-6 runs with dataset/version, architecture, epochs, image size, precision/recall/mAP, walltime, model size, measured FPS/device benchmark and resource use; overlay metric histories aligned by epoch; define best accuracy vs fastest only for measured comparable hardware/configurations, Pareto frontier and CSV export; missing values visible.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** No inappropriate cross-device inference ranking; table and chart values match immutable runs.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 23 without my instruction. Do not silently merge into `main`.

---

## PHASE 23 — Model Registry and Promotion Workflow

**Git branch:** `phase-23-model-registry-promotion-workflow`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 23: **Model Registry and Promotion Workflow**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-23-model-registry-promotion-workflow`.
>
> **Implementation scope:** Integrate MLflow model versions/aliases or equivalent registry; link trained checkpoint, dataset version, run, evaluation and sha256, status Candidate/Approved/Production/Archived, approval reason, rollback and audit log, immutable binaries, retention policies; never overwrite same version; optional license compliance metadata.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Promote and rollback without losing lineage, role interfaces wired for Phase31, downloads hash-verified.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 24 without my instruction. Do not silently merge into `main`.

---

## PHASE 24 — Single Image and Batch Inference Test Bench

**Git branch:** `phase-24-single-image-batch-inference-test-bench`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 24: **Single Image and Batch Inference Test Bench**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-24-single-image-batch-inference-test-bench`.
>
> **Implementation scope:** Test registered models on drag/drop images or batch folder using async tasks, confidence/IoU controls and task-appropriate prediction format; bounding boxes, per-class counts and latency breakdown (preprocess/inference/postprocess), clear measured hardware label; compare models side-by-side; uploads temporary and quota-controlled.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Prediction boxes match source pixel geometry; batch output downloadable; no untrusted file execution; inference tested end-to-end.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 25 without my instruction. Do not silently merge into `main`.

---

## PHASE 25 — Video, Webcam and RTSP Testing

**Git branch:** `phase-25-video,-webcam-rtsp-testing`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 25: **Video, Webcam and RTSP Testing**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-25-video,-webcam-rtsp-testing`.
>
> **Implementation scope:** Add upload video with server worker processing, optional browser webcam local acquisition with explicit permission, RTSP backend capture with allowlist/SSRF protection, FPS, frame sampling, run controls, annotated video download and live low-latency previews with backpressure; define privacy/retention defaults and disable RTSP by default until secure.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Stop/reconnect and stream failures recover cleanly; FPS measured; upload and RTSP security checks; no camera auto-enablement.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 26 without my instruction. Do not silently merge into `main`.

---

## PHASE 26 — Portable Model Export Manager

**Git branch:** `phase-26-portable-model-export-manager`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 26: **Portable Model Export Manager**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-26-portable-model-export-manager`.
>
> **Implementation scope:** Implement PT artifact retrieval, ONNX export jobs with input shape/precision/opset options and opset compatibility, export logs/metadata, post-export numerical and sample-image equivalence tests within configurable tolerance, progress, checksums, downloadable model plus inference README; plugin interface for later formats; document licensing.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** ONNX loads and runs in ONNX Runtime on fixture; predictions compared to PT; failure artifacts preserved.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 27 without my instruction. Do not silently merge into `main`.

---

## PHASE 27 — TensorRT and Edge Export Pipelines

**Git branch:** `phase-27-tensorrt-edge-export-pipelines`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 27: **TensorRT and Edge Export Pipelines**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-27-tensorrt-edge-export-pipelines`.
>
> **Implementation scope:** Add remote GPU-bound TensorRT engine export, FP16/FP32 and calibrated INT8 with representative validation-approved calibration samples; record GPU architecture, TensorRT/CUDA versions and build host, platform compatibility warnings; optional OpenVINO/TFLite later; Jetson profiles and artifact bundles; never advertise portable TensorRT engines across arbitrary GPUs.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Engine compiles on compatible machine and executes inference; quantized accuracy re-evaluated; clear unsupported workflow errors.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 28 without my instruction. Do not silently merge into `main`.

---

## PHASE 28 — Edge Hardware Benchmarking

**Git branch:** `phase-28-edge-hardware-benchmarking`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 28: **Edge Hardware Benchmarking**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-28-edge-hardware-benchmarking`.
>
> **Implementation scope:** Design benchmark agent protocol for Jetson Nano/Orin Nano/Orin NX, desktop CUDA, CPU and later Raspberry Pi/Android; device registration, warmup, repeatable timing excluding/including preprocessing separately, FPS/latency p50/p95, peak RSS/VRAM, power only if available, model compatibility, network independent benchmark, quality-vs-speed report; reject unmeasured placeholder metrics.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Hardware/environment/profile attached to every number; compare like-for-like; independent agent authentication ready.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 29 without my instruction. Do not silently merge into `main`.

---

## PHASE 29 — HTML and PDF Technical Reporting

**Git branch:** `phase-29-html-pdf-technical-reporting`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 29: **HTML and PDF Technical Reporting**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-29-html-pdf-technical-reporting`.
>
> **Implementation scope:** Report builder with executive summary, data lineage/classes/splits, dataset health, training config/environment, epoch plots, evaluation metrics curves, annotated TP/FP/FN samples, experiments, benchmark hardware, deployment notes, limitations, reproducibility references and methodology; render responsive HTML and print-ready PDF using stable server-side rendering, version report schema and downloadable CSV/JSON.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Reports match tracked metrics and include evidence/provenance; no invented results; PDF visual verification and snapshot tests.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 30 without my instruction. Do not silently merge into `main`.

---

## PHASE 30 — Rules-Based Training Advisor and Optional LLM Explainer

**Git branch:** `phase-30-rules-based-training-advisor-optional-llm`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 30: **Rules-Based Training Advisor and Optional LLM Explainer**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-30-rules-based-training-advisor-optional-llm`.
>
> **Implementation scope:** First implement deterministic evidence-based rules for overfitting (train/val divergence), low class support, poor tiny-object recall, duplicates, anomalous labels, missing data, bottlenecks with confidence limits; suggestions link to graphs and samples; optional configurable local/Ollama or API LLM layer turns structured evidence into prose but cannot invent numbers and must be clearly labeled experimental.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Every advice includes reason, evidence and action; safe handling missing metrics; no unproven automated hyperparameter changes.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 31 without my instruction. Do not silently merge into `main`.

---

## PHASE 31 — Multi-User Authentication and Authorization

**Git branch:** `phase-31-multi-user-authentication-authorization`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 31: **Multi-User Authentication and Authorization**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-31-multi-user-authentication-authorization`.
>
> **Implementation scope:** Implement secure login, password hashing, invite workflow, session rotation/revocation, CSRF strategy if cookies, rate limits, roles Admin/Trainer/Annotator/Viewer with project scope, API/WebSocket/download/storage authorizations, audit trails; initial single-user development protected when exposed, migration without insecure bypass; optional SSO later.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** All cross-project access tests pass; auth covers live events, artifacts and uploads; secrets protected.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 32 without my instruction. Do not silently merge into `main`.

---

## PHASE 32 — Distributed Remote GPU Worker Support

**Git branch:** `phase-32-distributed-remote-gpu-worker-support`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 32: **Distributed Remote GPU Worker Support**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-32-distributed-remote-gpu-worker-support`.
>
> **Implementation scope:** Secure device onboarding with short-lived tokens/mTLS design, heartbeat, health and GPU capability scheduler, job artifact transfer with hashes and signed scoped URLs, replay events, resilient checkpoints and retries, worker isolation, remote path agnostic manifests, disk pressure signals, job affinity, worker disable/drain; support local CPU dev and remote Linux NVIDIA executor.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Disconnect/reconnect tested; no worker impersonation; dataset never duplicated unnecessarily; corrupted artifacts rejected.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 33 without my instruction. Do not silently merge into `main`.

---

## PHASE 33 — Production Docker Deployment and Hardening

**Git branch:** `phase-33-production-docker-deployment-hardening`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 33: **Production Docker Deployment and Hardening**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-33-production-docker-deployment-hardening`.
>
> **Implementation scope:** Create dev and production Compose profiles for React build/static Nginx, FastAPI, Postgres, Redis, worker, MLflow and optional MinIO; GPU Docker runtime docs, healthchecks, persistent volumes, backup/restore, TLS reverse proxy, secrets, CORS, request limits, least privilege, no docker.sock mount, monitoring/metrics, log rotation, migrations, CPU-only fallback; deployment guidance for Utho CPU server + remote GPU training host.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Fresh install/upgrade/backup restore smoke tests; HTTPS, non-root where feasible, data survives restart; security checklist signed off.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 34 without my instruction. Do not silently merge into `main`.

---

## PHASE 34 — Electron Desktop Packaging and Cross-Platform Integration

**Git branch:** `phase-34-electron-desktop-packaging-cross-platform`

### COPY-PASTE PROMPT

> Work on **AI Vision Trainer**, Phase 34: **Electron Desktop Packaging and Cross-Platform Integration**. First inspect repository state, existing database migrations, OpenAPI, previous-phase acceptance tests and AGENTS.md. Create/use the branch `phase-34-electron-desktop-packaging-cross-platform`.
>
> **Implementation scope:** Wrap existing React UI with Electron secure contextIsolation/sandbox and minimal preload IPC, nodeIntegration off, external link policy and packaging for Windows, macOS Intel/Apple Silicon and Ubuntu x64/arm64 where dependencies allow; do NOT bundle CUDA models/toolchains by default, desktop points to configured local/remote backend, auth and updater signing strategy, image file picker with secure upload.
>
> **Required deliverables:** Implement complete API routes/services, persistence and migrations as applicable; build working React pages and accessible UI feedback; connect real API data (not fake cards); implement background work in the worker where needed; maintain project/dataset/run provenance, error handling and structured logs; unit, API, worker and frontend component tests; update docs, `.env.example`, and operations instructions. Follow Master Prompt constraints strictly.
>
> **Acceptance checks:** Desktop launches on supported OS, connects to backend, imports datasets, and trains remotely; security tests and reproducible installers.
>
> **Final response format:** (a) exact files changed, (b) functionality completed and important design decisions, (c) commands run and actual test results, (d) step-by-step local verification with expected behavior, (e) new API endpoints/database tables and migrations, (f) limitations and risks, (g) suggested commit message and git commands. Do **not** begin Phase 35 without my instruction. Do not silently merge into `main`.

---

## Final integration and release acceptance gate (after Phase 34)

Conduct a fresh-install end-to-end trial: import a labelled YOLO dataset, inspect annotations, validate errors, publish dataset version, train a tiny detector, stop/restart worker, reconnect live WebSocket, run validation, explore FP/FN, compare runs, register a model, export ONNX, measure one actual inference device, generate and visually inspect PDF and HTML reports, and test desktop connectivity. Verify exact dataset/model/checkpoint lineage throughout. On GPU machine test CUDA training and TRT export; on CPU do not report those checks as passed. Run dependency/license/security review and backup restore exercise. Generate release notes, manual, API documentation, deployment runbook and issues list.

## Reference documentation
- Ultralytics: https://docs.ultralytics.com/models/yolo26/
- Ultralytics modes: https://docs.ultralytics.com/modes/
- FiftyOne detections: https://docs.voxel51.com/user_guide/evaluation/detections.html
- MLflow model registry: https://mlflow.org/docs/latest/model-registry/
