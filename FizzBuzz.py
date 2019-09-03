# Program FizzBuzz
# Ask the op. for an integer
#  Loop through integers 0 to that number
#  if the current val is divisible by FIZZ_DENOMINATOR then print "Fizz" instead of the number
#  if current val is divisible by BUZZ_DENOMINATOR  then print "Buzz"instead of the number
#  if both, print FizzBuzz instead of the number
# else print current value
# There's a DEBUG setting
#  Also: there's a default MAX_VALUE


# Constants
FIZZ_DENOMINATOR = 3
BUZZ_DENOMINATOR = 5
MAX_VALUE_DEFAULT = 100
DEBUG = True

# loop in python
curval =0
maxval = MAX_VALUE_DEFAULT

s_Outstring = "Starting the game.  Enter a positive integer above 10 "
str_maxval = input (s_Outstring )
if DEBUG :
    print ('Working with :' )
    print ('\ncurval: ', curval, type(curval))
    print ('\nmaxval: ', maxval , type(maxval))
    print ('\nstr_maxval : ', str_maxval, type(str_maxval))


maxval = int(str_maxval)
print(s_Outstring + " to" + str(maxval))

for curval in range(0, maxval+1) :
    s_Outstring = str(curval)
    # replace curval with Fiz and/or Buzz
    if (curval % FIZZ_DENOMINATOR) == 0 :
        # clear the string
        s_Outstring = ""
        s_Outstring = s_Outstring +"Fizz"

    if curval % BUZZ_DENOMINATOR == 0 :

        if s_Outstring == str(curval) :
            # clear the string unless it's Fizz already
            s_Outstring = ""
        s_Outstring = s_Outstring +"Buzz"

    print (s_Outstring)
    curval = curval + 1
    input ("Hit Enter for the next number")
    # end for
print ("FizzBuzz Fizzled Out")
