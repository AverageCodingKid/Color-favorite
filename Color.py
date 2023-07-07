def color():
    favorite = str(input("What is your favorite color? "))
    if favorite.lower() == "blue":
        print("I like that color too, it is the color of the ocean!")
    elif favorite.lower() == "red":
        print("I like that color too, it is the color of poppies!")
    elif favorite.lower() == "green":
        print("I like that color too, it is the color of grass!")
    elif favorite.lower() == "white":
        print("I like that color too, it is the color of many old TV shows and movies!")
    elif favorite.lower() == "black":
        print("I like that color too, it is the color of void")
    else:
        print("Sorry, I am not familiar with this color. Tip: You can edit my code and follow the same pattern of the rest of the code.")

color()