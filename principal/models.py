# Models Basado en GAE
from google.appengine.ext import db

import os

class Proyecto(db.Model):
	autor = db.UserProperty()
	nombre = db.StringProperty()
	descripcion = db.StringProperty(multiline=True)
	fecha = db.DateTimeProperty(auto_now_add=True)



