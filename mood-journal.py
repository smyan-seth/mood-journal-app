from datetime import date
entry=input('How was your day?\n')
mood=int(input('How is your mood today on a scale of 1-10?\n1 being the worst, 10 being amazing: '))
with open('journal.txt','a') as journal:
    journal.write(f"Date: {date.today()}\nEntry: {entry}\nMood: {mood}\n{'-'*20}\n")
print('Entry recorded')