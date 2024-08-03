#Case Conversion Function
def snake_case_char_converter(pascal_or_camel_cased_char):
    #Conversion using for and if/else loop
    '''
    snake_case_char_list = []
    for char in pascal_or_camel_cased_char:
        if char.isupper():
            converted_character = '_' + char.lower()
            snake_case_char_list.append(converted_character)
        else:
            snake_case_char_list.append(char)
        snake_case_string = ''.join(snake_case_char_list)
        clean_snake_case_string = snake_case_string.strip('_')
        return clean_snake_case_string
    '''
    #Conversion using list comphrension
    snake_case_char_list = [
        '_' + char.lower() if char.isupper() else char for char in pascal_or_camel_cased_char
    ]
    return "".join(snake_case_char_list).strip('_')
#Main program
def main():
    #Takes user input
    text = input("Enter Pascal or Camel case string: ")
    #Prints the output in Snake case
    print(snake_case_char_converter(text))

main()