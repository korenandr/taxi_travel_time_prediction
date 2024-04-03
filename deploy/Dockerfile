FROM python:3.12.2-slim-bullseye as prod

# Installing poetry
RUN pip install poetry==1.8.2

# Configuring poetry
RUN poetry config virtualenvs.create false

# Copying requirements of a project
COPY pyproject.toml poetry.lock /app/src/
WORKDIR /app/src

# Installing requirements
RUN poetry install --only main

# Copying actuall application
COPY . /app/src/
RUN poetry install --only main

CMD ["/usr/local/bin/python", "-m", "taxi_travel_time_prediction"]

FROM prod as dev

RUN poetry install
