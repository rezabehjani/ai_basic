
#https://blog.faradars.org/text-preprocessing-in-python/

import re
input_str = '’Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls.'

#remove number
result1 = re.sub(r'\d+', '', input_str)
print(result1)
print("--------------------------------------------------")

#################### remove  [!”#$%&’()*+,-./:;<=>?@[\]^_`{|}~] ####################################


# import string library function
import string

# Storing the sets of punctuation in variable result
result = string.punctuation

# Printing the punctuation values
print(result)

input_str = " \t a string example\t "
input_str = input_str.strip()
print(input_str)

import string
input_str = 'This &is [an] example? {of} string. with.? punctuation!!!!' # Sample string
result = str.translate(input_str.maketrans('',''), string.punctuation)
print(result)