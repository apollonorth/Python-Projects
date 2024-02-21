import math

# This function takes a numeric input n, which decides the number of iterations used to approximate pi, return pi
def compute_pi(n):
    # Set pi to 0, denominator to 1
    pi = 0
    denominator = 1
    # From 0-(n-1). if an even iteration add 1/denom , if its odd subtract 1/denom
    for i in range(n):
        if i % 2 == 0:
            pi += (1 / denominator)
        else:
            pi -= (1 / denominator)
        # increment denominator by 2
        denominator += 2
    # Multiply by 4 and return
    pi *= 4
    return pi


# This function takes numeric input x and approximates its sqrt, returning that value
def compute_sqrt(x):
    # Start with first guess at 1, next guess is (0.5 * (last + x/last))
    last = 1
    next = 0.5 * (last + x / last)
    # Loop ten times with last = next and next = same formula as before
    for i in range(10):
        last = next
        next = 0.5 * (last + x / last)

    # Approximation was calculated and now will be returned
    return next


# This function takes a numeric input n and prints all prime numbers less than or equal to n
def display_primes(n):
    print('Prime numbers less than or equal to ' + str(n) + ':')
    first_prime = True
    # Loop from 2 - n-1 calling is_prime(), and printing the primes
    for i in range(2, n):
        if is_prime(i):
            if first_prime:
                print(i, end='')
                first_prime = False
            # After first prime printed, print commas before number
            else:
                print(',', i, end='')


# This function takes a numeric input n and determines if it is prime
def is_prime(n):
    # Loop from 2 - n-1 and check if n can be evenly divided by i
    for i in range(2, n):
        # If even division of n with i, it is not prime, return false
        if n % i == 0:
            return False
    # If no even divisions are found, return true, indicating it is prime
    return True


# This function repeatedly prompts user for student names and scores, then calculates the min, avg, and max, outputs
def process_scores():
    # Declare and initialize a number of variables to be used
    sum_of_scores = 0
    count = 0
    min_score = 999999999
    max_score = -999999999
    min_name = ''
    max_name = ''

    # Loop breaks when user enters q and loop breaks
    while True:
        # Prompt user and store name and score in input string variable
        inputStr = input('Enter student name and score (or enter \'q\' to quit): ')
        # Check if input is q or Q and return if so
        if inputStr.lower() == 'q':
            break

        # Break input into a list and store in name and score variables
        input_list = inputStr.split()
        name = input_list[0]
        current_score = (int) (input_list[1])

        # Add score into scores sums, increment count
        sum_of_scores += current_score
        count += 1

        # Check if score is lower than min and or more than max, update
        if current_score < min_score:
            min_score = current_score
            min_name = name
        if current_score > max_score:
            max_score = current_score
            max_name = name
    # Calculate average and print results
    average = sum_of_scores / count
    print('\nAverage Score:', average)
    print('Minimum Score:', min_name, '-', min_score)
    print('Maximum Score:', max_name, '-', max_score)


# This function takes info about a person and calculates and returns their tax amount
def compute_tax(income, status, state):
    # Get normal tax rate for in state depending on income and marital status
    if status == 'single':
        if income < 30000:
            tax_rate = 0.2
        else:
            tax_rate = 0.25
    else:
        if income < 50000:
            tax_rate = 0.1
        else:
            tax_rate = 0.15

    # Subtract 0.03 if out of state
    if state == 'o':
        tax_rate -= 0.03

    # Calculate tax amount and return
    tax_amount = income * tax_rate
    return tax_amount


# This function takes numeric inputs a, b, and c and solves the quadratic equation, returning two inputs
def solve_quadratic(a, b, c):
    # Find discriminant
    d = (b * b) - (4 * a * c)
    # If no solutions exist, return two zeros
    if d < 0:
        return 0, 0
    # Solve for x1
    x1 = (-b + (math.sqrt(d))) / (2 * a)
    # Solve for x2
    x2 = (-b - (math.sqrt(d))) / (2 * a)

    return x1, x2


# This functions uses selection sort to sort a list
def sort(list):
    # Copy list to make the original list unchanged
    sorted_list = list.copy()
    length = len(sorted_list)

    # Selection sort
    for i in range(length):
        min_index = i
        # Find next min in list
        for j in range(i+1, length):
            if sorted_list[j] < sorted_list[min_index]:
                min_index = j
        # Swap min element with i index
        temp = sorted_list[i]
        sorted_list[i] = sorted_list[min_index]
        sorted_list[min_index] = temp

    # Return now sorted list
    return sorted_list


# This function takes a first and last name as input and returns a generated ID and Password
def id_password(first, last):
    # Change to uppercase
    first = first.upper()
    last = last.upper()

    # Generate ID
    id = first[0] + last

    # Generate Password, make sure last name length works with password
    if len(last) == 1:
        password = first[0] + first[(len(first) - 1)] + last[0] + str(len(first)) + str(len(last))
    elif len(last) == 2:
        password = first[0] + first[(len(first) - 1)] + last[0:2] + str(len(first)) + str(len(last))
    else:
        password = first[0] + first[(len(first) - 1)] + last[0:3] + str(len(first)) + str(len(last))

    # Return id and passwrod
    return id, password


