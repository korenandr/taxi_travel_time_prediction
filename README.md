# taxi_travel_time_prediction

This project was generated using fastapi_template.

## Poetry

This project uses poetry. It's a modern dependency management
tool.

To run the project use this set of commands:

```bash
poetry install
poetry run python -m taxi_travel_time_prediction
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f deploy/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "taxi_travel_time_prediction"
taxi_travel_time_prediction
├── conftest.py  # Fixtures for all tests.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "TAXI_TRAVEL_TIME_PREDICTION_" prefix.

For example if you see in your "taxi_travel_time_prediction/settings.py" a variable named like
`random_parameter`, you should provide the "TAXI_TRAVEL_TIME_PREDICTION_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `taxi_travel_time_prediction.settings.Settings.Config`.

An example of .env file:
```bash
TAXI_TRAVEL_TIME_PREDICTION_RELOAD="True"
TAXI_TRAVEL_TIME_PREDICTION_PORT="8000"
TAXI_TRAVEL_TIME_PREDICTION_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/

## Kubernetes
To run your app in kubernetes
just run:
```bash
kubectl apply -f deploy/kube
```

It will create needed components.

If you haven't pushed to docker registry yet, you can build image locally.

```bash
docker-compose -f deploy/docker-compose.yml --project-directory . build
docker save --output taxi_travel_time_prediction.tar taxi_travel_time_prediction:latest
```


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.


2. Run the pytest.
```bash
pytest -vv .
```

## Build and save docker image
```bash
docker-compose -f deploy/docker-compose.yml -f deploy/docker-compose.dev.yml --project-directory . build
docker save --output taxi_travel_time_prediction.tar taxi_travel_time_prediction:latest
```


## Setup minikube cluster
```bash
minikube start --addons=ingress --vm=true --namespace="taxi-travel-time-prediction"
minikube image load ./taxi_travel_time_prediction.tar
kubectl apply -f deploy/kube/namespace.yml
kubectl apply -f deploy/kube/app.yml
```


## Check that everything is good
```bash
kubectl get pods
kubectl logs <your pod id> -f
kubectl describe ingress
```


## Test request
```bash
curl -X POST $(minikube ip)/api/echo/ -H "Host: taxi-travel-time-prediction.local" -H "accept: application/json" -H "Content-Type: application/json" -d '{"message": "Hello, world!"}'
```
