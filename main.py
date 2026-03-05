"""
Vizualizace matematických funkcí pomocí NumPy a Matplotlib
Spuštění: python main.py [název_funkce]
Dostupné funkce: linear, quadratic, sin, cos, exp, log
Příklad: python main.py sin
Bez argumentu: vykreslí všechny funkce
"""

import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from functions import linear, quadratic, sine, cosine, exponential, logarithm, FUNCTIONS

# Nastavení
IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

# Rozsah x hodnot
X = np.linspace(-10, 10, 1000)
X_POSITIVE = np.linspace(0.01, 10, 1000)  # pro logaritmus


def plot_with_extremes(ax, x, y, color="royalblue", label="f(x)"):
    """Vykreslí funkci a vyznačí maximum a minimum."""
    valid = ~np.isnan(y)
    x_v, y_v = x[valid], y[valid]

    ax.plot(x_v, y_v, color=color, linewidth=2, label=label)

    if len(y_v) > 0:
        idx_max = np.argmax(y_v)
        idx_min = np.argmin(y_v)

        ax.scatter(x_v[idx_max], y_v[idx_max], color="red", zorder=5,
                   s=80, label=f"Maximum ({x_v[idx_max]:.2f}, {y_v[idx_max]:.2f})")
        ax.scatter(x_v[idx_min], y_v[idx_min], color="green", zorder=5,
                   s=80, label=f"Minimum ({x_v[idx_min]:.2f}, {y_v[idx_min]:.2f})")


def save_plot(fig, filename):
    path = os.path.join(IMAGES_DIR, filename)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    print(f"  Uloženo: {path}")
    plt.close(fig)


# ── 1. Lineární funkce ────────────────────────────────────────────────────────
def plot_linear():
    fig, ax = plt.subplots(figsize=(8, 5))
    for a, b, color in [(1, 0, "royalblue"), (2, 3, "tomato"), (-1, 5, "seagreen")]:
        ax.plot(X, linear(X, a, b), color=color, linewidth=2,
                label=f"f(x) = {a}x + {b}")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_title("Lineární funkce: f(x) = ax + b", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "linear.png")


# ── 2. Kvadratická funkce ─────────────────────────────────────────────────────
def plot_quadratic():
    fig, ax = plt.subplots(figsize=(8, 5))
    for a, b, c, color in [(1, 0, 0, "royalblue"), (1, -2, -3, "tomato"), (-0.5, 1, 4, "seagreen")]:
        ax.plot(X, quadratic(X, a, b, c), color=color, linewidth=2,
                label=f"f(x) = {a}x² + {b}x + {c}")
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_ylim(-20, 20)
    ax.set_title("Kvadratická funkce: f(x) = ax² + bx + c", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "quadratic.png")


# ── 3. Sinusová funkce (různé frekvence) ──────────────────────────────────────
def plot_sine():
    fig, ax = plt.subplots(figsize=(8, 5))
    for freq, color in [(1, "royalblue"), (2, "tomato"), (3, "seagreen")]:
        ax.plot(X, sine(X, frequency=freq), color=color, linewidth=2,
                label=f"sin({freq}x)")
    ax.set_title("Sinusová funkce: sin(nx)", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "sine.png")


# ── 4. Exponenciální funkce ───────────────────────────────────────────────────
def plot_exponential():
    x_exp = np.linspace(-5, 3, 1000)
    fig, ax = plt.subplots(figsize=(8, 5))
    plot_with_extremes(ax, x_exp, exponential(x_exp), color="royalblue", label="eˣ")
    ax.set_title("Exponenciální funkce: f(x) = eˣ", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_ylim(-1, 25)
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "exponential.png")


# ── 5. Logaritmická funkce ────────────────────────────────────────────────────
def plot_logarithm():
    fig, ax = plt.subplots(figsize=(8, 5))
    for base, color, lbl in [(np.e, "royalblue", "ln(x)"), (10, "tomato", "log₁₀(x)"), (2, "seagreen", "log₂(x)")]:
        ax.plot(X_POSITIVE, logarithm(X_POSITIVE, base), color=color, linewidth=2, label=lbl)
    ax.set_title("Logaritmická funkce", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "logarithm.png")


# ── 6. Kombinovaný graf ───────────────────────────────────────────────────────
def plot_multiple():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(X, sine(X), color="royalblue", linewidth=2, label="sin(x)")
    ax.plot(X, cosine(X), color="tomato", linewidth=2, label="cos(x)")
    ax.plot(X, linear(X, 0.3, 0), color="seagreen", linewidth=2, label="0.3x")
    ax.plot(X, quadratic(X, 0.05, 0, -1), color="darkorchid", linewidth=2, label="0.05x² - 1")
    ax.set_ylim(-4, 4)
    ax.axhline(0, color="black", linewidth=0.8, linestyle="--")
    ax.axvline(0, color="black", linewidth=0.8, linestyle="--")
    ax.set_title("Kombinovaný graf více funkcí", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    save_plot(fig, "multiple_functions.png")


# ── 7. Experimentování (sin s různými parametry) ──────────────────────────────
def plot_experiment():
    """Možnost B: různé parametry sinusoidy + vyznačení maxima/minima."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    configs = [
        {"amplitude": 1, "frequency": 1, "title": "sin(x), interval ⟨-10, 10⟩", "x": X},
        {"amplitude": 2, "frequency": 1, "title": "2·sin(x), interval ⟨-10, 10⟩", "x": X},
        {"amplitude": 1, "frequency": 3, "title": "sin(3x), interval ⟨-5, 5⟩",
         "x": np.linspace(-5, 5, 1000)},
    ]
    for ax, cfg in zip(axes, configs):
        x = cfg["x"]
        y = sine(x, amplitude=cfg["amplitude"], frequency=cfg["frequency"])
        plot_with_extremes(ax, x, y, color="royalblue", label=cfg["title"])
        ax.set_title(cfg["title"], fontsize=11)
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        ax.legend(fontsize=8)
        ax.grid(True, alpha=0.3)
    fig.suptitle("Experimentování: vliv parametrů na sinusoidu", fontsize=13, y=1.02)
    fig.tight_layout()
    save_plot(fig, "experiment.png")


# ── Výběr jedné funkce z příkazové řádky ──────────────────────────────────────
def plot_single(name):
    PLOT_MAP = {
        "linear": plot_linear,
        "quadratic": plot_quadratic,
        "sin": plot_sine,
        "cos": plot_sine,       # cos se vykreslí v kombinaci
        "exp": plot_exponential,
        "log": plot_logarithm,
    }
    if name not in PLOT_MAP:
        print(f"Neznámá funkce '{name}'. Dostupné: {', '.join(PLOT_MAP.keys())}")
        sys.exit(1)
    print(f"Kreslím funkci: {name}")
    PLOT_MAP[name]()


# ── Hlavní program ────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) > 1:
        plot_single(sys.argv[1])
    else:
        print("Kreslím všechny funkce...")
        plot_linear()
        plot_quadratic()
        plot_sine()
        plot_exponential()
        plot_logarithm()
        plot_multiple()
        plot_experiment()
        print("Hotovo! Grafy jsou uloženy ve složce images/")


if __name__ == "__main__":
    main()
