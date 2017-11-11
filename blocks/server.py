import http.server
import socketserver

def start():
    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(('127.0.0.1', PORT), Handler) as httpd:
        print('serving at port', PORT)
        httpd.serve_forever()
