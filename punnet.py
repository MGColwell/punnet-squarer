#!/usr/bin/env python3
import sys,math

def mergegametes(gam1, gam2):
  #print(gam1,gam2) #comment/uncomment for debug
  gamete = ""
  counter = 0
  while (counter < len(gam1)):
    gamete += gam1[counter]
    gamete += gam2[counter]
    counter += 1
  #print(gamete) #comment/uncomment for debug
  return gamete

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
  trait_flip[-1] = -1
  while (len(gametes1) < gamete_total):
    #move trait_flip forwards by one
    #I should reimplement this as a bitmask maybe because it's just binary counting
    #print(len(gametes1))
    counter2 = len(trait_flip) - 1
    trait_flip[counter2] += 1
    while(counter2 > 0):
      if (trait_flip[counter2] == 2):
        trait_flip[counter2] = 0
        trait_flip[counter2 - 1] += 1
      else:
        break
      counter2 -= 1
    counter = 0
    #print(trait_flip) #comment/uncomment for debug
    for trait in trait_flip:
      if (trait == 0):
        currgamete += (sys.argv[1][counter])
      else:
        currgamete += (sys.argv[1][counter+1])
      counter += 2
    #print(currgamete) #comment/uncomment for debug
    gametes1.append(currgamete)
    currgamete = ""
  counter = 0
  counter3 = 0
  while (counter < len(sys.argv[1])):
    trait_flip[counter3] = 0
    counter += 2
    counter3 += 1
  counter = 0
  trait_flip[-1] = -1
  while (len(gametes2) < gamete_total):
    counter2 = len(trait_flip) - 1
    trait_flip[counter2] += 1
    while(counter2 > 0):
      if (trait_flip[counter2] == 2):
        trait_flip[counter2] = 0
        trait_flip[counter2 - 1] += 1
      else:
        break
      counter2 -= 1
    counter = 0
    for trait in trait_flip:
      if (trait == 0):
        currgamete += (sys.argv[2][counter])
      else:
        currgamete += (sys.argv[2][counter+1])
      counter += 2
    gametes2.append(currgamete)
    currgamete = ""

  #prints first line

  print(" " * (len(gametes1[0])+2), end = "")
  print("|  ", end = "")
  for gamete in gametes1:
    print(gamete, "  |  ", end = "")
  print(" ")

  #prints the rest
  for gamete2 in gametes2:
    print("",gamete2, end = "")
    #print("gamete2") #comment/uncomment for debug
    for gamete in gametes1:
      print(" | ", end = "")
      print(mergegametes(gamete,gamete2), end = "")
    print(" ")

main(sys.argv[1:2])
