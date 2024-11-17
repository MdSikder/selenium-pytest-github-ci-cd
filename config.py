import yaml
import os


class Config:
    # Set the default environment (can be overridden)
    ENV = os.getenv('ENV', 'test')  # Default to 'test' if not specified

    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)

    # Dynamically select the environment
    BASE_URL = config[ENV]["base_url"]
    USERNAME = config[ENV]["username"]
    PASSWORD = config[ENV]["password"]
