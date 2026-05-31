# Dictionary of English keys and Norwegian values
dict_nor = {
  # Nouns
  # Animals
  "cat": "katt",
  "dog": "hund",
  "horse": "hest",
  "bird": "fugl",
  "fish": "fisk",
  "wolf": "ulf",
  "whale": "hval",
  "shark": "hai",
  "elk": "elg",
  "salmon": "laks",
  "chicken": "kylling",
  "elk": "elg",

  # Food, drink
  "strawberry": "jordbær",
  "raspberry": "bringebær",
  "blueberry": "blåbær",
  "apple": "eple",
  "banana": "banan",
  "(an) orange": "appelsin",
  "vegetable": "grønnsak",
  "meat": "kjøtt",
  "chocolate": "sjokolade",
  "breakfast": "frokost",
  "lunch": "lunsj",
  "dinner": "middag",

  # People
  "girl": "jente",
  "boy": "gutt",
  "woman": "kvinne",
  "man": "mann",
  "friend": "venn",
  "child": "barn",
  "parent": "forelder",

  # Non-natural
  "car": "bil",
  "shop": "butikk",
  "house": "hus",
  "book": "bok",
  "newspaper": "avis",
  "fist": "neve",

  # Natural
  "earth": "jord",
  "sky": "himmel",
  "sea": "sjø",
  "ocean": "hav",
  "beach": "strand",
  "flower": "blomst",
  "tree": "tre",
  "snow": "snø",

  # Abstract
  "love": "kjærlighet",
  "year": "år",
  "day": "dag",
  "week": "uke",
  "hour": "time",
  "time": "tid",
  
  # Adjectives
  "red": "rød",
  "orange": "orange",
  "yellow": "gul",
  "green": "grønn",
  "blue": "blå",
  "purple": "lilla",
  "pink": "rosa",
  "black": "svart",
  "white": "hvit",
  "grey": "grå",
  "brown": "brun",
  "gold": "gull",
  "silver": "sølv",
  "hungry": "sulten",
  
  # Verbs
  "to use": "bruke",
  "to wish": "ønske",
  "to need": "trenge",
  "to make": "lage",
  "to run": "løpe",
  "to eat": "spise",
  "to know": "vite",
  "to mean": "betyr",
  "to care": "bry seg",
  "to answer": "svar",
  
  # Pronouns
  "I": "jeg",
  "me": "meg",
  "my": "mi/min/mitt",
  "you": "du/deg",
  "we": "vi",
  "us": "oss",
  "he": "han",
  "she": "hun",

  # Misc.
  "who": "hvem",
  "what": "hva",
  "when": "når",
  "where": "hvor",
  "why": "hvorfor",
  "how": "hvordan",
  "thanks": "takk",
  "maybe": "kanskje",
  "and": "og",
  "about": "om",
  "yes": "ja",
  "no": "nei",
  "hello": "hei",
  "goodbye": "ha det bra",
  "bye": "ha det"
}

# Set the current dictionary, split into lists of keys and values, find dictionary length
def dict_set(dict_choice):
  # Set the current dictionary
  dict_cur = dict_choice

  # Split into lists of keys and values
  keys_cur = list(dict_cur.keys())
  vals_cur = list(dict_cur.values())

  # Find dictionary length
  len_dict = len(dict_cur)
  return dict_cur, keys_cur, vals_cur, len_dict

dict_cur, keys_cur, vals_cur, len_dict = dict_set(dict_nor)

# Run the game
def game_cycle():
  def game_word():
    # Pick a random number in the range of the current dictionary
    import random
    rand_num = (random.randint(1, len_dict)) - 1

    # Find the key and value the random number
    rand_word = vals_cur[rand_num]
    rand_ans = keys_cur[rand_num]

    return rand_word, rand_ans

  rand_word, rand_ans = game_word()

  # Ask user for an answer, check it
  def get_check_ans():
    # Ask for input
    answer = input("What does '" + rand_word + "' mean? ").lower()

    # Check answer
    if answer == rand_ans:
      print("That's correct!\n")
    else:
      print("That's incorrect")
      print(rand_word.capitalize() + " means '" + rand_ans + "'\n")

  game_word()
  get_check_ans()

# Play the game
print("####################")
print("Welcome to Word-match!")

lets_play = ""

# Loop the game_cycle while user wants to play
def play_game(lets_play):
  while lets_play != "no":
    lets_play = input("Do you want to play? ").lower()
    if lets_play == "yes" or lets_play == "y":
      game_cycle()
    else:
      lets_play = "no"
      print("Maybe next time...")
      print("####################")

play_game(lets_play)