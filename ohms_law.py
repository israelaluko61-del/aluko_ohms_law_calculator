"""
Ohm's Law and Power Calculator
CTE123 Python Mini Project

This program calculates voltage, current, resistance, and electrical power.
It also keeps a history of calculations during the current session.
"""

def get_number(prompt):
    """Ask for a number and keep asking until the input is valid."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a value that is zero or greater.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number, not a letter.")


def calculate_voltage():
    """Calculate voltage using V = I x R."""
    current = get_number("Enter current in amperes (A): ")
    resistance = get_number("Enter resistance in ohms (Ω): ")
    voltage = current * resistance
    return f"Voltage = {voltage:.2f} V"


def calculate_current():
    """Calculate current using I = V / R."""
    voltage = get_number("Enter voltage in volts (V): ")
    resistance = get_number("Enter resistance in ohms (Ω): ")

    if resistance == 0:
        return "Error: Resistance cannot be zero when calculating current."

    current = voltage / resistance
    return f"Current = {current:.2f} A"


def calculate_resistance():
    """Calculate resistance using R = V / I."""
    voltage = get_number("Enter voltage in volts (V): ")
    current = get_number("Enter current in amperes (A): ")

    if current == 0:
        return "Error: Current cannot be zero when calculating resistance."

    resistance = voltage / current
    return f"Resistance = {resistance:.2f} Ω"


def calculate_power():
    """Calculate electrical power using P = V x I."""
    voltage = get_number("Enter voltage in volts (V): ")
    current = get_number("Enter current in amperes (A): ")
    power = voltage * current
    return f"Power = {power:.2f} W"


def main():
    """Display the menu and run the calculator until the user quits."""
    history = []

    while True:
        print("\n===== OHM'S LAW AND POWER CALCULATOR =====")
        print("1. Calculate Voltage")
        print("2. Calculate Current")
        print("3. Calculate Resistance")
        print("4. Calculate Power")
        print("5. View Calculation History")
        print("6. Quit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            result = calculate_voltage()
            print(result)
            history.append(result)

        elif choice == "2":
            result = calculate_current()
            print(result)
            if not result.startswith("Error"):
                history.append(result)

        elif choice == "3":
            result = calculate_resistance()
            print(result)
            if not result.startswith("Error"):
                history.append(result)

        elif choice == "4":
            result = calculate_power()
            print(result)
            history.append(result)

        elif choice == "5":
            print("\n--- CALCULATION HISTORY ---")
            if history:
                for number, item in enumerate(history, start=1):
                    print(f"{number}. {item}")
            else:
                print("No calculations have been recorded yet.")

        elif choice == "6":
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid menu choice. Please select a number from 1 to 6.")


# Start the program.
if __name__ == "__main__":
    main()
