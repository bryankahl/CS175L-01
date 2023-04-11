x = open('WorldSeriesWinners.txt','r')

team_winners = []

for i in x:
    i = i.rstrip('\n')
    team_winners.append(i)


def function():
    b = True
    while b:
        number_of_wins = 0

        enter_team = input('Enter the name of a team: ')

        team = []

        search = [line for line in x if enter_team.lower() in line.lower()]

        for i in search:
            if i not in team:
                team.append(i)

        for line in team:
            print(line)
            number_of_wins += 1

        better_counter = 0

        specific_team = input('Enter the name of the team you would like to focus on: ')

        y = open('WorldSeriesWinners.txt','r')

    

        for line in y:
            line = line.rstrip('\n')
            if specific_team.lower() in line.lower():
                better_counter += 1


        print(f"\nThe team '{specific_team}' appears {better_counter} times between 1903 and 2009")
        a = True
        while a:
            question = input('Do you want to keep inputing teams? (input y/n)')
            if question == 'n':
               print('Code has ended!')
               a = False
               b = False
               break
            else:
                function()

function()
            
    
    
    
