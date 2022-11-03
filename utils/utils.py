from PIL import Image
import io
import os
import gdown


def decodeImage(imgstring, fileName):
    input_image = Image.open(io.BytesIO(imgstring)).convert("RGB") 
    input_image.save(fileName)


def get_model_folder_gdrive( folder_path : str  = "model_config"  , folder_id : str = "1uALvT4VbCfRxNzBo_Z_d8evnKtNo0NO4" ):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
        print("Creating folder : {}".format(folder_path))
        gdown.download_folder(id= folder_id, output= folder_path , quiet=True )
    else:
        print("Folder {} already exists".format(folder_path))
