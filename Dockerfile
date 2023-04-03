FROM continuumio/anaconda3

COPY . /

RUN conda env create -f environment.yml

RUN echo "source activate myenv" > ~/.bashrc