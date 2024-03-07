from scipy.stats import norm
from scipy.optimize import fsolve

# Part (a): Determining the minimum number of emails needed

# Given data for part (a)
alpha = 0.05  # Level of significance for the test
p0 = 0.5  # Null hypothesis proportion (believing at most 50% of emails are spam)
x_spam_emails = 55  # Number of spam emails received

# Finding the critical Z value for the specified alpha level (one-tailed test)
Z_alpha = norm.ppf(1 - alpha)
print(f"Critical Z value for alpha = {alpha} (one-tailed test): {Z_alpha}")

# Initial guess for the total number of emails received
# This is a rough estimate based on the number of spam emails and the null hypothesis proportion
n_initial_guess = x_spam_emails / p0
print(f"Initial guess for the total number of emails: {n_initial_guess}")

# Define a function to calculate the difference between the calculated Z statistic and the critical Z value
def z_stat(n):
    # Calculate the sample proportion of spam emails
    p_hat = x_spam_emails / n
    # Calculate the standard error of the sample proportion
    std_error = (p0 * (1 - p0) / n) ** 0.5
    # Return the difference between the calculated Z statistic and the critical Z value
    return (p_hat - p0) / std_error - Z_alpha

# Solve for the total number of emails (n) that makes the Z statistic equal to the critical Z value
n_optimal, = fsolve(z_stat, x_spam_emails / p0)
n_optimal = round(n_optimal)
print(f"Optimal total number of emails for part (a): {n_optimal}")

# Part (b): Determining the maximum number of card guesses

# Given data for part (b)
p0_b = 1/3  # Null hypothesis proportion (guessing the suit correctly no more than 1/3 of the time)
x_correct_guesses = 28  # Number of correct guesses

# Define a function to calculate the Z statistic for part (b) based on the number of observations (n)
def z_stat_b(n):
    # Calculate the sample proportion of correct guesses
    p_hat = x_correct_guesses / n
    # Calculate the standard error of the sample proportion
    std_error = (p0_b * (1 - p0_b) / n) ** 0.5
    # Return the difference between the calculated Z statistic and the critical Z value
    return (p_hat - p0_b) / std_error - Z_alpha

# Solve for the maximum number of card guesses (n) for which the friend's claim is believed
n_max_b, = fsolve(z_stat_b, x_correct_guesses / p0_b)
n_max_b = round(n_max_b)
print(f"Maximum number of card guesses for part (b): {n_max_b}")
