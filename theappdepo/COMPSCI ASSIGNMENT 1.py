import logging
import time

tired=True

yes_list=["y","yes","yeah","sure","okay"]

coffee_types={
    "light":'light_roast',
    "medium":"medium_roast",
    "dark":"dark_roast",
}

def make_coffee(type_of_coffee):
    print("Getting coffee initiated!!")
    time.sleep(.5)
    print("Getting type of coffee")
    print(f"{type_of_coffee} is selected.\n")
    
    make_coffee=input("Would you like to continue? Y/N?")
    make_coffee=make_coffee.lower()

    if make_coffee in yes_list:
        
        print("Uhhhh! Fine.... I guess I will make coffee")

        for i in range(3):

            print("Brewing...")
            time.sleep(.3)

        print("Theres your freaking coffe dude!")

        return(f"It is a {selection} coffee like you asked your highness.")

    elif make_coffee not in yes_list:

        print("Sounds good to me. I hate my job anyways..")
        return(print("User selected NO or an improper selection"))
    
    else:
        print("OH MY GOD! SOMETHING WENT WRONG!!!")
        time.sleep(.3)
        print("SOMETHING WENT WRONG!!")
        time.sleep(.3)
        print("SOMETHING WENT WRONG! DONT FREAK OUT!")
        return(logging.warning("Error in function"))
    

while tired is True:

    print("I see you are tired, lets make coffee!")

    get_type_of_coffee=input("Would you like, light, medium, or dark roast?")
    get_type_of_coffee=get_type_of_coffee.lower()
    get_type_of_coffee.split(" ")

    if "light" in get_type_of_coffee and "medium" or "dark" not in get_type_of_coffee:
        selection=coffee_types["light"]
    elif "medium" in get_type_of_coffee and "light" or "dark" not in get_type_of_coffee:
        selection=coffee_types["medium"]
    elif "dark" in get_type_of_coffee and "light" or "medium" not in get_type_of_coffee:
        selection=coffee_types["dark"]
    else:
        print("there may be an error. You are still tired")
        tired=True

    try:
        make_coffee(selection)
        tired=False
    except:
        print("Something went wrong..")

