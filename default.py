from flask import Flask, request, render_template
# discovered Py3 incompatibility with Flask Triangle, unicode issue
import builtins
builtins.unicode = str
# end unicode assignment to allow Flask Triangle to work with Python 3

from flask.ext.triangle import Triangle
import os, socket
from config import *

app = Flask (__name__)
Triangle(app)

@app.route('/')
def default():
    if (request.args.get('debug') == '0'):
        app.debug = False
    return render_template('default.html', is_debug=BASEDIR)

if __name__ == '__main__':
    app.debug = hostname in debug_hostnames
    app.run()
