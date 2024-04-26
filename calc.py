from termcolor import cprint
def start_text():
     cprint("Welcome!","green",attrs=["bold"])
     cprint("- to my simple calculator program","grey")
     
     cprint("Symbols: //,*,-,+","green")
     print("-------------------")
     print("calculator:")
     print()

def user():

     start = True
     while start:
        
        symbol = str(input("Symbol: "))
        try:
            zahl1 = int(input("Zahl-1: "))
            zahl2 = int(input("Zahl-2: "))
        except ValueError:
            cprint("Please type a number.","red",attrs=["bold"])
            continue

        if symbol == "//":
            x = zahl1 // zahl2
            print()
            cprint(f"Result: {x}","green",attrs=["bold"])
        elif symbol == "+":
            y = zahl1 + zahl2
            print()
            cprint(f"Result: {y}","green",attrs=["bold"])
        elif symbol == "-":
            z = zahl1 - zahl2
            print()
            cprint(f"Result: {z}","green",attrs=["bold"])
        elif symbol == "*":
            o = zahl1 * zahl2
            print()
            cprint(f"Result: {o}","green",attrs=["bold"])
        else:
            print()
            cprint("Invalid symbol!","red",attrs=["bold"])
        print()
        choice = str(input("Do you want to exit?(j/n): "))
        if choice == "j":
          print("Goodbye!")
          start = False
        else:
          start = True
        
def main():
     start_text()
     user()
if __name__ == "__main__":
    main()