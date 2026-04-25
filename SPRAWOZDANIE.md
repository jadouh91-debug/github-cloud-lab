# Sprawozdanie

Nazwa: Hasan Jadou 70421-GitHub

## Cel

Celem bylo przygotowanie praktycznych cwiczen pokazujacych GitHub jako rozwiazanie chmurowe. Projekt obejmuje Git, GitHub Actions, Docker, Docker Compose, Kubernetes, Minikube, Helm oraz GitHub Container Registry.

## Zadanie 1

Przygotowano plik hello.py. Zawiera funkcje greet oraz farewell. W normalnej pracy na GitHub nalezy wykonac branche feature/hello-world oraz feature/farewell, otworzyc Pull Request i polaczyc zmiany do main.

## Zadanie 2

Dodano modul src/calculator.py oraz testy w tests/test_calculator.py. Dodano workflow .github/workflows/ci.yml. Workflow uruchamia testy i buduje obraz Docker.

## Zadanie 3

Dodano aplikacje Flask w folderze webapp. Dodano Dockerfile oraz docker-compose.yml. Aplikacja korzysta z Redis i pokazuje licznik odwiedzin.

## Zadanie 4

Dodano manifesty Kubernetes w folderze k8s. Sa tam Deployment i Service dla webapp oraz Redis. Projekt mozna uruchomic lokalnie w Minikube.

## Zadanie 5

Dodano pelny pipeline .github/workflows/pipeline.yml. Pipeline robi lint, testy, budowanie i wypchniecie obrazu do ghcr.io, skan Trivy oraz symulacje wdrozenia na staging. Dodano tez upload artifact z wynikami testow.

## Jak sprawdzic

1. Otworz repozytorium w GitHub Codespaces.
2. Uruchom testy: python -m pytest tests/ -v.
3. Uruchom aplikacje: docker compose up -d --build.
4. Sprawdz Kubernetes: minikube start --driver=docker, potem kubectl apply -f k8s/.
5. Wypchnij projekt na GitHub i sprawdz zakladke Actions.

## Uwaga

W tym ZIP sa przygotowane pliki projektu. Operacje wymagajace konta GitHub, takie jak otwieranie Pull Request, tworzenie Issue, zatwierdzanie Environment i publikowanie paczki do ghcr.io, trzeba wykonac na swoim koncie GitHub.
