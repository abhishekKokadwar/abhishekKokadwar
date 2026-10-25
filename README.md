<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/header.svg" width="100%" alt="abhishek kokadwar. data pipelines, backend, the boundaries between systems" />

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

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-exp.svg" width="100%" alt="Experience" />

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

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-active.svg" width="100%" alt="Currently building" />

### CIDRA — CI debugging and repair agent

<sub>`python` · `langgraph` · `claude api` · `docker` · `pydantic` · <a href="https://github.com/abhishekKokadwar/CIDRA">repo →</a></sub>

A **LangGraph** pipeline (20 nodes) that reads a failing GitHub Actions run, works out why, and then — the part that matters — reproduces the failure in a network-isolated Docker container and proposes a fix only after it passes there with no other test breaking. A static audit gate refuses patches that make a test pass by cheating: deleted or skipped tests, weakened asserts, deleted or swallowed errors.

Measured on **40 real bugs from BugsInPy** with a small model (claude-haiku-4-5, $0.65 for the whole run): 32/40 diagnosed correctly, all 16 out-of-scope bugs declined, 4 of 24 fixable bugs fixed. Every fix it calls verified is judged afterwards by held-out tests the model never saw — and **1 of those 4 was still wrong** (4 of 9 in the run before, which is what drove the audit rules). That number is the one I care about: an agent that confidently proposes a broken fix is worse than one that says it doesn't know. <a href="https://github.com/abhishekKokadwar/CIDRA#measured-results">results and method →</a>

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-done.svg" width="100%" alt="Shipped" />

### GridPulse — real-time campus energy monitoring

<sub>`kafka` · `spark` · `duckdb` · `delta lake` · `next.js` · <a href="https://gridpulse-campus.vercel.app">live →</a> · <a href="https://github.com/abhishekKokadwar/GridPulse">repo →</a></sub>

Telemetry from **42 simulated sub-meters** streamed through Kafka into Spark 5-minute windows, with PostgreSQL for the hot path and Delta Lake for history.

The part worth defending is what happens after the aggregate lands. Anomalies are flagged by Isolation Forest crossed with a z-score, and 24-hour load is forecast at **11.5% MAPE** — accurate enough to fire a peak-shaving alert before the peak, which is the only time such an alert is worth anything.

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/pipeline.svg" width="100%" alt="Meters into Kafka into Spark Structured Streaming, then forking into a hot path to Postgres and a cold path to date-partitioned storage, with a dashboard reading the hot path." />

</div>

A 5-minute sliding window with a 1-minute slide and a **2-minute event-time watermark**, because sensor packets do not arrive in the order they were measured and pretending otherwise gives you clean-looking numbers that are wrong. The storage split is the design: freshness is bought with batch size, history with partitioning, and neither pays for the other.

---

### MCP Zero-Trust Gateway — kernel confinement for agent tools

<sub>`python` · `fastapi` · `seccomp-bpf` · `landlock` · `docker` · <a href="https://pypi.org/project/mcp-ztgateway/">PyPI →</a> · <a href="https://github.com/abhishekKokadwar/MCP_Zero-Trust_Gateway_BTP">repo →</a> · <a href="https://drive.google.com/drive/folders/1UxaBiMxdcX8KH6rdeaSiJ0nu2eWcyXNQ?usp=sharing">evaluation →</a></sub>

An MCP tool server describes its own capabilities. That description is a claim, not a fact, and the gateway treats it that way: **declare, verify, confine.**

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/gateway.svg" width="100%" alt="Declared capabilities compared against syscalls observed under strace in a locked-down container, compiled into a per-tool seccomp-BPF filter that denies anything outside the declaration at the kernel boundary." />

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

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-dsa.svg" width="100%" alt="DSA" />

The most consistent thing I do — 306 active days, and the reason a cost-per-operation instinct shows up in everything above.

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/dsa.svg?v=881b8195" width="92%" alt="859 solved, LeetCode contest rating 1640, 29 contests, 273 easy / 399 medium / 55 hard" />

