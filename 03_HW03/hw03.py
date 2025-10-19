import sys
from pathlib import Path
from colorama import init, Fore, Style, Back



def view_dir_struct() :
    if len(sys.argv) == 2:
        print(sys.argv[1])
        path = Path(sys.argv[1])
    else:
        path = Path(".")
    init(autoreset=True)
    print(Fore.BLUE + Style.BRIGHT + Path.cwd().name + "/")
    for entry in path.iterdir():
        if entry.is_dir():
            print(Fore.YELLOW + Style.BRIGHT + "    " + entry.name + '/')
        else:
            print(Fore.LIGHTGREEN_EX + Style.NORMAL + "    " + entry.name)

if __name__ == '__main__':
    view_dir_struct()




