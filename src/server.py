from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json
from cowpy import cow
# import sys


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # import pdb; pdb.set_trace()
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'''<!DOCTYPE html>
<html>
<head>
    <title> cow </title>
</head>
<body>
    <header>
        <nav>
        Click on the link to procede.
        <ul>
            <li><a href="/cowsay">cowsay</a></li>
        </ul>
        </nav>
    <header>''')
        
        elif parsed_path.path == '/cowsay':
            mutilated = cow.Mutilated()
            msg = mutilated.milk('This is a cow after running thru a combine. If you want to set your own message replace cowsay in the address bar with: cow?msg=(your message here)')
            
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(msg))

        elif parsed_path.path == '/cow':
            try:
                # import pdb; pdb.set_trace()
                text = parsed_qs['msg'][0]
                mutilated = cow.Mutilated()
                msg = mutilated.milk(text)
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'You did a bad thing')
                return
        
            self.send_response(200)
            self.end_headers()
            self.wfile.write(str.encode(msg))

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Not found')

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.send_response_only()


def create_server():
    return HTTPServer(('127.0.0.1', 3000), SimpleHTTPRequestHandler)


def run_forever():
    server = create_server()

    try:
        print('Starting server on port 3000')
        server.serve_forever()
    except KeyboardInterrupt:
        server.shutdown()
        server.server_close()


if __name__ == '__main__':
    run_forever()
