import sys
from pathlib import Path
from colorama import init, Fore, Style, Back



def view_dir_struct() :  
    if len(sys.argv) == 2:                 # Check for comand line arguments
        #print(sys.argv[1])
        path = Path(sys.argv[1])           # Using command line arguments as path
    else:
        path = Path(".")                   # If no arguments submitted, than using current path
    init(autoreset=True)                   # Reset colors after each print
    print(Fore.BLUE + Style.BRIGHT + Path.cwd().name + "/")      # Current dir name in BLUE
    for entry in path.iterdir():                                 # Iteratiing over Path object - files and dirs   
        if entry.is_dir():                                       # Check if pbject is Directory
            print(Fore.YELLOW + Style.BRIGHT + "    " + entry.name + '/') # Formating Directory print     
        else:                                                    # If not Directory - than its file
            print(Fore.LIGHTGREEN_EX + Style.NORMAL + "     " + entry.name) # Formating as file

if __name__ == '__main__':
    view_dir_struct()




