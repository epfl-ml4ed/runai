FROM continuumio/anaconda3

RUN apt update

COPY . /

# Create the environment:
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "runai", "/bin/bash", "-c"]

# Demonstrate the environment is activated:
RUN echo "Make sure wandb is installed:"
RUN python -c "import wandb"

ENTRYPOINT ["conda", "run", "-n", "runai", "python", "run.py"]