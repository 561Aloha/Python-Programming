# Write a function parse_functions that, extracts information about functions in a Python file.
#Implement a main function to test `line_number` on problem 1 Python source file. Display the returned tuple from `parse_functions`."""
def line_number(file_path):
    count = 0
    new_file = open("new.txt","a")
    for line in file_path:
        new_line = f"{count}: {line}"
        new_file.write(new_line)
        count += 1
    new_file.close()

def parse_functions(line_str):
    #symbol_str=""
    #quantity_str=""
    field_list = line_str.strip().split(',')
    name_str= field_list[1] + ""+ field_list[0]
    grade=[]
    for element in field_list[2:]:
        grade.append(int(element))
    return name_str, grade
    """for ch in line:
        if ch.isalpha():
            symbol_str= symbol_str + ch
        else:
            quantity_str = quantity_str + ch    
    if quantity_str == "":
        quantity_str= "1"
    return symbol_str, quantity_str
"""
def main():
    file_name = input('Open what file: ')
    file_path = open(file_name, "r")
    
    print('{:>2s}{:>15s}'.format('Number', 'Name'))
    print('-' * 30)

    for line_str in file_path:
        parts = line_str.split(":")
        if len(parts) == 2:
            number = parts[0].strip()
            name = parts[1].strip()
            print('{:>2s}{:>19s}'.format(number, name))

    file_path.close()

if __name__ == "__main__":
    main()
