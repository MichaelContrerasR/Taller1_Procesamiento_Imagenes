import cv2
import numpy as np
import sys
import os


class basicColor:

    def __init__(self, image):
        self.image = image
        # self.image_name = image_name
        # = os.path.join(path, image_name)
        # Read the image

    def displayProperties(self):
        # get dimensions of image
        dimensions = self.image.shape

        # height, width, number of channels in image
        height = self.image.shape[0]
        width = self.image.shape[1]
        channels = self.image.shape[2]
        tam = (height * width * channels) / 1000000
        # print("La imagen tiene un tamaño de ", "{0:.1f}".format(tam), "MP")
        # print("La imagen se compone por ", channels, "Canales")
        return print("La imagen tiene un tamaño de ", "{0:.1f}".format(tam), "MP y se compone por ", channels,
                     "Canales")

    def makeBW(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        # Otsu's global threshold
        ret, Ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Image Binarizada", Ibw_otsu)
        cv2.waitKey(0)
        return Ibw_otsu

    def colorize(self):
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        H = int(input("ingresa el valor de Hue: "))
        h, s, v = cv2.split(image_hsv)
        h = H * np.ones_like(h)
        # v = 255 * np.ones_like(v)
        image_hue = cv2.merge((h, s, v))
        image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
        cv2.imshow("Image hsv a bgr", image_hue_bgr)
        cv2.waitKey(0)
        return image_hue_bgr

    def __str__(self):
        return "()"