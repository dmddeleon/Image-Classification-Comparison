import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils
class IntelImage:
    def __init__(self) -> None:
        utils.data_header("Intel image dataset")
    
if __name__ == '__main__':
    file = IntelImage()