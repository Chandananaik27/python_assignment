import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def mutate_string():
    string = input("Enter the string: ")
    position, character = input("enter the position and character: ").split()
    string_input = string[:position] + character + string[position + 1:]
    logging.debug(string_input)
    return string_input