"""
CognitiveCloud.ai — Mulch Math
Fractions · Rates · Decimals · Sixteenths & Multiples
Grade 8 · Crusader Vision Pedagogy
"""

import streamlit as st
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import pandas as pd
from fractions import Fraction
from datetime import datetime
import io
import time

st.set_page_config(page_title="Mulch Math · CognitiveCloud.ai", page_icon="🌿", layout="wide")

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap');
html,body{background:#f5f5f3 !important;color:#111827 !important;}
[class*="css"],.main,.block-container{background:#f5f5f3 !important;color:#111827 !important;}
p,span,div,li,label,small,h1,h2,h3,h4,h5,h6,
.stMarkdown,.stMarkdown p,.stMarkdown li,.stMarkdown span,
[data-testid="stMarkdownContainer"] p,
[data-testid="stMarkdownContainer"] li,
[data-testid="stMarkdownContainer"] span{color:#111827 !important;font-family:"DM Sans",sans-serif !important;}
label,.stSelectbox label,.stRadio label,.stNumberInput label,.stTextInput label,.stTextArea label{color:#111827 !important;font-weight:600 !important;}
input,textarea,[data-testid="stNumberInput"] input{color:#111827 !important;background:#ffffff !important;border:1.5px solid #d1d5db !important;}
[data-testid="stAlert"] p,[data-testid="stAlert"] div{color:#111827 !important;}
code,pre{color:#1e40af !important;background:#eff6ff !important;}
[data-testid="stDataFrame"] td,[data-testid="stDataFrame"] th{color:#111827 !important;}
div[data-testid="stSidebar"]{background:#f0ede8 !important;border-right:1px solid #d1d5db;}
div[data-testid="stSidebar"] p,div[data-testid="stSidebar"] span,
div[data-testid="stSidebar"] label,div[data-testid="stSidebar"] div{color:#111827 !important;}
div[data-baseweb="select"] *,div[data-baseweb="select"] div,div[data-baseweb="select"] span,
[data-testid="stSelectbox"] *,[data-testid="stSelectbox"] div{color:#111827 !important;background-color:#ffffff !important;}
div[role="listbox"],div[role="listbox"] *,div[role="option"],div[role="option"] *{color:#111827 !important;background-color:#ffffff !important;}
div[role="option"]:hover,div[role="option"]:hover *{background-color:#f1f5f9 !important;color:#111827 !important;}
div[aria-selected="true"],div[aria-selected="true"] *{background-color:#e0f2fe !important;color:#0369a1 !important;}
.dev-credit{background:linear-gradient(135deg,#14532d 0%,#166534 100%);padding:20px;border-radius:10px;margin-bottom:20px;box-shadow:0 4px 6px rgba(0,0,0,.15);}
.dev-credit h2{margin:0;color:#ffffff !important;font-size:1.3rem;}
.dev-credit p{margin:5px 0;color:rgba(255,255,255,.9) !important;font-size:.9rem;}
.dev-credit span,.dev-credit div{color:rgba(255,255,255,.9) !important;}
.dev-credit hr{border:1px solid rgba(255,255,255,.3);margin:10px 0;}
.dev-credit a{color:#86efac !important;text-decoration:underline;}
.pill{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;padding:3px 12px;border-radius:20px;margin:22px 0 14px;color:#fff;}
.p-1{background:#16a34a;}.p-2{background:#0891b2;}.p-3{background:#7c3aed;}
.p-4{background:#d97706;}.p-5{background:#e11d48;}.p-6{background:#374151;}
.p-g{background:linear-gradient(90deg,#f59e0b,#ef4444);}
.mcard{background:#ffffff;border:2px solid #d1d5db;border-radius:12px;padding:16px 20px;margin-bottom:10px;}
.mcard-t{font-size:.7rem;color:#374151 !important;font-weight:600;margin:0 0 2px;}
.mcard-v{font-size:1.9rem;font-weight:700;font-family:"DM Mono",monospace;color:#111827 !important;}
.mcard-u{font-size:.72rem;color:#6b7280 !important;}
.irow{display:flex;justify-content:space-between;align-items:center;padding:9px 13px;background:#e8ecf0;border-radius:8px;margin-bottom:5px;border:1px solid #d1d5db;}
.ik{font-size:.76rem;color:#374151 !important;font-weight:600;}
.iv{font-size:.8rem;font-family:"DM Mono",monospace;font-weight:700;color:#111827 !important;}
.xp-chip{display:inline-block;background:#fef3c7;border:1px solid #fbbf24;color:#92400e;font-size:.65rem;font-weight:700;padding:2px 8px;border-radius:99px;margin-top:4px;}
.xp-bar-wrap{background:#e2e8f0;border-radius:99px;height:14px;width:100%;margin:6px 0 2px;}
.xp-bar{height:14px;border-radius:99px;background:linear-gradient(90deg,#16a34a,#86efac);}
.xp-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:2px;}
.xp-label{font-size:.72rem;font-weight:700;color:#111827 !important;}
.xp-num{font-family:"DM Mono",monospace;font-size:.8rem;font-weight:700;color:#16a34a !important;}
.badge-row{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0;}
.badge{display:inline-flex;align-items:center;gap:5px;padding:5px 12px;border-radius:20px;font-size:.72rem;font-weight:600;}
.badge-earned{background:#f0fdf4;border:1px solid #86efac;color:#15803d;}
.badge-locked{background:#f8fafc;border:1px solid #e2e8f0;color:#94a3b8;}
.celebrate-box{background:linear-gradient(135deg,#f0fdf4,#dcfce7 50%,#bbf7d0);border:2px solid #16a34a;border-radius:16px;padding:28px 32px;text-align:center;margin:20px 0;}
.celebrate-title{font-size:1.6rem;font-weight:700;color:#111827 !important;margin-bottom:6px;}
.celebrate-sub{font-size:.9rem;color:#14532d !important;}
</style>
""", unsafe_allow_html=True)

# ── CONSTANTS ─────────────────────────────────────────────────────────────────
LEVELS = [
    (0,"Mulch Rookie","🌱"),(50,"Fraction Finder","🔢"),
    (120,"Decimal Digger","🪴"),(220,"Rate Ranger","⚡"),
    (350,"Fraction Master","🏆"),
]
BADGES = [
    ("pile1_done","Pile 1 Pro","🟢","Complete Pile 1 analysis"),
    ("decimal_ace","Decimal Ace","💙","Convert fraction to decimal correctly"),
    ("half_spotter","Half Spotter","🟡","Identify if more or less than half remains"),
    ("sixteenth_star","Sixteenth Star","⭐","Explore all fractions to sixteenths"),
    ("multiples_mind","Multiples Mind","🧠","Complete the multiples lesson"),
    ("first_session","First Session","🌿","Complete your first Mulch Math session"),
]

def xp_for_correct(): return 15
def get_level(xp):
    li = 0
    for i,(t,n,ic) in enumerate(LEVELS):
        if xp >= t: li = i
    return li, LEVELS[li]
def xp_to_next(xp):
    for i,(t,n,ic) in enumerate(LEVELS):
        if xp < t:
            prev = LEVELS[i-1][0] if i > 0 else 0
            return t, xp-prev, t-prev
    return None, 0, 1

def xp_bar_html(xp, xp_in, xp_tot, name, icon, idx):
    pct = min(int(xp_in/max(xp_tot,1)*100), 100)
    nxt = LEVELS[idx+1][1] if idx+1 < len(LEVELS) else "MAX"
    return f"""
    <div class="xp-header"><span class="xp-label">{icon} {name}</span>
      <span class="xp-num">⚡ {xp} XP</span></div>
    <div class="xp-bar-wrap"><div class="xp-bar" style="width:{pct}%;"></div></div>
    <div style="display:flex;justify-content:space-between;font-size:.65rem;color:#6b7280;">
      <span>{xp_in}/{xp_tot} to next</span><span>→ {nxt}</span></div>"""

# ── VERTICAL PILE GRAPHIC WITH DOTTED Y-AXIS ──────────────────────────────────
def vertical_pile_graphic(frac_done_1, frac_done_2, hours):
    """Two vertical pile columns with dotted fraction lines on y-axis."""
    fig, axes = plt.subplots(1, 2, figsize=(8, 6), facecolor="#f5f5f3")
    fig.suptitle(f"Mulch Piles After {hours} Hours", fontsize=12,
                 fontweight="bold", color="#111827", y=1.01)

    fraction_marks = [
        (Fraction(1,2),  "1/2"),
        (Fraction(1,4),  "1/4"),
        (Fraction(3,4),  "3/4"),
        (Fraction(1,8),  "1/8"),
        (Fraction(3,8),  "3/8"),
        (Fraction(5,8),  "5/8"),
        (Fraction(7,8),  "7/8"),
    ]

    for ax, frac_done, label, color_done in zip(
            axes, [frac_done_1, frac_done_2],
            ["Pile 1", "Pile 2"],
            ["#16a34a", "#0891b2"]):

        ax.set_facecolor("#f5f5f3")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis("off")
        ax.set_title(label, fontsize=12, fontweight="bold", color="#111827", pad=8)

        # Full pile = MULCH STILL HERE (brown/tan — the pile IS the undone portion)
        pile = patches.FancyBboxPatch((0.25, 0.02), 0.5, 0.90,
            boxstyle="round,pad=0.01", facecolor="#92400e",
            edgecolor="#78350f", linewidth=2, alpha=0.85)
        ax.add_patch(pile)

        # Mulch texture dots on the UNDONE (remaining) pile
        frac_undone = 1 - frac_done
        if frac_undone > 0.05:
            rng = np.random.default_rng(99)
            n_dots = int(frac_undone * 80)
            fill_start = 0.02 + 0.90 * frac_done
            fill_end   = 0.02 + 0.90
            ys_dots = rng.uniform(fill_start + 0.02, fill_end - 0.02, n_dots)
            xs_dots = rng.uniform(0.28, 0.72, n_dots)
            ax.scatter(xs_dots, ys_dots, s=8, color="#fbbf24", alpha=0.35, zorder=4)

        # Spread portion (bottom = done — green ground showing through)
        if frac_done > 0:
            fill_h = 0.90 * frac_done
            fill = patches.FancyBboxPatch((0.25, 0.02), 0.5, fill_h,
                boxstyle="round,pad=0.01", facecolor=color_done,
                edgecolor="none", alpha=0.80)
            ax.add_patch(fill)

        # Texture dots on DONE (spread) area — lighter speckles like spread mulch
        if frac_done > 0.05:
            rng2 = np.random.default_rng(42)
            n_dots2 = int(frac_done * 50)
            xs2 = rng2.uniform(0.28, 0.72, n_dots2)
            ys2 = rng2.uniform(0.03, 0.02 + 0.90*frac_done - 0.03, n_dots2)
            ax.scatter(xs2, ys2, s=5, color="white", alpha=0.3, zorder=4)

        # Dotted fraction lines on y-axis
        for frac, frac_label in fraction_marks:
            y_pos = 0.02 + float(frac) * 0.90
            # Dotted line across pile
            ax.plot([0.22, 0.78], [y_pos, y_pos],
                    color="#374151", linewidth=1.0,
                    linestyle=(0, (4, 3)), alpha=0.7, zorder=5)
            # Label on left
            ax.text(0.18, y_pos, frac_label,
                    ha="right", va="center", fontsize=7.5,
                    color="#374151", fontweight="600")
            # Tick mark
            ax.plot([0.23, 0.25], [y_pos, y_pos],
                    color="#374151", linewidth=1.5, zorder=5)

        # 0 and 1 labels
        ax.text(0.18, 0.02,  "0",   ha="right", va="center", fontsize=8, color="#374151", fontweight="bold")
        ax.text(0.18, 0.92, "1",   ha="right", va="center", fontsize=8, color="#374151", fontweight="bold")
        ax.text(0.18, 0.92, "Whole pile", ha="right", va="bottom", fontsize=6.5, color="#6b7280")

        # Vertical axis line
        ax.plot([0.23, 0.23], [0.02, 0.92],
                color="#374151", linewidth=1.5, zorder=5)

        # Done/Left labels
        frac_left = 1 - frac_done
        ax.text(0.50, 0.02 + 0.90*frac_done + 0.02,
                f"← {frac_left:.2f} LEFT",
                ha="center", va="bottom", fontsize=8,
                color="#6b7280", fontweight="bold")
        ax.text(0.50, 0.02 + 0.90*frac_done * 0.5,
                f"{frac_done:.2f} DONE",
                ha="center", va="center", fontsize=9,
                color="white" if frac_done > 0.12 else "#374151",
                fontweight="bold", zorder=6)

        # Highlight the student fraction line
        y_student = 0.02 + frac_done * 0.90
        ax.plot([0.24, 0.76], [y_student, y_student],
                color="#f97316", linewidth=2.5, zorder=6)
        ax.plot(0.24, y_student, "<", color="#f97316", markersize=7, zorder=7)

    plt.tight_layout()
    return fig

def fraction_strip_vertical(numer, denom, title=""):
    """Vertical fraction strip with dotted y-axis fraction marks."""
    fig, ax = plt.subplots(figsize=(2.5, 5), facecolor="#f5f5f3")
    ax.set_facecolor("#f5f5f3")
    ax.set_xlim(0, 1); ax.set_ylim(0, denom)
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=9, fontweight="bold", color="#111827", pad=6)

    for i in range(denom):
        y = denom - 1 - i  # top = full
        color = "#16a34a" if i < numer else "#e5e7eb"
        edge  = "#15803d" if i < numer else "#9ca3af"
        rect = patches.Rectangle((0.15, y+0.05), 0.6, 0.88,
            facecolor=color, edgecolor=edge, linewidth=1.5)
        ax.add_patch(rect)
        ax.text(0.45, y+0.49, f"1/{denom}",
                ha="center", va="center",
                fontsize=max(5.5, 9-denom//3),
                color="white" if i < numer else "#6b7280",
                fontweight="bold")
        # Dotted line at each boundary
        ax.plot([0.13, 0.77], [y+0.05, y+0.05],
                color="#9ca3af", linewidth=0.8,
                linestyle=(0,(3,3)), alpha=0.6)
        # Y-axis tick
        ax.plot([0.10, 0.14], [y+0.05, y+0.05], color="#374151", linewidth=1.2)
        ax.text(0.08, y+0.05, f"{denom-i-1}/{denom}",
                ha="right", va="center", fontsize=6.5, color="#374151")

    # Axis line
    ax.plot([0.11, 0.11], [0.05, denom-0.07], color="#374151", linewidth=1.5)
    ax.text(0.45, -0.3, f"{numer}/{denom} = {numer/denom:.4f}",
            ha="center", fontsize=8.5, fontweight="bold", color="#16a34a")

    fig.tight_layout()
    return fig

def fraction_explorer_chart(frac_decimal):
    """Bar chart of all fractions halves to sixteenths vs student fraction."""
    fracs = []
    for d in [2,4,8,16]:
        for n in range(1, d):
            fracs.append((n, d, n/d))
    seen = set(); unique = []
    for n,d,v in sorted(fracs, key=lambda x: x[2]):
        if round(v,6) not in seen:
            seen.add(round(v,6)); unique.append((n,d,v))
    labels = [f"{n}/{d}" for n,d,v in unique]
    vals   = [v for n,d,v in unique]
    colors = ["#16a34a" if abs(v-frac_decimal)<0.001 else
              "#86efac" if abs(v-frac_decimal)<0.065 else "#d1d5db"
              for v in vals]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=labels, y=vals, marker_color=colors,
        text=[f"{v:.3f}" for v in vals], textposition="outside",
        textfont=dict(size=8, color="#374151")))
    fig.add_hline(y=frac_decimal, line_color="#e11d48", line_width=2,
                  line_dash="dash",
                  annotation_text=f"Your fraction: {frac_decimal:.3f}",
                  annotation_font_color="#e11d48")
    fig.add_hline(y=0.5, line_color="#f97316", line_width=1.5, line_dash="dot",
                  annotation_text="1/2", annotation_font_color="#f97316")
    fig.update_layout(
        title=dict(text="All Fractions — Halves to Sixteenths",
                   font=dict(size=12, color="#111827")),
        paper_bgcolor="#f5f5f3", plot_bgcolor="#f5f5f3",
        xaxis=dict(tickfont=dict(size=9, color="#374151"), gridcolor="#e2e8f0"),
        yaxis=dict(range=[0,1.15], tickfont=dict(size=9, color="#374151"),
                   gridcolor="#e2e8f0", tickformat=".2f"),
        margin=dict(l=30,r=30,t=50,b=30), height=320, showlegend=False)
    return fig

def multiples_chart():
    """Vertical strips showing halves through thirty-seconds."""
    fig, axes = plt.subplots(1, 5, figsize=(11, 5), facecolor="#f5f5f3")
    fig.suptitle("Doubling the Parts — Halves to Thirty-Seconds",
                 fontsize=11, fontweight="bold", color="#111827")
    rows = [(2,"Halves","#16a34a"),(4,"Quarters","#0891b2"),
            (8,"Eighths","#7c3aed"),(16,"Sixteenths","#d97706"),(32,"Thirty-Seconds","#e11d48")]
    for ax,(d,label,color) in zip(axes,rows):
        ax.set_facecolor("#f5f5f3"); ax.axis("off")
        ax.set_xlim(0,1); ax.set_ylim(0,d)
        ax.set_title(label, fontsize=8, fontweight="bold", color=color, pad=4)
        for i in range(d):
            shade = 0.85 if i%2==0 else 0.55
            rect = patches.Rectangle((0.1, i+0.04), 0.8, 0.9,
                facecolor=color, alpha=shade, edgecolor="white", linewidth=1.2)
            ax.add_patch(rect)
            # dotted line at each boundary
            ax.plot([0.08, 0.92], [i+0.04, i+0.04],
                    color="white", linewidth=0.7,
                    linestyle=(0,(3,2)), alpha=0.8)
            if d <= 16:
                ax.text(0.50, i+0.49, f"1/{d}",
                        ha="center", va="center",
                        fontsize=max(4.5, 9-d//4),
                        color="white", fontweight="bold")
        # Vertical axis with dotted lines at common fractions
        ax.plot([0.07,0.07],[0,d], color="#374151", linewidth=1.2)
        ax.text(0.50, -0.6, f"×{d}", ha="center", fontsize=8, color=color, fontweight="bold")
    plt.tight_layout()
    return fig

def number_line_sixteenths(highlight_frac=None):
    """Vertical number line 0 to 1 with sixteenths and dotted fraction marks."""
    fig, ax = plt.subplots(figsize=(3.5, 8), facecolor="#f5f5f3")
    ax.set_facecolor("#f5f5f3"); ax.axis("off")
    ax.set_xlim(0, 1); ax.set_ylim(-0.02, 1.05)
    ax.set_title("Number Line — Every Sixteenth", fontsize=9,
                 fontweight="bold", color="#111827", pad=4)

    # Main vertical line
    ax.plot([0.5, 0.5], [0, 1], color="#374151", linewidth=2.5)

    colors_by_denom = {2:"#e11d48", 4:"#f97316", 8:"#7c3aed", 16:"#0891b2"}

    for d in [16, 8, 4, 2]:
        for n in range(0, d+1):
            y = n/d
            f = Fraction(n, d)
            if f.denominator == d:
                c = colors_by_denom[d]
                tick_w = 0.18 if d==2 else 0.13 if d==4 else 0.09 if d==8 else 0.06
                # Dotted horizontal line
                ax.plot([0.5-tick_w-0.05, 0.5+tick_w+0.05], [y, y],
                        color=c, linewidth=0.8,
                        linestyle=(0,(3,3)), alpha=0.5)
                # Tick mark
                ax.plot([0.5-tick_w, 0.5+tick_w], [y, y], color=c, linewidth=2.0)
                if n not in [0, d]:
                    label = f"{f.numerator}/{f.denominator}"
                    ax.text(0.5-tick_w-0.06, y, label,
                            ha="right", va="center",
                            fontsize=max(5, 8-d//6), color=c, fontweight="bold")

    ax.text(0.5-0.3, 0,   "0", ha="center", va="center", fontsize=9, fontweight="bold", color="#374151")
    ax.text(0.5-0.3, 1.0, "1", ha="center", va="center", fontsize=9, fontweight="bold", color="#374151")

    if highlight_frac is not None and 0 <= highlight_frac <= 1:
        ax.plot([0.35, 0.65], [highlight_frac, highlight_frac],
                color="#16a34a", linewidth=3, zorder=5)
        ax.plot(0.5, highlight_frac, "o", color="#16a34a", markersize=10, zorder=6)
        ax.text(0.68, highlight_frac, f"← {highlight_frac:.3f}",
                ha="left", va="center", fontsize=8, color="#16a34a", fontweight="bold")

    # Legend
    for i,(d,c,lbl) in enumerate([(2,"#e11d48","Halves"),(4,"#f97316","Quarters"),
                                   (8,"#7c3aed","Eighths"),(16,"#0891b2","16ths")]):
        ax.plot([0.05], [0.97-i*0.04], "s", color=c, markersize=7)
        ax.text(0.10, 0.97-i*0.04, lbl, fontsize=7, color=c, va="center")

    fig.tight_layout()
    return fig

# ── SESSION STATE ─────────────────────────────────────────────────────────────
for k in ["q1_answers","q1_attempts","q2_answers","q2_attempts"]:
    if k not in st.session_state:
        st.session_state[k] = {}
if "earned_badges" not in st.session_state:
    st.session_state.earned_badges = set()

# ── DEV CREDIT ────────────────────────────────────────────────────────────────
st.markdown("""
<div class="dev-credit">
  <h2>🌿 Mulch Math — Fractions, Rates &amp; Real Work</h2>
  <p>CognitiveCloud.ai · Grade 8 Applied Fractions</p><hr>
  <p>💻 Powered by <strong><a href="https://www.cognitivecloud.ai" target="_blank">
  www.cognitivecloud.ai</a></strong> | Developed by Xavier Honablue M.Ed</p>
</div>""", unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### Student Profile")
    student_name = st.text_input("Name", placeholder="e.g. Jordan Smith")
    student_id   = st.text_input("Student ID", placeholder="e.g. CC-2024-001")
    st.divider()
    st.caption("CognitiveCloud.ai · Mulch Math v1.0")
    st.caption(f"Session: {datetime.now().strftime('%d %b %Y')}")

# ── TITLE & HOOK ──────────────────────────────────────────────────────────────
st.title("🌿 Mulch Math")
st.markdown("""
### The Situation
You and your partner are spreading mulch at a community garden.
There are **two piles** — same size. You have been working on Pile 1.

**Your job:** use fractions, rates, and decimals to figure out:
- How much of Pile 1 is left
- How long the whole job will take
- Whether you are more or less than halfway through
- Every possible fraction of the pile — all the way to sixteenths
---
""")

st.info("📚 **Grade 8 Standards:** 8.F.B.4 · 8.EE.B.5 · 7.NS.A.2 · 5.NF.B.3")

st.markdown("#### Common Core & NGSS Standards Covered")
standard = st.selectbox("Select a standard to highlight:", [
    "5.NF.B.3 — A fraction a/b is a ÷ b",
    "6.RP.A.1 — Understand ratio: hours worked per fraction of pile completed",
    "6.RP.A.2 — Unit rate: fraction of pile per hour",
    "7.NS.A.2 — Multiply and divide rational numbers",
    "7.RP.A.1 — Compute unit rates with fractions",
    "8.F.B.4 — Construct a linear function: work_done = rate × hours",
    "8.EE.B.5 — Proportional relationships: double hours = double pile done",
    "8.NS.A.1 — Fractions and decimals are the same number, different form",
])
std_tips = {
    "5.NF.B.3": "When 3/4 of the pile is done, that fraction 3/4 IS 3 ÷ 4 = 0.75.",
    "6.RP.A.1": "Your rate = fraction completed ÷ hours worked. That ratio drives everything.",
    "6.RP.A.2": "Rate per hour IS a unit rate — fraction of pile per 1 hour.",
    "7.NS.A.2": "Total time = hours ÷ fraction done. Dividing by a fraction — flip and multiply!",
    "7.RP.A.1": "0.375 pile per hour — that comes from dividing a fraction by a whole number.",
    "8.F.B.4":  "work_done(h) = rate × h is linear. Rate is the slope. Zero at hour zero.",
    "8.EE.B.5": "3/4 done in 2 hours → 6/4 done in 4 hours. Proportional.",
    "8.NS.A.1": "Every fraction has a decimal. 3/4 = 0.75. Same number, different dress.",
}
for k,tip in std_tips.items():
    if k in standard:
        st.success(f"💡 **Connection:** {tip}")
        break
st.markdown("---")

# ── VOCABULARY ────────────────────────────────────────────────────────────────
st.header("Vocabulary")
vc1,vc2,vc3 = st.columns(3)
with vc1:
    st.markdown("""
**Fraction** — part of a whole. 3/4 means 3 out of 4 equal parts.

**Numerator** — the top number. How many parts you have.

**Denominator** — the bottom number. How many equal parts total.
""")
with vc2:
    st.markdown("""
**Decimal** — another way to write a fraction. 3/4 = 0.75.

**Rate** — fraction comparing two different units. 3/4 pile per 2 hours.

**Equivalent fractions** — same value, different numbers. 1/2 = 2/4 = 4/8.
""")
with vc3:
    st.markdown("""
**Benchmark fraction** — a common fraction used for comparison. 1/2, 1/4, 3/4.

**Sixteenth** — 1/16. The whole cut into 16 equal parts.

**Multiple** — result of multiplying. 32 is a multiple of 16.
""")
st.markdown("---")

# ── SECTION 1: SETUP ──────────────────────────────────────────────────────────
st.markdown('<span class="pill p-1">Section 1 — Set Up the Problem</span>', unsafe_allow_html=True)

col_in1, col_in2 = st.columns(2)
with col_in1:
    hours_worked = st.number_input("Hours worked on Pile 1",
        min_value=0.5, max_value=12.0, value=2.0, step=0.5)
with col_in2:
    st.markdown("**Fraction of Pile 1 completed:**")
    frac_numer = st.number_input("Numerator (top)",      min_value=1, max_value=15, value=3, step=1)
    frac_denom = st.number_input("Denominator (bottom)", min_value=2, max_value=16, value=4, step=1)

if frac_numer >= frac_denom:
    st.warning("Numerator must be less than denominator — you have not finished Pile 1 yet!")
    frac_numer = frac_denom - 1

frac_done  = frac_numer / frac_denom
frac_left  = 1 - frac_done
frac_left_f = Fraction(frac_denom - frac_numer, frac_denom)

st.markdown(f"#### You completed **{frac_numer}/{frac_denom}** of Pile 1 in **{hours_worked} hours**")
st.pyplot(vertical_pile_graphic(frac_done, 0.0, hours_worked))
st.markdown("---")

# ── SECTION 2: PILE 1 ANALYSIS ────────────────────────────────────────────────
st.markdown('<span class="pill p-2">Section 2 — Pile 1 Analysis</span>', unsafe_allow_html=True)

rate = frac_done / hours_worked
total_time_pile1 = 1 / rate
time_remaining_pile1 = frac_left / rate
hours_int = int(time_remaining_pile1)
hours_frac_decimal = time_remaining_pile1 - hours_int
minutes_remaining = hours_frac_decimal * 60

c1,c2,c3,c4 = st.columns(4)
for col,(title,val,unit) in zip([c1,c2,c3,c4],[
    ("Fraction Done",    f"{frac_numer}/{frac_denom}", ""),
    ("Fraction Left",    str(frac_left_f),             ""),
    ("Work Rate",        f"{rate:.4f}",                 "pile/hr"),
    ("Total Time Pile 1",f"{total_time_pile1:.2f}",     "hrs"),
]):
    col.markdown(f"""
    <div class="mcard">
      <div class="mcard-t">{title}</div>
      <div class="mcard-v">{val}<span class="mcard-u"> {unit}</span></div>
    </div>""", unsafe_allow_html=True)

vc1, vc2 = st.columns(2)
with vc1:
    st.markdown(f"**Pile 1 — {frac_numer}/{frac_denom} done**")
    st.pyplot(fraction_strip_vertical(frac_numer, frac_denom,
        f"{frac_numer}/{frac_denom} done"))
with vc2:
    st.markdown(f"**Remaining — {frac_left_f}**")
    st.pyplot(fraction_strip_vertical(frac_denom - frac_numer, frac_denom,
        f"{frac_left_f} left"))

# Decimal lesson
st.markdown(f"""
<div style="background:#f0f9ff;border:1px solid #7dd3fc;border-left:4px solid #0891b2;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:16px 0;">
  <div style="font-weight:700;color:#111827;margin-bottom:8px;font-size:1rem;">
    Decimal Lesson — Converting Fraction Hours</div>
  <div style="color:#111827;font-size:.9rem;line-height:1.9;">
    Time remaining on Pile 1: <strong>{time_remaining_pile1:.4f} hours</strong><br>
    That is <strong>{hours_int} full hours</strong> and <strong>{hours_frac_decimal:.4f}</strong> of an hour.<br><br>
    Convert decimal part to minutes: multiply by 60<br>
    <code>{hours_frac_decimal:.4f} × 60 = {minutes_remaining:.1f} minutes</code><br><br>
    So you need about <strong>{hours_int} hr {minutes_remaining:.0f} min</strong> to finish Pile 1.<br><br>
    <em>Why? Clocks use base-60. Math uses base-10. The decimal 0.5 hours = 30 min because 0.5 × 60 = 30.</em>
  </div>
</div>""", unsafe_allow_html=True)
st.markdown("---")

# ── SECTION 3: MORE OR LESS THAN HALF ─────────────────────────────────────────
st.markdown('<span class="pill p-3">Section 3 — More or Less Than Half?</span>', unsafe_allow_html=True)

half_diff = frac_left - 0.5
if abs(half_diff) < 0.001:
    half_msg = f"Exactly half ({frac_left_f}) remains."; half_color = "#f97316"
elif half_diff > 0:
    half_msg = f"MORE than half left — {frac_left_f} is {abs(half_diff):.3f} MORE than 1/2."; half_color = "#e11d48"
else:
    half_msg = f"LESS than half left — {frac_left_f} is {abs(half_diff):.3f} LESS than 1/2."; half_color = "#16a34a"

st.markdown(f"""
<div style="background:#ffffff;border:2px solid {half_color};border-radius:12px;
  padding:18px 22px;text-align:center;margin:12px 0;">
  <div style="font-size:1.3rem;font-weight:700;color:{half_color};">{half_msg}</div>
  <div style="font-size:.85rem;color:#374151;margin-top:8px;">
    Your fraction: {float(frac_left_f):.4f} | One half: 0.5000 | Difference: {abs(half_diff):.4f}
  </div>
</div>""", unsafe_allow_html=True)

sc1, sc2, sc3 = st.columns(3)
with sc1:
    st.markdown(f"**Your remainder: {frac_left_f}**")
    st.pyplot(fraction_strip_vertical(frac_denom-frac_numer, frac_denom, str(frac_left_f)))
with sc2:
    st.markdown("**Benchmark: 1/2**")
    st.pyplot(fraction_strip_vertical(1, 2, "1/2"))
with sc3:
    st.markdown("**Benchmark: 1/4**")
    st.pyplot(fraction_strip_vertical(1, 4, "1/4"))
st.markdown("---")

# ── SECTION 4: TRANSLATE TO PILE 2 ───────────────────────────────────────────
st.markdown('<span class="pill p-4">Section 4 — Translating Your Rate to Pile 2</span>', unsafe_allow_html=True)
st.markdown(f"""
Pile 2 is the same size. You work at the same rate: **{rate:.4f} pile per hour**.

How many of your **{frac_numer}/{frac_denom}**-sized pieces fit in one whole pile?
""")
st.markdown(f"""
<div style="background:#fefce8;border:1px solid #fbbf24;border-left:4px solid #f59e0b;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;">
  <div style="font-weight:700;color:#111827;margin-bottom:8px;">Pieces of {frac_numer}/{frac_denom} in Pile 2:</div>
  <div style="color:#111827;font-size:.9rem;line-height:2;">
    1 ÷ {frac_numer}/{frac_denom} = 1 × {frac_denom}/{frac_numer} = <strong>{frac_denom/frac_numer:.3f} pieces</strong><br>
    Time to complete Pile 2: 1 ÷ {rate:.4f} = <strong>{1/rate:.2f} hours</strong>
  </div>
</div>""", unsafe_allow_html=True)
st.markdown("---")

# ── SECTION 5: FRACTION EXPLORER ─────────────────────────────────────────────
st.markdown('<span class="pill p-3">Section 5 — Fractions That Describe the Remainder</span>', unsafe_allow_html=True)
st.markdown(f"Your remaining fraction is **{frac_left_f}** = **{float(frac_left_f):.4f}**. "
            "Which standard fractions are closest?")
st.plotly_chart(fraction_explorer_chart(float(frac_left_f)), use_container_width=True)

all_fracs = []
for d in [2,4,8,16]:
    for n in range(1,d):
        f = Fraction(n,d)
        all_fracs.append((f.numerator,f.denominator,float(f),abs(float(f)-float(frac_left_f))))
all_fracs.sort(key=lambda x: x[3])
seen_v = set(); unique_close = []
for n,d,v,diff in all_fracs:
    if round(v,6) not in seen_v:
        seen_v.add(round(v,6)); unique_close.append((n,d,v,diff))

st.markdown("**Closest fractions to your remaining pile:**")
close_cols = st.columns(4)
for i,(n,d,v,diff) in enumerate(unique_close[:4]):
    close_cols[i].markdown(f"""
    <div class="mcard" style="text-align:center;">
      <div class="mcard-t">Rank {i+1} closest</div>
      <div class="mcard-v">{n}/{d}</div>
      <div class="mcard-u">= {v:.4f} | off by {diff*100:.1f}%</div>
    </div>""", unsafe_allow_html=True)

st.markdown("**Vertical strip comparison:**")
strip_cols = st.columns(4)
for col,(n,d,v,diff) in zip(strip_cols, unique_close[:4]):
    with col:
        st.pyplot(fraction_strip_vertical(n,d,f"{n}/{d}"))
st.markdown("---")

# ── SECTION 6: EXPLORE TO SIXTEENTHS ─────────────────────────────────────────
st.markdown('<span class="pill p-2">Section 6 — Explore All Fractions to Sixteenths</span>', unsafe_allow_html=True)

ex_c1, ex_c2 = st.columns(2)
with ex_c1:
    explore_denom = st.number_input("Choose a denominator (2-16)", min_value=2, max_value=16, value=8, step=1)
with ex_c2:
    explore_numer = st.number_input("Choose a numerator",
        min_value=1, max_value=int(explore_denom)-1, value=min(3,int(explore_denom)-1), step=1)

ex_frac = Fraction(explore_numer, explore_denom)
ec1, ec2 = st.columns([2,1])
with ec1:
    st.pyplot(fraction_strip_vertical(explore_numer, explore_denom,
        f"{explore_numer}/{explore_denom} = {explore_numer/explore_denom:.4f}"))
with ec2:
    st.markdown(f"""
    <div class="mcard">
      <div class="mcard-t">Simplified</div>
      <div class="mcard-v">{ex_frac}</div>
      <div class="mcard-u">= {float(ex_frac):.6f}</div>
    </div>
    <div class="irow"><span class="ik">Percent</span>
      <span class="iv">{float(ex_frac)*100:.2f}%</span></div>
    <div class="irow"><span class="ik">vs 1/2</span>
      <span class="iv">{"MORE" if float(ex_frac)>0.5 else "LESS" if float(ex_frac)<0.5 else "EQUAL"}</span></div>
    <div class="irow"><span class="ik">vs 1/4</span>
      <span class="iv">{"MORE" if float(ex_frac)>0.25 else "LESS" if float(ex_frac)<0.25 else "EQUAL"}</span></div>
    """, unsafe_allow_html=True)

nl_c1, nl_c2 = st.columns([1,3])
with nl_c1:
    st.pyplot(number_line_sixteenths(float(frac_left_f)))
with nl_c2:
    st.markdown("""
    **Reading the number line:**
    - Each color represents a different denominator
    - Red = halves, Orange = quarters, Purple = eighths, Blue = sixteenths
    - The green dot shows YOUR remaining fraction
    - Dotted lines help you see which fractions are equivalent
    """)
st.markdown("---")

# ── SECTION 7: MULTIPLES LESSON ───────────────────────────────────────────────
st.markdown('<span class="pill p-5">Section 7 — Multiples: Sixteenths to Thirty-Seconds</span>', unsafe_allow_html=True)
st.markdown("""
Every time you **double the denominator**, you cut each piece in half.

- 1/2 → cut each half into 2 → **1/4** (quarters)
- 1/4 → cut each quarter into 2 → **1/8** (eighths)
- 1/8 → cut each eighth into 2 → **1/16** (sixteenths)
- 1/16 → cut each sixteenth into 2 → **1/32** (thirty-seconds)

**1/32 is not double 1/16 — it is HALF the size.**
The denominator doubled, so each piece got smaller.
""")
st.pyplot(multiples_chart())
st.markdown(f"""
<div style="background:#fdf4ff;border:1px solid #d8b4fe;border-left:4px solid #7c3aed;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:14px 0;">
  <div style="font-weight:700;color:#111827;margin-bottom:8px;">The Multiple Rule</div>
  <div style="color:#111827;font-size:.9rem;line-height:1.9;">
    <strong>Doubling the denominator</strong> = twice as many pieces = each piece is half the size.<br>
    1/16 × 2 = 2/16 = 1/8 — two sixteenths equal one eighth.<br>
    1/32 × 2 = 2/32 = 1/16 — two thirty-seconds equal one sixteenth.<br><br>
    This is why 32 is a multiple of 16: 16 × 2 = 32.<br>
    A 32nd-inch ruler has twice as many marks as a 16th-inch ruler. Same ruler. Twice the precision.
  </div>
</div>""", unsafe_allow_html=True)
st.markdown("---")

# ── EQUIVALENT FRACTIONS ──────────────────────────────────────────────────────
st.markdown('<span class="pill p-1">Section 8 — Equivalent Fractions</span>', unsafe_allow_html=True)
st.markdown("""
**Equivalent fractions** name the same amount with different numbers.
Multiply (or divide) both top and bottom by the same number.
""")
eq_c1, eq_c2 = st.columns(2)
with eq_c1:
    eq_n = st.number_input("Start numerator",   min_value=1, max_value=8, value=1, step=1, key="eq_n")
    eq_d = st.number_input("Start denominator", min_value=2, max_value=8, value=2, step=1, key="eq_d")
with eq_c2:
    eq_m = st.number_input("Multiply both by",  min_value=2, max_value=8, value=4, step=1, key="eq_m")

eq_nn = eq_n * eq_m; eq_nd = eq_d * eq_m
st.markdown(f"""
<div style="background:#f0fdf4;border:1px solid #86efac;border-left:4px solid #16a34a;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;text-align:center;font-size:1.2rem;font-weight:700;color:#111827;">
  {eq_n}/{eq_d} × ({eq_m}/{eq_m}) = {eq_nn}/{eq_nd} &nbsp;&nbsp;
  {"✅ Equal!" if abs(eq_n/eq_d - eq_nn/eq_nd) < 0.0001 else "❌"}
  &nbsp;&nbsp; ({eq_n/eq_d:.6f} = {eq_nn/eq_nd:.6f})
</div>""", unsafe_allow_html=True)

eqvc1, eqvc2 = st.columns(2)
with eqvc1:
    st.markdown(f"**Original: {eq_n}/{eq_d}**")
    st.pyplot(fraction_strip_vertical(eq_n, eq_d, f"{eq_n}/{eq_d}"))
with eqvc2:
    st.markdown(f"**Equivalent: {eq_nn}/{eq_nd}**")
    st.pyplot(fraction_strip_vertical(eq_nn, eq_nd, f"{eq_nn}/{eq_nd}"))
st.markdown("---")


# ── X & Y AXIS TUTORIAL ───────────────────────────────────────────────────────
st.markdown('<span class="pill p-4">Section 9 — X &amp; Y Axis: Graphing Your Work Over Time</span>',
            unsafe_allow_html=True)

st.markdown("""
### The Word Problem

Marcus and Destiny are spreading mulch at the community garden.
They have **2 piles** — same size. They start working together at 8:00 AM.

After working for a while, Marcus notices they have finished
**{frac_numer}/{frac_denom}** of Pile 1.

**Nobody knows how long the whole job will take.**

Their teacher asks: *"Can you graph your progress and estimate
what time you will finish both piles?"*

That is what we are going to do — using an **x and y axis.**
""".format(frac_numer=frac_numer, frac_denom=frac_denom))

st.markdown("""
<div style="background:#f0f9ff;border:1px solid #7dd3fc;border-left:4px solid #0891b2;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;">
  <div style="font-weight:700;color:#111827;margin-bottom:8px;font-size:1rem;">
    What do X and Y mean here?</div>
  <div style="color:#111827;font-size:.9rem;line-height:1.9;">
    <strong>X-axis (horizontal) = Time</strong> — hours worked. We do not know the total yet.
    Time always goes on the x-axis when something changes over time.<br><br>
    <strong>Y-axis (vertical) = Piles completed</strong> — goes from 0 (nothing done)
    to 2 (both piles finished). We divide it into halves, quarters, and eighths
    so we can plot any fraction.<br><br>
    <strong>The line</strong> = your work rate. Every hour you move up the same amount.
    That steady climb is what makes this a <em>linear function</em>: y = rate × x.
  </div>
</div>""", unsafe_allow_html=True)

# ── BUILD THE GRAPH ────────────────────────────────────────────────────────────
st.markdown("#### Your Progress Graph")
st.markdown("Adjust your **time estimate** below — the graph updates live. "
            "Try to find the x value where the line crosses **y = 2 piles**.")

student_time_estimate = st.number_input(
    "Your estimate: total hours to finish BOTH piles",
    min_value=0.5, max_value=24.0, value=round(2/rate, 1), step=0.5,
    help="Drag up or down until the line crosses y=2 at your estimated time.")

def xy_axis_graph(rate, hours_worked, frac_done, time_estimate):
    """X-Y graph: x=time, y=piles done (0 to 2), with dotted fraction grid."""
    true_total = 2 / rate          # actual time to finish both piles
    x_max      = max(time_estimate * 1.15, true_total * 1.1, 6.0)

    fig, ax = plt.subplots(figsize=(9, 6), facecolor="#f5f5f3")
    ax.set_facecolor("#f8fafc")
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, 2.15)

    # ── Y-axis fraction grid lines (halves down to eighths) ──
    y_fractions = []
    for d in [8, 4, 2]:
        for n in range(1, 2*d):
            y_fractions.append((n, d, n/d))
    # deduplicate by value
    seen_y = set(); y_unique = []
    for n,d,v in sorted(y_fractions, key=lambda x: x[2]):
        if round(v,6) not in seen_y and v <= 2.0:
            seen_y.add(round(v,6)); y_unique.append((n,d,v))

    for n,d,v in y_unique:
        lw   = 1.4 if d==2 else 0.9 if d==4 else 0.5
        dash = (0,(4,3)) if d==2 else (0,(3,4)) if d==4 else (0,(2,5))
        col  = "#374151" if d==2 else "#6b7280" if d==4 else "#9ca3af"
        alpha = 0.7 if d==2 else 0.5 if d==4 else 0.3
        ax.axhline(y=v, color=col, linewidth=lw, linestyle=dash, alpha=alpha, zorder=1)
        # Y-axis label
        if d <= 4:
            label = f"{n}/{d}" if v != int(v) else f"{int(v)}"
            ax.text(-x_max*0.025, v, label, ha="right", va="center",
                    fontsize=8, color=col, fontweight="bold" if d==2 else "normal")

    # Whole pile markers (y=1 and y=2)
    ax.axhline(y=1, color="#16a34a", linewidth=2.0, linestyle="--", alpha=0.8, zorder=2)
    ax.axhline(y=2, color="#e11d48", linewidth=2.0, linestyle="--", alpha=0.8, zorder=2)
    ax.text(x_max*0.98, 1.02, "Pile 1 done ✅", ha="right", fontsize=8.5,
            color="#16a34a", fontweight="bold")
    ax.text(x_max*0.98, 2.03, "Both piles done!", ha="right", fontsize=8.5,
            color="#e11d48", fontweight="bold")

    # ── Work rate line ──
    x_line = np.linspace(0, x_max, 200)
    y_line = rate * x_line
    y_line_clipped = np.minimum(y_line, 2.0)
    ax.plot(x_line, y_line_clipped, color="#0891b2", linewidth=3,
            label=f"Work rate: y = {rate:.3f}x", zorder=4)

    # ── True finish time ──
    ax.axvline(x=true_total, color="#16a34a", linewidth=1.5,
               linestyle=(0,(4,3)), alpha=0.7, zorder=3)
    ax.text(true_total+x_max*0.01, 1.85, f"Actual finish {true_total:.2f} hrs",
            fontsize=8, color="#16a34a", va="top")

    # ── Student estimate line ──
    y_at_estimate = min(rate * time_estimate, 2.0)
    ax.axvline(x=time_estimate, color="#f97316", linewidth=2.0,
               linestyle=(0,(5,3)), alpha=0.9, zorder=3)
    ax.text(time_estimate+x_max*0.01, 0.12, f"Your estimate: {time_estimate} hrs",
            fontsize=8, color="#f97316")

    # ── Current position dot ──
    x_now  = hours_worked
    y_now  = frac_done          # fraction of pile 1 = y value
    ax.plot(x_now, y_now, "o", color="#e11d48", markersize=12, zorder=6,
            label=f"Now: ({x_now}h, {y_now:.3f} piles)")
    # Dotted drop lines to both axes
    ax.plot([0, x_now], [y_now, y_now], color="#e11d48",
            linewidth=1.2, linestyle=(0,(3,3)), alpha=0.7, zorder=5)
    ax.plot([x_now, x_now], [0, y_now], color="#e11d48",
            linewidth=1.2, linestyle=(0,(3,3)), alpha=0.7, zorder=5)
    ax.text(x_now+x_max*0.01, y_now+0.04,
            f"  ({x_now}h, {frac_numer}/{frac_denom})",
            fontsize=9, color="#e11d48", fontweight="bold", zorder=7)

    # ── Axes styling ──
    ax.set_xlabel("Time (hours)", fontsize=11, fontweight="bold", color="#111827")
    ax.set_ylabel("Piles Completed", fontsize=11, fontweight="bold", color="#111827")
    ax.set_title("Mulch Work Progress — Both Piles", fontsize=12,
                 fontweight="bold", color="#111827", pad=10)

    # X-axis ticks
    x_ticks = np.arange(0, x_max+0.5, 0.5)
    ax.set_xticks(x_ticks)
    ax.set_xticklabels([f"{t:.1f}" for t in x_ticks], fontsize=8, color="#374151")

    # Y-axis major ticks
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0])
    ax.set_yticklabels(["0","1/4","1/2","3/4","1","1¼","1½","1¾","2"],
                       fontsize=9, color="#374151")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#374151")
    ax.spines["bottom"].set_color("#374151")
    ax.tick_params(colors="#374151")
    ax.grid(axis="x", color="#e2e8f0", linewidth=0.8, alpha=0.5)

    # Shaded "done" zone
    x_fill = np.linspace(0, min(true_total, x_max), 100)
    y_fill = np.minimum(rate * x_fill, 2.0)
    ax.fill_between(x_fill, 0, y_fill, alpha=0.08, color="#0891b2", zorder=0)

    ax.legend(loc="upper left", fontsize=9, framealpha=0.9)
    fig.tight_layout()
    return fig

st.pyplot(xy_axis_graph(rate, hours_worked, frac_done, student_time_estimate))

# ── Estimate feedback ──────────────────────────────────────────────────────────
true_total_time = 2 / rate
estimate_error  = abs(student_time_estimate - true_total_time)
estimate_pct    = (estimate_error / true_total_time) * 100

if estimate_error < 0.25:
    est_msg   = f"Excellent estimate! You are only {estimate_error:.2f} hrs off."
    est_color = "#16a34a"
elif estimate_error < 1.0:
    est_msg   = f"Good estimate — {estimate_error:.2f} hrs off ({estimate_pct:.0f}%)."
    est_color = "#d97706"
else:
    diff_dir  = "too high" if student_time_estimate > true_total_time else "too low"
    est_msg   = f"Off by {estimate_error:.2f} hrs ({estimate_pct:.0f}%) — {diff_dir}. Try again!"
    est_color = "#e11d48"

st.markdown(f"""
<div style="background:#ffffff;border:2px solid {est_color};border-radius:12px;
  padding:16px 22px;margin:14px 0;">
  <div style="font-size:1.1rem;font-weight:700;color:{est_color};">{est_msg}</div>
  <div style="font-size:.88rem;color:#374151;margin-top:8px;line-height:1.8;">
    <strong>Actual finish time:</strong> {true_total_time:.2f} hours &nbsp;|&nbsp;
    <strong>Your estimate:</strong> {student_time_estimate} hours<br>
    <strong>Formula:</strong> Total time = 2 piles ÷ {rate:.4f} pile/hr = {true_total_time:.2f} hrs<br>
    <strong>As a fraction:</strong> {Fraction(frac_numer,frac_denom)} done in {hours_worked} hrs
    → rate = {Fraction(frac_numer,frac_denom)}/{int(hours_worked) if hours_worked==int(hours_worked) else hours_worked}
    pile/hr = {rate:.4f} pile/hr
  </div>
</div>""", unsafe_allow_html=True)

# ── Reading the graph lesson ───────────────────────────────────────────────────
st.markdown("""
<div style="background:#fefce8;border:1px solid #fbbf24;border-left:4px solid #f59e0b;
  border-radius:0 10px 10px 0;padding:16px 20px;margin:12px 0;">
  <div style="font-weight:700;color:#111827;margin-bottom:8px;">
    How to Read This Graph</div>
  <div style="color:#111827;font-size:.9rem;line-height:1.9;">
    <strong>Find your dot</strong> (red circle) — that is where you are RIGHT NOW.<br>
    Drop straight DOWN to the x-axis → that tells you how many hours you have worked.<br>
    Go straight LEFT to the y-axis → that tells you what fraction of the whole job is done.<br><br>
    <strong>The blue line</strong> is your work rate — it is straight because you work at a constant rate.<br>
    Every hour you move up the same amount on the y-axis. That equal spacing is what makes it LINEAR.<br><br>
    <strong>Where the line hits y = 2</strong> → read down to the x-axis → that is your finish time.
  </div>
</div>""", unsafe_allow_html=True)

st.markdown("---")

# ── QUIZ 1 ────────────────────────────────────────────────────────────────────
st.header("Quiz 1 — Fractions & Rates")
q1_questions = {
    "If you completed 3/4 of a pile in 2 hours, what is your work rate?": {
        "options":["3/8 pile per hour","3/4 pile per hour","8/3 pile per hour","2/3 pile per hour"],
        "correct":"3/8 pile per hour",
        "hint":"💡 Rate = fraction done ÷ hours. So (3/4) ÷ 2 = 3/4 × 1/2 = 3/8.",
        "explanation":"Rate = (3/4) ÷ 2 = 3/8 pile per hour.",
    },
    "3/4 done means what fraction is LEFT?": {
        "options":["3/4","1/2","1/4","2/3"],
        "correct":"1/4",
        "hint":"💡 The whole pile = 1. Subtract what is done: 1 - 3/4 = 1/4.",
        "explanation":"1 - 3/4 = 4/4 - 3/4 = 1/4. One quarter remains.",
    },
    "Which of these is NOT equivalent to 1/2?": {
        "options":["2/4","4/8","3/8","8/16"],
        "correct":"3/8",
        "hint":"💡 3/8 = 0.375, not 0.5. All others equal exactly 0.5.",
        "explanation":"3/8 = 0.375. 2/4, 4/8, and 8/16 all equal 0.5.",
    },
}
for qi,(question,data) in enumerate(q1_questions.items()):
    st.write(f"**{question}**")
    ans = st.radio("Your answer:", data["options"], key=f"q1_{qi}")
    if qi not in st.session_state.q1_attempts: st.session_state.q1_attempts[qi]=0
    if st.button("Check Answer", key=f"q1_check_{qi}"):
        if ans == data["correct"]:
            st.success(f"✅ Correct! {data['explanation']}")
            st.session_state.q1_answers[qi]=True
            st.session_state.q1_attempts[qi]=0
            st.session_state.earned_badges.add("pile1_done")
        else:
            st.session_state.q1_attempts[qi]+=1
            if st.session_state.q1_attempts[qi]==1:
                st.warning("❌ Not quite — hint:"); st.info(data["hint"])
                st.session_state.q1_answers[qi]=False
            else:
                st.error(f"❌ {data['explanation']}")
                st.warning(f"💡 Correct answer: **{data['correct']}**")
                st.session_state.q1_answers[qi]=False
if len(st.session_state.q1_answers)==3 and all(st.session_state.q1_answers.values()):
    st.success("🎉 Perfect Quiz 1!"); st.balloons()
st.markdown("---")

# ── QUIZ 2 ────────────────────────────────────────────────────────────────────
st.header("Quiz 2 — Decimals & Sixteenths")
q2_questions = {
    "What is 3/8 as a decimal?": {
        "options":["0.375","0.38","0.83","0.35"],
        "correct":"0.375",
        "hint":"💡 Divide 3 ÷ 8. Or: 1/8 = 0.125, so 3/8 = 3 × 0.125 = 0.375.",
        "explanation":"3 ÷ 8 = 0.375.",
    },
    "How many sixteenths equal one half?": {
        "options":["4","6","8","16"],
        "correct":"8",
        "hint":"💡 1/2 ÷ 1/16 = 1/2 × 16 = 8.",
        "explanation":"1/2 = 8/16. Eight sixteenths make one half.",
    },
    "If 1/16 is one piece, 1/32 is...": {
        "options":["Double the size","The same size","Half the size","4 times the size"],
        "correct":"Half the size",
        "hint":"💡 Doubling the denominator (16→32) cuts each piece in half.",
        "explanation":"1/32 is half of 1/16. Two thirty-seconds = one sixteenth.",
    },
}
for qi,(question,data) in enumerate(q2_questions.items()):
    st.write(f"**{question}**")
    ans = st.radio("Your answer:", data["options"], key=f"q2_{qi}")
    if qi not in st.session_state.q2_attempts: st.session_state.q2_attempts[qi]=0
    if st.button("Check Answer", key=f"q2_check_{qi}"):
        if ans == data["correct"]:
            st.success(f"✅ Correct! {data['explanation']}")
            st.session_state.q2_answers[qi]=True
            st.session_state.q2_attempts[qi]=0
            st.session_state.earned_badges.add("decimal_ace")
        else:
            st.session_state.q2_attempts[qi]+=1
            if st.session_state.q2_attempts[qi]==1:
                st.warning("❌ Hint:"); st.info(data["hint"])
                st.session_state.q2_answers[qi]=False
            else:
                st.error(f"❌ {data['explanation']}")
                st.warning(f"💡 Correct: **{data['correct']}**")
                st.session_state.q2_answers[qi]=False
if len(st.session_state.q2_answers)==3 and all(st.session_state.q2_answers.values()):
    st.success("🏆 Perfect Quiz 2!"); st.balloons()
    st.session_state.earned_badges.update(["sixteenth_star","multiples_mind"])
st.markdown("---")

# ── XP REPORT ─────────────────────────────────────────────────────────────────
st.markdown('<span class="pill p-g">XP &amp; Achievement Report</span>', unsafe_allow_html=True)
q1c = sum(1 for v in st.session_state.q1_answers.values() if v)
q2c = sum(1 for v in st.session_state.q2_answers.values() if v)
session_xp = (q1c + q2c) * xp_for_correct() + 10
st.session_state.earned_badges.add("first_session")
level_idx,(_,level_name,level_icon) = get_level(session_xp)
_,xp_in_lvl,lvl_total = xp_to_next(session_xp)

xp_c1,xp_c2 = st.columns([2,3])
with xp_c1:
    st.markdown(xp_bar_html(session_xp,xp_in_lvl,lvl_total,level_name,level_icon,level_idx), unsafe_allow_html=True)
    st.markdown(f"""
    <div style="margin-top:12px;">
      <div class="irow"><span class="ik">Quiz 1</span><span class="iv">+{q1c*xp_for_correct()} XP</span></div>
      <div class="irow"><span class="ik">Quiz 2</span><span class="iv">+{q2c*xp_for_correct()} XP</span></div>
      <div class="irow"><span class="ik">Session complete</span><span class="iv">+10 XP</span></div>
      <div class="irow" style="background:#fef3c7;border:1px solid #fbbf24;">
        <span class="ik" style="font-weight:700;">Total</span>
        <span class="iv" style="color:#16a34a;font-size:1rem;">{session_xp} XP</span></div>
    </div>""", unsafe_allow_html=True)
with xp_c2:
    st.markdown("**Achievements**")
    bh = '<div class="badge-row">'
    for bid,bname,bicon,bdesc in BADGES:
        if bid in st.session_state.earned_badges:
            bh += f'<span class="badge badge-earned" title="{bdesc}">{bicon} {bname}</span>'
        else:
            bh += f'<span class="badge badge-locked" title="{bdesc}">🔒 {bname}</span>'
    bh += '</div>'
    st.markdown(bh, unsafe_allow_html=True)
st.markdown("---")

# ── REFLECTION ────────────────────────────────────────────────────────────────
st.header("Reflection")
reflection = st.text_area("How does the fraction of Pile 1 you completed help predict Pile 2? Use at least one number.",
    placeholder=f"e.g. I completed {frac_numer}/{frac_denom} in {hours_worked} hours so my rate is {rate:.3f}...",
    height=100)
if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Great thinking! Numbers make your reflection stronger.")
        st.balloons()
    else:
        st.warning("Please write your reflection first.")
st.markdown("---")

# ── FINAL REPORT ──────────────────────────────────────────────────────────────
if st.button("Complete Session & Generate Report", use_container_width=True):
    with st.spinner("Compiling Mulch Math report..."): time.sleep(1)
    name_display = student_name if student_name else "Student"
    grade = "Outstanding" if session_xp>=80 else "Great" if session_xp>=50 else "Good Start"
    st.markdown(f"""
    <div class="celebrate-box">
      <div class="celebrate-title">{grade} — Session Complete!</div>
      <div class="celebrate-sub">
        {name_display} · Fraction: {frac_numer}/{frac_denom} ·
        Rate: {rate:.3f} pile/hr · Level: {level_icon} {level_name} · XP: {session_xp}
      </div>
    </div>""", unsafe_allow_html=True)
    st.balloons()

# ── RESOURCES ─────────────────────────────────────────────────────────────────
st.header("Practice Resources")
st.subheader("IXL Practice")
ixl = {
    "Grade 5 — Fractions (5.NF)": [
        ("5.NF.A.1","Add fractions with unlike denominators","https://www.ixl.com/math/grade-5/add-and-subtract-fractions-with-unlike-denominators"),
        ("5.NF.B.3","Fractions as division — word problems","https://www.ixl.com/math/grade-5/divide-whole-numbers-to-find-fractions"),
        ("5.NF.B.7","Divide unit fractions by whole numbers","https://www.ixl.com/math/grade-5/divide-unit-fractions-by-whole-numbers"),
    ],
    "Equivalent Fractions": [
        ("4.NF.A.1","Equivalent fractions — concept","https://www.ixl.com/math/grade-4/equivalent-fractions"),
        ("4.NF.A.2","Compare fractions using benchmarks","https://www.ixl.com/math/grade-4/compare-fractions-using-benchmarks"),
        ("5.NF.A.1","Fractions on a number line","https://www.ixl.com/math/grade-5/fractions-on-number-lines"),
    ],
    "Grade 6–7 — Rates & Ratios": [
        ("6.RP.A.1","Understand ratios","https://www.ixl.com/math/grade-6/understand-ratios"),
        ("6.RP.A.2","Find unit rates","https://www.ixl.com/math/grade-6/unit-rates"),
        ("7.RP.A.1","Unit rates with fractions","https://www.ixl.com/math/grade-7/unit-rates-with-fractions"),
    ],
    "Grade 8 — Functions": [
        ("8.F.B.4","Write a linear function from a word problem","https://www.ixl.com/math/grade-8/write-a-linear-function-word-problems"),
        ("8.EE.B.5","Graph proportional relationships","https://www.ixl.com/math/grade-8/graph-a-proportional-relationship"),
        ("8.NS.A.1","Convert fractions to decimals","https://www.ixl.com/math/grade-8/convert-fractions-to-decimals"),
    ],
}
for topic,lessons in ixl.items():
    st.markdown(f"""
    <div style="background:#ffffff;border:1px solid #d1d5db;border-left:4px solid #e11d48;
      border-radius:0 8px 8px 0;padding:12px 16px;margin-bottom:10px;">
      <div style="font-size:.8rem;font-weight:700;color:#111827;margin-bottom:8px;">{topic}</div>
      {"".join(f'<div style="margin-bottom:6px;"><a href="{url}" target="_blank" style="font-size:.8rem;font-weight:600;color:#1d4ed8;text-decoration:none;">🔗 {name}</a> <code style="font-size:.68rem;background:#f1f5f9;padding:1px 5px;border-radius:4px;color:#374151;">{std}</code></div>' for std,name,url in lessons)}
    </div>""", unsafe_allow_html=True)

st.subheader("Khan Academy")
khan = {
    "Equivalent Fractions": ("Core of Section 8 — why 1/2 = 2/4 = 4/8.",
        "https://www.khanacademy.org/math/cc-fourth-grade-math/cc-4th-fractions-topic/cc-4th-equivalence-fractions/v/equivalent-fractions"),
    "Fractions as Division (5.NF.B.3)": ("3 divided by 4 IS 3/4 — the foundation of your work rate.",
        "https://www.khanacademy.org/math/cc-fifth-grade-math/cc-5th-fractions-topic/cc-5th-fractions-as-division/v/fractions-as-division"),
    "Dividing Fractions (7.NS)": ("Total time = 1 pile ÷ rate. Flip and multiply.",
        "https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-fractions/cc-7th-div-fractions/v/dividing-fractions-word-problems"),
    "Unit Rates (6.RP)": ("Your work rate per hour is a unit rate.",
        "https://www.khanacademy.org/math/cc-sixth-grade-math/cc-6th-ratios-prop-topic/cc-6th-unit-rates/v/unit-rates"),
    "Decimals from Fractions (8.NS)": ("Every fraction has a decimal. 3/8 = 0.375.",
        "https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-numbers-operations/cc-8th-repeating-decimals/v/converting-fractions-to-decimals"),
    "Linear Functions (8.F.B.4)": ("work_done = rate × hours. Rate is the slope.",
        "https://www.khanacademy.org/math/cc-eighth-grade-math/cc-8th-linear-equations-functions/8th-slope-intercept-form/v/slope-intercept-form"),
}
kc1,kc2 = st.columns(2)
for i,(title,(desc,url)) in enumerate(khan.items()):
    with (kc1 if i%2==0 else kc2):
        st.markdown(f"""
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:10px;padding:12px 16px;margin-bottom:10px;">
          <div style="font-size:.8rem;font-weight:700;color:#111827;margin-bottom:4px;">{title}</div>
          <div style="font-size:.74rem;color:#374151;margin-bottom:8px;">{desc}</div>
          <a href="{url}" target="_blank" style="font-size:.72rem;font-weight:600;color:#1d4ed8;text-decoration:none;">Watch on Khan Academy →</a>
        </div>""", unsafe_allow_html=True)

st.subheader("Interactive Tools & Outside Resources")
outside = {
    "Desmos — Fraction Explorer": ("Type (3/4) on a number line. Type (3/4)=(x/8) to find equivalents.","https://www.desmos.com/calculator","#f97316","Free · Browser"),
    "Fraction Wall — Math is Fun": ("Visual fraction wall halves through twelfths.","https://www.mathsisfun.com/numbers/fraction-number-line.html","#0891b2","Free · Visual"),
    "GeoGebra — Fraction Number Line": ("Drag fractions onto a line and see equivalents snap.","https://www.geogebra.org/m/fraction-number-line","#7c3aed","Free · Interactive"),
    "Math Antics — Fractions (YouTube)": ("Highly rated video series on fractions and mixed numbers.","https://www.youtube.com/watch?v=n0FZhQ_GkKw","#e11d48","Free · Video"),
    "OpenStax Prealgebra — Fractions": ("Free peer-reviewed textbook chapter on fractions and rates.","https://openstax.org/books/prealgebra-2e/pages/4-1-visualize-fractions","#16a34a","Free Textbook"),
    "NCTM Illuminations — Fraction Games": ("Games from the National Council of Teachers of Mathematics.","https://illuminations.nctm.org/search/?keyword=fraction","#374151","NCTM · Standards-Aligned"),
    "Michigan Works! — STEM Careers": ("Michigan-specific career resources connecting math to real jobs.","https://www.michiganworks.org","#0f3460","Michigan · Local"),
    "FIRST Robotics Competition": ("High school robotics — uses rates and functions to control robots.","https://www.firstinspires.org/robotics/frc","#dc2626","Competition · Scholarships"),
}
oc1,oc2 = st.columns(2)
for i,(name,(desc,url,color,tag)) in enumerate(outside.items()):
    with (oc1 if i%2==0 else oc2):
        st.markdown(f"""
        <a href="{url}" target="_blank" style="text-decoration:none;">
        <div style="background:#f8fafc;border:1px solid #e2e8f0;border-left:4px solid {color};
          border-radius:0 10px 10px 0;padding:13px 16px;margin-bottom:12px;">
          <div style="font-size:.8rem;font-weight:700;color:#111827;margin-bottom:3px;">{name} ↗</div>
          <div style="font-size:.74rem;color:#475569;line-height:1.6;margin-bottom:5px;">{desc}</div>
          <span style="font-size:.62rem;font-weight:700;color:{color};background:{color}15;padding:2px 8px;border-radius:99px;">{tag}</span>
        </div></a>""", unsafe_allow_html=True)

st.subheader("Personalised Study Plan")
sp_level = st.selectbox("Your comfort with fractions:", [
    "Beginner — fractions feel confusing",
    "Developing — basics OK but equivalents trip me up",
    "Proficient — fractions fine but rates confuse me",
    "Advanced — ready for ratios, rates, and functions",
], key="sp_level")
if st.button("Generate My Study Plan", key="sp_btn"):
    st.success("Your Fraction Study Plan:")
    if "Beginner" in sp_level:
        st.markdown("""
        **Week 1:** Watch Math Antics Fractions · IXL: Equivalent fractions (4.NF.A.1) · Use Fraction Wall daily
        **Week 2:** IXL: Convert fractions to decimals · Khan: Fractions as Division · For every fraction you write, also write its decimal
        """)
    elif "Developing" in sp_level:
        st.markdown("""
        **Week 1:** IXL: Generate equivalent fractions (4.NF.A.1) · GeoGebra: drag fractions on a number line
        **Week 2:** Khan: Unit Rates · IXL: Rate problems (6.RP.A.3) · Change the hours in this app and watch the rate update
        """)
    elif "Proficient" in sp_level:
        st.markdown("""
        **Week 1:** IXL: Unit rates with fractions (7.RP.A.1) · Khan: Dividing Fractions
        **Week 2:** IXL: Write a linear function (8.F.B.4) · Desmos: graph y = rate × x for your pile
        """)
    else:
        st.markdown("""
        **Advanced:** Explore inverse functions — given total time, solve for fraction done · Research how landscaping companies use rates for job bids · Write a Python function that takes hours and fraction_done and returns total_time and rate
        """)

st.markdown("---")
st.markdown(f"**Standard Focus:** {standard}")
st.markdown("""
<div style="text-align:center;font-size:.72rem;color:#6b7280;padding:16px 0 8px;">
  CognitiveCloud.ai · Mulch Math v1.0 · Developed by Xavier Honablue M.Ed ·
  <a href="https://cognitivecloud-launcher.streamlit.app" style="color:#16a34a;">Back to Launcher</a>
</div>""", unsafe_allow_html=True)
