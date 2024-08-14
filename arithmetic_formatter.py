import re

def arithmetic_arranger(problems, show_answers=False):
    first = ""
    second = ""
    lines = ""
    result = ""
    string = ""
    if len(problems) > 5:
        raise ValueError("Error: Too many problems.")
    
    for problem in problems:
        if re.search("[^\s0-9.+-]", problem):
            if re.search("[/]", problem) or re.search("[*]", problem):
                raise ValueError("Error: Operator must be '+' or '-'.")
            raise ValueError("Error: Numbers must only contain digits.")
        
    first_number = problem.split(" ")[0]
    operator = problem.split(" ")[1]
    second_number = problem.split(" ")[2]

    if len(first_number) >= 5 or len(second_number) >= 5:
        raise ValueError("Error: Numbers cannot be more than four digits.")
    result = ""
    if operator == "+":
        result = str(int(first_number) + int(second_number))
    else:
        result = str(int(first_number) - int(second_number))
    
     



    return problems

print(f"\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "1234 + 49"])}")