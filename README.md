# MFGSAE

This repository contains the proposed MFGSAE road network simplification method, organized as a cleaner GitHub-style Python project.

## Project Structure

```text
MFGSAE/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── run_bani_ours_preserve_closures.py
├── configs/
│   └── default.yaml
├── data/
│   └── .gitkeep
├── experiments/
│   └── run_all.py
└── mfgsae/
    ├── __init__.py
    ├── _core.py
    ├── _shared.py
    ├── model.py
    ├── features.py
    ├── simplification.py
    ├── metrics.py
    └── visualization.py
```

## Notes

- Core implementation logic is stored in `mfgsae/_core.py`.
- Shared preprocessing, metrics, and plotting utilities are stored in `mfgsae/_shared.py`.
- Public-facing package modules are separated into model, features, simplification, metrics, and visualization.
- This repository is focused on the proposed method only and does not include the ablation pipeline.

## Installation

```powershell
pip install -r requirements.txt
```

## Example Usage

### Run the main method on one dataset

```powershell
python .\main.py --dataset "PATH_TO_DATASET.osm" --output_dir ".\results" --target_ndr 0.145
```

### Run through the experiment entry point

```powershell
python .\experiments\run_all.py --dataset "PATH_TO_DATASET.osm" --output_dir ".\results" --target_ndr 0.145
```

### Run `bani` preserved-closure visualization

```powershell
python .\run_bani_ours_preserve_closures.py
```

## Public Release Scope

This repository does not include:

- baseline model code
- ablation experiment entry scripts
- local datasets
- local cached results
- machine-specific output files
