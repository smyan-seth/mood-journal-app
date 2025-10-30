from datetime import date
def getMoods():
    moods=[]
    try:
        with open('journal.txt','r') as f:
            lines=f.readlines()
            for line in lines:
                if "Mood:" in line:
                    temp=line.split(':')
                    temp=int(temp[1])
                    moods.append(temp)
    except FileNotFoundError:
        return -1
    return moods

print('-'*20+'Welcome to Journal'+'-'*20)

entry=input('How was your day?\n')
mood=int(input('How is your mood today on a scale of 1-10?\n1 being the worst, 10 being amazing: '))
with open('journal.txt','a') as journal:
    journal.write(f"Date: {date.today()}\nEntry: {entry}\nMood: {mood}\n{'-'*20}\n")
moods=getMoods()
noOfEntries=len(moods)
avgMood=sum(moods)/len(moods)
print(f'Entry recorded, you have written {noOfEntries} times.\nAverage mood {avgMood}')

                




    