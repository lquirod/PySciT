from flask import Flask
import PyTSys_web.mainWeb
app = Flask(__name__)

import PyTSys_web.mainRoutes
import PyTSys_web.operations