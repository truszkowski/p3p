#-*- coding: utf-8 -*-

import gevent
from gevent import socket

def ask(address, args):
	print ('Connecting to %s:%d...' % address)

	conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
	conn.settimeout(10.0)
	conn.connect(address)
	f = conn.makefile()
	
	answers = []
	for arg in args:
		f.write(arg + '\n')
		f.flush()
		msg = f.readline()
		if not msg:
			print ('Server %s:%d disconnected' % address)
			break

		print ('Gotta answer, %d: %r' % (len(msg), msg))
		answers.append(msg)

	return answers
	