<br/>

<sub>across <a href="https://leetcode.com/u/abhiii1005_/">LeetCode</a>, <a href="https://www.geeksforgeeks.org/profile/abhi_iiitm">GeeksforGeeks</a>, <a href="https://www.naukri.com/code360/profile/1d0eab26-a66e-4d90-99ed-46328d444eab">Code360</a> (4x monthly topper) and CodeChef · rating and difficulty split fetched live · totals tracked on <a href="https://codolio.com/profile/abhishek_1005">Codolio</a></sub>

</div>

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-oss.svg" width="100%" alt="Open source" />

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/oss.svg?v=55e76507" width="92%" alt="Merged upstream pull requests, issues closed, the repos they landed in, and the most recent merges. Regenerated from the GitHub API." />

</div>

Merged upstream across Kubeflow and Karmada, and a [Kubeflow org member](https://github.com/kubeflow/internal-acls/pull/979) since September 2026. Small in line count, mostly; the interesting part is that each one was a disagreement between two pieces of a system that each looked correct alone.

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

**[kubeflow/trainer #4088](https://github.com/kubeflow/trainer/pull/4088)**
<br/><sub>the error path panicked before it could report the error</sub>

</td>
<td valign="top">

`Reconcile` handles an unresolvable `runtimeRef` by setting a `Failed` condition, then handed the runtime it had just failed to find to `setTrainJobStatus`, which called a method on a nil interface. controller-runtime recovers the panic and requeues, so the manager stays up, but the unwind happens before the status patch: the condition never reaches the API server, every retry panics at the same point, and the TrainJob sits there with nothing in its status saying why. Admission normally rejects these, which is why it went unnoticed, but a webhook `failurePolicy` of `Ignore` lets one through. Now the status is derived only when a runtime was found, with a test for a branch that had none.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/trainer #3918](https://github.com/kubeflow/trainer/pull/3918)**
<br/><sub>validation stopped at the first job it decided to skip</sub>

</td>
<td valign="top">

The Volcano plugin checks each ReplicatedJob's `priorityClassName`, but returned early on a reserved class instead of continuing, so every job listed after it went unvalidated and a bad name surfaced as a scheduling failure rather than at admission. The skip turned out to be unnecessary as well: the reserved classes are ordinary `PriorityClass` objects and resolve like any other. Verifying that in KinD surfaced the larger bug. The controller's ClusterRole never granted read on `priorityclasses`, so the informer cache never synced and the webhook timed out for any TrainJob using a user-defined class.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/pipelines #14753](https://github.com/kubeflow/pipelines/pull/14753)**
<br/><sub>page two began with the same item as page one, and the tests agreed</sub>

</td>
<td valign="top">

With pipelines stored in Kubernetes, paging through `ListPipelines` could repeat items, skip them, or hand back the first page again. The store sorted by the requested field only, and the cache builds its list by ranging over a Go map, so objects with equal sort values came back in a different order on every call. The default sort is a creation timestamp with one-second precision, which makes ties easy to hit. And if the object the page token named had been deleted in the meantime, the lookup found nothing and the page silently restarted from index 0. Both list functions now share one helper that breaks ties by UUID and resumes at the first item at or after the token's position, the way the SQL stores already did. Four existing assertions had expected the duplicate.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/pipelines #14739](https://github.com/kubeflow/pipelines/pull/14739)**
<br/><sub>the fake said yes to everything, so the test never ran its own case</sub>

</td>
<td valign="top">

If a recurring run's ScheduledWorkflow was gone from the cluster (deleted with `kubectl`, or the database restored onto another cluster), disabling the run and archiving its experiment both returned Internal Server Error, every time, leaving the experiment stuck. An earlier fix had removed the existence check before the patch but left the error from `Patch` itself fatal. A missing ScheduledWorkflow cannot trigger runs, so disabling now logs the NotFound and proceeds; enabling still fails, as it should. The reason this survived: the fake client's `Patch` returned `nil, nil` no matter what, so `TestDisableJob_CustomResourceNotFound` passed without ever exercising the case in its name. The fake now answers like the real API server.

</td>
</tr>
<tr>
<td valign="top">

**[kubeflow/mcp-server #344](https://github.com/kubeflow/mcp-server/pull/344)**
<br/><sub>with no allowlist, any string was a namespace</sub>

</td>
<td valign="top">

A caller-supplied namespace was checked only against the namespace policy, and with no allowlist configured the policy accepts anything. So `Bad_NS!` reached the Kubernetes API, the agent was told the job was not found, and nothing in that answer suggested the namespace was the problem. A confirmed delete went as far as sending the DELETE. The format check now lives in the shared helper every namespaced tool already calls, rather than in seven tools separately, which also closed the same gap in three submission tools the issue had not listed. One parametrized test covers every tool with a `namespace` parameter and asserts no API call is made, so a new tool is picked up automatically.

</td>
</tr>
</table>

Smaller fixes, one line each:

- **kubeflow/mcp-server** · [#237](https://github.com/kubeflow/mcp-server/pull/237) and [#296](https://github.com/kubeflow/mcp-server/pull/296): blocked responses and confirm-gate previews no longer advertise a next step for an action that never ran · [#236](https://github.com/kubeflow/mcp-server/pull/236): runtime names validated in the platform runtime tools · [#411](https://github.com/kubeflow/mcp-server/pull/411) and [#426](https://github.com/kubeflow/mcp-server/pull/426): an unknown persona or a broken policy file now stops the server with a one-line error instead of a traceback
- **Windows-only test failures** · [mcp-server #290](https://github.com/kubeflow/mcp-server/pull/290): tests that slept 60 ms and trusted a 15.6 ms clock to measure it · [#324](https://github.com/kubeflow/mcp-server/pull/324): a test that built a fake home and read the real one · [trainer #4191](https://github.com/kubeflow/trainer/pull/4191): a "stale manifests" failure that was CRLF at checkout
- **karmada-io/dashboard** · [#700](https://github.com/karmada-io/dashboard/pull/700): TypeScript strictness across the member-cluster services · [#702](https://github.com/karmada-io/dashboard/pull/702): a shebang on the wrong line, so the i18n CLI could not run

Also contributing through **GSSoC**, and a published inference model on [HuggingFace Hub](https://huggingface.co/abhishek1005). See [all merged PRs](https://github.com/pulls?q=is%3Apr+author%3AabhishekKokadwar+is%3Amerged).

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-stack.svg" width="100%" alt="Stack" />

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

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/rule.svg" width="100%" alt="" />

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/h-lately.svg" width="100%" alt="Lately" />

<div align="center">

<img src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@main/assets/github.svg?v=d63d417f" width="92%" alt="GitHub contributions, commits, merged PRs, public repos and stars, with a language share bar" />

<br/><br/>

<img width="92%" src="https://streak-stats.demolab.com?user=abhishekKokadwar&hide_border=true&background=0d1117&stroke=1f2733&ring=58a6ff&fire=58a6ff&currStreakNum=e6edf3&sideNums=e6edf3&currStreakLabel=58a6ff&sideLabels=8b949e&dates=6e7681" alt="contribution streak" />

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@output/github-contribution-grid-snake-dark.svg" />
  <img width="100%" src="https://cdn.jsdelivr.net/gh/abhishekKokadwar/abhishekKokadwar@output/github-contribution-grid-snake.svg" alt="contribution snake" />
</picture>

<br/><br/>

<sub>Integrated Dual Degree (B.Tech IT + MBA) · IIITM Gwalior · graduating 2028</sub>

<br/>

<sub>if something here looks wrong, it probably is. <a href="https://github.com/abhishekKokadwar/abhishekKokadwar/issues">tell me</a></sub>

</div>
