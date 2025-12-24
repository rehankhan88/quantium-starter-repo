# Quantium Challenge
This repo contains everything you need to get started on the program! Good luck!

## References
- [Check the Quantium Challenge Yourself!](https://www.theforage.com/simulations/quantium/software-engineering-j6ci)
- [Docs for this project](/quantium-starter-repo/_docs)

## Skills to be learnt/tested
- Python
- Virtual environment
- Data management
- Dashboard tools
- Data analysis
- CSS
- Python testing
- Test automation
- Shell scripting

## Data processing script
Run it to generate a single cleaned CSV for Pink Morsels sales.

The script is idempotent and will create the `data/processed/` folder if missing.

## How to run the Dash app

1. Install dependencies (preferably in a virtual environment):

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

3. Open the app in your browser at `http://127.0.0.1:8050`.

The app reads the single processed source of truth at `data/processed/pink_morsels_sales.csv`.

---

## Task status

- **Tasks 1–4 completed:** data processing, aggregation, Dash visualiser and Task 4 UI/CSS improvements are implemented.
- **Dashboard entrypoint:** `app.py` (run with `python app.py`).
- **Data source:** `data/processed/pink_morsels_sales.csv` (single source of truth).

```bash
git add README.md pink_morsels/ assets/ app.py
git commit -m "task4: add region filter and styling; scaffold pink_morsels package"
git push origin main
```