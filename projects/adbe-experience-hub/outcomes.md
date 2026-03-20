# Experience Hub — Outcomes

## Analysis: 2026-03-20

*Source: ~91 Adobe Analytics (CJA) dashboard screenshots taken March 20, 2026. Data spans May 2025 through March 2026. GA was August 26, 2025 — this read is 7 months post-launch.*

---

### State of the product

Experience Hub is a functioning home screen that has not yet become the AI front door it is supposed to be. The base product works: ~4,930 weekly active users, a 70%+ repeat rate, and reasonable engagement with Navigation and Quick Actions. Users who land on Experience Hub come back. That is genuinely good for a 7-month-old product sitting on top of an established AEM user base that has its own inertia. But the AI story — the actual strategic bet — is not landing. Agent usage across all tracked AI features sits in the 0.04%–0.06% range. AI Capabilities (Storage Hints, handcrafted prompts) have sub-1% engagement. If the goal is to make Experience Hub the surface where AEM agents get adopted at scale, the current data says we are not close. The gap between the base product health and the AI feature engagement is the defining signal in this dashboard.

---

### Metrics that matter (track weekly)

**1. Weekly Active Users (WAU)**
Currently ~4,930. The one number that tells you whether the product is alive. Watch it week over week. Any sustained decline below 4,000 is a red flag; growth above 6,000 signals adoption momentum.

**2. Repeat user rate**
Currently 70%+. Repeat users run roughly 10,400–11,200 in any measured period against 14,900–15,400 total active users. This is the stickiness signal. If repeat rate drops, the product is losing retention. If it holds while WAU grows, you are acquiring and keeping users.

**3. Adoption funnel penetration (AEM base → EH active)**
The adoption funnel screenshot shows a 3-segment bar: a large green block (~60–70%), a medium teal block (~20–30%), and a small gray block (~10–20%). Without knowing the exact definitions, this likely maps to: exposed to EH / ever visited, actively using, and deeply engaged. That means roughly 70–80% of the AEM base has been exposed but only 20–30% are active at any level. The gap between exposed and active is the conversion problem.

**4. AI/Agent interactions**
The number that matters most strategically, currently the worst performing. AI Agents Roles behavior is running at 0.04%–0.06%. "Events since GA" for agent interactions showed 21 as a summary metric for Jun–Sep 2025. These numbers are too small to treat as a normal adoption curve. This is near-zero usage of the flagship product direction.

**5. Navigation depth (beyond landing)**
Navigation events by persona show 10%–60% engagement ranges — meaning a meaningful portion of users are clicking into the navigation and going somewhere. This is the health check for whether Experience Hub is actually being used as a hub or just a landing page that gets immediately exited.

---

### What to skip

**Per-shortcut click breakdowns.** There are multiple screenshots tracking individual shortcut clicks, split by persona, by date, by segment. Useful for UX decisions, not worth Director-level attention unless a specific shortcut is dying or spiking.

**Individual prompt text analytics.** The submitted prompts table is many pages long and tracks the text of every prompt submitted. This is input data for improving prompt quality, not a weekly exec signal.

**Announcement widget raw event counts.** The announcements section shows views and impressions by date going back to September 2025. The CTR (0.30%–2.22%) is the only number worth tracking from this section — and it only matters if you are actively using announcements for adoption campaigns.

**Per-persona navigation event granularity.** The navigation by persona tables go deep. Good input for Eugene (UX) on what to redesign. Not worth pulling into a weekly read.

---

### What looks good

**Stickiness is real.** 70%+ repeat rate is not a small thing. Most enterprise SaaS home screens see significant drop-off after first contact. The fact that a majority of users who come to Experience Hub come back regularly means the core UX is working. That foundation is worth protecting.

**Navigation and Quick Actions are being used.** Engagement rates of 10%–60% across navigation events by persona signal that users are interacting with the product, not just landing and bouncing. The base behavior the product was designed for — giving people a faster way in — appears to be working.

**Announcement CTR in range.** Up to 2.22% CTR on in-product announcements (Sep–Oct 2025 data) is at the high end of normal for enterprise in-app messaging. If you run an agent adoption campaign through announcements, you have an audience that pays attention.

---

### What's alarming

**AI agent engagement is near zero.** This is the main finding. AI Agents Roles behavior logged at 0.04%–0.06%. AI Capabilities features (Storage Hints from Extension, handcrafted prompt experiments) at sub-1%. A metric that reads "Events since GA: 21" for a multi-month period is not a slow start — it is a signal that something fundamental is broken in the AI discovery and delivery path. Given what we know about 40–50% agent failure rates, this is likely a quality problem as much as a discoverability problem. Users may be trying agents and abandoning because the responses are poor. The data cannot distinguish between "users are not finding agents" and "users found agents and gave up" — but either way, the outcome is the same.

**Adoption funnel gap.** Only 20–30% of the AEM base is actively using Experience Hub at any level, 7 months post-GA. AEM has a large installed base with deep muscle memory around existing UIs. If Experience Hub is going to become the default starting point, the product needs a conversion narrative for the 70–80% who have been exposed but are not active. The dashboard does not show what is happening to those users after first touch.

**AI Capabilities experiments have not validated.** The Try Before You Buy and Storage Hints experiments show up in the data but with engagement so low they are not informative. Running experiments at these volumes means we cannot learn. You need minimum viable traffic to get a signal — and right now the AI features do not have it.

---

### Story to tell upward

Experience Hub has a working base. Users are coming and returning. The home screen does what a home screen should do. That is a credible foundation.

But the next chapter — agents through Experience Hub — does not have evidence yet. Seven months post-GA, agent interactions are in the dozens. This is not a distribution problem; there are 4,900 weekly active users in the product. It is a quality and experience problem. Agents fail 40–50% of the time, the prompt discovery path is not obvious, and nothing in the data suggests users are finding and trusting AI features yet.

The honest version of the upward story: Experience Hub bought us the user base. Now we have to earn their trust on AI. The path is not pushing adoption of broken experiences — it is fixing agent quality first, making the prompt interaction feel reliable, and then using Experience Hub's reach (70%+ repeat, active navigation, 4,900+ weekly users) to drive agent discovery at scale. The product is a front door. Right now the AI rooms inside the house are not ready for guests. The work for 2026 is finishing the rooms.

This framing gives leadership something real: a clear problem statement, a sequenced plan, and a PM who is calling the situation accurately instead of spinning the early numbers. That is the kind of read Bertrand and Loni should hear from a new PM taking over a product with a visibility problem.

---
