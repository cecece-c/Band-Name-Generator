# Display banner
print("\nWelcome to the Band Name Generator.")


# Get city name and store it in variable 'city' (String)
city = input("\nWhat's the name of the city you grew up in?\n")


# Get pet's name and store it in variable 'pet' (String)
pet = input("\nWhat's your pet's name?\n")


# Display band name suggestion
print(f"\nYour band name could be:\n{city.capitalize()} {pet.capitalize()}\n")
