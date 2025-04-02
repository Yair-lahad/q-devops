from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from Git-to-Kubernetes pipeline!")

if __name__ == "__main__":
    HTTPServer(("", 8000), Handler).serve_forever()
