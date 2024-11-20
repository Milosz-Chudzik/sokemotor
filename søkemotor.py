def åpne_fil():
    list = []
    with open("redhood.txt", "r") as file:
        content = file.read()
        list.append(content)

    print(list)

def main():
    valg = int(input("vil du se hele teksten skriv 1, søke etter ord i teksten trykk 2 eller finne hvilken linje ordet er på skriv 3: "))
    if valg == 1:
        åpne_fil()
    
    elif valg == 2:
        search_string()

    elif valg == 3:
        finn_linje()
    
    else:
        print("velg 1, 2 eller 3.")

def search_string():
    try:
        with open("redhood.txt", "r") as file:
            content = file.read()
            search_term = input("skriv inn ordet du leter etter: ")
            result = count_string(content, search_term) 
            print(result)
    except FileNotFoundError:
        return "Error: The file 'redhood.txt' was not found."
    
    

def count_string(content, search_term):
    count = content.count(search_term)
    if count > 0:
        return f"ordet '{search_term}' kommer frem {count} ganger i filen."
    else:
        return f"ordet  '{search_term}' var ikke funnet i filen."


def finn_linje():
    search_term = input("skriv inn ordet du leter etter: ")
    file = open("redhood.txt", "r")
    try:
        line_number = 1
        for line in file:
            if search_term in line:
                print(f"'{search_term}' ble funnet på {line_number}.")
            line_number += 1
        
        linje = finn_linje()
        print(linje)
        
    
    except FileNotFoundError:
        return "Error: The file 'redhood.txt' was not found."
    
    
main()


