# Function Visualization

Projekt pro vizualizaci matematických funkcí pomocí knihoven **NumPy** a **Matplotlib**.

## Co program dělá

Program vykresluje různé matematické funkce, ukládá grafy jako obrázky do složky `images/` a umožňuje:

- Vykreslení každé funkce zvlášť s různými parametry
- Kombinovaný graf více funkcí najednou
- Vyznačení **maxima** a **minima** v grafu
- Spuštění pro konkrétní funkci přes argument příkazové řádky
- Experimentování s různými amplitudami, frekvencemi a intervaly

## Instalace závislostí

```bash
pip install numpy matplotlib
```

> Na Debian/Ubuntu systémech může být nutné přidat příznak:
> ```bash
> pip install numpy matplotlib --break-system-packages
> ```

## Jak spustit

### Vykreslení všech funkcí najednou:
```bash
python main.py
```

### Vykreslení konkrétní funkce (možnost A):
```bash
python main.py sin
python main.py cos
python main.py linear
python main.py quadratic
python main.py exp
python main.py log
```

## Jaké funkce program vykresluje

| Funkce | Vzorec | Soubor |
|---|---|---|
| Lineární | `f(x) = ax + b` | `images/linear.png` |
| Kvadratická | `f(x) = ax² + bx + c` | `images/quadratic.png` |
| Sinusová | `f(x) = A·sin(nx)` | `images/sine.png` |
| Exponenciální | `f(x) = eˣ` | `images/exponential.png` |
| Logaritmická | `f(x) = log(x)` | `images/logarithm.png` |
| Kombinovaný graf | sin, cos, lineární, kvadratická | `images/multiple_functions.png` |
| Experiment | sin s různými parametry | `images/experiment.png` |

## Struktura projektu

```
function-visualization/
│
├── main.py          # Hlavní program – kreslení a ukládání grafů
├── functions.py     # Definice matematických funkcí
├── README.md        # Tato dokumentace
└── images/          # Vygenerované obrázky grafů
```

## Experimentování

Byla zkoumána sinusová funkce se změnou parametrů:

| Varianta | Změna | Efekt |
|---|---|---|
| `sin(x)` na `⟨-10, 10⟩` | základní | 3 celé periody |
| `2·sin(x)` | dvojnásobná amplituda | dvojnásobný rozsah hodnot (⟨-2, 2⟩) |
| `sin(3x)` na `⟨-5, 5⟩` | trojnásobná frekvence + užší interval | více period na menším úseku |

Zvýšení frekvence způsobí více kmitů na stejném intervalu. Zvýšení amplitudy pouze roztáhne funkci ve směru osy y.
