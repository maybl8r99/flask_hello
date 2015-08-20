from flask import Flask, request
import socket

app = Flask (__name__)

hostname = socket.gethostname()
debug_hostnames = ['EastWind-Server.local',]

@app.route('/')
def default():
    if (request.args.get('debug') == '0'):
        app.debug = False
    return 'Hello world.\n' + hostname + ' debug mode is ' + str(app.debug)

if __name__ == '__main__':
    app.debug = hostname in debug_hostnames
    app.run()
