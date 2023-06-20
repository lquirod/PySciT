from flask import Flask

import PyTSys_web
import PyTSys_web.home as h

app = Flask(__name__)       # 1º argumento: nombre del módulo o paquete de la aplicación, con palabra reservada __name__.

h.hola()