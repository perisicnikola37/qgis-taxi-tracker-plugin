import json


def load_config(config_file="config.json"):
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        return config
    except Exception as e:
        raise Exception(f"Error during configuration initialization: {str(e)}")


config = load_config()

LAYER_NAME = config.get("LAYER_NAME", "Istorija_ruta")
