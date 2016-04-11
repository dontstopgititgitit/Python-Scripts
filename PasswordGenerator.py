#!/usr/bin/env python

import sys    
from random import Random

mixed = Random()
allchars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-"_=+|\]}[{:;<>?/,.'

try:
 passwordLength = int(sys.argv[1])
except:
 passwordLength = 8 #Defaults at 8
try:
 number_of_passwords = int(sys.argv[2])
except:
 number_of_passwords = 1 #Defaults at 1

for i in range(number_of_passwords):
 for j in range(passwordLength):
  sys.stdout.write( mixed.choice(allchars) )
  
 sys.stdout.write("\n")
