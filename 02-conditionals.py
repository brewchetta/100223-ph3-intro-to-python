########### Conditionals ###########

# JS:
# let name = "Bob"

# if (name === "Bob") {
#     console.log("OMG it's Bob!")
# } else {
#     console.log(`Hello ${name} the raccoon`)
# }

name = "Bob"

if name == "Bob":
    print("OMG ITS BOB!!!!!!")
else:
    print(f"hello {name} the raccoon")

name = "Raphael"

if name == "Donatello" or name == "Raphael":
    print("Chowabunga dude!")
elif name == "Leonardo" or name == "Michelangelo":
    print("It's turtle time!")

# if (name === "Donatello" || name === "Raphael") {
#     console.log("Cowabunga dude!")
# } else if (name === "Leonardo" || name === "Michelangelo") {
#     console.log("It's turtle time!")
# }

# console.log("Free Pineapple Pizza on Tuesdays!")

# let weekday = "Tuesday"
# let myPizza = weekday === "Tuesday" ? "Pineapple Pizza" : "Pepperoni Pizza"

weekday = "Wednesday"

my_pizza = "Pineapple Pizza" if weekday == "Tuesday" else "Veggie Pizza"

my_pizza_with_wednesday = "Pineapple Pizza" if weekday == "Tuesday" else "Veggie Pizza" if weekday == "Wednesday" else "Pepperoni Pizza"