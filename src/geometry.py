def compute_scale_factor(pdf_page, image):
    """
    Computes scale factors between PDF coordinates and image pixels.
    """
    pdf_width = pdf_page.width
    pdf_height = pdf_page.height

    img_height, img_width, _ = image.shape

    scale_x = img_width / pdf_width
    scale_y = img_height / pdf_height

    return scale_x, scale_y
