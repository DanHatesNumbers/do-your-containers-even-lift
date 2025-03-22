# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.14.0a6-alpine3.21

WORKDIR /app

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=secret,id=pipconf,target=/root/.config/pip/pip.conf \
    pip3 install --trusted-host host.docker.internal -r requirements.txt

RUN adduser -D dycel-user

USER dycel-user

COPY . /app

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT ["python3"]
CMD ["app.py"]
