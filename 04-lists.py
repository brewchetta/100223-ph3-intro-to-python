########### Lists ###########

# JS:
# const animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]
# console.log(animals)

animals = ["Aardvark", "Bobcat", "Cardinal", "Deer"]

# console.log(`First animal: ${animals[0]}`)

# animals.push("Elephant")
# console.log(animals)

animals.append("Elephant")

# animals.pop()
# console.log(animals)

animals.pop() # will remove the last item of the list

animals.pop(0) # will remove the first item of the list

# console.log(`There are ${animals.length} animals`)

print(f"There are { len(animals) } animals")

# const randomAnimal = animals[Math.floor(Math.random() * animals.length())]
# console.log(randomAnimal)

from random import choice
random_animal = choice(animals)

# const firstTwoAnimals = animals.slice(0, 2)
# console.log(`First two animals: ${firstTwoAnimals}`)

# const lastAnimal = animals[animals.length - 1]
# console.log(lastAnimal)

# function printEachAnimal() {
#     for (let i = 0; i < animals.length; i++) {
#         console.log( animals[i] )
#     }
# }

def print_each_animal():
    for animal_item in animals:
        print(animal_item)

# printEachAnimal()

# const animalsToLowerCase = animals.map( animal => animal.toLowerCase() )
# console.log(animalsToLowerCase)

lower_case_animals = [ animal_item.lower() for animal_item in animals ]

# also.... WHAT THE HECK IS A TUPLE???

my_tuple = ("Aardvark",) # <<-- a tuple ALWAYS needs a comma, even with one item

my_animals_tuple = ("Aardvark", "Bat", "Cat")