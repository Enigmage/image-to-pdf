import os
from app import app
from PIL import Image

def image_to_pdf_normal(filenames: list, pdfname):

    img_list = []
    first_image = Image.open(os.path.join(app.config['UPLOAD_PATH'], filenames[0]))
    first_image_RGB = first_image.convert('RGB')

    for f in range(1, len(filenames)):
        image_x = Image.open(os.path.join(app.config['UPLOAD_PATH'], filenames[f]))
        image_x_rgb = image_x.convert('RGB')
        img_list.append(image_x_rgb)

    first_image_RGB.save(os.path.join(app.config['DOWNLOAD_PATH'], f"{pdfname}.pdf"), resolution=100.0, save_all=True, append_images=img_list)

def remove_files(filenames):
    for f in filenames:
        path = os.path.join(app.config['UPLOAD_PATH'], f)
        if os.path.exists(path):
            os.remove(path)

def image_to_pdf_scanned():
    pass
