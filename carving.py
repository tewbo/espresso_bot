import numpy as np
from PIL import Image
import seam_carving

MAX_SIZE = 2000


def make_carving(picture_name: str):
    src = np.array(Image.open(f"images/{picture_name}"))
    src_h, src_w = src.shape[0], src.shape[1]
    if src_h > MAX_SIZE or src_w > MAX_SIZE:
        raise ValueError(f"Error: Both of picture dimensions must be less then {MAX_SIZE}px")
    dst = seam_carving.resize(
        src,  # source image (rgb or gray)
        size=(src_w / 2, src_h / 2),  # target size
        energy_mode="backward",  # choose from {backward, forward}
        order="width-first",  # choose from {width-first, height-first}
        keep_mask=None,  # object mask to protect from removal
    )
    Image.fromarray(dst).save(f"result/{picture_name}")
