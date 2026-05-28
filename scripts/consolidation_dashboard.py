#!/usr/bin/env python3
"""Generate consolidation-dashboard.html from the repo's own state.

Reads only repo data (git log over knowledge/ + .claude/memory/, INDEX.md
inventory, hypotheses files, memory files). No manual maintenance: regenerate
at the end of /consolidate. Self-contained, stdlib only.

The dashboard is a "sharpen the saw" meta-view of the knowledge system's
health and consolidation history — NOT a project status board.
"""
import subprocess, re, html, datetime, pathlib, collections

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "consolidation-dashboard.html"
RED = "#fa0f00"
PREFIX_COLOR = {
    "learn": RED, "pattern": "#111", "hypothesis": "#111",
    "correct": "#111", "experiment": "#111", "note": "#888",
}


def git(*args):
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True
    ).stdout


# --- commits touching knowledge/ or .claude/memory/ ---
SEP_R, SEP_F = "\x1e", "\x1f"
raw = git("log", "--date=short",
          f"--pretty=tformat:{SEP_R}%H{SEP_F}%ad{SEP_F}%s{SEP_F}%b",
          "--", "knowledge", ".claude/memory")
commits = []
for rec in raw.split(SEP_R):
    if not rec.strip():
        continue
    parts = rec.strip("\n").split(SEP_F)
    parts += [""] * (4 - len(parts))
    h, date, subj, body = parts[0], parts[1], parts[2], parts[3]
    files = git("diff-tree", "--no-commit-id", "--name-only", "-r", h,
                "--", "knowledge", ".claude/memory").split()
    prefix = subj.split(":")[0].strip() if ":" in subj else "other"
    commits.append(dict(h=h[:9], date=date, subj=subj, body=body.strip(),
                        files=files, prefix=prefix))

# --- knowledge folder counts from INDEX inventory table ---
index_txt = (ROOT / "knowledge" / "INDEX.md").read_text()
folder_counts = [(f, int(n)) for f, n in
                 re.findall(r"\|\s*`([\w-]+)/`\s*\|.*?\|\s*\w+\s*\|\s*(\d+)\s*\|",
                            index_txt)]
kn_total = sum(n for _, n in folder_counts)


def count_h(p):
    f = ROOT / "knowledge" / "hypotheses" / p
    return len(re.findall(r"^## H-", f.read_text(), re.M)) if f.exists() else 0


h_active, h_resolved = count_h("active.md"), count_h("resolved.md")
act_f = ROOT / "knowledge" / "hypotheses" / "active.md"
active_list = re.findall(r"^## (H-\d+):\s*(.+)$", act_f.read_text(), re.M) if act_f.exists() else []

mem_files = [p for p in (ROOT / ".claude" / "memory").glob("*.md") if p.name != "MEMORY.md"]
prefix_mix = collections.Counter(c["prefix"] for c in commits)

today = datetime.date.today()
parse = lambda d: (datetime.date.fromisoformat(d) if re.fullmatch(r"\d{4}-\d\d-\d\d", d) else None)
dates = [d for d in (parse(c["date"]) for c in commits) if d]
last = max(dates) if dates else None
days_since = (today - last).days if last else "n/a"

review = "see .claude/state.md"
state_f = ROOT / ".claude" / "state.md"
if state_f.exists():
    m = re.findall(r"20\d\d-\d\d-\d\d", state_f.read_text())
    if m:
        review = max(m)

e = html.escape


def summary(c):
    lines = [l.strip() for l in c["body"].splitlines() if l.strip()]
    text = " ".join(lines[:2]) if lines else c["subj"]
    text = re.sub(r"\s+", " ", text)
    return text[:240] + ("…" if len(text) > 240 else "")


def badge(prefix):
    color = PREFIX_COLOR.get(prefix, "#555")
    return f'<span class="badge" style="background:{color}">{e(prefix)}</span>'


# ---- build cards ----
cards = []
for c in commits[:30]:
    fl = c["files"]
    files_html = "".join(f"<li>{e(f)}</li>" for f in fl[:12])
    more = f"<li class='more'>+{len(fl) - 12} more</li>" if len(fl) > 12 else ""
    cards.append(f"""
    <div class="card">
      <div class="card-head">{badge(c['prefix'])}<span class="date">{e(c['date'])}</span><span class="hash">{e(c['h'])}</span></div>
      <div class="subj">{e(c['subj'])}</div>
      <div class="sum">{e(summary(c))}</div>
      <details><summary>{len(fl)} file(s) touched</summary><ul class="files">{files_html}{more}</ul></details>
    </div>""")

folder_rows = "".join(
    f"<tr><td><code>{e(f)}/</code></td><td class='num'>{n}</td></tr>" for f, n in folder_counts
)
prefix_rows = "".join(
    f"<tr><td>{badge(p)}</td><td class='num'>{n}</td></tr>"
    for p, n in prefix_mix.most_common()
)
active_rows = "".join(
    f"<li><b>{e(hid)}</b> — {e(title)}</li>" for hid, title in active_list
) or "<li>none active</li>"

