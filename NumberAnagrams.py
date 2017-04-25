# This small program finds all the Palindromes in the range of 0 to 100,000 -
# it then prints out the answers in tabular form

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

# Main program
#
def main() :
    # This sets the maximum number in range
    maxnum = 100000
    answerset = []

    # Find all the palindromes in the range, add to list answerset
    for i in range(maxnum) :
        if isPalindrome(i) :
            answerset.append(i)

    print()
    # format adds comma separator to large integer
    print("These are all the Number Anagrams (i.e. Palindromes) between 0 and {:,}:".format(maxnum))
    print()
    j = -1
    while j < len(answerset):
        # Allow for tabular printing with 17 columns width
        for k in range(j + 1, j + 18) :
            # Test for end of list before printing next value
            if k < len(answerset) :
                print("{:10}".format(answerset[k]), end="")  # print the list w/o brackets or commas, cols spacing at 10
        print()
        j += 17 # iterate list to start next line at appropriate value

main()