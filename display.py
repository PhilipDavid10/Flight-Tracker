def show_menu():
    print("========================")
    print("     Flight Tracker     ")
    print("========================\n")

    menu_options = ["Search by Flight Number", "Search by Airport", "View Search History", "Exit"]

    for number, options in enumerate(menu_options, start=1):
        print(f"{number}. {options}")

def display_flight(flight):
    print("========================")
    print("   Flight Information   ")
    print("========================\n")

        