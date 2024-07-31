#python L2_Challenge3_Task3.py
# Code Wars: Numbers to objects


###SIMPLIFY###
def num_obj(s):
    list_of_dict = []
    dict = {}
    numbers = [str(i) for i in s]
    char_code = []
    for num in s:
        for digit in [num]:
            char_code += chr(num)
    list_of_tuples = list(zip(numbers,char_code))
    list_of_dicts = []
    for tuple in list_of_tuples:
        list_of_dicts.append({tuple[0]: tuple[1]})
    return (list_of_dicts)

print(num_obj([118,117,120]))
