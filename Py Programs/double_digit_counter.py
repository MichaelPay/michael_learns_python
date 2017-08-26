# takes an integer input
# counts the two integers next to each other
# returns digit

def double_digit_counter(number):
    counter = 0  # function starts with the count 0
    last_digit = None  # last_digit variable uses None
    for digit in str(number):  # the int input is converted into a string and iterated "digit by digit" in a for loop.
        if digit == last_digit:  # compares the current digit to see if it's the same as the last digit
            counter += 1  # if it is, meaning there's a double, the counter goes up by 1
        last_digit = digit  # set the last digit variable to the current digit before continuing with the loop.
    return counter  # returns the integer count of duplicates.
