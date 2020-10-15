# Deploy ML models

It's just an interface for interacting with the machine learning model

## Prerequisites

Install ```docker``` and ```docker-compose```

- Linux

    ```
    sudo apt-get install docker docker-compose
    ```

- MacOS

    ```
    brew install docker docker-compose
    ```

## Install

Clone this repository and go to cloning folder

```
git clone https://github.com/ChesnovAE/jupyter_docker.git && cd jupyter_docker
```

Now you need to build docker container

```
docker-compose build
```

## Usage

Start your container with command

```
docker-compose up -d
```

By defaults project starts in port ```5000```. If you need to run it on another port, you can change port in file run.py

```python
from app import app


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=...)
```