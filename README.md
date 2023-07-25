# PyTSys
A (Python) Pipelines Toolkit System

gitHub: https://github.com/lquirod/PyTSys

## Installing
Clone repository:
$ git clone https://github.com/lquirod/PyTSys

Create and activate virtual environment:
$ cd PyTSys/
$ python3 -m venv venv/
$ source venv/bin/activate

	Cuando el entorno esté activado se indicará en nuestro terminal como
$ (venv) myuser:path$

Install requirements:
$ pip3 install -r requirements.txt

Install flask application:
$ pip install -e .

Execute:
$ flask --app PyTSys_web run


<!-- 
En Linux/Mac:
export FLASK_ENV="development"
En Windows:
set "FLASK_ENV=development"

export FLASK_APP="tests/webTests/mainTest.py"
deactivate
source venv/bin/activate
export FLASK_ENV="development"
export FLASK_APP="mainWeb.py" 
flask run --debug
flask run
pip install -e .
flask --app PyTSys_web run --debug
-->