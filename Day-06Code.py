# Day 6 - Looping & Loop Control
# Task: Print even numbers from 1–50, skip 20, break at 40

# This Function to represent introduction of this assignment / Project. Starting with a little welcome message.
def show_intro():
    print("🔹 Welcome to Day 6 of Python 30-Day Challenge!")
    print("🔹 Topic: Looping & Loop Control")
    print("🔁 Task: Print even numbers from 1–50, skip 20, break at 40\n")

# This function displays the even numbers from 1-50 by skipping at 20 and breaking at 40
def PrintEvenWithControl():

    # Looping numbers from 1-50
    for number in range(1, 51):

        # In loop if it identifies 20 it will skip it
        if number == 20:
            # Displaying skipping msg to user
            print("⚠️ Skipping 20")
            # As 20 is even also we're skipping it completely
            continue 

        # In loop if it identifies 40 it will break the loop there itself
        if number == 40:
            # Displaying breaking msg to user
            print("🛑 Breaking at 40")
            # As 40 is even also we're breaking the loop when python identifies 40 in loop.
            break

        # Checks if number is even or not, if even only then it displays the result
        if number % 2 == 0:
            print(f"✅ Even: {number}")

# main function, where program execution starts
def main():

    # calling show_intro() for basic inroduction
    show_intro()

    # calling PrintEvenWithControl() to checking and displaying even numbers from 1-50, if 20 skip it, if 40 break the loop there itself.
    PrintEvenWithControl()

# # calling main() to starting execution of program
if __name__ == "__main__":
    main()
