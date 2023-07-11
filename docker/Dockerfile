FROM python:3.9-slim-bullseye
WORKDIR /usr/src/app

# Install and Configure Poetry
ENV POETRY_VERSION=1.4.2
ENV POETRY_HOME=/opt/poetry
RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/opt/poetry/bin:$PATH"
RUN poetry config virtualenvs.in-project true

# Setup project
RUN mkdir my_plugin; touch my_plugin/__init__.py
COPY pyproject.toml poetry.lock README.md ./
COPY ./docker/default.yml ./

RUN poetry install --without=dev

COPY ./my_plugin my_plugin

ENTRYPOINT ["poetry", "run", "aca-py"]
CMD ["start",  "--plugin", "my_plugin", "--arg-file", "default.yml"]
