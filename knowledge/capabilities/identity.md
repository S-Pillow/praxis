# Identity and account services

**No new service / existing / local first:** Avoid accounts for local single-user tools where appropriate. Reuse approved identity provider; consider self-hosted identity only if the team can maintain it. Do not implement bespoke password handling merely to avoid a service.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-I01
**Name:** Supabase Auth
- **Tags:** auth, identity
- **Candidate use:** Candidate authentication when platform and application trust boundaries are suitable.
- **Constraints to check:** Tenant isolation, session expiry, recovery, MFA/SSO, account/export/deletion, MAU billing, data location, legal terms.
- **Official documentation pointer(s):** https://supabase.com/docs/guides/auth
- **Pricing / terms / licensing pointer(s):** https://supabase.com/pricing
- **Observation / verification state:** P2 candidate/price pointer; product-specific feature and limits unverified; no accounts enabled.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

