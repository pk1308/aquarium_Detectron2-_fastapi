import cv2 as cv
from detectron2.config import get_cfg
from detectron2.data import MetadataCatalog
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer


class Detector:

    def __init__(self, filename):
        # set model and test set
        self.model = 'faster_rcnn_R_50_FPN_3x.yaml'
        self.filename = filename

        # obtain detectron2's default config
        self.cfg = get_cfg()

        # load values from a file
        self.cfg.merge_from_file("config.yml")

        # set device to cpu
        self.cfg.MODEL.DEVICE = "cpu"

        # get weights
        self.cfg.MODEL.WEIGHTS = "model_final.pth"

        # set the testing threshold for this model
        self.cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.50

    def inference(self, file):
        predictor = DefaultPredictor(self.cfg)
        im = cv.imread(file)
        outputs = predictor(im)
        metadata = MetadataCatalog.get(self.cfg.DATASETS.TRAIN)

        # visualise
        v = Visualizer(im[:, :, ::-1], metadata=metadata, scale=1.2)
        v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
        predicted_image = v.get_image()
        return predicted_image
