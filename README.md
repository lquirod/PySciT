# PySciT
A (Python) Pipelines Toolkit System

gitHub: https://github.com/lquirod/PySciT

## Installing
Clone repository:
$ git clone https://github.com/lquirod/PySciT

Create and activate virtual environment:

	$ cd PySciT/
	$ python3 -m venv venv/
	$ source venv/bin/activate

Changed to:

	$ (venv) myuser:path$

Install requirements:

	$ pip3 install -r requirements.txt

Install flask application:

	$ pip install -e .

Execute:

	$ flask --app PySciT_web run


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
flask --app PySciT_web run --debug
-->