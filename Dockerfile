FROM nvidia/cuda:11.2.0-base-ubuntu20.04

RUN apt-get update && \
    apt-get install --yes git python3-pip

RUN mkdir /aquarium

COPY . /aquarium
WORKDIR /aquarium
RUN pip install -r requirements.txt
RUN pip install torch==1.12.1 torchvision==0.13.1 torchaudio==0.12.1 
RUN pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN python3 utils.py

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]