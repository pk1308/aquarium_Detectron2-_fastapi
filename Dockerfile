FROM tiangolo/uvicorn-gunicorn:python3.9-slim

LABEL maintainer="team-erc"

ENV WORKERS_PER_CORE=4 
ENV MAX_WORKERS=24
ENV LOG_LEVEL="warning"
ENV TIMEOUT="200"

RUN mkdir /app

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cpu
RUN pip install 'git+https://github.com/facebookresearch/detectron2.git'

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]