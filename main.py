#Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.
startnumber = int(input("Pick a starting number: "))
endnumber = int(input("Pick an ending number: "))
diff = int(input("Pick a number by which to count: "))
endnumber = endnumber + 1
for a in range(startnumber, endnumber, diff):
  print(a, end=" \n")


#Create a program that gets a message from the user and then prints it out backwards.
b = input('\nEnter a message: ')
print(b[::-1])


#Improve Word Jumble so that each word is paired with a hint. The player sees the hint if they are stuck. Add a scoring system that rewards players who solve a jumble without asking for a hint.
import random
WORDS = ("welkin", "oculus", "traveler", "waypoint", "desert", "abyss")
word = random.choice(WORDS)
correct = word
jumble = " "
hintwelkin = "This word means 'sky'."
hintoculus = "This word means 'a circular opening'."
hinttraveler = "A synonym of this word is 'wanderer'."
hintwaypoint = "This word helps travelers find their way and/or signifies a place of rest."
hintdesert = "This word describes the Sahara Desert."
hintabyss = "This word can be used to describe an ocean."
count = 0

while word:
  position = random.randrange(len(word))
  jumble += word[position]
  word = word[:position] + word[(position + 1):]
print("\nThe jumble is: ", jumble)
guess = input("Your guess: ")

while guess != correct and guess != " ":
  print("Wrong. Guess again.")
  guess == input("Your guess: ")
      
  if count == 0:
    hint = input("Would you like a hint? : ")
    if hint == "no":
      guess = input("Your guess: ")
    else:
      print("loading hint...")
      if correct == "welkin":
        print(hintwelkin)
        guess = input("Your guess: ")
        count += 1
      if correct == "oculus":
        print(hintoculus)
        guess = input("Your guess: ")
        count += 1
      if correct == "traveler":
        print(hinttraveler)
        guess = input("Your guess: ")
        count += 1
      if correct == "waypoint":
        print(hintwaypoint)
        guess = input("Your guess: ")
        count += 1
      if correct == "desert":
        print(hintdesert)
        guess = input("Your guess: ")
        count += 1
      if correct == "abyss":
        print(hintabyss)
        guess = input("Your guess: ")
        count += 1

if guess == correct:
  print("You got it!")
  print("Thanks for playing!")