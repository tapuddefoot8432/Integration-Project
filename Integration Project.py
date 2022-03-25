#My name is Toby Puddefoot
#This program is meant to guess the users rank in rocket league based on
#their reponse to some questions
rank1 = "Bronze 1"
rank2 = "Bronze 2"
rank3 = "Bronze 3"
rank4 = "Silver 1"
rank5 = "Silver 2"
rank6 = "Silver 3"
rank7 = "Gold 1"
rank8 = "Gold 2"
rank9 = "Gold 3"
rank10 = "Platinum 1"
rank11 = "Platinum 2"
rank12 = "Platinum 3"
rank13 = "Diamond 1"
rank14 = "Diamond 2"
rank15 = "Diamond 3"
rank16 = "Champion 1"
rank17 = "Champion 2"
rank18 = "Champion 3"
rank19 = "Grand Champion 1"
rank20 = "Grand Champion 2"
rank21 = "Grand Champion 3"
rank22 = "Supersonic Legend"
#The variables above are all the ranks in rocket league.
print("Hello " * 3)
name = ""
while not name:
    name = input("What is your name?")
print("Nice to meet you", name)
print("my name is Toby Puddefoot.")
print("I'm going to ask you some questions to determine your rank on Rocket League.")
#All of the introducing code and explaining to the user what the program does.
assists = input("How many assists do you average per game? ")
assists1 = float(assists)
goals = input("How many goals do you average per game? ")
goals1 = float(goals)
saves = input("How many saves do you average per game? ")
saves1 = float(saves)
per_game = (assists1 * 50 + goals1 * 100 + saves1 * 50)
#User inputs how many assists, goals and saves they average and the program
#tells them the amount of points they average.
if per_game != 0:
    print("Wow, you're talented!")
print("For example if you averaged 2 of each you would average:",20 ** 2)
print("Your average score per game: ", format(per_game, "0.2f"), sep='')
print("Your average score minute:",per_game / 5)
print("Your average score from assists per minute:",assists1 * 50 // 5)
print("Your average score from goals per minute:",goals1 * 100 // 5)
print("Your average score from saves per minute:",saves1 * 50 // 5)
print("Your average remainder of score:",per_game % 5)
print("Your average score without saves:",goals1 * 100 + assists1 * 50 + saves1 - saves1)
flip_resets = input("Can you consistantly do a flip reset?")
if flip_resets == "yes":
    print("Good Job!")
else:
    print("Keep practicing!")
hours = int(input("How many hours do you have?"))
for i in range(0,1):
    print("Interesting!")
def hours_daily(hours2):
    print("How many hours a week you spend on Rocket League:", hours2 * 7)
def main():
    hours2 = int(input("On average how many hours do you play per day?:"))
    hours_daily(hours2)
main()
#The code above asks the user questions to determine their rank.
if hours <= 10 or hours <= 20:
    print("Your rank:", rank1)
elif hours <= 20:
    print("Your rank:", rank2)
elif hours <= 30:
    print("Your rank:", rank3)
elif hours <= 40:
    print("Your rank:", rank4)
elif hours <= 50:
    print("Your rank:", rank5)
elif hours <= 75:
    print("Your rank:", rank6)
elif hours <= 90:
    print("Your rank:", rank7)
elif hours <= 100:
    print("Your rank:", rank8)
elif hours <= 115:
    print("Your rank:", rank9)
elif hours <= 125:
    print("Your rank:", rank10)
elif hours <= 150:
    print("Your rank:", rank11)
elif hours <= 175:
    print("Your rank:", rank12)
elif hours <= 200:
    print("Your rank:", rank13)
elif hours <= 250:
    print("Your rank:", rank14)
elif hours <= 300:
    print("Your rank:", rank15)
elif hours <= 400:
    print("Your rank:", rank16)
elif hours <= 1000:
    print("Your rank:", rank17)
elif hours <= 1500:
    print("Your rank:", rank18)
elif hours <= 2500:
    print("Your rank:", rank19)
elif hours <= 3500 and flip_resets == "yes":
    print("Your rank:", rank20)
elif hours <= 4400 and flip_resets == "yes":
    print("Your rank:", rank21)
elif hours > 4400 and flip_resets == "yes":
    print("Your rank:", rank22)
#This is all the code that determines and prints the rank.
