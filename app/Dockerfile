# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM python:3.14.0a6-alpine3.21

WORKDIR /app

COPY pip.conf /etc/pip.conf

COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --trusted-host host.docker.internal -r requirements.txt

RUN rm /etc/pip.conf

RUN adduser -D dycel-user

USER dycel-user

COPY . /app

HEALTHCHECK CMD curl --fail http://localhost:8000 || exit 1

ENTRYPOINT ["python3"]
CMD ["app.py"]
