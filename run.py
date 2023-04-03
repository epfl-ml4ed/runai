import wandb

project = "test"
name = "hello world"

wandb.init(project=project, name=name)

with open("hello.txt", "w") as hello_file:
    hello_file.write("Hello World")

wandb.save("hello.txt")

wandb.finish()
