#CS175L
#Bryan Kahl
#CalculateAverage.py


def inputScores():
    total = 0
    count = 0
    score1 = int(input("Enter score 1: "))
    total = total + score1
    count = count +1
    score2 = int(input("Enter score 2: "))
    total = total + score2
    count = count +1
    score3 = int(input("Enter score 3: "))
    total = total + score3
    count = count +1
    score4 = int(input("Enter score 4: "))
    total = total + score4
    count = count +1
    score5 = int(input("Enter score 5: "))
    total = total + score5
    count = count +1
    return total,count,score1,score2,score3,score4,score5


def determine_grades(score):
    if score >=90 and score <=100:
        return ('A')
    elif score >= 80:
        return('B')
    elif score >= 70:
        return('C')
    elif score >= 60:
        return('D')
    else:
        return('F')

def calc_average(T,C):
    return T/C
   
    

def main():
    tot,ct,score1,score2,score3,score4,score5 = inputScores()
    print("Score          Numeric Grade  Letter Grade")
    print("-----------------------------------------------------")
    print('score 1:',score1,determine_grades(score1))
    print('score 2:',score2,determine_grades(score2))
    print('score 3:',score3,determine_grades(score3))
    print('score 4:',score4,determine_grades(score4))
    print('score 5:',score5,determine_grades(score5))
    avg = calc_average(tot,ct)
    print('Average Score:',(avg), determine_grades(avg))



    


main()
ask = True
while ask:
    ask_again = str(input("Would you like another calculation? "))

    if ask_again.lower() == 'yes' or ask_again.lower() == 'y':
        ask = True
        main()
    elif ask_again.lower() == 'no' or ask_again.lower() == 'n':
        ask = False
        print('Have a splendid day!')
        break
