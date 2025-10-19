import sys
import pathlib
import colorama
import os



def view_dir_struct() :
    if len(sys.argv) == 2:
        print(sys.argv[1])
        path = sys.argv[1]
    
    current_path = os.getcwd()
    print(pathlib.Path(current_path))
    print(colorama.Fore.CYAN + colorama.Style.BRIGHT + os.path.basename(current_path) + "/")
    print(os.listdir(current_path))

    


if __name__ == '__main__':
    view_dir_struct()




