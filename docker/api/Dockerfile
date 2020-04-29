# Faz o build do projeto dentro do docker
FROM python:3.8-slim-buster AS build-env
MAINTAINER Waldir Borba Junior <wborbajr@gmail.com>
ARG POETRY_VERSION=1.0.5
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install poetry=="$POETRY_VERSION"
# Copia o lockfile e pyproject.toml primeiro para cachear melhor a imagem
COPY ./bpapi/pyproject.toml /bpapi/pyproject.toml
COPY ./bpapi /bpapi
WORKDIR /bpapi
RUN poetry build

# Instala e roda o projeto já empacotado
FROM python:3.8-slim-buster AS exec-env
MAINTAINER Waldir Borba Junior <wborbajr@gmail.com>
COPY --from=build-env /bpapi/dist .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install *.whl
WORKDIR /bpapi
CMD ["uvicorn", "bpapi.main:app", "--host", "0.0.0.0", "--port", "9090", "--reload"]
