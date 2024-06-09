# Import 'time' library
import time


# Display banner
print("\nWelcome to the Band Name Generator.")


# Get city name and store value in 'city' (String)
city = input("\nWhat's the name of the city you grew up in?\n")


# Get pet's name and store value in 'pet' (String)
pet = input("\nWhat's your pet's name?\n")


# Display suggestion for band name
print(f"\nYour band name could be:\n{city.capitalize()} {pet.capitalize()}")


# Delay exit
print("\nProgram exiting...")
for delay in range(5):
    time.sleep(1)
exit(0)
