import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s")

def mutate_string(string, position, character):
    string_input = string[:position] + character + string[position + 1:]
    logging.debug(string_input)
    return string_input
