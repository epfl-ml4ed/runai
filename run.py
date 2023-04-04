import wandb
import json


def write_hello(config):
    wandb.init(project=config["project"], name=config["run_name"])

    with open(config["file"], "w") as hello_file:
        hello_file.write("Hello World")

    wandb.save(config["file"])

    wandb.finish()


def main():
    config = json.load(open("config.json"))
    write_hello(config)


if __name__ == "__main__":
    main()
