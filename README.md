
# flask-playground

learn [flask](https://www.palletsprojects.com/p/flask/), the python web application framework

* [`server.py`](server.py) - flask server
* [`client.py`](client.py) - http client.  uses `requests` to POST the [`image.jpeg`](image.jpeg) image file
* [`load-test.sh`](load-test.sh) - load test via parallel requests

## Prerequisites

* [pipenv](https://pipenv.kennethreitz.org/) for python environment/packages

## Running

```sh
# install all dependencies
pipenv install --dev

# load python enviroment
pipenv shell

# run server in debug (livereload - reload on file changes) mode
FLASK_DEBUG=1 FLASK_RUN_PORT=5000 FLASK_APP=server.py flask run

# run client
python client.py

# load test
chmod +x load-test.sh
./load-test.sh
```