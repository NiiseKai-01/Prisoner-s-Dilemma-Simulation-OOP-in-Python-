<div align="center">

![logo](https://img.shields.io/badge/Project-OOP_Simulation-ff715b?style=for-the-badge&labelColor=232626&color=ff715b)

# Prisoner's Dilemma Simulation

**An object-oriented simulation of the classic Prisoner's Dilemma game theory problem**

> A Python simulation exploring how different game-theoretic strategies perform against each other in repeated rounds of the Prisoner's Dilemma. Built with OOP principles — choose your strategies, name your players, and see who comes out on top.

<br/>

[![Python](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=3776AB&labelColor=0d0d0d)](https://www.python.org/)
[![OOP](https://img.shields.io/badge/Paradigm-Object_Oriented-23C48E?style=for-the-badge&labelColor=0d0d0d)]()

<br/>

<a href="#overview"><kbd> <br> Overview <br> </kbd></a>&ensp;
<a href="#payoff"><kbd> <br> Payoff Matrix <br> </kbd></a>&ensp;
<a href="#strategies"><kbd> <br> Strategies <br> </kbd></a>&ensp;
<a href="#structure"><kbd> <br> Structure <br> </kbd></a>&ensp;
<a href="#usage"><kbd> <br> Usage <br> </kbd></a>&ensp;
<a href="#example"><kbd> <br> Example Run <br> </kbd></a>

</div>

<br/>

---

<h2 id="overview">// OVERVIEW</h2>

&ensp;› A **Python-based simulation** of the Prisoner's Dilemma, a classic problem in game theory

&ensp;› Players choose to **Cooperate (1)** or **Defect (0)** against each other over multiple rounds

&ensp;› Each player is driven by a **strategy class**, all inheriting from a common `player` base class

&ensp;› Designed as an **interactive CLI game** — pick strategies, name your players, and run rounds

&ensp;› Demonstrates core **OOP concepts**: inheritance, polymorphism, encapsulation, and abstraction

---

<h2 id="payoff">// PAYOFF MATRIX</h2>

<br/>

<div align="center">

| Player A \ Player B | **Cooperate (1)** | **Defect (0)** |
|:---:|:---:|:---:|
| **Cooperate (1)** | `3, 3` | `0, 5` |
| **Defect (0)** | `5, 0` | `1, 1` |

</div>

<br/>

&ensp;› **Mutual Cooperation** → Both earn 3 (best collective outcome)

&ensp;› **Mutual Defection** → Both earn only 1 (Nash Equilibrium)

&ensp;› **One Defects, One Cooperates** → Defector earns 5, cooperator earns 0 (temptation payoff)

---

<h2 id="strategies">// STRATEGIES</h2>

<br/>

<div align="center">

| Index | Strategy | Description |
|:---:|:---|:---|
| `1` | **Always Cooperate** | Always plays Cooperate (1), no matter what |
| `2` | **Always Defect** | Always plays Defect (0), no matter what |
| `3` | **Tit-for-Tat** | Cooperates first, then mirrors opponent's last move |
| `4` | **Grim Trigger** | Cooperates until opponent defects once — then defects forever |
| `5` | **Random Strategy** | Randomly assigns one of the above strategies |
| `6` | **Random** | Randomly picks Cooperate or Defect each round |
| `7` | **Quit** | Ends the game |

</div>

---

<h2 id="structure">// PROJECT STRUCTURE</h2>

```
Prisoner-s-Dilemma-Simulation-OOP-in-Python/
│
├── player_classes
│   ├── always_cooperate   # Strategy subclass
│   ├── always_defect      # Strategy subclass
│   ├── titfortat          # Strategy subclass
│   ├── Grim_trigger       # Strategy subclass
│   └── Random             # Strategy subclass
│
├── simulation.py          # Main simulation file
│
└── README.md
```

**Key components:**

```
  ├── player          → Abstract base class with shared state (rewards, move history)
  ├── payoff()        → Resolves a round between two players and updates scores
  ├── payoff_matrix   → Dictionary mapping action pairs to reward tuples
  ├── switch          → Maps user input integers to strategy classes
  └── random_choice() → Helper to assign a random strategy at runtime
```

---

<h2 id="usage">// HOW TO RUN</h2>

**1. Make sure Python is installed**

```bash
python --version   # Python 3.x recommended
```

**2. Run the simulation**

```bash
python simulation.py
```

**3. Follow the prompts:**

```
Select Strategy for Player 1: [1-7]
Enter name for Player 1: Alice
Select Strategy for Player 2: [1-7]
Enter name for Player 2: Bob
Enter no of rounds to play: 10
```

**4. After each match:**

```
Enter 1 to continue and 0 to end and print all players till now
```

---

<h2 id="example">// EXAMPLE RUN</h2>

```
Player 1 action = 1 and reward = 3, Player 2 action = 1 and reward = 3 ==> Winner = None
Player 1 action = 1 and reward = 0, Player 2 action = 0 and reward = 5 ==> Winner = Bob
Player 1 action = 0 and reward = 1, Player 2 action = 0 and reward = 1 ==> Winner = None
...
Total rewards of Alice = 14, OP moves = [1, 0, 0, 1, 1, 0, 0, 1, 1, 0]
Total rewards of Bob   = 18, OP moves = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
The winner is Bob
```

---

<h2 id="concepts">// OOP CONCEPTS DEMONSTRATED</h2>

&ensp;› **Abstraction** — `player.act()` is an abstract method; each subclass defines its own behavior

&ensp;› **Inheritance** — All strategy classes inherit attributes like `rewards` and `opponent_last_moves` from `player`

&ensp;› **Polymorphism** — `payoff()` calls `a.act()` and `b.act()` without knowing the underlying strategy

&ensp;› **Encapsulation** — Player state (rewards, move history, trigger flags) is managed within each object

---

<div align="center">

![footer](https://img.shields.io/badge/OOP_Project-Prisoner's_Dilemma_Simulation-3776AB?style=flat-square&labelColor=0d0d0d)

</div>
