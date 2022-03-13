import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils
class MedicalImage:
    def __init__(self) -> None:
        utils.data_header("Medical Image dataset")
    
if __name__ == '__main__':
    file = MedicalImage()