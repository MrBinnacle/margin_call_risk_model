# 🧱 Margin Call Simulator – System Architecture

```mermaid
graph TD

  subgraph CLI Layer
    CLI[cli.py]
  end

  subgraph App Core
    Main[app.py]
    Config[config.py]
    Var[var_engine.py]
    Liquidation[liquidation.py]
    Replay[replay_utils.py]
    Lore[lore_utils.py]
    Scenario[scenario_presets.py]
  end

  subgraph Data
    CSV[(demo_price_data.csv)]
  end

  subgraph Tests
    test_var[test_var_engine.py]
    test_liq[test_liquidation.py]
    test_scen[test_scenario_replay.py]
  end

  subgraph Package
    MarginCallSim[margin_call_sim (Python Package)]
  end

  CLI --> MarginCallSim
  MarginCallSim --> Main
  MarginCallSim --> Config
  MarginCallSim --> Var
  MarginCallSim --> Liquidation
  MarginCallSim --> Replay
  MarginCallSim --> Lore
  MarginCallSim --> Scenario

  CLI --> CSV
  Tests --> Var
  Tests --> Liquidation
  Tests --> Replay

  test_var --> Var
  test_liq --> Liquidation
  test_scen --> Replay
```

## Folder Structure

```text
margin_call_sim/
├── margin_call_sim/
│   ├── __init__.py
│   ├── app.py
│   ├── cli.py
│   ├── config.py
│   ├── var_engine.py
│   ├── liquidation.py
│   ├── replay_utils.py
│   ├── lore_utils.py
│   ├── scenario_presets.py
├── tests/
│   ├── test_var_engine.py
│   ├── test_liquidation.py
│   ├── test_scenario_replay.py
├── demo_price_data.csv
├── setup.py
├── requirements.txt
├── README.md
```

This diagram highlights the key components of the Margin Call Simulator package and how tests connect to core modules. Use it as a reference when adding new modules or features.

