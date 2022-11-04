FROM python:3.8

RUN mkdir /aquarium

COPY . /aquarium
WORKDIR /aquarium

ENV PORT 8000
ENV HOST "0.0.0.0"
RUN apt-get install git
RUN pip install -r requirements.txt
RUN pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install 'git+https://github.com/facebookresearch/detectron2.git'
RUN python  utils.py
EXPOSE $PORT
CMD ["uvicorn", "main:app"]