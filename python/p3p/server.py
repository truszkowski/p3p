#-*- coding: utf-8 -*-

import gevent

def serve(socket, address):
	print ('New connection from %s:%d' % address)

	socket.settimeout(10.0)
	f = socket.makefile()

	while True:
		msg = f.readline()
		if not msg:
			print ('Client %s:%d disconnected' % address)
			break

		print ('received, %d: %r' % (len(msg), msg))
		f.write('OK %s' % msg)
		f.flush()
