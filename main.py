from basicColor import basicColor
import cv2
import os
# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
   # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    path = input("ingresa el path de tu imagen: ")
    image_name = input("ingresa el nombre de tu imagen seguido de . y formato: ")
    path_file = os.path.join(path, image_name)
    imag = cv2.imread(path_file)

    # Check the image is valid
    assert imag is not None, "There is no image at {}".format(path_file)
    Color = basicColor()
    Color.displayProperties(imag)
    print(Color.displayProperties())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
