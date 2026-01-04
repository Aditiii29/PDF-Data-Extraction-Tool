from pdf2image import convert_from_path
import numpy as np

def pdf_pages_to_images(pdf_path, dpi=300, poppler_path=None):
    pages = convert_from_path(
        pdf_path,
        dpi=dpi,
        poppler_path=poppler_path
    )

    images = []
    for page in pages:
        images.append(np.array(page))

    return images
