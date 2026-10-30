# ADR 0002: Core Technology Stack & Monorepo Topology

## Context
AI Vision Trainer needs to be scalable, reproducible, and verifiable. It must support both zero-GPU CPU developer workstations and high-throughput multi-GPU production servers. The system involves rich interactive frontend tooling (dataset curation, real-time training telemetry, annotation review) and intensive background ML workloads.

## Decision
1. **Frontend**: React 18+ (Vite) with JavaScript.
   - Styling: Tailwind CSS and shadcn/ui design patterns for an accessible, dark-first technical interface.
   - State & Motion: Framer Motion for non-blocking visual state indicators; Plotly/Recharts for accurate loss/mAP curves.
2. **Backend**: FastAPI (Python 3.11+).
   - Validation: Pydantic v2 for strict type checking and contract generation.
   - Database: PostgreSQL with SQLAlchemy 2.0 (asyncio-ready) and Alembic for tracked migrations. SQLite supported for lightweight unit test fixtures without external dependencies.
3. **Queue & Workers**: Redis durable queue with isolated Python worker processes.
   - Web API server strictly dispatches jobs and reports status; training and dataset heavy operations run in worker processes.
4. **API Contract**: Versioned REST (`/api/v1`) paired with native WebSockets for streaming hardware metrics and step-by-step training telemetry.
5. **Observability**: MLflow for experiment tracking and metric logging; FiftyOne optional visual dataset inspection bridge.
6. **Zero-GPU CPU Bootstrap**: All automated tests, unit tests, and the initial vertical slice must execute on CPU without GPU hardware assumptions.

## Status
Accepted.

## Consequences
- High development velocity, modular maintainability, and clean decoupling of API request cycles from heavy ML workloads.
