FROM bentoml/model-server:0.11.0-py312

RUN pip install rdkit==2025.3.2

WORKDIR /repo
COPY . /repo
