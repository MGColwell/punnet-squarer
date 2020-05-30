#!/usr/bin/env python3
import sys,math

def main(argv):
  #print (argv) #comment/uncomment for debug

  if (len(sys.argv) < 2):
    print("Needs at least 1 arg, try help")
    exit()

  if (sys.argv[1] == "help"):
    print("Create a punnet square given two text strings")
    print("Usage: ./punnet.py <firststring> <secondstring>")
    print("Example: ./punnet.py AaBB AAbB")
    exit()

  if (len(sys.argv) != 3):
    print("Invalid number of arguments. Try help.")
    exit()

  if (len(sys.argv[1]) != len(sys.argv[2])):
    print("You cannot make a punnet square out of an unequal number of genes")
    exit()

  #generate gametes
  gametes1 = []
  gametes2 = []
  currgamete = ""
  counter = 0
  counter2 = 0
  #calculate how many gametes there'll be
  gamete_total = math.sqrt(2 ** (len(sys.argv[1])))
  #print (gamete_total) #comment/uncomment for debug
  trait_flip = []
  while (counter < len(sys.argv[1])):
    trait_flip.append(0)
    counter += 2
  counter = 0
  #print(len(trait_flip)) #comment/uncomment for debug
  trait_flip[0] = -1
  while (len(gametes1) < gamete_total):
    #move trait_flip forwards by one
    #I should reimplement this as a bitmask maybe because it's just binary counting
    print(len(gametes1))
    trait_flip[???] = ???
    #if (trait_flip[counter2] == 1):
    #  counter2 += 1
    #trait_flip[counter2] += 1
    counter = 0
    for trait in trait_flip:
      if (trait == 0):
        currgamete += (sys.argv[1][counter])
      else:
        currgamete += (sys.argv[1][counter+1])
      counter += 2
    gametes1.append(currgamete)
  print(gametes1) #comment/uncomment for debug
  exit()

  #prints first line
  print("   ", end = "")
  for gamete in gametes1:
    print(" | ", gamete, end = "")
  print(" ")

  #prints the rest
  for char2 in sys.argv[2]:
    print(" ",char2," ", end = "")
    for char in sys.argv[1]:
      print("| ", char, char2, " ", end = "", sep = "")
    print(" ")

main(sys.argv[1:])
