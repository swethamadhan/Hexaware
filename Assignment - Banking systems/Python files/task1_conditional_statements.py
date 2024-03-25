                                            #Banking System
                                        #Control Structure
#Task 1: Conditional Statements
#In a bank, you have been given the task is to create a program that checks if a customer is eligible for 
#a loan based on their credit score and income. The eligibility criteria are as follows:
#• Credit Score must be above 700.
#• Annual Income must be at least $50,000.
#Tasks:
#1. Write a program that takes the customer's credit score and annual income as input.
#2. Use conditional statements (if-else) to determine if the customer is eligible for a loan.
#3. Display an appropriate message based on eligibility.


def check_loan_eligibility(credit_score, annual_income):
    if credit_score > 700 and annual_income >= 50000:
        return True
    else:
        return False

# Main function
def main():
    # Take input from user
    credit_score = int(input("Enter customer's credit score: "))
    annual_income = float(input("Enter customer's annual income: $"))

    # Check eligibility
    eligible = check_loan_eligibility(credit_score, annual_income)

    # Display result
    if eligible:
        print("Congratulations! The customer is eligible for a loan.")
    else:
        print("Sorry, the customer is not eligible for a loan.")

# Execute the main function
if __name__ == "__main__":
    main()
