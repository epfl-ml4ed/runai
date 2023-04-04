import wandb
import json
import sys


def write_hello(config):
    wandb.init(project=config["project"], name=config["run_name"])

    with open(config["file"], "w") as hello_file:
        hello_file.write("Hello World")

    wandb.save(config["file"])

    wandb.finish()


def restore(config, run_id):
    file = wandb.restore(
        config["file"],
        run_path=f"{config['profile']}/{config['project']}/{run_id}",
    )
    print(file.read())


def main():
    args = sys.argv[1:]
    run = args[0]
    config = json.load(open("config.json"))
    if run == "new":
        write_hello(config)
    else:
        restore(config, run)


if __name__ == "__main__":
    main()
