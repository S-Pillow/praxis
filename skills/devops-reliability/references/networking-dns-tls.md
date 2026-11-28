# Networking, DNS and TLS

Use only applicable cards. Examples are synthetic and unexecuted. Source IDs resolve through [SOURCES](../SOURCES.md); provider facts must be verified at use.

## DO-D16 — At which layer does a network symptom arise?

**Applicability / context:** Existing named permitted target, failing request and time; capture expected host/port/protocol and client/network context. Avoid broad probing.

**Decision and alternatives:** Compare authoritative DNS and the client's recursive resolver (CNAME chain, A/AAAA, TTL, negative cache) before inferring propagation; then connection route/port, TLS SNI/hostname/trust/expiry, HTTP proxy/routing/headers, app and dependency latency. Use existing logs, config, target-scoped lookup or safe request only when authorized. Keep competing hypotheses until a discriminating observation. No public zone, firewall, ingress or certificate mutation based on guess.

**Counterexample:** Client timeout due to upstream app while DNS resolves; success on one resolver does not prove all clients updated. Disabling certificate verification is not a fix.

**Observable verification:** Compare actual DNS responses and exact endpoint, connect/TLS and user request outcomes at permitted vantage points; note cache/time, missing logs and limitations. Verify recovery at original failing client path.

**Sources and limits:** DO-S02 (network notes), DO-S14–18; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.

## DO-D17 — What should DNS/TLS and routing changes protect?

**Applicability / context:** Authorized hostname, DNS ownership, reverse proxy/load balancer, cert/renewal, application routing or network policy.

**Decision and alternatives:** Use approved existing provider/ingress; identify authoritative zone, record owner and rollback values, TTL timing, host/path routing, TLS certificate chain and renewal authority. Keep private services private and preserve access/redirect/auth. Test each affected hostname/path, don't open wide ports or bypass security to diagnose. Separate desired DNS change from actual authoritative and client observations.

**Counterexample:** Certificate valid for another hostname or proxy serves default host; making a database public fixes connectivity but violates trust boundary.

**Observable verification:** Observe intended record and unaffected records, resolution, certificate hostname/chain, real authorized client request and forbidden access negative case; document unobserved regions or caches.

**Sources and limits:** DO-S02, DO-S03, DO-S18, DO-S50; retained source-level observations, not selected or executed tools. For general engineering synthesis, use approved project context and qualify any version-sensitive claim.
