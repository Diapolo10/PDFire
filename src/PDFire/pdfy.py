"""Code for handling PDF conversion."""

import uuid
from pathlib import Path

from PIL import Image

from PDFire.config import EXPORTS_DIR, IMAGE_CONVERSION_MODE


def pdf(directory: Path) -> Path:
    """
    Goes through the directory of uploads, and fuses the uploaded media into one PDF file.

    Returns the path to the PDF file.
    """
    images: list[Image.Image] = []
    for file in directory.iterdir():
        with Image.open(file) as image:
            images.append(image.convert(IMAGE_CONVERSION_MODE))

    export_pdf = EXPORTS_DIR / f'{uuid.uuid4()}.pdf'
    images[0].save(export_pdf, save_all=True, append_images=images[1:])
    return export_pdf
