# Example8.py
# Print a pattern using nested loops
# Pattern:
# * ooooo *
# ** oooo **
# *** ooo ***
# **** oo ****
# ***** o *****
# ****** *******
# ****** *******
# ***** o *****
# **** oo ****
# *** ooo ***
# ** oooo **
# * ooooo *

for i in range (1,6):
    print ('*'*i,'o'*(6-i),'*'*(i))
for i in range (6,0,-1):
    print ('*'*i,'o'*(6-i),'*'*(i+1))