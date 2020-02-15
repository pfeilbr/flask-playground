
# flask-playground

learn [flask](https://www.palletsprojects.com/p/flask/), the python web application framework

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
```