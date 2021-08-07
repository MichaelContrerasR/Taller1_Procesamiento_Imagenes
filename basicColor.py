import cv2
import numpy as np

""" Clase BasicColor para visualizar y manipular propiedades de la imagen 

"""


class BasicColor:
    def __init__(self, image):
        self.image = image

    # Obtener propiedades de la imagen (Tamaño y Canales)
    def displayproperties(self):
        # Obtener Propiedades de la imagen (altura, anchura, número de canales)
        height = self.image.shape[0]
        width = self.image.shape[1]
        channels = self.image.shape[2]
        # Calcular Tamaño de la imagen con las Propiedades
        tam = (height * width * channels) / 1000000
        print("La imagen tiene un tamaño de ", "{0:.1f}".format(tam), "MP y esta compuesta por ", channels, "Canales")

    # Segmentacion Otsu y Binarizacion de la imagen
    def makebw(self):
        image_gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Umbral global de Otsu
        ret, ibw_otsu = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        cv2.imshow("Imagen Binarizada", ibw_otsu)
        cv2.waitKey(5000)

    # Manipulacion de la imagen con valor variable de entrada en componente Hue de HSV
    def colorize(self):
        image_hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        H = int(input("Ingresa el valor h de Hue entre 0 y 179: "))
        h, s, v = cv2.split(image_hsv)
        h = H * np.ones_like(h)
        image_hue = cv2.merge((h, s, v))
        image_hue_bgr = cv2.cvtColor(image_hue, cv2.COLOR_HSV2BGR)
        cv2.imshow("Imagen convertida de hsv a bgr con variacion de h", image_hue_bgr)
        cv2.waitKey(0)
