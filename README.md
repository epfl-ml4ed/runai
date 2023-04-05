# RunAI
How to use RunAI

Pricing can be found here: https://icitdocs.epfl.ch/display/clusterdocs/Pricing

## Basic example to get familiar with Docker and wanbd

Requirements for this minimal working example:
- wandb for tracking experiments: https://wandb.ai/ (you must be logged in)
- conda (https://conda.io/projects/conda/en/latest/user-guide/install/index.html)



Before running the minimal example with Docker and wandb: **change the config file** and the dockerfile ENV varaibles with your profile (this solution is not very secure yet, since you need to put your APIKEY in your dockerfile, I'll find sonmething better later)

Build the docker image with name wandb and tag 1.0:
```bash
docker build -t wandb:1.0 .
```

Note for WSL2 users: if you encounter issues when building the docker image such as HTTPS 000 errors, try restarting you computer (restarting wsl only did not work for me)

Run the image:
```bash
wandb docker-run --env RUN=new wandb:1.0
```
(it is ok if you get a warning "wandb: Couldn't detect image argument, running command without the WANDB_DOCKER env variable")

If everything went well:
- a wandb project named test has been created
- a run named docker has been created in the test project
- a file named hello.txt containing Hello World has been saved in your run  

If you want to restore an existing file from wandb, find the id of your run (here it is 5aj8t1jz) and do:
```bash
wandb docker-run --env RUN=5aj8t1jz wandb:1.0 
```

If everything went well, it should recover the file hello.txt from the run and print the content of the hello.txt file.


## Use RunAI

There is a great detailed tutorial that can be found here: https://github.com/bayazitdeniz/epic-guide.github.io/blob/main/_tools/compute_storage.md#runai

Here are some instructiuons for setting up RunAI: https://github.com/bayazitdeniz/epic-guide.github.io/blob/main/_tools/compute_storage.md#setting-up-runai-on-your-own-machine

For the following I am going to assume that you managed to 
- get access to runai
- install runai
- install kubectl
- install helm
- set up the kube config file

### Here is the short version:
Login to runai:

```bash
runai login
```
Login to the ic-registry

```bash
docker login ic-registry.epfl.ch
```

Tag your image to the ic-registry

```bash
docker tag wandb:1.0 ic-registry.epfl.ch/d-vet/wandb:1.0
```

Push your image to the ic-registry
```bash
docker push ic-registry.epfl.ch/d-vet/wandb:1.0
```

Run your image
```bash
runai submit --name test1 -i ic-registry.epfl.ch/d-vet/wandb:1.0 --cpu-limit 1 --gpu 0 -e RUN=new
```

Once again,If everything went well:
- a wandb project named test has been created
- a run named docker has been created in the test project
- a file named hello.txt containing Hello World has been saved in your run  