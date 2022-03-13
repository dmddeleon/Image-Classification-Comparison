





COMMAND_ARGUMENTS = {
    '--download': 'download',
    '-D':'download',
    '--save': 'save',
    '-S':'save',
    
}

def download ( link, file_dir ):
    data_header("downloading...")

def unzipFiles( file_dir, unzip_dir):
    data_header("unzipping files...") 

def check_if_valid(args):
    for argument in args[1:]:
        if argument not in COMMAND_ARGUMENTS.keys():
            raise Exception(f'Invalid Arguments {argument}') 
        
def call_args( args):
    command_function = {i: False for i in set(COMMAND_ARGUMENTS.values())}
    for argument in args[1:]:
        command_function[COMMAND_ARGUMENTS[argument]] = True
    return command_function  
    

def data_header(title):
    print('==============================================================')
    print('\t',title)
    print('==============================================================')