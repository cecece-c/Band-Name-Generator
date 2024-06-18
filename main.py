# Import 'time' library
import time


# Display welcome message
print("\nWelcome to the Band Name Generator.")


# Get city name and store it in 'city' (String)
city = input("\nWhat's the name of the city you grew up in?\n")


# Get pet's name and store it in 'pet' (String)
pet = input("\nWhat's your pet's name?\n")


# Display suggestion
print(f"\nYour band name could be:\n{city.capitalize()} {pet.capitalize()}")


# Display exit message
print("\nProgram exiting...")


# Exit program after 5 second delay
for delay in range(5):
    time.sleep(1)
