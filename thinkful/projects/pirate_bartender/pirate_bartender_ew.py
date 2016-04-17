import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

verbs = ["Fightin'", "Brawlin'","Wailin'","Sailin'"]

nouns = ["Whale", "Captain", "Treasure", "Dutchman"]

def get_answers ():
  answers = {}
  for flavor, question in questions.items():
    print (question)
    answers[flavor] = input().lower() in ["y", "yes"]
    print ("")
  return (answers)
 
def get_drink(answers):
  drink = []
  for alcohol, yes in answers.items():
    if not yes:
      continue
    drink.append(random.choice(ingredients[alcohol]))
  return (drink)

def main():
  answers = get_answers()
  drink = get_drink(answers)
  print ("Here is the drink. It contains:")
  for ingredient in drink:
    print ("A {}".format(ingredient))
  print ("This drink's name is:")
  print (random.choice(verbs) + " " + random.choice(nouns))

if __name__ == "__main__":
  main()
