FROM continuumio/anaconda3

RUN apt update

ENV WANDB_ENTITY=YOURPROFILE 
ENV WANDB_API_KEY=YOURKEY

COPY . /

RUN chmod u+x entrypoint.sh

# Create the environment:
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
RUN echo "conda activate runai" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

ENTRYPOINT ["./entrypoint.sh"]