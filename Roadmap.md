# Project roadmap for the distributed-system-diagnostics portfolio repo
# This file is intended to capture the roadmap, milestones, and scope.
# It replaces the earlier conversation export content.

# Project Roadmap

## Project Vision
A lightweight diagnostics toolkit for distributed transaction systems. The goal is to demonstrate forward deployed engineering skills by building a deployable reconciliation and root-cause analysis service that works with synthetic transaction data and requires minimal infrastructure.

## Problem Statement
Three systems—payment processor, ledger, and settlement—often disagree on transaction state, amount, or timing. The tool should detect mismatches, classify the root cause, and provide remediation guidance so teams can quickly resolve reconciliation issues without deep backend access.

## Scope
- Build an API-driven diagnostics engine using FastAPI
- Simulate transaction records across three systems
- Detect timing lag, duplicate records, missing settlements, amount mismatches, and data quality issues
- Add CI automation, Docker deployment, and clear documentation

## Week 1: MVP Foundation

### Day 1-2: Architecture and setup
- Define repository layout and requirements
- Create the Python FastAPI app with a simple `/diagnose` endpoint
- Add documentation skeleton in `docs/`
- Add local development support with `requirements.txt` and a venv

### Day 3-5: Core reconciliation engine
- Implement transaction matching across payment processor, ledger, and settlement
- Add diagnostics classification and confidence scoring
- Create unit tests for each mismatch scenario
- Add sample API requests and responses in documentation

### Day 6-7: Initial deployment readiness
- Add Dockerfile and `docker-compose.yml`
- Add GitHub Actions workflow for automated testing
- Ensure local tests pass and the app starts successfully

## Week 2: Enhanced diagnostics and polish

### Day 8-10: Advanced diagnosis
- Add richer root-cause categories such as duplicate transaction, amount mismatch, timing lag, and malformed data
- Add remediation guidance for each category
- Improve simulator and scenario coverage in `docs/SCENARIOS.md`

### Day 11-12: Integration and CI/CD
- Add GitHub Actions workflow to run tests on push and pull request
- Update README with CI badge and running instructions
- Add deployment documentation for Docker and optional free hosting

### Day 13-14: Portfolio polish
- Review documentation for clarity and recruiter-ready language
- Add roadmap and architecture summary
- Add sample requests and scenario explanations

## Milestones
1. MVP API and reconciliation engine
2. Diagnostics classification and scenario tests
3. Docker deployment and CI workflow
4. Documentation and portfolio polish

## Repository structure
```
distributed-system-diagnostics/
├── README.md
├── Roadmap.md
├── docs/
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   ├── DEPLOYMENT.md
│   └── SCENARIOS.md
├── src/
│   ├── __init__.py
│   ├── api.py
│   ├── diagnostics.py
│   ├── reconciler.py
│   └── simulator.py
├── tests/
│   ├── test_diagnostics.py
│   ├── test_reconciler.py
│   └── test_simulator.py
├── docker-compose.yml
├── Dockerfile
├── .github/
│   └── workflows/
│       └── python-ci.yml
├── requirements.txt
└── LICENSE
```

## Next steps
- Commit this roadmap and CI workflow
- Push changes to GitHub
- Add README badge for the workflow and verify the repo build
- Continue by improving scenario coverage and adding a `/simulate` endpoint
