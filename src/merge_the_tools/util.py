import logging
logging.basicConfig(level=logging.DEBUG, format="%(message)s" )
def merge_tools():
    string_input = input("Enter the string value: ")
    k = int(input("Enter the factor value: "))

    n= len(string_input)
    res=""
    for i in range(0,n,k):
        sub_string = string_input[i:i+k]
        unique_list=[]
        for j in sub_string:
            if j not in unique_list:
                unique_list.append(j)
                res+=j
        res+="\n"
        result=(''.join(unique_list))
        logging.debug(f"The output is {result}")
    return res