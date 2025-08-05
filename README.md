
# Reinforcement Learning Agent – GridWorld + Q-learning

Tento projekt ukazuje jednoduchého agenta v prostředí `GridWorld`, který se pomocí Q-learningu učí nacházet cestu k cíli. Cílová pozice se v každé epizodě mění, což nutí agenta generalizovat naučené chování.

## 🔧 Použité soubory

- `environment.py` – vlastní RL prostředí (mřížka s dynamickým cílem)
- `agent.py` – tabulkový Q-learning agent
- `train.py` – hlavní skript pro trénink, test a vizualizaci výsledků

## 🧠 Co agent umí

- Najít nejkratší cestu z výchozí pozice `(0, 0)` do náhodného cíle
- Přizpůsobit se měnícím podmínkám
- Učit se z odměny a penalizace
- Vizualizovat „jistotu“ rozhodnutí pomocí heatmapy Q-hodnot

## ▶️ Spuštění

1. Aktivuj virtuální prostředí (pokud máš):

```
source .venv/bin/activate        # macOS/Linux
.\.venv\Scripts ctivate         # Windows
```

2. Nainstaluj závislosti:

```
pip install -r requirements.txt
```

3. Spusť skript:

```
python train.py
```

## 📊 Výstupy

- **Heatmapa Q-hodnot** – ukazuje, kde má agent vysokou důvěru v rozhodnutí
- **Test po tréninku** – ukazuje, jak agent reaguje bez náhodnosti
- **Výpis nejlepší trajektorie** – nejkratší cesta k libovolnému cíli
- **Výpis nejlepších odměn** – pro každou cílovou pozici

## ✅ Příklad výstupu

```
Epizoda 500: odměna = 0.93

Agent dosáhl cíle za 8 kroků!

Nejkratší nalezená trajektorie (1 kroků):
  1. (0, 0)
  2. (1, 0)

Nejlepší dosažené odměny podle cílových pozic:
  Cíl (0, 1): odměna = 1
  Cíl (4, 4): odměna = 0.88
  ...
```

## 📁 Doporučená struktura repozitáře

```
reinforcement_agent/
├── agent.py
├── environment.py
├── train.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🎓 Poznámka

Projekt je ideální pro výuku principů:
- Reinforcement Learningu
- Q-learningu
- generalizace v dynamickém prostředí
