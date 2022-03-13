import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils
class IndorScenes:
    def __init__(self) -> None:
        utils.data_header("Indoor Scenes dataset")


if __name__ == '__main__':
    file = IndorScenes()