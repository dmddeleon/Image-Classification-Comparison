import sys, os
from turtle import down 
sys.path.append(os.path.abspath(os.path.join('.','')))
import utils
class Sum397:
    
    def __init__(self, *args, **kwargs) -> None:
            
        self.download_link = ''
        self.download_dir = ''
        
        self.downloaded_zip_dir = ''
        self.downloaded_unzip_dir = ''
        
        self.__created__(*args, **kwargs)
        
        
    def __created__(self,*args, **kwargs):
        utils.data_header("Sum 397 dataset")
        utils.check_if_valid(*args)
        
        commands = utils.call_args(*args)
        if( commands['download'] == True):
            utils.download(self.download_link, self.download_dir )
            utils.data_header('Done downloading')
            
            
        if( commands['save'] == True):
            utils.unzipFiles( self.downloaded_zip_dir,self.downloaded_unzip_dir )
            utils.data_header('Done unzipping')   
if __name__ == '__main__':
    file = Sum397(sys.argv)