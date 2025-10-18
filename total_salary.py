path_input = "salary_example.txt"                                                    # Input path test

def total_salary(path: str) -> tuple:
    with open(path, "r") as file:                                                     # Open file to read
        salary_dict = {}                                                              # Creating empty dictionary
        while True:
            line = file.readline()                                                    # Read a line from file
            if not line:
                break
            
            line_data = line.split(sep = ",", maxsplit = 1)                           # Transform line into list with name and salary
            salary_dict[line_data[0]] = line_data[1]                                  # Add to dictionary - name as key and sallary as value.  
    
    salary_dict = {name: int(salary.strip()) for name, salary in salary_dict.items()} # Striping salary from '\n' AND converting to int
                                         
    total_salary = sum(salary_dict.values())                                          # Total sum of salary
    avg_salary = total_salary / len(salary_dict)                                      # Average sallary 
    return (total_salary, avg_salary)                                                 # return as tuple: (total sum, avg)


print(total_salary(path_input))


