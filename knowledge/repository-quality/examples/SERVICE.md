# Example: Status Echo (synthetic service/AI profile)

Original instructional illustration, not a deployed project or real customer API. No real hostname, credential, price or uptime claim.

## Strong sample

# Status Echo

Local demonstration service that returns the status of a synthetic task. For maintainers evaluating a service boundary; no production deployment, hosted monitoring, persistent data or authentication claim. Illustrative supported setup: Python 3.12 standard library, disposable working directory, permission for a loopback socket. It starts only an ephemeral loopback listener, sends one local request and closes it. No external network, install or service provision.

Save this sample as status_echo.py:

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

Run `python status_echo.py`. Expected illustrative stdout: `{"status": "ready"}`. A different route responds with HTTP 404 and not_found; binding or request failure is not service readiness. This example describes a local endpoint, not live availability; test actual output in your environment.

### Operating boundary

For a real service README, identify supported runtime, configuration names (not secrets), trust/auth, environment, readiness vs user outcome, data retention, logs and recovery. For AI-backed service also identify model/prompt/skill version, data flow, permissions, host limits, costs and actual evaluation vs trace. Link approved architecture, privacy and runbook only when present. Separate authority for provisioning or release; no production credentials.

## Faulty contrast

“Production-ready on every cloud, 100% uptime, free forever, secure by design.” Generic badge and unverified demo link do not establish availability, cost, security or real setup. Do not expose debug listener or upload real data to make the demonstration work.

## Verification plan

In a disposable directory, execute the documented sample with permitted loopback; verify exact response, nonready/unknown-route or unavailable behavior, no unintended writes, actual source and cleanup. Observe actual rendering and first-reader interpretation separately. Source alone does not prove execution or visual quality.
