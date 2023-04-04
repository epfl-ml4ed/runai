# runai
How to use Runai

## Basic example to get familiar with Docker and wanbd

Requirements for this minimal working example:
- wandb for tracking experiments: https://wandb.ai/ (you must be logged in)

Run minimal example with Docker and wandb:

Build the docker image with name wandb and tag 1.0:
```bash
docker build -t wandb:1.0
```

Note for WSL2 users: if you encounter issues when building the docker image such as HTTPS 000 errors, try restarting you computer (restarting wsl only did not work for me)

Run the image (it is ok if you get a warning "wandb: Couldn't detect image argument, running command without the WANDB_DOCKER env variable"):
```bash
wandb docker-run wandb:1.0
```

If everything went well:
- a wandb project named test has been created
- a run named docker has been created in the test project
- a file named hello.txt containing Hello World has been saved in your run  



[run.py](run.py) creates file hello.txt and writes "Hello World" in it. The file is then saved on Wandb.

[restore.py](restore.py) downloads file hello.txt from Wandb and prints the content

[Detailed Guide](https://github.com/bayazitdeniz/epic-guide.github.io/blob/main/_tools/compute_storage.md)

[Pricing](https://icitdocs.epfl.ch/display/clusterdocs/Pricing)

