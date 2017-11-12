from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading, json, time, hashlib, random

Block = lambda index, previousBlock, previousHash, timestamp, data: {
    'index' : index,
    'previousBlock' : previousBlock,
    'previousHash' : str(previousHash),
    'timestamp' : timestamp,
    'data' : data,
    'hash' : hashlib.sha256(str(random.random())).hexdigest()
}

getGenesisBlock = lambda : Block(0, 0, '0', int(time.time()), 'genesis block')

getNextBlock = lambda blockData: Block(
    blockData['index'] + 1,
    blockData['previousBlock'] + 1,
    blockData['hash'],
    int(time.time()),
    "new data" + str(blockData['index'] + 1)
)

blocks = [getGenesisBlock()]

class Handler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.blockchain = blocks
        return BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def do_GET(self):
        print self.path
        self.send_response(200)
        self.end_headers()
        message =  threading.currentThread().getName()

        self.blockchain.append(getNextBlock(self.blockchain[-1:][0]))

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
