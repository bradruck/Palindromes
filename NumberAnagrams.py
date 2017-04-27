# This small program finds all the Palindromes in the range of 0 to a set value -
# it then prints out the answers in tabular form that the user specifies in column width

import math # for rounding up (ceil) to next integer

# Method tests if the number is a palindrome, returns true if it is
#
def isPalindrome(testint) :
    # Convert integer to string
    string = str(testint)
    # Assign starting positions
    i = 0
    j = len(string) - 1

    while i < j :
        # Compare left to right digits
        if string[i] != string[j] :
            return False
        # Iterate from the left most digit -> up
        i += 1
        # Iterate from the right most digit -> down
        j -= 1
    return True

# Method prints solutions on a row by column basis
#
def printRowByColumn(maxnum, numcolumns, columnwidth, answerset) :
    print()
    # format adds comma separator to large integer
    print("These are all the Number Anagrams (i.e. Palindromes) between 0 and {:,}".format(maxnum),
          "- displayed in a", math.ceil(len(answerset)/numcolumns), "row X", numcolumns, "column format:")
    print()
    j = 0
    while j < len(answerset) :
        # Allow for tabular printing with user specified number of columns
        for k in range(j, j + numcolumns) :
            # Test for end of list before printing next value
            if k < len(answerset) :
                print("{:>{}}".format(answerset[k], columnwidth), end="")
                                                                           # print the list w/o brackets or commas,
                                                                           # column spacing can be set
        print()
        j += numcolumns                                     # iterate list to start next row at next value

# Method prints solutions on a column by row basis
#
def printColumnByRow(maxnum, numcolumns, columnwidth, answerset) :
    print()
    # format adds comma separator to large integer
    print("These are all the Number Anagrams (i.e. Palindromes) between 0 and {:,}".format(maxnum),
          "- displayed in a", numcolumns, "column X", math.ceil(len(answerset)/numcolumns), "row format:")
    print()
    j = 0
    while j < int(math.ceil(len(answerset)/numcolumns)) :
        for k in range(j, j + numcolumns) :
            # Test for end of list before printing next value
            if (k * math.ceil(len(answerset)/numcolumns) - j * math.ceil(len(answerset)/numcolumns) + j) < len(answerset) :
                print("{:>{}}".format(answerset[k * math.ceil(len(answerset)/numcolumns) -
                                                j * math.ceil(len(answerset)/numcolumns) + j],columnwidth), end="")
                                                                            # print the list w/o brackets or commas,
                                                                            # column spacing can be set
        print()
        j += 1                                             # iterate list to start next column at next value

# Main Program
#
def main() :
    maxnum = 120000                                                  # This sets the maximum number in range
    columnwidth = 10                                                 # This sets the column widths for display
    answerset = []                                                   # This creates the list for palindromes that exist

    # Find all the palindromes in the range, add to list answerset
    for i in range(maxnum) :
        if isPalindrome(i) :
            answerset.append(i)

    # Print out the total number of palindromes found
    print("\nThere are a total of {:,}".format(len(answerset)), "palindromes from 0 to {:,}".format(maxnum))

    # Prompt user for output configuration preference
    print("\nWould you like to see your results in (1) a row by column format, or (2) a column by row format?")
    choice = input("Please enter either a 1 or 2: ")
    numcolumns = int(input("\nPlease enter the number of columns you would like to display: "))

    if choice == '1' :
        printRowByColumn(maxnum, numcolumns, columnwidth, answerset)
    else :
        printColumnByRow(maxnum, numcolumns, columnwidth, answerset)

main()