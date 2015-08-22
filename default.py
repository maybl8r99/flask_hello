from flask import Flask, request, render_template
# discovered Py3 incompatibility with Flask Triangle, unicode issue
import builtins
builtins.unicode = str
# end unicode assignment to allow Flask Triangle to work with Python 3

from flask.ext.triangle import Triangle
from flask.ext.sqlalchemy import SQLAlchemy

import os, socket
from config import *

app = Flask (__name__)
Triangle(app)
app.secret_key = 'my_precious'
app.config['SQLALCHEMY_DATABASE_URI'] = DBConfig.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

@app.route('/')
def default():
    if (request.args.get('debug') == '0'):
        app.debug = False
    data = {}
    data['name'] = NAME
    data['config'] = app.config
    return render_template('default.html', data=data)

if __name__ == '__main__':
    app.debug = hostname in debug_hostnames
    app.run(host="0.0.0.0", port=5000, threaded=True)
