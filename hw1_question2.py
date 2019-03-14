def is_identical(list):
    """
    Runs through a given list of pairs of digits and returns True if all pairs on the list are identical.
    """
    for i in range(0, len(list):
        if list[i][0] != list[i][1]:
            return False
    return True

def check_palindrome():
   """
   Runs through all 6-digit numbers and checks the mentioned conditions.
   The function prints out the numbers that satisfy this condition.

   Note: It should print out the first number (with a palindrome in its last 4 digits),
   not all 4 "versions" of it.
   """ 
   for number in range(100000, 1000000):
       if is_identical([[number[2],number[5]], [number[3], number[4]]):
           a = number+1
           if is_identical([[a[1], a[5]], [a[2], a[4]]):
               a = a+1
               if is_identical([[a[1], a[5]], [a[2], a[4]]]):
                   a = a+1
                   if is_identical([a[0], a[5]], [a[1],a[4]], [a[2], a[3]]):
                       print(number)

if __name__ == '__main__':
    # Question 2
    return_value = check_palindrome()
    print(f"Question 2 solution: {return_value}")                       

