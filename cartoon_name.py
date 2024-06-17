import random

# Assuming you have a file 'adjectives.txt' with one adjective per line
with open('adjectives.txt') as f:
    adjectives = [line.strip() for line in f.readlines()]

animals = [

    "Penguin", "Koala", "Raccoon", "Sloth", "Unicorn", "Aardvark", "Albatross", "Alligator", "Alpaca", "Antelope",

    "Armadillo", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee", "Bison", "Blackbird", "Boa", "Boar",

    "Buffalo", "Butterfly", "Camel", "Caribou", "Cassowary", "Cat", "Caterpillar", "Cheetah", "Chimpanzee", "Chinchilla",

    "Cobra", "Cockatoo", "Coyote", "Crab", "Crane", "Crocodile", "Crow", "Deer", "Dingo", "Dolphin", "Donkey",

    "Dragonfly", "Duck", "Eagle", "Eel", "Elephant", "Emu", "Falcon", "Ferret", "Finch", "Flamingo", "Fox", "Frog",

    "Gazelle", "Gecko", "Giraffe", "Goat", "Goose", "Gorilla", "Grasshopper", "Guinea Pig", "Hamster", "Hare", "Hawk",

    "Hedgehog", "Heron", "Hippopotamus", "Hornet", "Horse", "Hummingbird", "Hyena", "Ibex", "Ibis", "Iguana", "Jackal",

    "Jaguar", "Jellyfish", "Kangaroo", "Kingfisher", "Kiwi", "Komodo Dragon", "Lemur", "Leopard", "Llama", "Lobster",

    "Lynx", "Macaw", "Magpie", "Manatee", "Mandrill", "Meerkat", "Mole", "Mongoose", "Monkey", "Moose", "Mosquito",

    "Narwhal", "Newt", "Nightingale", "Octopus", "Okapi", "Opossum", "Orangutan", "Ostrich", "Otter", "Owl", "Ox",

    "Panda", "Panther", "Parrot", "Peacock", "Pelican", "Pheasant", "Platypus", "Porcupine", "Possum", "Prairie Dog",

    "Pufferfish", "Puma", "Quail", "Quokka", "Rabbit", "Rattlesnake", "Reindeer", "Rhino", "Robin", "Salamander",

    "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Skunk", "Snail", "Snake", "Sparrow", "Spider", "Squirrel",

    "Starfish", "Stork", "Swan", "Tapir", "Tarantula", "Tasmanian Devil", "Termite", "Tiger", "Toad", "Toucan", "Turtle",

    "Viper", "Vulture", "Wallaby", "Walrus", "Warthog", "Wasp", "Weasel", "Whale", "Wildcat", "Wolf", "Wolverine",

    "Wombat", "Woodpecker", "Worm", "Yak", "Zebra", "Zebu"

]


modifiers = [
    lambda x: x + 'o',

    lambda x: x + '-' + x,
    lambda x: x,
]

def generate_cartoon_name():
    adjective = random.choice(adjectives)
    animal = random.choice(animals)
    modifier = random.choice(modifiers)
    
    name = f"{modifier(adjective)} {animal}"
    return name

print(generate_cartoon_name())