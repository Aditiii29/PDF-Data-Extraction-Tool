import yaml
from pathlib import Path

def load_config(config_path="config/settings.yaml"):
    # Project root = parent of src/
    project_root = Path(__file__).resolve().parent.parent
    path = project_root / config_path

    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with open(path, "r") as f:
        return yaml.safe_load(f)

