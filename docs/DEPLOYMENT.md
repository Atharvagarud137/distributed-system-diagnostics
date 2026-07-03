# Deployment Guide

This document explains how to run the Distributed System Health Monitor & Diagnostic Toolkit locally and deploy it using container-based platforms.

## Local Deployment

### Prerequisites

- Docker installed and running
- Python 3.9+ if running locally without Docker
- Git

### Run locally with Docker

```bash
git clone https://github.com/Atharvagarud137/distributed-system-diagnostics.git
cd distributed-system-diagnostics
docker build -t distributed-system-diagnostics:latest .
docker run --rm -p 8000:8000 distributed-system-diagnostics:latest
```

Then open `http://localhost:8000/health` to verify the service is running.

### Run locally with Python

```bash
python -m venv venv
venv\Scripts\activate      # Windows
# OR
source venv/bin/activate    # Mac/Linux
pip install -r requirements.txt
python -m uvicorn src.api:app --reload
```

The service will run at `http://localhost:8000`.

## Docker Compose

If the repository includes `docker-compose.yml`, launch the stack with:

```bash
docker-compose up --build
```

This starts the app on port `8000` by default.

## Free-Tier Deployment Options

This project is designed to deploy on free-tier container platforms.

### Render.com

1. Create a free Render account.
2. Connect your GitHub repository.
3. Create a new Web Service.
4. Use the Dockerfile from this repository.
5. Set the port to `8000`.
6. Deploy.

Render will provide a public URL for the service.

### Railway.app

1. Create a free Railway account.
2. Connect your GitHub repository.
3. Create a new project and deploy from the `master` or `main` branch.
4. Configure the service to expose port `8000`.

Railway will deploy the app and provide a public endpoint.

## Deployment Checklist

- [ ] `requirements.txt` contains the runtime dependencies
- [ ] `Dockerfile` builds a working Python image
- [ ] `docker-compose.yml` exposes port `8000`
- [ ] `src/api.py` includes the `/health` endpoint
- [ ] `docs/API_REFERENCE.md` documents the API contract
- [ ] `docs/ARCHITECTURE.md` and `docs/SCENARIOS.md` are included for reviewers

## Monitoring and Health

- Validate deployment by calling `GET /health`.
- Review logs for startup errors and request handling.
- For container platforms, use the provided service logs and health check features.

## Notes

- This project is intentionally lightweight to fit within free-tier constraints.
- The app can be extended with persistent storage or cloud logging once the POC is validated.
