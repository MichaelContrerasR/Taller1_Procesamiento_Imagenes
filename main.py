from basicColor import BasicColor
import cv2
import os

""" Manejo de imagen y creacion de Clase. Taller 1 

    main.py <path_to_image> <image_name>
"""

# Pulsar el botón verde en la barra superior para ejecutar el script.
if __name__ == '__main__':
    path = input("ingresa el path de tu imagen: ")
    image_name = input("ingresa el nombre de tu imagen seguido de .formato ejemplo (.png, .jpg, etc): ")
    path_file = os.path.join(path, image_name)
    image = cv2.imread(path_file)

    # Comprobar que la imagen es válida
    assert image is not None, "There is no image at {}".format(path_file)
    # Llamado de la función
    Color = BasicColor(image)
    # Extraer ropiedades de la imagen (Tamaño y Canales)
    Color.displayproperties()
    # Segmentacion Otsu y Binarizacion de la imagen
    Color.makebw()
    # Manipulacion de la imagen con valor variable de entrada en componente Hue de HSV
    Color.colorize()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
