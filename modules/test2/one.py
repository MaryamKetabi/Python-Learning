import two

################

import test

################

import two
two.say_sth_to_users()
two.names

################

from two import say_sth_to_users
say_sth_to_users()

################

from two import names
print(names)

################

from two import say_sth_to_users as greet
greet()

################

from two import *

print(names)
print(number)
say_sth_to_users()