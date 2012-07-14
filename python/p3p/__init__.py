#-*- coding: utf-8 -*-

import sys
import getopt
import gevent

from gevent.server import StreamServer

import p3p.client
import p3p.server

def serve(socket, address):
	p3p.server.serve(socket, address)

def start(argv):
	try:
		opts, args = getopt.getopt(argv, 'sca:p:', ['server','client','address','port'])
	except getopt.GetoptError, e:
		print ('Error: %r' % e)
		sys.exit(1)

	server = True
	address = '127.0.0.1'
	port = 6060

	for o, a in opts:
		if o in ('-s', '--server'):
			server = True
		elif o in ('-c', '--client'):
			server = False
		elif o in ('-a', '--address'):
			address = a
		elif o in ('-p', '--port'):
			port = a
		else:
			assert False, 'unhandled option'
	
	if server:
		server = StreamServer((address, port), p3p.server.serve)
		print ('Starting server on %s:%d' % (address, port))
		server.serve_forever()
	else:
		print ('%r' % p3p.client.ask((address, port), args))
		
