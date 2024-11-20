def search_string():
    try:
        with open("redhood.txt", "r") as file:
            content = file.read()
            search_term = input("Enter the string to search: ")
            result = count_string(content, search_term) 
            result2 = finn_linje(search_term)
            print(result, result2)
    except FileNotFoundError:
        return "Error: The file 'redhood.txt' was not found."
    
def åpne_textfil(text_fil):
    text_fil = []
    with open("redhood.txt", "r") as file:
        for line in file:
            text_fil.append(line.strip())
    

def count_string(content, search_term):
    count = content.count(search_term)
    if count > 0:
        return f"The string '{search_term}' appears {count} times in the file."
    else:
        return f"The string '{search_term}' was not found in the file."


def finn_linje(search_term):
    file = open("redhood.txt", "r")
    try:
        line_number = 1
        for line in file:
            if search_term in line:
                print(f"The string '{search_term}' was found on line {line_number}.")
            line_number += 1
    
    except FileNotFoundError:
        return "Error: The file 'redhood.txt' was not found."
    
    
search_string()
