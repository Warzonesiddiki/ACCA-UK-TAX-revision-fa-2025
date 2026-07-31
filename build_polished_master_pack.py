import sys, os, re

def generate_polished_pack():
    print("Generating complete, polished 100-part TX-UK_Revision_Pack.html...")

    # We will assemble all 100 parts cleanly
    parts = []

    # -------------------------------------------------------------------------
    # PART 1: SHELL & CSS BASE
    # -------------------------------------------------------------------------
    p1 = """<!-- ═══ PART 1/100 · SHELL & CSS BASE ═══ -->
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ACCA TX-UK (FA2025) Master Revision Pack</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300..800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&family=IBM+Plex+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ═══════════════════════════════════════════════════════════════
   DESIGN SYSTEM TOKENS & FISCAL LEDGER BASE STYLES
   ═══════════════════════════════════════════════════════════════ */
:root {
  --ink: #14261f;
  --ink-soft: #41564c;
  --ink-faint: #6d8177;
  --paper: #f4f6f0;
  --paper-deep: #eaeee4;
  --card: #fdfdfa;
  --line: #d7ddd0;
  --line-strong: #b9c4b4;
  --green: #0c4a38;
  --green-deep: #083527;
  --green-bright: #177a5b;
  --green-pale: #e2efe8;
  --gold: #a8790f;
  --gold-bright: #c99a2e;
  --gold-pale: #f6ecd4;
  --red: #b3372f;
  --red-pale: #f7e4e1;
  --blue: #1e5fa8;
  --blue-pale: #e2ebf6;
  --violet: #6b4fa3;
  --violet-pale: #ece6f6;
  
  --font-display: 'Bricolage Grotesque', sans-serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-mono: 'IBM Plex Mono', monospace;

  --shadow-sm: 0 1px 3px rgba(20, 38, 31, 0.06), 0 1px 2px rgba(20, 38, 31, 0.04);
  --shadow-md: 0 4px 12px rgba(20, 38, 31, 0.08), 0 2px 4px rgba(20, 38, 31, 0.04);
  --shadow-lg: 0 12px 28px rgba(20, 38, 31, 0.12), 0 4px 8px rgba(20, 38, 31, 0.06);
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-size: 16px;
  scroll-behavior: smooth;
  background-color: var(--paper);
  color: var(--ink);
}

body {
  font-family: var(--font-body);
  font-weight: 400;
  line-height: 1.6;
  min-height: 100vh;
  position: relative;
  background-color: var(--paper);
  background-image: 
    linear-gradient(to right, rgba(179, 55, 47, 0.12) 1px, transparent 1px),
    linear-gradient(to bottom, var(--line) 1px, transparent 1px),
    radial-gradient(circle at 10% 20%, rgba(12, 74, 56, 0.05) 0%, transparent 40%),
    radial-gradient(circle at 90% 80%, rgba(168, 121, 15, 0.05) 0%, transparent 40%);
  background-size: 100% 100%, 100% 28px, 100% 100%, 100% 100%;
  background-position: 56px 0, 0 0, 0 0, 0 0;
  background-attachment: fixed;
  padding-left: 0;
  overflow-x: hidden;
}

/* Vertical Ledger Margin Line */
body::before {
  content: "";
  position: fixed;
  top: 0;
  bottom: 0;
  left: 56px;
  width: 2px;
  background-color: rgba(179, 55, 47, 0.35);
  z-index: 99;
  pointer-events: none;
}

/* Typography Base */
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  color: var(--green-deep);
  line-height: 1.25;
  font-weight: 700;
  letter-spacing: -0.02em;
}

h1 { font-size: 2.5rem; }
h2 { font-size: 1.85rem; }
h3 { font-size: 1.35rem; }
h4 { font-size: 1.15rem; }

p { margin-bottom: 1rem; }
p:last-child { margin-bottom: 0; }

code, pre, .mono {
  font-family: var(--font-mono);
}

/* Layout Containers */
.container {
  max-width: 1120px;
  margin: 0 auto;
  padding: 0 1.5rem 0 4.5rem;
}

.part-section {
  position: relative;
  padding: 3.5rem 0;
  border-bottom: 2px dashed var(--line-strong);
  scroll-margin-top: 80px;
}

.part-header {
  margin-bottom: 2rem;
  position: relative;
}

.part-kicker {
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--gold);
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.4rem;
}

.part-kicker::before {
  content: "";
  display: inline-block;
  width: 8px;
  height: 8px;
  background-color: var(--gold);
  border-radius: 50%;
}

.part-title {
  font-size: 2.25rem;
  color: var(--green-deep);
  margin-bottom: 0.5rem;
}

.part-subtitle {
  font-size: 1.05rem;
  color: var(--ink-soft);
  max-width: 800px;
}

/* Sticky Header Progress & Command Bar */
.sticky-command-bar {
  position: sticky;
  top: 0;
  z-index: 1000;
  background: rgba(253, 253, 250, 0.94);
  backdrop-filter: blur(8px);
  border-bottom: 2px solid var(--green);
  box-shadow: var(--shadow-md);
  padding: 0.65rem 1.5rem;
}

.command-bar-inner {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  flex-wrap: wrap;
}

.brand-badge {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-family: var(--font-display);
  font-weight: 800;
  color: var(--green-deep);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-size: 0.95rem;
}

.brand-badge .pill {
  background-color: var(--green);
  color: var(--paper);
  padding: 0.2rem 0.55rem;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 0.75rem;
}

.search-box {
  display: flex;
  align-items: center;
  background: var(--paper);
  border: 1px solid var(--line-strong);
  border-radius: 4px;
  padding: 0.3rem 0.6rem;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  gap: 0.4rem;
}

.search-box input {
  border: none;
  background: transparent;
  outline: none;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  color: var(--ink);
  width: 160px;
}

.hud-metrics {
  display: flex;
  align-items: center;
  gap: 1.25rem;
}

.hud-item {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.hud-label {
  font-family: var(--font-mono);
  font-size: 0.65rem;
  text-transform: uppercase;
  color: var(--ink-faint);
  letter-spacing: 0.05em;
}

.hud-value {
  font-family: var(--font-mono);
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--green-deep);
}

.progress-container {
  flex: 1;
  max-width: 220px;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.progress-bar-bg {
  width: 100%;
  height: 8px;
  background-color: var(--line);
  border-radius: 4px;
  overflow: hidden;
  border: 1px solid var(--line-strong);
}

.progress-bar-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, var(--green-bright), var(--gold-bright));
  transition: width 0.4s ease;
}

/* Cards & Dossier Panels */
.card {
  background-color: var(--card);
  border: 1px solid var(--line-strong);
  border-radius: 6px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  box-shadow: var(--shadow-sm);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-md);
}
/* ═══ PART 1 END — PART 2 CONTINUES CSS ═══ */
<!-- ═══ END PART 1/100 ═══ -->"""
    parts.append(p1)

    # PART 2: CSS PT2
    p2 = """<!-- ═══ PART 2/100 · CSS PT2 CALLOUTS & DRILLS ═══ -->
/* Callout Boxes */
.callout {
  padding: 1.25rem;
  border-radius: 6px;
  margin-bottom: 1.25rem;
  border-left: 4px solid;
  font-size: 0.95rem;
}

.callout-hook {
  background-color: var(--violet-pale);
  border-color: var(--violet);
  color: #3b236e;
}

.callout-trap {
  background-color: var(--red-pale);
  border-color: var(--red);
  color: #721c24;
}

.callout-examiner {
  background-color: var(--red-pale);
  border-color: var(--red);
  color: #61181f;
  font-style: italic;
}

.callout-tip {
  background-color: var(--green-pale);
  border-color: var(--green-bright);
  color: var(--green-deep);
}

.callout-title {
  font-family: var(--font-mono);
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.8rem;
  letter-spacing: 0.05em;
  margin-bottom: 0.4rem;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

/* Fiscal Tables */
.fiscal-table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  font-size: 0.92rem;
  background-color: var(--card);
  border: 1px solid var(--line-strong);
  box-shadow: var(--shadow-sm);
}

.fiscal-table th, .fiscal-table td {
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  text-align: left;
}

.fiscal-table th {
  background-color: var(--paper-deep);
  font-family: var(--font-display);
  font-weight: 700;
  color: var(--green-deep);
  text-transform: uppercase;
  font-size: 0.8rem;
  letter-spacing: 0.03em;
}

.fiscal-table tr:nth-child(even) {
  background-color: rgba(244, 246, 240, 0.4);
}

.fiscal-table .num {
  font-family: var(--font-mono);
  text-align: right;
}

/* Computation Blocks */
.computation-box {
  background-color: #f8faf6;
  border: 1px solid var(--line-strong);
  border-left: 3px solid var(--green);
  padding: 1.25rem;
  border-radius: 4px;
  margin-bottom: 1.25rem;
  font-family: var(--font-mono);
  font-size: 0.88rem;
  overflow-x: auto;
  white-space: pre-wrap;
}

/* Question Drill Components */
.drill-card {
  background-color: var(--card);
  border: 1px solid var(--line-strong);
  border-radius: 6px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
  position: relative;
}

.drill-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--line);
}

.drill-title {
  font-family: var(--font-display);
  font-size: 1.1rem;
  font-weight: 700;
  color: var(--green-deep);
  display: flex;
  align-items: center;
  gap: 0.6rem;
}

.chip {
  display: inline-flex;
  align-items: center;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 0.7rem;
  font-weight: 700;
  text-transform: uppercase;
}

.chip-xp {
  background-color: var(--gold-pale);
  color: var(--gold);
  border: 1px solid rgba(168, 121, 15, 0.3);
}

.chip-type {
  background-color: var(--blue-pale);
  color: var(--blue);
}

.options-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin: 1.25rem 0;
}

.option-item {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  padding: 0.75rem 1rem;
  border: 1px solid var(--line);
  border-radius: 5px;
  background-color: var(--paper);
  cursor: pointer;
  transition: background-color 0.15s ease, border-color 0.15s ease;
}

.option-item:hover {
  background-color: var(--paper-deep);
  border-color: var(--green-bright);
}

.option-item.correct {
  background-color: var(--green-pale) !important;
  border-color: var(--green-bright) !important;
  font-weight: 600;
}

.option-item.incorrect {
  background-color: var(--red-pale) !important;
  border-color: var(--red) !important;
}

.solution-toggle-btn {
  background-color: var(--green);
  color: var(--paper);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  transition: background-color 0.2s ease;
}

.solution-toggle-btn:hover {
  background-color: var(--green-bright);
}

.solution-content {
  display: none;
  margin-top: 1.25rem;
  padding-top: 1.25rem;
  border-top: 2px dashed var(--line-strong);
}

.solution-content.open {
  display: block;
}

.mark-done-check {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-family: var(--font-mono);
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--ink-soft);
  cursor: pointer;
}

.mark-done-check input[type="checkbox"] {
  width: 18px;
  height: 18px;
  accent-color: var(--green-bright);
  cursor: pointer;
}
/* ═══ PART 2 END — PART 3 CONTINUES CSS ═══ */
<!-- ═══ END PART 2/100 ═══ -->"""
    parts.append(p2)

    # PART 3: JS & COVER
    p3 = """<!-- ═══ PART 3/100 · CSS PRINT ENGINE & JS CORE ═══ -->
@media print {
  body {
    background: #ffffff !important;
    color: #000000 !important;
    padding-left: 0 !important;
  }
  body::before, .sticky-command-bar, .solution-toggle-btn, .mark-done-check {
    display: none !important;
  }
  .container {
    max-width: 100% !important;
    padding: 0 !important;
  }
  .part-section {
    page-break-before: always;
    border-bottom: none !important;
    padding: 1rem 0 !important;
  }
  .solution-content {
    display: block !important;
  }
  .card, .drill-card, .fiscal-table {
    box-shadow: none !important;
    border: 1px solid #ccc !important;
  }
  @page {
    size: A4;
    margin: 2cm;
  }
}
</style>

<script>
/* ═══════════════════════════════════════════════════════════════
   GAMIFICATION & PROGRESS JS ENGINE
   ═══════════════════════════════════════════════════════════════ */
const GAMIFICATION = {
  totalXP: 0,
  completedTasks: new Set(),
  
  ranks: [
    { title: 'Cadet', minXP: 0 },
    { title: 'Apprentice', minXP: 300 },
    { title: 'Analyst', minXP: 800 },
    { title: 'Strategist', minXP: 1600 },
    { title: 'Commander', minXP: 2800 },
    { title: 'Tax Titan', minXP: 4500 }
  ],

  init() {
    this.loadState();
    this.updateHUD();
  },

  loadState() {
    const saved = localStorage.getItem('TX_REVISION_PACK_SAVED_STATE');
    if (saved) {
      try {
        const data = JSON.parse(saved);
        this.totalXP = data.xp || 0;
        this.completedTasks = new Set(data.completed || []);
      } catch(e) {
        console.error('State load error', e);
      }
    }
  },

  saveState() {
    localStorage.setItem('TX_REVISION_PACK_SAVED_STATE', JSON.stringify({
      xp: this.totalXP,
      completed: Array.from(this.completedTasks)
    }));
  },

  toggleTask(taskId, xpValue, isChecked) {
    if (isChecked) {
      if (!this.completedTasks.has(taskId)) {
        this.completedTasks.add(taskId);
        this.totalXP += xpValue;
      }
    } else {
      if (this.completedTasks.has(taskId)) {
        this.completedTasks.delete(taskId);
        this.totalXP = Math.max(0, this.totalXP - xpValue);
      }
    }
    this.saveState();
    this.updateHUD();
  },

  getRank() {
    let currentRank = 'Cadet';
    for (const r of this.ranks) {
      if (this.totalXP >= r.minXP) {
        currentRank = r.title;
      }
    }
    return currentRank;
  },

  updateHUD() {
    const xpEl = document.getElementById('hud-xp-val');
    const rankEl = document.getElementById('hud-rank-val');
    const certRankEl = document.getElementById('cert-rank');
    const fillEl = document.getElementById('hud-progress-fill');
    const percentEl = document.getElementById('hud-percent-val');

    if (xpEl) xpEl.textContent = this.totalXP + ' XP';
    if (rankEl) rankEl.textContent = this.getRank();
    if (certRankEl) certRankEl.textContent = this.getRank();
    
    const totalDrills = document.querySelectorAll('.mark-done-check input').length || 100;
    const countDone = this.completedTasks.size;
    const pct = Math.min(100, Math.round((countDone / totalDrills) * 100));

    if (fillEl) fillEl.style.width = pct + '%';
    if (percentEl) percentEl.textContent = pct + '%';

    document.querySelectorAll('.mark-done-check input').forEach(chk => {
      const id = chk.getAttribute('data-task-id');
      if (id && this.completedTasks.has(id)) {
        chk.checked = true;
      }
    });
  },

  toggleSolution(btn) {
    const content = btn.parentElement.querySelector('.solution-content');
    if (content) {
      content.classList.toggle('open');
      if (content.classList.contains('open')) {
        btn.innerHTML = '▲ Hide Working & Solution';
      } else {
        btn.innerHTML = '▼ Show Working & Solution';
      }
    }
  },

  filterSearch(query) {
    const q = query.toLowerCase().trim();
    const sections = document.querySelectorAll('.part-section');
    sections.forEach(sec => {
      if (!q) {
        sec.style.display = 'block';
      } else {
        const text = sec.textContent.toLowerCase();
        if (text.includes(q)) {
          sec.style.display = 'block';
        } else {
          sec.style.display = 'none';
        }
      }
    });
  }
};

document.addEventListener('DOMContentLoaded', () => {
  GAMIFICATION.init();
});
</script>
</head>
<body>

<!-- STICKY HUD COMMAND BAR -->
<div class="sticky-command-bar">
  <div class="command-bar-inner">
    <div class="brand-badge">
      <span>ACCA TX-UK</span>
      <span class="pill">FA2025</span>
    </div>

    <div class="search-box">
      <span>🔍</span>
      <input type="text" placeholder="Search topic / Q..." oninput="GAMIFICATION.filterSearch(this.value)">
    </div>
    
    <div class="progress-container">
      <div style="display:flex; justify-content:space-between; font-family:var(--font-mono); font-size:0.7rem; color:var(--ink-soft);">
        <span>PROGRESS</span>
        <span id="hud-percent-val">0%</span>
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" id="hud-progress-fill"></div>
      </div>
    </div>

    <div class="hud-metrics">
      <div class="hud-item">
        <span class="hud-label">RANK</span>
        <span class="hud-value" id="hud-rank-val">Cadet</span>
      </div>
      <div class="hud-item">
        <span class="hud-label">EXPERIENCE</span>
        <span class="hud-value" id="hud-xp-val">0 XP</span>
      </div>
    </div>
  </div>
</div>

<div class="container">

<!-- COVER PAGE -->
<section class="part-section" id="cover">
  <div style="padding: 3rem 0; text-align: center; border-bottom: 2px solid var(--green);">
    <div class="part-kicker" style="justify-content: center;">Kaplan Exam Kit FA2025 • Official Revision System</div>
    <h1 style="font-size: 3.2rem; color: var(--green-deep); margin: 0.8rem 0;">ACCA TX-UK (FA2025)<br>100-PART MASTER REVISION PACK</h1>
    <p style="font-size: 1.25rem; color: var(--ink-soft); max-width: 750px; margin: 0 auto 2rem auto;">
      A comprehensive, gamified, self-contained study dossier transforming the entire official Kaplan TX-UK Exam Kit into interactive drills, masterclasses, and formula sheets.
    </p>
    <div style="display: flex; gap: 1rem; justify-content: center; font-family: var(--font-mono); font-size: 0.85rem; flex-wrap: wrap;">
      <span class="chip chip-xp">Sittings: June 2026 – June 2027</span>
      <span class="chip chip-type">100 Sequential Modules</span>
      <span class="chip" style="background:var(--paper-deep); color:var(--ink);">Target Score: 70%+</span>
    </div>
  </div>
</section>
<!-- ═══ END PART 3/100 ═══ -->"""
    parts.append(p3)

    # Let's read the current file or generate full rich sections for all remaining parts
    # Let's verify we have parts 4 to 100 with complete content!
    
    # We can write a python function to generate each part cleanly with rich content so that NO part is short!
    
    # PART 4: MISSION BRIEFING
    p4 = """<!-- ═══ PART 4/100 · MISSION BRIEFING & GAMIFICATION GUIDE ═══ -->
<section class="part-section" id="part-4">
  <div class="part-header">
    <div class="part-kicker">ACT 0 • COMMAND CENTER</div>
    <h2 class="part-title">Part 4: Mission Briefing & Gamification System</h2>
    <p class="part-subtitle">How to navigate the 100-part dossier, earn XP, advance in rank, and master the exam kit.</p>
  </div>

  <div class="card">
    <h3>🎯 How to Use This Revision Pack</h3>
    <p>This pack converts the entire Kaplan Finance Act 2025 Exam Kit into a structured, step-by-step revision campaign. Follow these operational rules to guarantee exam success:</p>
    <ul style="margin-left: 1.5rem; margin-bottom: 1rem;">
      <li><strong>Study Core Notes:</strong> Review the statutory rules, tax bands, memory hooks, and trap warnings before attempting questions.</li>
      <li><strong>Attempt Drills Under Timed Conditions:</strong> Allow 1.8 minutes per mark (e.g., 3.6 minutes for a 2-mark Section A OTQ).</li>
      <li><strong>Check & Mark Done:</strong> Tick the "Mark Done" checkbox on every completed question to claim Experience Points (XP). Your progress and rank are automatically persisted in your browser's LocalStorage.</li>
      <li><strong>Study the Model Answers:</strong> Reveal full workings, mono calculations, and examiner comments to understand where marks are awarded.</li>
    </ul>
  </div>

  <div class="card">
    <h3>🏆 XP & Rank Ladder</h3>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Task Type</th>
          <th>XP Awarded</th>
          <th>Rank Progression</th>
          <th>Min XP Required</th>
        </tr>
      </thead>
      <tbody>
        <tr><td>Section A OT Question</td><td class="num">+10 XP</td><td><strong>Cadet</strong></td><td class="num">0 XP</td></tr>
        <tr><td>Section B OT Case Question</td><td class="num">+25 XP</td><td><strong>Apprentice</strong></td><td class="num">300 XP</td></tr>
        <tr><td>Section C Masterclass</td><td class="num">+40 XP</td><td><strong>Analyst</strong></td><td class="num">800 XP</td></tr>
        <tr><td>Act Boss Battle</td><td class="num">+100 XP</td><td><strong>Strategist</strong></td><td class="num">1,600 XP</td></tr>
        <tr><td>Specimen Mock Exam</td><td class="num">+250 XP</td><td><strong>Commander</strong></td><td class="num">2,800 XP</td></tr>
        <tr><td>Full Revision Completion</td><td class="num">+500 XP</td><td><strong>Tax Titan</strong></td><td class="num">4,500 XP</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🎨 Callout Box Legend</h3>
    <div class="callout callout-hook">
      <div class="callout-title">🧠 MEMORY HOOK (VIOLET)</div>
      Essential memory aids, mnemonics, and mental models to lock in key tax rules.
    </div>
    <div class="callout callout-trap">
      <div class="callout-title">⚠️ TRAP WARNING (RED)</div>
      Frequent candidate errors, tricky phrasing, and statutory exceptions flagged by examiners.
    </div>
    <div class="callout callout-examiner">
      <div class="callout-title">🔴 EXAMINER SAYS (CRIMSON)</div>
      Verbatim feedback and quotes from official ACCA examining team reports.
    </div>
    <div class="callout callout-tip">
      <div class="callout-title">🟢 TUTOR'S TOP TIP (GREEN)</div>
      Actionable exam technique, time-saving shortcuts, and pro-forma strategies.
    </div>
  </div>
</section>
<!-- ═══ END PART 4/100 ═══ -->"""
    parts.append(p4)

    # PART 5: EXAM BLUEPRINT
    p5 = """<!-- ═══ PART 5/100 · EXAM BLUEPRINT & HEAT MATRIX ═══ -->
<section class="part-section" id="part-5">
  <div class="part-header">
    <div class="part-kicker">ACT 0 • COMMAND CENTER</div>
    <h2 class="part-title">Part 5: Exam Blueprint & Past Exam Heat Matrix</h2>
    <p class="part-subtitle">Exam format, mark allocation, time management rules, and syllabus frequency breakdown.</p>
  </div>

  <div class="card">
    <h3>⏱️ ACCA TX-UK Exam Format (3 Hours • 100 Marks)</h3>
    <p>The TX-UK examination is a 3-hour Computer-Based Examination (CBE) comprising 100 marks. The standard timing rate is <strong>1.8 minutes per mark</strong>.</p>
    <table class="fiscal-table">
      <thead>
        <tr><th>Section</th><th>Structure</th><th>Total Marks</th><th>Time Allocation</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Section A</strong></td><td>15 Objective Test Questions (OTQs) × 2 marks each</td><td class="num">30 Marks</td><td class="num">54 Mins</td></tr>
        <tr><td><strong>Section B</strong></td><td>3 OT Case Studies (5 OTQs × 2 marks each)</td><td class="num">30 Marks</td><td class="num">54 Mins</td></tr>
        <tr><td><strong>Section C</strong></td><td>1 × 10-mark constructed response question<br>2 × 15-mark constructed response questions (1 Income Tax, 1 Corporation Tax)</td><td class="num">40 Marks</td><td class="num">72 Mins</td></tr>
        <tr style="font-weight:700; background-color:var(--paper-deep);"><td>TOTAL</td><td>Compulsory across all syllabus areas</td><td class="num">100 Marks</td><td class="num">180 Mins (3 Hours)</td></tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🔥 Syllabus Heat Matrix</h3>
    <table class="fiscal-table">
      <thead>
        <tr><th>Syllabus Area</th><th>Exam Weighting</th><th>Key Topics Tested</th><th>Frequency in Section C</th></tr>
      </thead>
      <tbody>
        <tr><td><strong>Income Tax & NIC</strong></td><td class="num">40 – 45%</td><td>Employment benefits, trading profit adjustments, capital allowances, loss relief, PA restriction, NIC Class 1/1A/4.</td><td class="num" style="color:var(--red); font-weight:700;">HIGH (15 Marks guaranteed)</td></tr>
        <tr><td><strong>Corporation Tax</strong></td><td class="num">25 – 30%</td><td>Trading profits, capital allowances (AIA, Full Expensing), marginal relief, loss relief set-offs, group relief, associated companies.</td><td class="num" style="color:var(--red); font-weight:700;">HIGH (15 Marks guaranteed)</td></tr>
        <tr><td><strong>Chargeable Gains</strong></td><td class="num">10 – 15%</td><td>Shares matching rules, PRR, Business Asset Disposal Relief (BADR), Gift Holdover Relief, Rollover relief.</td><td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 or 15 Marks)</td></tr>
        <tr><td><strong>Inheritance Tax</strong></td><td class="num">5 – 10%</td><td>PETs vs CLTs, lifetime tax, death estate computation, NRB / RNRB, spouse transfers, taper relief.</td><td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 Marks)</td></tr>
        <tr><td><strong>Value Added Tax</strong></td><td class="num">10 – 15%</td><td>Registration limits, fuel scale charges, special schemes (cash, flat rate, annual), bad debt relief, MTD penalties.</td><td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 Marks)</td></tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 5/100 ═══ -->"""
    parts.append(p5)

    # Let's read the current file and fix any remaining parts so that ALL 100 parts are fully formed and detailed!
    # Let's check how many parts we already built in the previous scripts.

    print("Checking parts in current TX-UK_Revision_Pack.html...")
    
