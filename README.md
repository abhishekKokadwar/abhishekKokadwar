<div align="center">

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/header.svg" width="100%" alt="abhishek kokadwar. data pipelines, backend, the boundaries between systems" />

<br/>

[![Portfolio](https://img.shields.io/badge/portfolio-0d1117?style=flat-square&logo=vercel&logoColor=white&labelColor=0d1117)](https://abhikokadwar.vercel.app/)
[![LinkedIn](https://img.shields.io/badge/linkedin-0d1117?style=flat-square&logo=linkedin&logoColor=white&labelColor=0d1117)](https://www.linkedin.com/in/abhishek-kokadwar/)
[![Email](https://img.shields.io/badge/email-0d1117?style=flat-square&logo=maildotru&logoColor=white&labelColor=0d1117)](mailto:abhikokadwar2@gmail.com)
[![PyPI](https://img.shields.io/badge/pypi-0d1117?style=flat-square&logo=pypi&logoColor=white&labelColor=0d1117)](https://pypi.org/project/mcp-ztgateway/)
[![Medium](https://img.shields.io/badge/medium-0d1117?style=flat-square&logo=medium&logoColor=white&labelColor=0d1117)](https://medium.com/@abhikokadwar2)

<br/>

[![Resume](https://img.shields.io/badge/download%20résumé-1f6feb?style=for-the-badge&logo=readdotcv&logoColor=white&labelColor=0d1117)](https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/abhishek-kokadwar-resume.pdf)

</div>

<br/>

Hi, I'm Abhishek.

I actually started out building web apps, mostly because you can see what you built right away. But a couple of internships in, I noticed the part I actually cared about had quietly moved somewhere else. Not the page itself, but the schema underneath it, and how many round trips it took just to fill in a form.

So these days I spend most of my time on two things: data in motion, and trust boundaries. Basically the two places where a system is most likely to be confidently wrong without anyone noticing. A dashboard that renders perfectly off a stale aggregate. A tool server that swears it only needs to read one file.

The habit I keep trying to build is measuring things instead of assuming them. Anyone can write "real-time" in a readme. It's a lot harder to say what your watermark actually is, what happens when a packet shows up four minutes late, or what your number looks like when you go back and actually check it.

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-exp.svg" width="100%" alt="Experience" />

Two internships, remote, sole developer on both. Both shipped to a live domain — which is a different kind of pressure than a repo nobody deploys.

<table>
<tr>
<td width="32%" valign="top">

**HiGigAi**
<br/><sub>Software Developer Intern</sub>
<br/><sub>Jul 2026 – Aug 2026 · remote</sub>

<sub>`next.js` · `sanity cms`</sub>
<br/><sub>`cloudinary` · `vercel`</sub>

<sub>↗ <a href="https://www.tridentpublicschool.com/">tridentpublicschool.com</a></sub>

</td>
<td valign="top">

A one-month engagement that had to outlive me. **Five branch sites on five subdomains from a single Next.js codebase**, so onboarding a sixth branch is content entry rather than a deploy.

25+ Sanity schemas with the Studio scoped through Structure Builder — the part that actually mattered: five branch admins manage 15+ page types with zero developer involvement, including mine.

Recurring infra came to **$0/month**. A planned Supabase tier replaced with Sanity-native forms and Cloudinary media, ISR plus webhooks for redeploy-free publishing. The cheapest thing to operate is the thing you didn't provision.

</td>
</tr>
<tr>
<td valign="top">

**Trionix Technologies**
<br/><sub>Software Developer Intern</sub>
<br/><sub>Jul 2025 – Sep 2025 · remote</sub>

<sub>`next.js` · `postgresql`</sub>
<br/><sub>`firebase` · `row-level security`</sub>

<sub>↗ <a href="https://saaro-creations.vercel.app/">saaro-creations</a></sub>

</td>
<td valign="top">

Architected the **Vyapar Pragati** admin platform: 6 backend modules, 500+ users, real-time Firestore messaging in place of manual polling.

Normalized the PostgreSQL schema with **Row-Level Security**, so tenant isolation is a database guarantee rather than a `WHERE` clause somebody has to remember. Eliminated the N+1 queries that were doubling DB round-trips on SSR routes.

First time a design decision of mine had users attached to it. That's the part that stuck.

</td>
</tr>
</table>

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-active.svg" width="100%" alt="Currently building" />

### CIDRA — CI debugging and repair agent

<sub>`python` · `langgraph` · `claude api` · `docker` · `pydantic` · <a href="https://github.com/abhishekKokadwar/CIDRA">repo →</a></sub>

A **LangGraph** pipeline that reads a failing GitHub Actions run, works out why, and then — the part that matters — reproduces the failure in a sandboxed Docker container and verifies the fix actually passes before proposing it. Model output is Pydantic-validated with bounded retry, so a malformed response is a retry rather than a crash.

100% Tier-1/2 diagnosis accuracy across 53+ tests, with **zero false "verified" claims**. The second number is the one I care about: an agent that confidently proposes a broken fix is worse than one that says it doesn't know.

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-done.svg" width="100%" alt="Shipped" />

### GridPulse — real-time campus energy monitoring

<sub>`kafka` · `spark` · `duckdb` · `delta lake` · `next.js` · <a href="https://gridpulse-campus.vercel.app">live →</a> · <a href="https://github.com/abhishekKokadwar/GridPulse">repo →</a></sub>

Telemetry from **42 simulated sub-meters** streamed through Kafka into Spark 5-minute windows, with PostgreSQL for the hot path and Delta Lake for history.

The part worth defending is what happens after the aggregate lands. Anomalies are flagged by Isolation Forest crossed with a z-score, and 24-hour load is forecast at **11.5% MAPE** — accurate enough to fire a peak-shaving alert before the peak, which is the only time such an alert is worth anything.

<div align="center">

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/pipeline.svg" width="100%" alt="Meters into Kafka into Spark Structured Streaming, then forking into a hot path to Postgres and a cold path to date-partitioned storage, with a dashboard reading the hot path." />

</div>

A 5-minute sliding window with a 1-minute slide and a **2-minute event-time watermark**, because sensor packets do not arrive in the order they were measured and pretending otherwise gives you clean-looking numbers that are wrong. The storage split is the design: freshness is bought with batch size, history with partitioning, and neither pays for the other.

---

### MCP Zero-Trust Gateway — kernel confinement for agent tools

<sub>`python` · `fastapi` · `seccomp-bpf` · `landlock` · `docker` · <a href="https://pypi.org/project/mcp-ztgateway/">PyPI →</a> · <a href="https://github.com/abhishekKokadwar/MCP_Zero-Trust_Gateway_BTP">repo →</a> · <a href="https://drive.google.com/drive/folders/1UxaBiMxdcX8KH6rdeaSiJ0nu2eWcyXNQ?usp=sharing">evaluation →</a></sub>

An MCP tool server describes its own capabilities. That description is a claim, not a fact, and the gateway treats it that way: **declare, verify, confine.**

<div align="center">

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/gateway.svg" width="100%" alt="Declared capabilities compared against syscalls observed under strace in a locked-down container, compiled into a per-tool seccomp-BPF filter that denies anything outside the declaration at the kernel boundary." />

</div>

Each server is profiled under `strace` in a `--cap-drop ALL --read-only` container, the observed syscalls are checked against what the server declared, and the verified result is compiled into a per-tool **seccomp-BPF** filter. Anything outside the declaration is denied at the kernel boundary, not by application code that can be talked out of it. Provenance gating on tool-call arguments and per-call manifest re-attestation close CVE-2025-54136.

The part I'd defend in an interview isn't the enforcement, it's the evaluation. A 7-corpus, 583-row harness that separates *detection* from *containment*, because a gateway that notices an attack and doesn't stop it deserves a different number than one that stops it. 84.6% runtime defence, 100% containment, 87.8% on MCPTox.

---

### Trinetra — parking enforcement intelligence, Bengaluru

<sub>`python` · `fastapi` · `xgboost` · `h3` · `next.js` · <a href="https://gridlockl-fugg.vercel.app">live →</a> · <a href="https://github.com/abhishekKokadwar/gridlock">repo →</a></sub>

**112K parking violations** clustered into **1,196 H3 hotspots**, each ranked with a 0–100 congestion-risk score, then forecast a week ahead with XGBoost at **0.80 Precision@10** across 53 police stations.

Most of the work was in the join, not the model. Violation records, geospatial cells and time-of-day buckets have to line up before anything downstream means much — and the discipline is resisting the urge to read a hotspot into what is really just a place with more reporting. SHAP reason chips sit next to each prediction so an officer can see *why* a cell ranked high, and greedy routing turns the ranking into patrol routes for N units. The finding I liked most wasn't a prediction at all: a **5.5% afternoon enforcement blind spot** city-wide, visible only once the data was honest.

Top 5% at the Flipkart Gridlock hackathon.

---

### RTI Copilot — right-to-information assistant

<sub>`next.js` · `llm api` · `vercel` · <a href="https://rti-copilot.vercel.app">live →</a> · <a href="https://github.com/abhishekKokadwar/RTI-copilot">repo →</a></sub>

An RTI filed at the wrong ministry doesn't get rejected — it gets *transferred*, and the statutory clock starts over. That single detail is the product: route the request correctly the first time, or the citizen silently loses a month.

So it routes grievances to the right ministry through an LLM against a curated directory, then rewrites the complaint as a **record request** — the form an office is legally obliged to answer, rather than the form it can file away. Appeals draft themselves when a deadline passes, and the deadline alert lands by email before it does.

---

### SmartReview — domain-adapted sentiment model

<sub>`pytorch` · `huggingface transformers` · <a href="https://huggingface.co/abhishek1005/smartreview-distilroberta-sentiment">model card →</a></sub>

DistilRoBERTa domain-adapted by masked-language-modelling over **61.5K phone reviews**, then fine-tuned for 3-class sentiment — all of it on a single 4GB GPU, which shaped every decision about batch size and sequence length.

**88.2% accuracy and 94.9% positive-class F1** on 8.4K held-out reviews, at roughly 50ms per review. The two-stage approach is the point: adapting the encoder to the vocabulary *before* touching the classification head is what a general-purpose sentiment model doesn't get you.

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-dsa.svg" width="100%" alt="DSA" />

The most consistent thing I do — 306 active days, and the reason a cost-per-operation instinct shows up in everything above.

<div align="center">

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/dsa.svg" width="92%" alt="859 solved, LeetCode contest rating 1640, 29 contests, 273 easy / 399 medium / 55 hard" />

<br/>

<sub>across <a href="https://leetcode.com/u/abhiii1005_/">LeetCode</a>, <a href="https://www.geeksforgeeks.org/profile/abhi_iiitm">GeeksforGeeks</a>, <a href="https://www.naukri.com/code360/profile/1d0eab26-a66e-4d90-99ed-46328d444eab">Code360</a> (4x monthly topper) and CodeChef · rating and difficulty split fetched live · totals tracked on <a href="https://codolio.com/profile/abhishek_1005">Codolio</a></sub>

</div>

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-oss.svg" width="100%" alt="Open source" />

Five merged upstream, across three CNCF projects. Small in line count, mostly; the interesting part is that each one was a disagreement between two pieces of a system that each looked correct alone.

<table>
<tr>
<td width="30%" valign="top">

**[kubeflow/trainer #3960](https://github.com/kubeflow/trainer/pull/3960)**
<br/><sub>validation read live state, reconciliation read a snapshot</sub>

</td>
<td valign="top">

`ValidateObjects` always fetched the **live** TrainingRuntime, while `NewObjects` reconciles from the per-TrainJob snapshot introduced by KEP-2599. So editing a runtime retroactively broke validation for TrainJobs already reconciled against the old one: remove a volumeMount and resuming a paused job is rejected, even though reconciliation would have used the still-valid snapshot. Delete the runtime — now legal, since KEP-2599 dropped the finalizers — and the job is stuck permanently, reconciling fine but never passing admission. Fixed by resolving updates from the snapshot, falling back to live only for pre-snapshot jobs.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/mcp-server #237](https://github.com/kubeflow/mcp-server/pull/237)**
<br/><sub>a blocked response still advertised a next step</sub>

</td>
<td valign="top">

The server set `_meta.next` even when the response reported blockers, so a client could be told what to do next by a call that had not actually succeeded. Withholding it makes the failure legible to the agent instead of inviting it to continue.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/mcp-server #236](https://github.com/kubeflow/mcp-server/pull/236)**
<br/><sub>unvalidated runtime names in platform tools</sub>

</td>
<td valign="top">

Runtime names reached the platform runtime tools unvalidated. 188 lines, nearly all of it the validation and its tests.

</td>
</tr>
<tr>
<td valign="top">

**[karmada-io/dashboard #700](https://github.com/karmada-io/dashboard/pull/700)**
<br/><sub>TypeScript strictness in member-cluster services</sub>

</td>
<td valign="top">

Tightened types across 7 files in the member-cluster service layer — the kind of change that finds bugs by refusing to compile rather than by failing at runtime.

</td>
</tr>
<tr>
<td valign="top">

**[karmada-io/dashboard #702](https://github.com/karmada-io/dashboard/pull/702)**
<br/><sub>a shebang on the wrong line</sub>

</td>
<td valign="top">

Two lines. The i18n CLI could not run because its shebang was not first in the file. Favourite kind of fix: the bug is obvious the moment you see it, and invisible until then.

</td>
</tr>
</table>

Also contributing through **GSSoC**, and a published inference model on [HuggingFace Hub](https://huggingface.co/abhishek1005). See [all merged PRs](https://github.com/pulls?q=is%3Apr+author%3AabhishekKokadwar+is%3Amerged).

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-stack.svg" width="100%" alt="Stack" />

<div align="center">

![Python](https://img.shields.io/badge/Python-0d1117?style=flat-square&logo=python&logoColor=white&labelColor=0d1117)
![SQL](https://img.shields.io/badge/SQL-0d1117?style=flat-square&logo=postgresql&logoColor=white&labelColor=0d1117)
![C++](https://img.shields.io/badge/C++-0d1117?style=flat-square&logo=cplusplus&logoColor=white&labelColor=0d1117)
![TypeScript](https://img.shields.io/badge/TypeScript-0d1117?style=flat-square&logo=typescript&logoColor=white&labelColor=0d1117)
![Bash](https://img.shields.io/badge/Bash-0d1117?style=flat-square&logo=gnubash&logoColor=white&labelColor=0d1117)

![Kafka](https://img.shields.io/badge/Kafka-0d1117?style=flat-square&logo=apachekafka&logoColor=white&labelColor=0d1117)
![Spark](https://img.shields.io/badge/Spark-0d1117?style=flat-square&logo=apachespark&logoColor=white&labelColor=0d1117)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-0d1117?style=flat-square&logo=postgresql&logoColor=white&labelColor=0d1117)
![Docker](https://img.shields.io/badge/Docker-0d1117?style=flat-square&logo=docker&logoColor=white&labelColor=0d1117)
![Linux](https://img.shields.io/badge/Linux-0d1117?style=flat-square&logo=linux&logoColor=white&labelColor=0d1117)
![AWS](https://img.shields.io/badge/AWS-0d1117?style=flat-square&logo=amazonwebservices&logoColor=white&labelColor=0d1117)

![Next.js](https://img.shields.io/badge/Next.js-0d1117?style=flat-square&logo=next.js&logoColor=white&labelColor=0d1117)
![FastAPI](https://img.shields.io/badge/FastAPI-0d1117?style=flat-square&logo=fastapi&logoColor=white&labelColor=0d1117)
![Sanity](https://img.shields.io/badge/Sanity-0d1117?style=flat-square&logo=sanity&logoColor=white&labelColor=0d1117)
![Firebase](https://img.shields.io/badge/Firebase-0d1117?style=flat-square&logo=firebase&logoColor=white&labelColor=0d1117)
![LangChain](https://img.shields.io/badge/LangChain-0d1117?style=flat-square&logo=langchain&logoColor=white&labelColor=0d1117)
![HuggingFace](https://img.shields.io/badge/HuggingFace-0d1117?style=flat-square&logo=huggingface&logoColor=white&labelColor=0d1117)

</div>

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/rule.svg" width="100%" alt="" />

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/h-lately.svg" width="100%" alt="Lately" />

<div align="center">

<img src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/main/assets/github.svg" width="92%" alt="GitHub contributions, commits, merged PRs, public repos and stars, with a language share bar" />

<br/><br/>

<img width="92%" src="https://streak-stats.demolab.com?user=abhishekKokadwar&hide_border=true&background=0d1117&stroke=1f2733&ring=58a6ff&fire=58a6ff&currStreakNum=e6edf3&sideNums=e6edf3&currStreakLabel=58a6ff&sideLabels=8b949e&dates=6e7681" alt="contribution streak" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/output/github-contribution-grid-snake-dark.svg" />
  <img width="100%" src="https://raw.githubusercontent.com/abhishekKokadwar/abhishekKokadwar/output/github-contribution-grid-snake.svg" alt="contribution snake" />
</picture>

<br/><br/>

<sub>B.Tech IT + MBA · IIITM Gwalior · graduating 2028</sub>

<br/>

<sub>if something here looks wrong, it probably is. <a href="https://github.com/abhishekKokadwar/abhishekKokadwar/issues">tell me</a></sub>

</div>
