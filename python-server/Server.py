import http.server as hs;
import ResponseGenerator as ResGen;

global rg;

class CustomHandler(hs.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200);
        self.send_header("content-type","application/json");
        self.send_header("encoding","utf-8");
        self.end_headers();

        path = self.path;
        if path == "/sample":
            data = rg.getSample();
            self.wfile.write(bytes(data,encoding="utf-8"));
        else:
            self.wfile.write(bytes("[ERROR] Bad Path",encoding="utf-8"));
        return;

    def do_POST(self):
        return;

if __name__ == "__main__":
    address = ("",1337);
    http_daemon = hs.HTTPServer(address, CustomHandler);
    rg = ResGen.ResponseGenerator();
    try:
        print("Starting server on port 1337");
        http_daemon.serve_forever();
    except KeyboardInterrupt as ki:
        print("\nQuitting server");
        exit();