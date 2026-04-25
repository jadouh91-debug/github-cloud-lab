# GitHub Cloud Lab

Projekt wykonany do cwiczen: GitHub as a Cloud Solution.

Autor: Hasan Jadou 70421

## Co jest w projekcie

- hello.py - prosty plik z funkcjami greet i farewell
- src/calculator.py - modul kalkulatora
- tests/test_calculator.py - testy pytest
- .github/workflows/ci.yml - prosty workflow CI
- .github/workflows/pipeline.yml - pelny workflow CI/CD
- Dockerfile - obraz do testow
- webapp/ - aplikacja Flask
- docker-compose.yml - aplikacja Flask z Redis
- k8s/ - pliki Kubernetes
- setup.cfg - konfiguracja flake8
- SPRAWOZDANIE.md - krotki opis wykonania zadan

## Uruchomienie testow

```bash
pip install -r requirements.txt --break-system-packages
python -m pytest tests/ -v
```

## Uruchomienie aplikacji Docker Compose

```bash
docker compose up -d --build
curl http://localhost:5000/
curl http://localhost:5000/health
docker compose down
```

## Kubernetes

```bash
minikube start --driver=docker
eval $(minikube docker-env)
docker build -t webapp:v1 webapp/
kubectl apply -f k8s/
minikube service webapp --url
```
