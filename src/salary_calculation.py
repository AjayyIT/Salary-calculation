# Employee Salary Calculation in Python

def calculate_net_salary(basic_pay, allowances, deductions, taxes):
    """Calculates the final net salary."""
    gross_salary = basic_pay + allowances
    # Note: Depending on local laws, tax is sometimes calculated on (gross_salary - deductions)
    total_deductions = deductions + (gross_salary * taxes / 100)
    net_salary = gross_salary - total_deductions
    return net_salary

def get_positive_float(prompt):
    """Prompts the user until a valid positive number is entered."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Error: Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")

if __name__ == "__main__":
    print("--- Employee Salary Calculator ---")
    
    # Safely gather inputs from the user
    basic_pay = get_positive_float("Enter the basic pay: ")
    allowances = get_positive_float("Enter the total allowances: ")
    deductions = get_positive_float("Enter the total deductions: ")
    taxes = get_positive_float("Enter the applicable taxes percentage: ")

    # Calculate net salary
    net_salary = calculate_net_salary(basic_pay, allowances, deductions, taxes)

    # Display the result
    print(f"\nThe net salary is: {net_salary:.2f}")
