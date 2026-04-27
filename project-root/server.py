from http.server import HTTPServer, SimpleHTTPRequestHandler

class BrotliHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith(".br"):
            self.send_header("Content-Encoding", "br")
            if self.path.endswith(".js.br"):
                self.send_header("Content-Type", "application/javascript")
            elif self.path.endswith(".wasm.br"):
                self.send_header("Content-Type", "application/wasm")
            elif self.path.endswith(".data.br"):
                self.send_header("Content-Type", "application/octet-stream")
        super().end_headers()

HTTPServer(("localhost", 8000), BrotliHandler).serve_forever()