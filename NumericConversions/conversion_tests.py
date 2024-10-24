#Description: This script tests various numeric
#             conversion techniques
# Author: Sam Q. Newprogrammer

a = "   101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5   '

#Transformation of Variables
a_transform = float(a.strip())
b_transform = int(b)
c_transform = str(c)
#d_transform = int(d) changed to str but ultimately was able to splice and output the below
d_transform = int(d[7:].strip())
#added strip function to d_transform to get rid of trailing spaces in output


print(a_transform, type(a_transform), b_transform, type(b_transform), c_transform, type(c_transform), d_transform, type(d_transform))
