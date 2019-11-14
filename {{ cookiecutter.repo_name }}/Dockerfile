FROM python:3.7-slim

WORKDIR {{ cookiecutter.repo_name }}/

# add environment variables if you want
ENV GOOGLE_APPLICATION_CREDENTIALS ./credentials/google-credential.json

RUN set -x \
  && apt-get update -yqq \
  && apt-get upgrade -yqq \
  && apt-get install -yqq --no-install-recommends \
    git \
    curl \
    build-essential \
    python-dev \
    apt-utils \
    libsndfile-dev \
    gcc \
    cmake \
    libyaml-dev

COPY ./ ./

RUN pip3 install pipenv \
  && pipenv --python 3.7 \
  && pipenv sync --dev \
  && pipenv run develop \
  && rm -rf /var/lib/apt/lists/*


CMD ["/bin/bash", "-c", "echo 'python container"]

