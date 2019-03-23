def is_palindrome(number):
    """
    Compares the first and the last index of a string argument.
    If they are equal, the function recursively calls herself with a smaller argument. If not, 'False' is returned.
    It returns 'True' when there's nothing left to compare.
    """
    if len(number) <= 1:
        return True
    else:
        if number[0] == number[-1]:
            return is_palindrome(number[1:-1])
        else:
            return False


def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """
   for number in range(100000, 1000000):
       str_num = str(number)
       if is_palindrome(str_num[2:]):
           str_num = str(number+1)
           if is_palindrome(str_num[1:]):
               str_num = str(number+2)
               if is_palindrome(str_num[1:5]):
                   str_num = str(number+3)
                   if is_palindrome(str_num):
                       print(number)

if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()
    print(f"Question 2 solution: {return_value}")                       