import wandb

project = "test"
name = "ncrxtvbj"

"""Use wandb to restore a file from a previous run"""
best_model = wandb.restore("hello.txt", run_path=f"jibrilfrej/{project}/{name}")

print(best_model.read())
