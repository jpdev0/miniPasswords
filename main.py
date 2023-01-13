# import some libraries
import random

def passGen():
  # make some available password prefixes
  prefixes = ["tree", "apple", "pear", "orange", "bird", "branch", "cloud", "clouds", "blanket", "giant", "skeleton", "thing", "cat", "dog", "peach", "plums", "apricot", "button", "seat", "chair", "ocean", "breeze", "zombie", "plant", "seeds", "sprouts"]


  # make some middle numbers
  middleNumbers = str(random.randint(11111, 99999))

  # make some letter+symbol combinations
  middleLetters = ["!aA", "AzZ^", "FrQ%", "HsDG-Px", "RwWm$K", "hWK", "KmhHH#s", "RcVb@", "MmKyT_", "A&RnGjK", "XcW@3"]

  # make some suffix numbers
  suffixNumbers = str(random.randint(11, 999))

  # make some suffix symbols
  suffixSymbols = ["!", "@", "#", "$", "%", "^", "&", "*", "()", "-", "_", "+", "=", ":", "/", "<", ">"]

  newPass = str(random.choice(prefixes) + middleNumbers + random.choice(middleLetters) + suffixNumbers + random.choice(suffixSymbols))

  return newPass

inputForPass = input("A password is ready to be generated! Are you ready? (yes/no) : ")

if inputForPass == "yes":
  print("Here is your personal password : " + passGen())