# This function rads an input file and creates a sorted output file based on student ID
def file_sort(infile, outfile):
    # Open files
    input_file = open(infile, 'r')
    output_file = open(outfile, 'w')
    # Get num of students
    num_students = int(input_file.readline().strip())

    # Store Student info into a 2d array
    student_info = []
    for i in range(num_students):
        # Get next line and split it into array, store that array into array of student info
        line = input_file.readline().strip()
        student_info.insert(len(student_info), line.split())

    # Use selection sort to sort IDs
    for i in range(num_students):
        min_index = i
        for j in range(i+1, num_students):
            # Accessing the first element of each student array for ID
            if student_info[j][0] < student_info[min_index][0]:
                min_index = j
        # Swap elements
        temp = student_info[i]
        student_info[i] = student_info[min_index]
        student_info[min_index] = temp

    # Write to output file
    output_file.write(str(num_students) + '\n')
    # Loop through students and loop through their info to print everything
    for i in range(num_students):
        for j in range(3):
            output_file.write(student_info[i][j])
            # Print spaces after each element except last
            if j != 2:
                output_file.write(' ')
        # New line after each line except last
        if i != (num_students - 1):
            output_file.write('\n')


# Function to display selection menu
def display_menu():
    print('\n      Selection Menu')
    print('--------------------------')
    print('1: Compute Pi')
    print('2: Compute Square Root')
    print('3: Display Primes')
    print('4: Process Scores')
    print('5: Compute Tax')
    print('6: Solve Quadratic')
    print('7: Sort List')
    print('8: Generate ID and Password')
    print('9: File Sort')
    print('10: Quit Program')


# Function to handle the selections 1-9 and other function calling
def handle_selection(selection):
    # Start conditionals to handle the different selections
    # Most prompt and scan input, call function, and print output
    if selection == '1':
        n = int(input('Approximate Pi with how many iterations? '))
        pi = compute_pi(n)
        print("Pi is approximately", pi)

    elif selection == '2':
        x = int(input('Approximate the square root of what number? '))
        sqrt = compute_sqrt(x)
        print('The square root of', x, 'is', sqrt)

    elif selection == '3':
        n = int(input('Find primes less than or equal to what number? '))
        display_primes(n)
        print()

    elif selection == '4':
        process_scores()

    elif selection == '5':
        income = int((input('Enter income: ')).strip())
        status = (input('Enter martial status (single or married): ').lower()).strip()
        state = (input('Enter \'i\' for in state, and \'o\' for out of state: ')).lower().strip()
        if income < 0:
            print('Income must be greater than or equal to 0.')
        elif status != 'single' and status != 'married':
            print('Marital status must be either \'single\' or \'married\'')
        elif state != 'o' and state != 'i':
            print('State must be either \'i\' or \'o\'')
        else:
            tax = compute_tax(income, status, state)
            print('Tax amount is $' + str(tax))

    elif selection == '6':
        # Get inputs in array by splitting, then store in a, b, c with int type casting
        inputs = (input('Enter three numbers separated by spaces (a b c): ')).split()
        a = int(inputs[0])
        b = int(inputs[1])
        c = int(inputs[2])
        x1, x2 = solve_quadratic(a, b, c)
        print('Solutions:', x1, 'and', x2)

    elif selection == '7':
        list = (input('Enter a list of numbers separated by spaces: ').strip().split())
        # Change strings to ints
        for element in list:
            element = int(element)
        sorted_list = sort(list)
        print('Input list:', list)
        print('Sorted list:', sorted_list)

    elif selection == '8':
        names = input('Enter first and last name separated by a space: ').strip().split()
        id, password = id_password(names[0], names[1])
        print('User ID:', id)
        print('Password:', password)

    elif selection == '9':
        infile = input('Enter input file name (must be in same dir as program.py): ')
        outfile = input('Enter output file name: ')
        file_sort(infile, outfile)
        # Print that output file has been written
        print('File output complete.')

    # If input is not 1-10
    else:
        print('Input must be a number 1-10')


# Test the Rectangle class
def rectangle_function():
    print('Testing the Rectangle class:')
    # Create a Rectangle object
    rectangle_obj = Rectangle(10, 5)

    # Test getting length and width
    print("Length:", rectangle_obj.get_length())
    print("Width:", rectangle_obj.get_width())

    # Test area calculation
    print("Area:", rectangle_obj.area())

    # Test modifying length and width
    rectangle_obj.set_length(20)
    rectangle_obj.set_width(10)
    print("Length after rectangleObj.set_length(20):", rectangle_obj.get_length())
    print("Width after rectangleObj.set_width(10):", rectangle_obj.get_width())

    # Test area calculation with new dimensions
    print("Area:", rectangle_obj.area())

    # Test string representation
    print("String Representation:", rectangle_obj)


def main():
    # Test code for rectangle class
    rectangle_function()

    # Looping menu, program will end when user selects 10
    while True:
        # Call function to display the menu
        display_menu()
        # Get selection from user and strip of white space
        selection = (input('\nMenu Choice: ')).strip()
        # End program if selection is 10
        if selection == '10':
            return
        # Call function to handle to selection
        handle_selection(selection)


# Rectangle Class
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def set_length(self, length):
        self.length = length


    def set_width(self, width):
        self.width = width


    def get_length(self):
        return self.length


    def get_width(self):
        return self.width

    def area(self):
        area = self.length * self.width
        return area

    def __str__(self):
        return 'Rectangle with length ' + str(self.length) + ' and width ' + str(self.width) + '.'

# Call main to run the program
main()

