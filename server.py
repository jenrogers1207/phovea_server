__author__ = 'Samuel Gratzl'

import os
import os.path
import sys

sys.path.append('plugins/')
print os.getcwd()
import caleydo_server.config

#append the plugin directories as primary lookup path
sys.path.extend(caleydo_server.config.getlist('pluginDirs','caleydo_server'))


#set configured registry
import caleydo_server.plugin

import dispatcher
import mainapp

#helper to plugin in function scope
def _loader(p):
  print 'add application: ' + p.id + ' at namespace: ' + p.namespace
  return lambda: p.load().factory()

#create a path dispatcher
_applications = { p.namespace : _loader(p) for p in caleydo_server.plugin.list('namespace') }

#create a dispatcher for all the applications
application = dispatcher.PathDispatcher(mainapp.default_app(), _applications)
from werkzeug.contrib.fixers import ProxyFix

application = ProxyFix(application)

def run():
  import argparse
  parser = argparse.ArgumentParser(description='Caleydo Web Server')
  parser.add_argument('--multithreaded' ,action='store_true', help='multi threaded using gevent')
  parser.add_argument('--port', '-p', type=int, default=caleydo_server.config.getint('port','caleydo_server'), help='server port')
  parser.add_argument('--address', '-a', default=caleydo_server.config.get('address','caleydo_server'), help='server address')
  parser.add_argument('--use_reloader', action='store_true', help='whether to automatically reload the server')
  args = parser.parse_args()

  if args.multithreaded or caleydo_server.config.getboolean('multithreaded','caleydo_server'):
    print 'run multi-threaded'
    from geventwebsocket.handler import WebSocketHandler
    from gevent.wsgi import WSGIServer

    http_server = WSGIServer((args.address, args.port), application, handler_class=WebSocketHandler)
    http_server.serve_forever()
  else:
    print 'run single-threaded'
    from werkzeug.serving import run_simple
    run_simple(args.address, args.port, application, use_reloader=args.use_reloader or caleydo_server.config.getboolean('use_reloader','caleydo_server'))