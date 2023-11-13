########### Variables ###########

# JS:
# let name = "Bob"
# console.log(name)

name = "Bob"
print(name)

# let species = "Raccoon"
# console.log(species)

species = "Raccoon"
print(species)

# let rabid = false
# console.log(rabid)

rabid = False

# name = `Bob the ${species}`
# console.log(name)

name = f"Bob the {species}"

# let numberOfRaccoonsInNYC = "300"
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )

number_of_raccoons_in_nyc = "300"
print(f"there are {number_of_raccoons_in_nyc} raccoons in NYC")

# numberOfRaccoonsInNewYork = parseInt( numberOfRaccoonsInNewYork )

number_of_raccoons_in_nyc = int(number_of_raccoons_in_nyc)

# numberOfRaccoonsInNewYork += 1
# console.log( `number of raccoons in NYC: ${numberOfRaccoonsInNewYork}` )

# const minutesPerHour = 60
# minutesPerHour = 55 // in JS this will break!
# console.log(minutesPerHour)

MINUTES_PER_HOUR = 60 # <<-- this is how we let other devs know this is a constant, we can still technically change it though!