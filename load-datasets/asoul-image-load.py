import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils


class LoadAsoulImage:
    def __init__(self) -> None:
        utils.data_header("Asoul Image Dataset")
        

if __name__ == '__main__':
    file = LoadAsoulImage()