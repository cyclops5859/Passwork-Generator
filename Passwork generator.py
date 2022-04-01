#created by cyclops!
import numbers
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbol = '!@#$%^&*'

x = lower+upper+number+symbol
length = 16
password = "".join(random.sample(x,length))
print (' ')
print (">>>", password, "<<<")
print (" ")