stale_flag = "ok" if isinstance(days_since, int) and days_since <= 14 else "stale"

HTMLDOC = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Consolidation &amp; Cleanup Dashboard</title>
<style>
 :root {{ --red:{RED}; }}
 * {{ box-sizing:border-box; }}
 body {{ font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
        color:#2b2b2b; background:#fff; margin:0; padding:32px; max-width:1100px; margin:0 auto; }}
 h1 {{ font-size:24px; color:#111; margin:0 0 4px; }}
 .sub {{ color:#888; margin:0 0 28px; font-size:13px; }}
 h2 {{ font-size:14px; text-transform:uppercase; letter-spacing:.06em; color:#111;
       border-bottom:2px solid #111; padding-bottom:6px; margin:34px 0 14px; }}
 .metrics {{ display:flex; flex-wrap:wrap; gap:12px; }}
 .metric {{ background:#f4f4f4; border:1px solid #ddd; border-radius:8px; padding:14px 18px; min-width:130px; }}
 .metric .n {{ font-size:28px; font-weight:700; color:#111; }}
 .metric .l {{ font-size:12px; color:#888; }}
 .metric.alert {{ border-color:var(--red); }}
 .metric.alert .n {{ color:var(--red); }}
 .cols {{ display:flex; gap:20px; flex-wrap:wrap; }}
 .col {{ flex:1; min-width:260px; }}
 table {{ width:100%; border-collapse:collapse; font-size:14px; }}
 td {{ padding:5px 8px; border-bottom:1px solid #eee; }}
 td.num {{ text-align:right; font-variant-numeric:tabular-nums; font-weight:600; }}
 code {{ background:#f4f4f4; padding:1px 5px; border-radius:4px; }}
 .badge {{ color:#fff; padding:2px 9px; border-radius:11px; font-size:11px; font-weight:700;
           text-transform:uppercase; letter-spacing:.04em; }}
 .card {{ background:#f4f4f4; border:1px solid #ddd; border-left:4px solid #ccc; border-radius:8px;
          padding:14px 16px; margin:0 0 12px; }}
 .card-head {{ display:flex; align-items:center; gap:10px; margin-bottom:6px; }}
 .card .date {{ color:#111; font-weight:600; font-size:13px; }}
 .card .hash {{ color:#aaa; font-size:12px; font-family:monospace; margin-left:auto; }}
 .card .subj {{ font-weight:600; color:#111; margin-bottom:4px; }}
 .card .sum {{ color:#555; font-size:13px; margin-bottom:6px; }}
 details {{ font-size:12px; color:#777; }} summary {{ cursor:pointer; }}
 ul.files {{ margin:6px 0 0; padding-left:18px; columns:2; }}
 ul.files li {{ font-family:monospace; font-size:11px; color:#666; }}
 ul.files li.more {{ color:var(--red); font-family:inherit; }}
 ul {{ margin:0; padding-left:18px; }} li {{ margin:3px 0; }}
</style></head><body>
<h1>Consolidation &amp; Cleanup Dashboard</h1>
<p class="sub">Knowledge-system health &amp; consolidation history. Generated {today.isoformat()} from git + INDEX + hypotheses + memory. Regenerate via <code>scripts/consolidation_dashboard.py</code>.</p>

<h2>System health</h2>
<div class="metrics">
  <div class="metric"><div class="n">{kn_total}</div><div class="l">knowledge entries</div></div>
  <div class="metric"><div class="n">{h_active}</div><div class="l">active hypotheses</div></div>
  <div class="metric"><div class="n">{h_resolved}</div><div class="l">resolved hypotheses</div></div>
  <div class="metric"><div class="n">{len(mem_files)}</div><div class="l">memory files</div></div>
  <div class="metric"><div class="n">{len(commits)}</div><div class="l">consolidation commits</div></div>
  <div class="metric {'alert' if stale_flag=='stale' else ''}"><div class="n">{days_since}</div><div class="l">days since last commit</div></div>
  <div class="metric"><div class="n" style="font-size:18px">{e(str(review))}</div><div class="l">last System Review (monthly)</div></div>
</div>

<div class="cols">
  <div class="col"><h2>Knowledge by folder</h2><table>{folder_rows}<tr><td><b>total</b></td><td class="num">{kn_total}</td></tr></table></div>
  <div class="col"><h2>Commit-prefix mix</h2><table>{prefix_rows}</table>
    <p class="sub" style="margin-top:8px">All <code>note:</code> = hygiene, no learning. Watch the mix.</p></div>
  <div class="col"><h2>Active hypotheses (drift)</h2><ul>{active_rows}</ul></div>
</div>

<h2>Consolidation history</h2>
{''.join(cards)}
</body></html>"""

OUT.write_text(HTMLDOC)
print(f"wrote {OUT} ({len(commits)} commits, {kn_total} knowledge entries)")
