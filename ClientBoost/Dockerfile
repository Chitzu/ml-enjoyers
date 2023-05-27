FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.14/main' >> /etc/apk/repositories
RUN apk --no-cache add \
    bash \
    curl \
    g++ \
    gcc \
    git \
    libc6-compat \
    gettext \
    freetds-dev \
    freetds \
    unixodbc-dev \
    unixodbc \
    libstdc++ \
    build-base \
    openldap=2.4.58-r0 \
    openldap-dev=2.4.58-r0 \
    python3-dev \
    zlib-dev \
    jpeg-dev \
    musl-dev

WORKDIR /code
COPY . /code/
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN python -m pip install pipenv
RUN pipenv install --deploy --system --ignore-pipfile
