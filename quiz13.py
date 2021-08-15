import random

class QA:
  def __init__(self, question, correctAnswer, otherAnswers):
    self.question = question
    self.corrAnsw = correctAnswer
    self.otherAnsw = otherAnswers

qaList = [QA("Which is moon's average orbital speed?", "1,022 km/s", ["100 km/s", "5,44 km/s"]),
QA("Which is Pluto's average orbital speed?", "4,743 km/s", ["10,75 km/s", "1,022 km/s", "100 km/s"]),
QA("Which is Titan's average orbital speed?", "5,57 km/s", ["1 km/s", " 2,73 km/s", "10,49 km/s"]),
QA("Which is Cronus average orbital speed?", "9,69 km/s", ["5,22 km/s", "11,33 km/s"]),
QA("Which is Uranus average orbital speed?", "6,8 km/s", ["3,5 km/s", "2,99 km/s", "9,72 km/s", "1,33 km/s"])]

corrCount = 0
random.shuffle(qaList)
for qaItem in qaList:
  print(qaItem.question)
  print("Possible answers are:")
  possible = qaItem.otherAnsw + [qaItem.corrAnsw] # square brackets turn correct answer into list for concatenating with other list
  random.shuffle(possible)
  count = 0 # list indexes start at 0 in python
  while count < len(possible):
    print(str(count+1) + ": " + possible[count])
    count += 1
  print("Please enter the number of your answer:")
  userAnsw = input()
  while not userAnsw.isdigit():
    print("That was not a number. Please enter the number of your answer:")
    userAnsw = input()
  userAnsw = int(userAnsw)
  while not (userAnsw > 0 and userAnsw <= len(possible)):
    print("That number doesn't correspond to any answer. Please enter the number of your answer:")
    userAnsw = input()
  if possible[userAnsw-1] == qaItem.corrAnsw:
    print("Your answer was correct.")
    corrCount += 1
  else:
    print("Your answer was wrong.")
    print("Correct answer was: " + qaItem.corrAnsw)
  print("")

print("You answered " + str(corrCount) + " of " + str(len(qaList)) + " questions correctly.")
