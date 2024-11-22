def åpne_fil(filnavn):
    list = [123]
    with open(filnavn, "r") as file:
        content = file.read()
        list.append(content)

    print(list)


def velg_fil():
    tekst_valg = int(input("""Velg hvilken fil du ønsker å åpne: \nredhood.txt = 1 \ntekstfil1.txt = 2 \ntekstfil2.txt = 3 \ntekstfil3.txt = 4 \nValg: """))

    if tekst_valg == 1:
        return "redhood.txt"
    elif tekst_valg == 2:
        return "tekstfil1.txt"
    elif tekst_valg == 3:
        return "tekstfil2.txt"
    elif tekst_valg == 4:
        return "tekstfil3.txt"
    else:
        print("velg 1, 2, 3 eller 4.")

def main():
    filnavn = velg_fil()
    valg = int(input("vil du se hele teksten skriv 1, søke etter ord i teksten trykk 2 eller finne hvilken linje ordet er på skriv 3: "))
    if valg == 1:
        print(åpne_fil(filnavn))
        valg2 = int(input("vil du åpne en annen fil skriv 1 \nsøke etter ett ord skriv 2 \nfinne hvilken linje ett ord er på skriv 3 \nvelg: "))

        if valg2 == 1:
            main()
        
        elif valg2 == 2:
            search_string()
        
        elif valg2 == 3:
            finn_linje()
        
        else:
            print("velg 1, 2 eller 3.")
    
    elif valg == 2:
        search_string()
        valg2 = int(input("vil du åpne en annen fil skriv 1 \nsøke etter ett annet ord skriv 2 \nfinne hvilken linje ordet er på skriv 3 \nvelg: "))

        if valg2 == 1:
            main()
        
        elif valg2 == 2:
            search_string()
        
        elif valg2 == 3:
            finn_linje()
        
        else:
            print("velg 1, 2 eller 3.")

    elif valg == 3:
        finn_linje()
        valg2 = int(input("vil du åpne en annen fil skriv 1 \nsøke etter ett ord skriv 2 \nvelge ett annet ord skriv 3 \nvelg: "))

        if valg2 == 1:
            main()
        
        elif valg2 == 2:
            search_string()
        
        elif valg2 == 3:
            finn_linje()
        
        else:
            print("velg 1, 2 eller 3.")
    
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
