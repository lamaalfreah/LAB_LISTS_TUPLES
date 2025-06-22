print("Welcome to the Cinema Booking System")
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

def display_booked_seats():
    print("Booked seats are:")
    if len(booked_seats)==0:
        print("No seats booked yet.")
    else:
        for row, seat in sorted(booked_seats):
            print(f"Row {row}, Seat {seat}")


def get_valid_input(prompt, min_val, max_val, label):
    while True:
        try:
            value = int(input(prompt))
            if value not in range(min_val, max_val + 1):
                print(f"Invalid {label}.")
            else:
                return value
        except ValueError:
            print(f"Invalid {label}.")

def check_availability()->bool:
    row = get_valid_input("Choose a row numeric value between 1 and 10: ", 1, 10, "row")
    seat = get_valid_input("Choose a seat numeric value between 1 and 20: ", 1, 20, "seat")
      
    if (row, seat) in booked_seats:
        print("Sorry, this seat is already booked :( Please try a different one. ")
        return False, row, seat
    else:
        print("The seat is available and ready to be booked :) ") 
        return True, row, seat
        
def add_booking():
    success, row, seat = check_availability()
    if success == True:
        booked_seats.append((row, seat))  
        print(f"Seat {seat} in row {row} has been successfully booked") 

def cancel_booking():
    row = get_valid_input("Choose a row numeric value between 1 and 10: ", 1, 10, "row")
    seat = get_valid_input("Choose a seat numeric value between 1 and 20: ", 1, 20, "seat")
    if (row, seat) in booked_seats:
        booked_seats.remove((row, seat))
        print(f"Seat {seat} in row {row} has been successfully canceled.")

    else:
        print(f"Seat {seat} in row {row} is not currently booked.")

def display_summary():
    print("Booking Summary:")
    print(f"Total booked seats: {len(booked_seats)}")
    counts = [0] * 10
    for row, seat in booked_seats:
        counts[row - 1] += 1

    for i in range(10):
        print("Row", i + 1, ":", counts[i], "seat(s) booked")

def run_cinema_program():
    while True:
        print("Cinema Booking Menu:")
        print("1. View all booked seats")
        print("2. Check seat availability")
        print("3. Add a booking")
        print("4. Cancel a booking")
        print("5. View booking summary")
        print("6. exit")
        choice = input("Enter your choice: ",)

        if choice == "1":
            display_booked_seats()
        elif choice == "2":
            check_availability()
        elif choice == "3":
            add_booking()
        elif choice == "4":
            cancel_booking()
        elif choice == "5":
            display_summary()
        elif choice == "6":
            print("Exiting... Thank you for using the Cinema Booking System!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
run_cinema_program()
