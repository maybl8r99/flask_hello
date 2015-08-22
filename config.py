import socket, os


basedir = os.path.abspath(os.path.dirname(__file__))
BASEDIR = basedir
NAME = __name__

hostname = socket.gethostname()
debug_hostnames = ['EastWind-Server.local',]

class DBConfig():
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, __name__+'.sqlite')
