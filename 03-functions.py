########### Functions ###########

# JS:
# function doStuff() {
#   return "This function does stuff!"
# }

def do_stuff():
    return "This function does stuff"

# console.log( doStuff() )

# function addition(x,y) {
#   return x + y
# }

def addition(x,y):
    return x + y

# console.log( addition(1,2) )
# console.log( addition("3", 4) )
# console.log( addition(5.6, 7) )

# let name = "Bob"

# function sayHiBob() {
#   return `Hello ${name}`
# }

name = "Bob"

def say_hi_bob():
    return f"Hello {name}"

# console.log( sayHiBob() )

# function countdown(number) {
#   let i = number
#   while (i > 0) {
#     console.log(i)
#     i -= 1
#   }
#   console.log('HAPPY NEW YEAR!')
# }

from time import sleep

def countdown(number=10):
    i = number
    while i > 0:
        print(i)
        i -= 1
        sleep(1)
    print("Happy new year")