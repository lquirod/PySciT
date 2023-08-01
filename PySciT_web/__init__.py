from flask import Flask
import PySciT_web.mainWeb
app = Flask(__name__)

import PySciT_web.mainRoutes
import PySciT_web.operations