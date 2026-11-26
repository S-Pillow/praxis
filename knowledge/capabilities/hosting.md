# Application delivery and hosting

**No new service / existing / local first:** No hosted service for offline/local tools; retain existing approved host or self-managed static/app server if it meets deployment, maintenance and traffic needs. Distinguish static assets from server runtime and background work.

The following are independently authored discovery candidates. Verify decisive facts at use; none grants installation, access, data transfer, billing or release permission.

## CAP-H01
**Name:** Cloudflare Pages / Workers
- **Tags:** static, edge, compute
- **Candidate use:** Static front ends or bounded request processing.
- **Constraints to check:** CPU/runtime, persistent filesystem assumptions, background duration, region, request/compute billing, overage, commercial terms.
- **Official documentation pointer(s):** https://developers.cloudflare.com/workers/
- **Pricing / terms / licensing pointer(s):** https://developers.cloudflare.com/workers/platform/pricing/
- **Observation / verification state:** P2 observed pricing 2026-11-25; no current numeric facts asserted; confirm Pages-specific limits separately.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-H02
**Name:** Vercel
- **Tags:** hosting, frontend, functions
- **Candidate use:** Managed web application delivery if runtime and policy fit.
- **Constraints to check:** Commercial eligibility, runtime/duration, build/execution/network billing, hard cap vs alerts, data location and exit.
- **Official documentation pointer(s):** https://vercel.com/docs
- **Pricing / terms / licensing pointer(s):** https://vercel.com/legal/terms ; https://vercel.com/pricing
- **Observation / verification state:** 2026-11-25 official Terms and pricing search observed Hobby restricted to personal/noncommercial use; disqualify for commercial workload. Recheck terms at point of use; other terms/limits unqualified.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

## CAP-H03
**Name:** GitHub Pages
- **Tags:** static, docs
- **Candidate use:** Project documentation/static sites where intended use fits.
- **Constraints to check:** Static-only requirements, use restrictions, build limits, privacy, traffic and deployment ownership.
- **Official documentation pointer(s):** https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits
- **Pricing / terms / licensing pointer(s):** https://docs.github.com/en/site-policy/github-terms/github-terms-for-additional-products-and-features
- **Observation / verification state:** 2026-11-25 official limits and additional terms search observed restrictions on use as free commercial SaaS/e-commerce hosting; no blanket ban on all business-related pages; qualify actual use.
- **Origin and redistribution:** original Praxis discovery record; provider/source pointer only; no upstream text/code/assets redistributed. Licensing/terms for adoption require exact scope qualification.

