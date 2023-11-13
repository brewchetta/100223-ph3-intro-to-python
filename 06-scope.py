##### Scope #####

# Global variables #

# JS:

# let name = "Bob the Raccoon"

name = "Bob the Raccoon"

# for (let i = 0; i < 5; i++) {
#   console.log(`Hello ${name}`)
# }



# for item in range(6):
#     print(name)

def say_hi_to_bob():
    print(f"Hello {name}")

# function sayHiToBob() {
#   console.log(`Hello ${name}`)
# }

# function changeName(newName) {
#   name = newName
# }

def change_name(new_name):
    global not_exists
    not_exists = new_name


# changeName("Rocket")

# console.log(name)



# Closure #

# JS:

# function speechGenerator(introduction) {
#   return function(speech) {
#     return `${introduction} ${speech}`
#   }
# }

# const fourScore = speechGenerator("Four score and seven years ago")

# const newSpeech = fourScore("something something speech goes here")

# console.log(newSpeech)

def outer_function():

    outer_var = "whatever"

    def inner_function():
        print(outer_var)

    return inner_function