import PIL
from PIL import Image
import PIL.Image

x = PIL.Image.open("C:/Users/namir/Downloads/7190623d_46d44e08b0e41b1513ea5a4de40d3c12190fa776.jpeg")

width, heigth = x.size
print(width, "x", heigth)