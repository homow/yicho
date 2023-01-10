import cv2
import numpy as np
# import matplotlib.pyplot as plt
import os

wm_img = cv2.imread(
    r"C:\Users\Administrator\Pictures\SMMS\homow-high-resolution-logo-color-on-transparent-background.png", cv2.IMREAD_UNCHANGED)
name = "f7e07509.jpg"


def add_alpha_channel(img):
    b_channel, g_channel, r_channel = cv2.split(img)
    alpha_channel = np.ones(
        b_channel.shape, dtype=b_channel.dtype) * 255
    img_new = cv2.merge(
        (b_channel, g_channel, r_channel, alpha_channel))
    return img_new


def add_water_mark(pic_name):
    orig_img = cv2.imread(pic_name, cv2.IMREAD_UNCHANGED)

    print(orig_img.shape)
    print(wm_img.shape)
    scal = orig_img.shape[1]/10/wm_img.shape[1]
    half = cv2.resize(wm_img, (0, 0), fx=scal, fy=scal)

    if orig_img.shape[2] == 3:
        orig_img = add_alpha_channel(orig_img)

    shapexx = int(half.shape[1]*0.1)
    # x1 = orig_img.shape[1] - int(half.shape[1]*1.1)
    # y1 = orig_img.shape[0] - int(half.shape[0]*1.1)
    x2 = orig_img.shape[1] - shapexx
    y2 = orig_img.shape[0] - shapexx
    x1 = x2 - half.shape[1]
    y1 = y2 - half.shape[0]

    alpha_png = half[:, :, 3] / 255.0
    alpha_jpg = 1 - alpha_png
    for c in range(0, 3):
        orig_img[y1:y2, x1:x2, c] = (
            (alpha_jpg*orig_img[y1:y2, x1:x2, c]) + (alpha_png*half[:, :, c]))

    base_name = os.path.splitext(pic_name)[0]
    cv2.imwrite(base_name + '-wm.jpg', orig_img)
