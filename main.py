from PIL import Image
from fastapi import FastAPI, File 
import os
from starlette.responses import Response
import io
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from ObjectDetector import Detector
from utils.utils import decodeImage , get_model_folder_gdrive

get_model_folder_gdrive()

detector = Detector(filename="file.jpg")

MESSAGE = "fish, jellyfish, penguins, sharks, puffins, stingrays, and starfish"


class ClientApp:
    def __init__(self):
        self.filename = "file.jpg"
        self.objectDetection = Detector(self.filename)


def run_inference(img_path="file.jpg"):
    # run inference using detectron2
    result_img = detector.inference(img_path)

    # clean up
    try:
        os.remove(img_path)
    except:
        pass

    return result_img


app = FastAPI(
    title="Custom Detectron2 API",
    description=""" objects trained = fish, jellyfish, penguins, sharks, puffins, stingrays, and starfish
                Obtain object value out of image
                    and return image and json result""",
    version="0.0.1",
)

origins = ["http://localhost", "http://localhost:8000", "*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return {"Classes trained": "fish, jellyfish, penguins, sharks, puffins, stingrays, and starfish"}


@app.get("/notify/v1/health")
def get_health():
    """
    Usage on K8S
    readinessProbe:
        httpGet:
            path: /notify/v1/health
            port: 80
    livenessProbe:
        httpGet:
            path: /notify/v1/health
            port: 80
    :return:
        dict(msg='OK')
    """
    return dict(msg="OK")

@app.post("/object-to-img")
async def detect_food_return_base64_img(file: bytes = File(...)):
    clApp = ClientApp()
    decodeImage(file, clApp.filename)
    result = clApp.objectDetection.inference("file.jpg")
    bytes_io = io.BytesIO()
    img_base64 = Image.fromarray(result)
    img_base64.save(bytes_io, format="JPEG")
    return Response(content=bytes_io.getvalue(), media_type="image/jpeg")
