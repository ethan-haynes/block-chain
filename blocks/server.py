from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading, json
from .block import Block, first_block, next_block

blocks = [ first_block() ]

class Handler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.blockchain = blocks
        return BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self):
        print self.path
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()

        self.blockchain.append(next_block(self.blockchain[-1:][0]))

        self.wfile.write(json.dumps({ 'blockchain': list(map(lambda b: str(b), self.blockchain)) }))
        self.wfile.write('\n')
        return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    '''Handle requests in a separate thread.'''

def run():
    PORT = 8080
    server = ThreadedHTTPServer(('localhost', 8080), Handler)
    print 'Starting server', PORT
    server.serve_forever()
