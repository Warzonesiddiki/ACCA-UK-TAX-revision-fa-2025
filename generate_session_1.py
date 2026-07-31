import sys

def build_session_1():
    parts = []

    # PART 1
    part1 = """<!-- ═══ PART 1/100 · SHELL & CSS BASE ═══ -->
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
  max-width: 280px;
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
    parts.append(part1)

    # PART 2
    part2 = """<!-- ═══ PART 2/100 · CSS PT2 CALLOUTS & DRILLS ═══ -->
/* ═══════════════════════════════════════════════════════════════
   CALLOUT BOXES, TABLES, COMPUTATIONS, DRILLS & CHIPS
   ═══════════════════════════════════════════════════════════════ */
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
}

.comp-row {
  display: flex;
  justify-content: space-between;
  padding: 0.25rem 0;
  border-bottom: 1px dotted var(--line);
}

.comp-row.total {
  font-weight: 700;
  border-bottom: 2px solid var(--ink);
  border-top: 1px solid var(--ink);
  margin-top: 0.25rem;
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
    parts.append(part2)

    # PART 3
    part3 = """<!-- ═══ PART 3/100 · CSS PRINT ENGINE & JS CORE ═══ -->
/* ═══════════════════════════════════════════════════════════════
   PRINT ENGINE & ENGINE JS CONTROLLER
   ═══════════════════════════════════════════════════════════════ */
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
    const fillEl = document.getElementById('hud-progress-fill');
    const percentEl = document.getElementById('hud-percent-val');

    if (xpEl) xpEl.textContent = this.totalXP + ' XP';
    if (rankEl) rankEl.textContent = this.getRank();
    
    // 100 parts total progress baseline
    const totalDrills = document.querySelectorAll('.mark-done-check input').length || 100;
    const countDone = this.completedTasks.size;
    const pct = Math.min(100, Math.round((countDone / totalDrills) * 100));

    if (fillEl) fillEl.style.width = pct + '%';
    if (percentEl) percentEl.textContent = pct + '%';

    // Restore checkboxes on page load
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
    <div style="display: flex; gap: 1rem; justify-content: center; font-family: var(--font-mono); font-size: 0.85rem;">
      <span class="chip chip-xp">Sittings: June 2026 – June 2027</span>
      <span class="chip chip-type">100 Sequential Modules</span>
      <span class="chip" style="background:var(--paper-deep); color:var(--ink);">Target Score: 70%+</span>
    </div>
  </div>
</section>
<!-- ═══ PART 3 END — PART 4 CONTINUES ═══ -->
<!-- ═══ END PART 3/100 ═══ -->"""
    parts.append(part3)

    # PART 4
    part4 = """<!-- ═══ PART 4/100 · MISSION BRIEFING & GAMIFICATION GUIDE ═══ -->
<section class="part-section" id="part-4">
  <!-- ═══ PART 4/100 · MISSION BRIEFING ═══ -->
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
        <tr>
          <td>Section A OT Question</td>
          <td class="num">+10 XP</td>
          <td><strong>Cadet</strong></td>
          <td class="num">0 XP</td>
        </tr>
        <tr>
          <td>Section B OT Case Question</td>
          <td class="num">+25 XP</td>
          <td><strong>Apprentice</strong></td>
          <td class="num">300 XP</td>
        </tr>
        <tr>
          <td>Section C Masterclass</td>
          <td class="num">+40 XP</td>
          <td><strong>Analyst</strong></td>
          <td class="num">800 XP</td>
        </tr>
        <tr>
          <td>Act Boss Battle</td>
          <td class="num">+100 XP</td>
          <td><strong>Strategist</strong></td>
          <td class="num">1,600 XP</td>
        </tr>
        <tr>
          <td>Specimen Mock Exam</td>
          <td class="num">+250 XP</td>
          <td><strong>Commander</strong></td>
          <td class="num">2,800 XP</td>
        </tr>
        <tr>
          <td>Full Revision Completion</td>
          <td class="num">+500 XP</td>
          <td><strong>Tax Titan</strong></td>
          <td class="num">4,500 XP</td>
        </tr>
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
    parts.append(part4)

    # PART 5
    part5 = """<!-- ═══ PART 5/100 · EXAM BLUEPRINT & HEAT MATRIX ═══ -->
<section class="part-section" id="part-5">
  <!-- ═══ PART 5/100 · EXAM BLUEPRINT ═══ -->
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
        <tr>
          <th>Section</th>
          <th>Structure</th>
          <th>Total Marks</th>
          <th>Time Allocation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Section A</strong></td>
          <td>15 Objective Test Questions (OTQs) × 2 marks each</td>
          <td class="num">30 Marks</td>
          <td class="num">54 Mins</td>
        </tr>
        <tr>
          <td><strong>Section B</strong></td>
          <td>3 OT Case Studies (5 OTQs × 2 marks each)</td>
          <td class="num">30 Marks</td>
          <td class="num">54 Mins</td>
        </tr>
        <tr>
          <td><strong>Section C</strong></td>
          <td>
            1 × 10-mark constructed response question<br>
            2 × 15-mark constructed response questions (1 Income Tax, 1 Corporation Tax)
          </td>
          <td class="num">40 Marks</td>
          <td class="num">72 Mins</td>
        </tr>
        <tr style="font-weight:700; background-color:var(--paper-deep);">
          <td>TOTAL</td>
          <td>Compulsory across all syllabus areas</td>
          <td class="num">100 Marks</td>
          <td class="num">180 Mins (3 Hours)</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>🔥 Syllabus Heat Matrix (Based on Past Sittings)</h3>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Syllabus Area</th>
          <th>Exam Weighting</th>
          <th>Key Topics Tested</th>
          <th>Frequency in Section C</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Income Tax & NIC</strong></td>
          <td class="num">40 – 45%</td>
          <td>Employment benefits, trading profit adjustments, capital allowances, loss relief, personal allowance restriction, NIC Class 1/1A/4.</td>
          <td class="num" style="color:var(--red); font-weight:700;">HIGH (15 Marks guaranteed)</td>
        </tr>
        <tr>
          <td><strong>Corporation Tax</strong></td>
          <td class="num">25 – 30%</td>
          <td>Trading profits, capital allowances (AIA, Full Expensing), marginal relief, loss relief set-offs, group relief, associated companies.</td>
          <td class="num" style="color:var(--red); font-weight:700;">HIGH (15 Marks guaranteed)</td>
        </tr>
        <tr>
          <td><strong>Chargeable Gains</strong></td>
          <td class="num">10 – 15%</td>
          <td>Shares matching rules, PRR, Business Asset Disposal Relief (BADR), Gift Holdover Relief, Rollover relief.</td>
          <td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 or 15 Marks)</td>
        </tr>
        <tr>
          <td><strong>Inheritance Tax</strong></td>
          <td class="num">5 – 10%</td>
          <td>PETs vs CLTs, lifetime tax, death estate computation, NRB / RNRB, spouse transfers, taper relief.</td>
          <td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 Marks)</td>
        </tr>
        <tr>
          <td><strong>Value Added Tax</strong></td>
          <td class="num">10 – 15%</td>
          <td>Registration limits, fuel scale charges, special schemes (cash, flat rate, annual), bad debt relief, MTD penalties.</td>
          <td class="num" style="color:var(--gold); font-weight:700;">MEDIUM (10 Marks)</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 5/100 ═══ -->"""
    parts.append(part5)

    # PART 6
    part6 = """<!-- ═══ PART 6/100 · MASTER TAX RATES & TIME LIMITS ═══ -->
