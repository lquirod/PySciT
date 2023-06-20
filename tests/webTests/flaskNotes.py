# https://j2logo.com/tutorial-flask-espanol/
# https://scikit-learn.org/stable/user_guide.html

from flask import Flask, render_template, url_for
# Instancia WSGI de la clase Flask llamada app (aplicación)
# Necesario para que Flask sepa donde encontrar las plantillas de nuestra aplicación o los ficheros estáticos.
app = Flask(__name__)       # 1º argumento: nombre del módulo o paquete de la aplicación, con palabra reservada __name__.

# Método que asocia las URLs que componen nuestra aplicación. Se correspondería con el controlador de un MVC.
@app.route('/')             #  Función hello_world que será invocada cada vez que se haga una petición a la URL raíz de nuestra aplicación.
def hello_world():
    return 'Hello, World! <h1>Mensaje</h1>'
# El decorador route de la aplicación (app) es el encargado de decirle a Flask qué URL debe ejecutar su correspondiente función.
# El nombre que le demos a nuestra función será usado para generar internamente URLs a partir de dicha función (esto lo veremos más adelante).
# Finalmente, la función debe devolver la respuesta que será mostrada en el navegador del usuario.

print(url_for("show_post", slug="leccion-1", preview=True))

# para formularios
@app.route("/signup/", methods=["GET", "POST"])
def show_signup_form():
    return render_template("signup_form.html")

# En Linux/Mac se encuentra en source env/bin/activate. Al final del fichero añadimos lo siguiente:
# $ export FLASK_APP="run.py"
# En Linux/Mac se encuentra en env/bin/activate. Al final del fichero añadimos lo siguiente:
# En Windows se encuentra en env\Scripts\activate.bat. Al final del fichero añadimos lo siguiente:
# $ set "FLASK_APP=run.py"
# Para que los cambios realizados se tengan en cuenta debemos salir del entorno Python y volver a entrar. Para salir, hay que ejecutar en el terminal deactivate.
# Luego flask run o python -m flask run

# Si queremos cambiar el puerto por cualquier motivo lo podemos hacer de dos formas distintas:
# Estableciendo la variable de entorno FLASK_RUN_PORT en un puerto diferente.
# Indicando el puerto al lanzar el servidor flask run --port 6000.
# Para aceptar peticiones de otros ordenadores de nuestra red lanzaremos el servidor de la siguiente manera:
# $ flask run --host 0.0.0.0

# Modo debug
# Flask viene con un modo debug que es muy útil usar mientras estamos desarrollando, ya que cada vez que hagamos un cambio en nuestro código reiniciará el servidor y no tendremos que hacerlo manualmente para que los cambios se tengan en cuenta.
# Para activar el modo debug simplemente hay que añadir la variable de entorno FLASK_ENV y asignarle el valor development.
# En Linux/Mac:
# export FLASK_ENV="development"
# En Windows:
# set "FLASK_ENV=development"
# export FLASK_APP="tests/webTests/mainTest.py"
# deactivate
# source venv/bin/activate
# export FLASK_ENV="development"
# export FLASK_APP="mainWeb.py" 
# flask run --debug
# flask run
# pip install -e .
flask --app PyTSys run