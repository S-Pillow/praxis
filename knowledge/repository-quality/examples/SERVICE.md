# Status Echo — synthetic local service README example

A loopback HTTP demo returns a constant readiness response. Illustrative only; not deployed.

Save the code below as `status_echo.py`. Run `python status_echo.py` → expected `{"status": "ready"}`.

## Setup and implementation

Use an available Python 3.12+ interpreter in a disposable directory with permission for a loopback socket. If needed, substitute the verified `python3` or `py` command. This uses the standard library, opens an ephemeral loopback listener, sends one local request and closes it. No external network, installation or hosted service.

```python
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from urllib.request import build_opener, ProxyHandler
import json

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/status":
            status, result = 200, {"status": "ready"}
        else:
            status, result = 404, {"status": "not_found"}
        data = json.dumps(result).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        pass

def main():
    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        worker = Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            opener = build_opener(ProxyHandler({}))
            url = f"http://127.0.0.1:{server.server_port}/status"
            with opener.open(url, timeout=3) as response:
                print(response.read().decode("utf-8"))
        finally:
            server.shutdown()
            worker.join(timeout=3)

if __name__ == "__main__":
    main()
```

A different route responds with HTTP 404 and not_found. Binding or request failure is not readiness. This sample does not establish live availability, authentication, persistent state or production monitoring.

## Operating boundary

For a real service README, identify supported runtime, configuration names (not secrets), trust and authentication, environment, readiness versus user outcome, data retention, logs and recovery. Link approved architecture, privacy and runbooks only when present. Provisioning or release requires separate authority; no production credentials.

### If the service is AI-backed

Document the actual model, prompt and skill versions; permitted inputs, outputs and tool actions; data flow and retention; host limitations; cost and quota bounds; and how evaluation differs from tracing. These are additional profile requirements when applicable, not features of Status Echo.

## Faulty contrast

“Production-ready on every cloud, 100% uptime, free forever, secure by design.” Generic badges and an unverified demo link do not establish availability, cost, security or real setup. Do not expose a debug listener or upload real data to make a demonstration work.

## Verification plan

In a disposable directory, execute the documented sample with permitted loopback. Verify the exact response, unknown route or unavailable behavior, no unintended writes, actual source and cleanup. Observe actual target rendering and first-reader interpretation separately. Illustrative output is not deployment or visual acceptance evidence.
