def åpne_fil():
    list = []
    with open("redhood.txt", "r") as file:
        content = file.read()
        list.append(content)

    print(list)

def main():
    valg = int(input("vil du se hele teksten skriv 1 eller søke etter ord i teksten trykk 2: "))
    if valg == 1:
        åpne_fil()
    
    elif valg == 2:
        search_string()
    
    else:
        print("velg 1 eller 2.")

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
    
    
main()

#fikse none
#splitte opp søke funk