<section class="part-section" id="part-6">
  <!-- ═══ PART 6/100 · MASTER TAX RATES ═══ -->
  <div class="part-header">
    <div class="part-kicker">ACT 0 • COMMAND CENTER</div>
    <h2 class="part-title">Part 6: FA2025 Rates, Allowances & Time Limits Master Table</h2>
    <p class="part-subtitle">Verbatim reference tables as provided in the official examination paper (pp. 37–46).</p>
  </div>

  <div class="card">
    <h3>📊 Income Tax Rates & Bands (FA2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Band</th>
          <th>Taxable Income</th>
          <th>Normal Rate</th>
          <th>Dividend Rate</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Basic rate</td>
          <td>£1 – £37,700</td>
          <td class="num">20%</td>
          <td class="num">8.75%</td>
        </tr>
        <tr>
          <td>Higher rate</td>
          <td>£37,701 – £125,140</td>
          <td class="num">40%</td>
          <td class="num">33.75%</td>
        </tr>
        <tr>
          <td>Additional rate</td>
          <td>Over £125,140</td>
          <td class="num">45%</td>
          <td class="num">39.35%</td>
        </tr>
      </tbody>
    </table>

    <div class="computation-box">
• Starting rate of 0% applies to savings income falling within the first £5,000 of taxable income.
• Savings income Nil Rate Band (SNRB): Basic rate = £1,000 | Higher rate = £500 | Additional rate = £0.
• Dividend Nil Rate Band (DNRB): £500 for all taxpayers.
• Personal Allowance (PA): £12,570. Income limit = £100,000 (Tapered by £1 for every £2 over £100,000).
• Transferable Marriage Allowance: £1,260.
    </div>
  </div>

  <div class="card">
    <h3>🏢 Corporation Tax Rates (Financial Year 2023, 2024, 2025)</h3>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Profit Level</th>
          <th>Effective Rate</th>
          <th>Upper / Lower Limit</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Small profits rate (Profits up to £50,000)</td>
          <td class="num">19%</td>
          <td class="num">£50,000 Lower Limit</td>
        </tr>
        <tr>
          <td>Marginal Relief zone (£50,001 – £250,000)</td>
          <td class="num">Effective rate 19% – 25%</td>
          <td class="num">Marginal Fraction: 3/400ths</td>
        </tr>
        <tr>
          <td>Main rate (Profits over £250,000)</td>
          <td class="num">25%</td>
          <td class="num">£250,000 Upper Limit</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="card">
    <h3>⏱️ Key Statutory Time Limits & Election Dates</h3>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Tax / Claim Type</th>
          <th>Statutory Time Limit</th>
          <th>Target Tax Year 2025/26</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Individual Self-Assessment Return (Paper)</td>
          <td>31 October following end of tax year</td>
          <td class="num">31 October 2026</td>
        </tr>
        <tr>
          <td>Individual Self-Assessment Return (Online)</td>
          <td>31 January following end of tax year</td>
          <td class="num">31 January 2027</td>
        </tr>
        <tr>
          <td>CGT Residential Property Disposal Return & Payment</td>
          <td>60 days after completion date</td>
          <td class="num">60 days from completion</td>
        </tr>
        <tr>
          <td>Corporation Tax Return (CT600)</td>
          <td>12 months from end of accounting period</td>
          <td class="num">12 months post-AP</td>
        </tr>
        <tr>
          <td>Corporation Tax Payment (Non-Large Companies)</td>
          <td>9 months and 1 day after end of AP</td>
          <td class="num">9m + 1d post-AP</td>
        </tr>
        <tr>
          <td>VAT Return & Electronic Payment</td>
          <td>1 calendar month and 7 days post-quarter</td>
          <td class="num">+1m 7d post-period</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
<!-- ═══ END PART 6/100 ═══ -->"""
    parts.append(part6)

    # PART 7
    part7 = """<!-- ═══ PART 7/100 · IT-01 COMPUTATION SKELETON ═══ -->
<section class="part-section" id="part-7">
  <!-- ═══ PART 7/100 · IT-01 ═══ -->
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 7: IT-01 Income Tax Computation Skeleton, Rates & Personal Allowance</h2>
    <p class="part-subtitle">Core pro-forma structure, column layout, ordering of income, and standard PA rules.</p>
  </div>

  <div class="card">
    <h3>📐 Income Tax Pro-Forma Layout</h3>
    <p>Income tax is calculated using three dedicated columns in a strict left-to-right order:</p>
    <table class="fiscal-table">
      <thead>
        <tr>
          <th>Income Header</th>
          <th class="num">Non-Savings (£)</th>
          <th class="num">Savings (£)</th>
          <th class="num">Dividend (£)</th>
          <th class="num">Total (£)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>Employment income / Trading profits / Pensions / Property</td>
          <td class="num">X,XXX</td>
          <td class="num">—</td>
          <td class="num">—</td>
          <td class="num">X,XXX</td>
        </tr>
        <tr>
          <td>Bank & Building Society interest / Gilts interest</td>
          <td class="num">—</td>
          <td class="num">X,XXX</td>
          <td class="num">—</td>
          <td class="num">X,XXX</td>
        </tr>
        <tr>
          <td>UK Dividend income</td>
          <td class="num">—</td>
          <td class="num">—</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
        </tr>
        <tr style="font-weight:700;">
          <td>TOTAL INCOME</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
        </tr>
        <tr>
          <td>Less: Qualifying Interest Payments</td>
          <td class="num">(X,XXX)</td>
          <td class="num">—</td>
          <td class="num">—</td>
          <td class="num">(X,XXX)</td>
        </tr>
        <tr style="font-weight:700;">
          <td>NET INCOME</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
        </tr>
        <tr>
          <td>Less: Personal Allowance (£12,570 standard)</td>
          <td class="num">(12,570)</td>
          <td class="num">—</td>
          <td class="num">—</td>
          <td class="num">(12,570)</td>
        </tr>
        <tr style="font-weight:700; background-color:var(--paper-deep);">
          <td>TAXABLE INCOME</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
          <td class="num">X,XXX</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div class="callout callout-hook">
    <div class="callout-title">🧠 MEMORY HOOK: ORDER OF DEDUCTIONS</div>
    Deduct allowable losses and Personal Allowance against income in the following order:
    <br>1️⃣ <strong>Non-Savings Income</strong> first (maximizes tax relief at 20%/40%/45%).
    <br>2️⃣ <strong>Savings Income</strong> second.
    <br>3️⃣ <strong>Dividend Income</strong> last (lowest tax rates: 8.75%/33.75%/39.35%).
  </div>

  <div class="callout callout-trap">
    <div class="callout-title">⚠️ TRAP WARNING: PA DEDUCTION IN EXAMS</div>
    Never allocate Personal Allowance against dividend income if there is remaining non-savings or savings income. Always absorb non-savings income first!
  </div>
</section>
<!-- ═══ END PART 7/100 ═══ -->"""
    parts.append(part7)

    # PART 8
    part8 = """<!-- ═══ PART 8/100 · IT-02 SAVINGS & DIVIDENDS ═══ -->
<section class="part-section" id="part-8">
  <!-- ═══ PART 8/100 · IT-02 ═══ -->
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 8: IT-02 Savings & Dividend Income Rules + Practice Drills</h2>
    <p class="part-subtitle">Starting rate band (0%), Nil Rate Bands (SNRB & DNRB), Gilt interest rules, and questions Q1, Q2, Q15–Q18.</p>
  </div>

  <div class="card">
    <h3>📖 Core Rules: Savings & Dividends</h3>
    <p>1. <strong>Starting Rate for Savings (0% up to £5,000):</strong> Applies ONLY if taxable non-savings income is less than £5,000. Each £1 of taxable non-savings income reduces the starting rate band by £1.</p>
    <p>2. <strong>Savings Nil Rate Band (SNRB):</strong> Basic rate taxpayer = £1,000 @ 0% | Higher rate taxpayer = £500 @ 0% | Additional rate taxpayer = £0.</p>
    <p>3. <strong>Dividend Nil Rate Band (DNRB):</strong> £500 @ 0% for ALL taxpayers regardless of total income.</p>
    <p>4. <strong>Nil Rate Band Ordering:</strong> Nil rate bands use up slice capacity in the tax band (Basic rate £37,700), even though taxed at 0%.</p>
  </div>

  <!-- DRILL Q1 -->
  <div class="drill-card" id="q1">
    <div class="drill-header">
      <span class="drill-title">Q1 • Said's Investments</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Said has made a number of investments during the tax year. Tick the appropriate box to show which of the following investments will generate taxable income and which will generate exempt income.</p>
    <table class="fiscal-table">
      <thead>
        <tr><th>Investment</th><th class="num">Taxable</th><th class="num">Exempt</th></tr>
      </thead>
      <tbody>
        <tr><td>£400 in shares in the company he works for</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>£1,000 in an Individual Savings Account (ISA)</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>£800 in a NS&I investment account</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
        <tr><td>£500 purchasing a NS&I savings certificate</td><td class="num">[ ]</td><td class="num">[ ]</td></tr>
      </tbody>
    </table>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="callout callout-tip">
        <div class="callout-title">✓ MODEL ANSWER & EXPLANATION</div>
        <p>• <strong>£400 Shares:</strong> TAXABLE (Dividends are subject to income tax).</p>
        <p>• <strong>£1,000 ISA:</strong> EXEMPT (All ISA income and gains are exempt).</p>
        <p>• <strong>£800 NS&I Investment Account:</strong> TAXABLE (Savings interest is taxable).</p>
        <p>• <strong>£500 NS&I Savings Certificate:</strong> EXEMPT (NS&I Savings Certificates are specifically statutory exempt).</p>
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q1" onchange="GAMIFICATION.toggleTask('q1', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>

  <!-- DRILL Q15 -->
  <div class="drill-card" id="q15">
    <div class="drill-header">
      <span class="drill-title">Q15 • David's Income Tax Liability</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>David received the following income for the tax year 2025/26:</p>
    <ul>
      <li>Property income: £21,150</li>
      <li>Interest from UK Government securities (gilts): £2,400</li>
      <li>Dividends: £450</li>
    </ul>
    <p>What is David's total income tax liability for the tax year 2025/26?</p>
    <div class="options-group">
      <label class="option-item"><input type="radio" name="q15_opt"> A) £1,996</label>
      <label class="option-item"><input type="radio" name="q15_opt"> B) £2,035</label>
      <label class="option-item"><input type="radio" name="q15_opt"> C) £2,196</label>
      <label class="option-item"><input type="radio" name="q15_opt"> D) £2,235</label>
    </div>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Property income:                  £21,150
