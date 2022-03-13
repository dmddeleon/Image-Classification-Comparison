import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils
class CellularImage:
    def __init__(self) -> None:
        utils.data_header("Cellular Image Datasetr")


if __name__ == '__main__':
    file = CellularImage()