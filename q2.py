from math import factorial

def birthday_paradox(n, days=365):
    # Calculate the probability of at least two people sharing a birthday
    prob_no_shared_birthday = 1
    for i in range(n):
        prob_no_shared_birthday *= (days - i) / days
    prob_at_least_two_shared = 1 - prob_no_shared_birthday
    return prob_at_least_two_shared

# Part (a) - Calculate for n = 23 to prove the birthday paradox
n_a = 24
prob_a = birthday_paradox(n_a)
print(prob_a)

# for part b one can start brute force from 1 to 365 and then find the solution

for i in range(1,365):
    prob_i = birthday_paradox(i)
    print(prob_i)
    if(prob_i > 0.75):
        print(i)
        print("This is your answer")
        break

# for part c of the assignment which assumes the condition that the computer randomly generates a date on a given real birthdate of the person we will use the following script in order to simulate this program and test the prob
def find_minimum_n_for_probability(p, days=365):
    # Initialize variables
    n = 0  # Starting number of people
    prob_no_match = 1.0  # Initial probability of no matches

    print("Starting the calculation to find the smallest integer n...")
    # Continue until the probability of at least one match is greater than or equal to p
    while True:
        # Calculate the probability of no match for both real and fake dates
        prob_no_match *= (days - n) / days * (days - n) / days
        prob_at_least_one_match = 1 - prob_no_match
        
        # Print the current status
        print(f"After considering {n+1} people, the probability of at least one match is {prob_at_least_one_match:.4f}.")
        
        # Check if the probability meets or exceeds the desired threshold
        if prob_at_least_one_match >= p or prob_no_match <= 0:
            break
        
        n += 1  # Increment the number of people
    
    # Print the result in a more presentable manner
    print("\nResult:")
    print(f"To achieve a probability of at least {p*100}% for at least one match (real or fake date),")
    print(f"you need a minimum of {n+1} people.")
    return n+1

# Example usage
print(find_minimum_n_for_probability(0.99))
