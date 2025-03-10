## Compose sample application
### Python/Flask application

Project structure:
```
.
├── compose.yaml
├── app
    ├── Dockerfile
    ├── requirements.txt
    └── app.py

```

[_compose.yaml_](compose.yaml)
```
services: 
  web: 
    build:
     context: app
     target: builder
    ports: 
      - '8000:8000'
```

## Deploy with docker compose

```
$ docker compose up -d
[+] Building 1.1s (16/16) FINISHED
 => [internal] load build definition from Dockerfile                                                                                                                                                                                       0.0s
    ...                                                                                                                                         0.0s
 => => naming to docker.io/library/flask_web                                                                                                                                                                                               0.0s
[+] Running 2/2
 ⠿ Network flask_default  Created                                                                                                                                                                                                          0.0s
 ⠿ Container flask-web-1  Started
```

## Expected result

Listing containers must show one container running and the port mapping as below:
```
$ docker compose ps
NAME                COMMAND             SERVICE             STATUS              PORTS
flask-web-1         "python3 app.py"    web                 running             0.0.0.0:8000->8000/tcp
```

After the application starts, navigate to `http://localhost:8000` in your web browser or run:
```
$ curl localhost:8000
Hello World!
```

Stop and remove the containers
```
$ docker compose down
```

## DevPi PyPi mirror
### Setup and starting
First, ensure `pipx` is setup by following the [pipx setup docs](https://github.com/pypa/pipx).

``` shell
pipx install devpi-server devpi-client supervisor
supervisord -c supervisor-config/supervisord.conf

mkdir -p ~/.config/pip
echo << EOF >> ~/.config/pip/pip.conf
[global]
index-url = http://localhost:3141/root/pypi/+simple/
EOF
```

Then use pip as normal, and DevPi will act as a pull through cache. Remove the index-url configured in `~/.config/pip/pip.conf`

### Stopping

``` shell
supervisorctl -c supervisor-config/supervisord.conf shutdown
```