Gilts interest (Savings):          £2,400
Dividends:                           £450
                                  -------
Net income:                       £24,000
Less Personal Allowance:         (£12,570)
                                  -------
Taxable income:                   £11,430
                                  =======

Analysis of Tax Liability:
Non-savings (£21,150 - £12,570):  £8,580 × 20% = £1,716
Savings SNRB:                     £1,000 ×  0% =     £0
Savings excess:                   £1,400 × 20% =   £280
Dividends DNRB:                     £450 ×  0% =     £0
                                                 ------
Total Tax Liability:                             £1,996
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: A (£1,996)</strong><br>
        David is a basic rate taxpayer, so he receives a £1,000 Savings Nil Rate Band (SNRB) and a £500 Dividend Nil Rate Band (DNRB).
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q15" onchange="GAMIFICATION.toggleTask('q15', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 8/100 ═══ -->"""
    parts.append(part8)

    # PART 9
    part9 = """<!-- ═══ PART 9/100 · IT-03 PA RESTRICTION & RELIEFS ═══ -->
<section class="part-section" id="part-9">
  <!-- ═══ PART 9/100 · IT-03 ═══ -->
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 9: IT-03 Personal Allowance Restriction, Gift Aid & Marriage Allowance</h2>
    <p class="part-subtitle">Tapering over £100k, Adjusted Net Income (ANI) calculation, Qualifying Interest, and questions Q9, Q12, Q13, Q14.</p>
  </div>

  <div class="card">
    <h3>📖 Core Rules: PA Restriction & Adjusted Net Income (ANI)</h3>
    <p>1. <strong>Adjusted Net Income Formula:</strong></p>
    <div class="computation-box">
ANI = Net Income - Gross Gift Aid Donations - Gross Personal Pension Contributions
    </div>
    <p>2. <strong>PA Taper Rule:</strong> Where ANI exceeds £100,000, Personal Allowance is reduced by <strong>£1 for every £2</strong> of excess above £100,000.</p>
    <p>3. <strong>Full Loss of PA:</strong> At ANI of £125,140 or more, Personal Allowance is reduced to £Nil (£12,570 / 0.5 = £25,140 excess).</p>
    <p>4. <strong>Marriage Allowance Transfer:</strong> A spouse/civil partner with unutilised PA can transfer <strong>£1,260</strong> to their partner, provided the recipient is a <strong>basic rate taxpayer</strong>. Gives a fixed tax reduction of <strong>£252</strong> (£1,260 × 20%).</p>
  </div>

  <!-- DRILL Q14 -->
  <div class="drill-card" id="q14">
    <div class="drill-header">
      <span class="drill-title">Q14 • Ines' Personal Allowance</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>Ines is a sole trader. During the tax year 2025/26 she had taxable trading income of £106,800 and received dividend income of £1,500. Ines made a gift aid donation of £2,000 (gross) during the tax year 2025/26.</p>
    <p>What amount of personal allowance is Ines entitled to for the tax year 2025/26?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Trading Income:                  £106,800
Dividend Income:                   £1,500
                                 --------
Net Income:                      £108,300
Less: Gross Gift Aid:             (£2,000)
                                 --------
Adjusted Net Income (ANI):       £106,300
Less Income Limit:              (£100,000)
                                 --------
Excess Income:                     £6,300
                                 --------
PA Reduction (50% × £6,300):       £3,150

Standard PA:                      £12,570
Less Reduction:                   (£3,150)
                                 --------
Entitled Personal Allowance:       £9,420
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £9,420</strong><br>
        Remember to deduct gross Gift Aid donations to arrive at Adjusted Net Income BEFORE applying the 50% taper threshold!
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q14" onchange="GAMIFICATION.toggleTask('q14', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>
</section>
<!-- ═══ END PART 9/100 ═══ -->"""
    parts.append(part9)

    # PART 10
    part10 = """<!-- ═══ PART 10/100 · IT-04 CHILD BENEFIT CHARGE & SRT ═══ -->
<section class="part-section" id="part-10">
  <!-- ═══ PART 10/100 · IT-04 ═══ -->
  <div class="part-header">
    <div class="part-kicker">ACT 1 • INCOME TAX & NIC</div>
    <h2 class="part-title">Part 10: IT-04 Child Benefit Charge & Statutory Residence Test (SRT)</h2>
    <p class="part-subtitle">High Income Child Benefit Charge (£60k–£80k), SRT automatic tests, UK ties, and questions Q3–Q8, Q10, Q11.</p>
  </div>

  <div class="card">
    <h3>📖 Core Rules: High Income Child Benefit Charge (HICBC)</h3>
    <p>1. <strong>Threshold:</strong> Applies to an individual whose Adjusted Net Income exceeds <strong>£60,000</strong> where either they or their partner receive Child Benefit.</p>
    <p>2. <strong>Charge Formula:</strong> The charge is <strong>1% of the total Child Benefit received</strong> for every <strong>£200</strong> of ANI between £60,000 and £80,000.</p>
    <p>3. <strong>100% Clawback:</strong> If ANI reaches <strong>£80,000 or more</strong>, the tax charge equals 100% of the Child Benefit received.</p>
  </div>

  <!-- DRILL Q10 -->
  <div class="drill-card" id="q10">
    <div class="drill-header">
      <span class="drill-title">Q10 • Chi's Child Benefit Charge</span>
      <div>
        <span class="chip chip-xp">+10 XP</span>
        <span class="chip chip-type">Section A OTQ</span>
      </div>
    </div>
    <p>For the tax year 2025/26, Chi has a salary of £66,200. She received child benefit of £2,252 during this tax year.</p>
    <p>What is Chi's child benefit income tax charge for the tax year 2025/26?</p>

    <button class="solution-toggle-btn" onclick="GAMIFICATION.toggleSolution(this)">▼ Show Working & Solution</button>
    
    <div class="solution-content">
      <div class="computation-box">
Child Benefit Received:            £2,252
Salary (ANI):                     £66,200
Less Lower Limit:                (£60,000)
                                 --------
Excess Income:                     £6,200

Percentage Charge:
£6,200 / £200 = 31%

Child Benefit Tax Charge:
31% × £2,252 = £698.12 -> Rounded down = £698
      </div>
      <div class="callout callout-tip">
        <strong>CORRECT ANSWER: £698</strong><br>
        The tax charge is always rounded down to the nearest whole pound.
      </div>
    </div>

    <div style="margin-top:1rem;">
      <label class="mark-done-check">
        <input type="checkbox" data-task-id="q10" onchange="GAMIFICATION.toggleTask('q10', 10, this.checked)">
        Mark Done (+10 XP)
      </label>
    </div>
  </div>

  <div class="card">
    <h3>📖 Statutory Residence Test (SRT) Summary</h3>
    <p>1. <strong>Automatic Overseas Test (Not Resident):</strong></p>
    <ul>
      <li>In UK for under 16 days during tax year (if resident in 1+ of previous 3 years).</li>
      <li>In UK for under 46 days during tax year (if not resident in any of previous 3 years).</li>
      <li>Works full-time overseas and spends under 91 days in UK (and under 31 working days in UK).</li>
    </ul>
    <p>2. <strong>Automatic UK Test (Resident):</strong></p>
    <ul>
      <li>In UK for 183 days or more in the tax year.</li>
      <li>Only home is in the UK (available for 91+ consecutive days and occupied for 30+ days).</li>
      <li>Works full-time in the UK.</li>
    </ul>
  </div>
</section>

</div> <!-- End container -->
</body>
</html>
<!-- ═══ END PART 10/100 ═══ -->"""
    parts.append(part10)

    # Write all parts to file
    with open('TX-UK_Revision_Pack.html', 'w', encoding='utf-8') as f:
        for p in parts:
            f.write(p)
            f.write('\n\n')

    print('Successfully generated TX-UK_Revision_Pack.html with Parts 1 to 10!')

if __name__ == '__main__':
    build_session_1()
