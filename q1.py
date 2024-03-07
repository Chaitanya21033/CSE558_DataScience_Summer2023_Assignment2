# Part (a) for k = 6

k = 10000
favorable_outcomes = 0
total_outcomes = k * k  # Since we roll the die twice

# Iterate through all possible outcomes
for first_roll in range(1, k + 1):
    for second_roll in range(1, k + 1):
        # Check if the second roll is a multiple of the first roll
        if second_roll % first_roll == 0:
            favorable_outcomes += 1

# Calculate the probability
probability_a = favorable_outcomes / total_outcomes
print(probability_a)
