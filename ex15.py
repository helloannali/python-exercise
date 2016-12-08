# import argv moudule
from sys import argv

# read argv, ann the put it to the var(script and filename)
script, filename = argv

# use function open to open a file, the open function return value is file object
txt = open(filename)

# print the var filename's value
print "Here's your file %r:" % filename

# use txt file object function to show the file content
print txt.read()
txt.close()

print "Type the filename again:"
# use raw_input function to get the user input value
file_again = raw_input("> ")

# then also use open function to get a file object
txt_again = open(file_again)

# use the file object to get a file content
print txt_again.read()
txt_again.close()