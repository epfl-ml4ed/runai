import wandb
import json


def main():
    config = json.load(open("config.json"))
    file = wandb.restore(
        config["file"],
        run_path=f"{config['profile']}/{config['project']}/{config['name']}",
    )
    print(file.read())


if __name__ == "__main__":
    main()
