from display import show_menu
from api import search_flight

def main():
    show_menu()
    choice = input("Choice: ")

    if choice == "1":
        flight_number = int(input("Enter Flight Number: "))
        flight = search_flight(flight_number)
        display_flight(flight)


    







main()