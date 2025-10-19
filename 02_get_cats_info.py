
input_path = "cats.txt"

def get_cats_info(path: str) -> list:     # Taking path as string  
    cat_lst = []                          # Creating empti list to store cats dicts
    cat_dict= {}                          # Empty dictionaory to store each cat info
    
    try:
        with open(path, "r", encoding='utf-8') as f:
            while True:
                line = f.readline()       # Read a line from file
                if not line:
                    break
                cat_info = line.split(sep=',')          # Getting list of strings from file about one cat - one string
                cat_dict = {"id": cat_info[0],          # Adding values from string to dictionary and converting age to int) 
                        "name": cat_info[1],
                        "age": int(cat_info[2].strip())}
                cat_lst.append(cat_dict)                # adding cats dictionary to list of cats dictionaries
    except FileNotFoundError:                           # Catching wrong file path input error
        print("File not found! Please provide  valid file path")
    return cat_lst
            

print(get_cats_info(input_path))

# c =  get_cats_info(input_path)
# age = 0
# for cat in c:
#     age += cat["age"]

# print(f"total age = {age} average age = {age / len(c)}")

    