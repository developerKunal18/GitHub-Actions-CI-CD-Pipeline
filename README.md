# GitHub Actions CI/CD Pipeline

Automated CI/CD pipeline for a Python Flask project.

## Pipeline

```text
Git Push
   ↓
GitHub Actions
   ↓
Install Dependencies
   ↓
Run Pytest
   ↓
Code Coverage
   ↓
Security Audit
   ↓
Docker Build
```

## Technologies

- Python
- Flask
- Pytest
- GitHub Actions
- Docker
- Coverage.py

## Local Testing

```bash
pip install -r requirements.txt
pytest
```

## Coverage

```bash
pytest --cov=app --cov-report=term-missing
```

## Docker

```bash
docker build -t api-testing-framework .
```

## CI

Every push to `main` and every pull request targeting `main` triggers the GitHub Actions pipeline.

## Purpose

Day 302 demonstrates automated testing, code coverage, security auditing, Docker builds, and CI/CD using GitHub Actions.
