import yaml

def load_config():
    with open("config/companies.yaml", "r") as file:
        return yaml.safe_load(file)

if __name__ == "__main__":
    config = load_config()
    print(config)