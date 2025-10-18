import re

path_input = "salary_example.txt" # Input path

def total_salary(path: str) -> tuple:
    with open(path, "r") as file:                           # open file to read
        salary_dict = {}                                  # creating empty dictionary
        while True:
            line = file.readline()                      # Read a line from file
            print(line)
            line_data = line.split(sep = ",", maxsplit = 1)     # transform line into list with name and salary
            print(line_data)                                                 # Add to dictionary - name as key and sallary as value.  
            #salary_dict[line_data[0]] = line_data[1]
    
    #print(salary_dict)
    return 1


total_salary(path_input)


