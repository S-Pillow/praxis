# Deferred work and scheduling

**No new service / existing / local first:** Direct bounded calls, in-process workers or durable SQL work records may suffice. Keep existing scheduler/queue if it fits. No queue solely for retries.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-Q01
**Name:** Cloudflare Queues
- **Tags:** hosted, queue
- **Candidate use:** Asynchronous work for compatible runtime and delivery model.
- **Constraints to check:** Delivery/ordering, ack, retry/duplicates, dead-letter, max size, batch limits, peak billing, privacy, export.
- **Official documentation pointer(s):** https://developers.cloudflare.com/queues/
- **Pricing / terms / licensing pointer(s):** https://developers.cloudflare.com/queues/platform/pricing/
- **Observation / verification state:** P2 shortlist; documentation/pricing pointers reference-only, current facts unverified.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

