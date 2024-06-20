def get_starting_number():
    while True:
        beers = input("How many bottles of beer on the wall?")
        try:
            beers = int(beers)
            if beers >= 1:
                break
            elif beers <1:
                continue
        except ValueError:
            continue
    return beers

def sing():
    beers = int(get_starting_number)
    i = beers
    while i != 0:
        if i == 1:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall.")
            break
        elif i == 2:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print("Take one down, pass it around, 1 bottle of beer on the wall.")
            continue
        elif i > 2: 
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall.")
            continue