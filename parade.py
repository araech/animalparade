import random

animals = ["aardvark", "actor", "adal", "baboon", "badger", "bear", "bee",
           "beetle", "black bear", "blogger", "bulldog", "bullfrog", "catfish",
           "centaur", "cheetah", "chicken", "chimp", "collie", "cow", "crab",
           "crane", "dachshund", "dancer", "deer", "dentist", "devil", "dingo",
           "doctor", "dodo", "dolphin", "donkey", "dormouse", "dragon", "duckling",
           "eagle", "emu", "erin", "falcon", "ferret", "fox", "frog", "gator",
           "gerbil", "goat", "goldfish", "goose", "gopher", "greyhound", "grizzly",
           "guppy", "hamster", "hornet", "human", "husband", "jackal", "jaguar",
           "japes", "kitty", "koala", "lady", "lemur", "leopard", "liger", "lion",
           "lizard", "llama", "lobster", "lynx", "magpie", "mandrill", "mastiff",
           "meerkat", "mister", "mole", "momo", "mongoose", "monkey", "moray",
           "mouse", "ostrich", "otter", "owl", "oyster", "panda", "panther",
           "parrot", "peacock", "penguin", "piggy", "pilot", "playwright",
           "plumber", "poet", "poodle", "puffin", "puzzbot", "rabbit", "raccoon",
           "ram", "rat", "reindeer", "rhino", "robot", "robin", "rodent", "sea cow",
           "shark", "sheep", "shih tzu", "shrimp", "singer", "skater", "skunk",
           "snail", "snake", "spaniel", "sparrow", "spider", "squid", "squirrel",
           "stagehand", "starfish", "tabby", "tapir", "termite", "tiger",
           "tortoise", "toucan", "tree frog", "turkey", "urchin", "vulture",
           "waiter", "walrus", "warthog", "weasel", "wife", "wolf", "woman",
           "wombat", "worm", "zebra", "android", "chunt", "hedgehog", "werewolf",
           "furry", "fanboy", "fangirl", "bobcat", "police horse", "cricket",
           "mallard"]

parades = ["axe to grind", "laptop", "taco", "shotglass", "problem", "hole in it",
           "apple pie", "ipod", "arts degree", "milk steak", "hagrid tat", "hangnail",
           "murder charge", "tophat", "pokemon", "monologue", "headband", "cola can",
           "tire iron", "plunger", "ipad", "pitchfork", "salad fork", "kumquot",
           "pear slice", "screenplay", "burglar mask", "grudge", "pizza", "lap dog",
           "yes man", "photograph", "shoelace", "sharpie", "paint brush", "pencil",
           "cd case", "hair tie", "cookie jar", "bucket", "tree stump", "bone to pick",
           "thing to say", "poor excuse", "sketchpad", "wagon", "cell phone", "piano",
           "bill to pay", "bad toupee", "glow stick", "bottle cap", "greeting card",
           "packing peanut", "nice bouquet", "carrot cake", "thermostat", "chill",
           "nasty cough", "maple leaf", "model car", "camera", "candy bar",
           "toothbrush", "hairbrush", "wii controller", "picture book", "helmet",
           "bracelet", "anklet", "rusty nail", "mustard stain", "mouse pad",
           "candelabra", "new blouse", "toilet roll", "shovel", "dental dam", "blanket",
           "tv show", "cardigan", "summer frock", "t-shirt", "bow tie", "tracksuit",
           "camisole", "cummerbund", "blazer", "rosebud", "tambourine", "banjo",
           "zither", "tuba", "bass guitar", "keyboard", "sad song", "oboe", "peony",
           "broomstick", "sweet pea", "heist to plan", "magic trick", "dance instructor",
           "podcast", "reason", "crossword", "noise complaint", "bird tattoo",
           "wedding dress", "laserdisc", "phonograph", "therapist", "tommy gun",
           "battle scar", "history", "pudding cup", "hand grenade", "attitude",
           "sugar daddy", "fear of heights", "leather kink", "aunt farm",
           "bag of trick", "valid point", "taste for blood", "need for speed",
           "pet rock", "skateboard", "backwards hat", "fortnite dance", "kettle on",
           "foster cat", "thing for cats", "haircut", "phantom limb", "murphy bed",
           "broken heart", "credit card", "bad romance", "neck brace"]

def get_article(word):
    if word[0] in ["a", "e", "i", "o", "u"]:
        return "an"
    else:
        return "a"

def animal_parade():
    animal = animals[random.randrange(len(animals))]
    parade = parades[random.randrange(len(parades))]
    phrase = '{} {} with {} {}'.format(get_article(animal), animal,
                                       get_article(parade), parade)
    return phrase.upper()
