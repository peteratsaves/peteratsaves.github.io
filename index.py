#pip install GitPython

teams = ['Atlanta Hawks','Brooklyn Nets','Los Angeles Lakers','New York Knicks','Oklahoma City Thunder','Utah Jazz',
'Golden State Warriors','Houston Rockets','Milwaukee Bucks','Minnesota Timberwolves','Orlando Magic','Washington Wizards',
'Charlotte Hornets','Detroit Pistons','Indiana Pacers','Memphis Grizzlies','Miami Heat','Portland Trail Blazers',
'Cleveland Cavaliers','Los Angeles Clippers','Phoenix Suns','San Antonio Spurs','Sacramento Kings','Toronto Raptors',
'Boston Celtics','Chicago Bulls','Dallas Mavericks','Denver Nuggets','New Orleans Pelicans','Philadelphia 76ers']

overs = [36.5,19.5,42.5,53.5,57.5,27.5,43.5,42.5,49.5,51.5,47.5,19.5,31.5,25.5,46.5,46.5,43.5,20.5,
48.5,35.5,48.5,35.5,46.5,28.5,58.5,28.5,49.5,50.5,45.5,49.5]

over_under = ['Over','Under','Over','Over','Over','Under','Under','Over','Over','Over','Over','Under','Over','Over','Under',
'Over','Over','Over','Over','Under','Over','Under','Over','Under','Over','Over','Under','Over','Over','Over']

people = ['Alan','Alan','Alan','Alan','Alan','Alan','Emil','Emil','Emil','Emil','Emil','Emil','Eric','Eric','Eric','Eric',
'Eric','Eric','Josh','Josh','Josh','Josh','Josh','Josh','Peter','Peter','Peter','Peter','Peter','Peter']

wins = []
losses = []
projected_wins = []

for i in range(0,30):
    wins.append(0)
    losses.append(0)
    projected_wins.append(0)

import pandas as pd
df = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2025_standings.html')
for i in range(0,df[0].shape[0]):
    team = str(df[0]['Eastern Conference'][i])
    index1 = team.index('(')
    team = str(team[0:index1-1])
    team_index = teams.index(team)
    win = int(df[0]['W'][i])
    loss = int(df[0]['L'][i])
    wins[team_index] = win
    losses[team_index] = loss
    projected_wins[team_index] = round(82 * (win/(win + loss)))

for i in range(0,df[1].shape[0]):
    team = str(df[1]['Western Conference'][i])
    index1 = team.index('(')
    team = str(team[0:index1-1])
    team_index = teams.index(team)
    win = int(df[1]['W'][i])
    loss = int(df[1]['L'][i])
    wins[team_index] = win
    losses[team_index] = loss
    projected_wins[team_index] = round(82 * (win/(win + loss)))

with open('C:/Users/atsav/OneDrive/Desktop/peteratsaves/peteratsaves.github.io/index.js', 'w') as f:
    ##What changes and what must be passed into javascript
    f.write('"use strict";\n')
    f.write('let teams=' + str(teams) + ';\n')
    f.write('let overs=' + str(overs) + ';\n')
    f.write('let over_under=' + str(over_under) + ';\n')
    f.write('let people=' + str(people) + ';\n')
    f.write('let wins=' + str(wins) + ';\n')
    f.write('let losses=' + str(losses) + ';\n')
    f.write('let projected_wins=' + str(projected_wins) + ';\n')
    f.write('\n//Existing Javascript code below\n')

    ##Existing Javascript code, uses input to make output
    file2 = open('C:/Users/atsav/OneDrive/Desktop/peteratsaves/peteratsaves.github.io/index.txt', 'r')
    Lines = file2.readlines()

    for line in Lines:
        f.write(line)

##Automatically push to GitHub
import git 
repo = git.Repo('C:/Users/atsav/OneDrive/Desktop/peteratsaves/peteratsaves.github.io') 
origin = repo.remote(name='origin') 
  
existing_branch = repo.heads['main'] 
existing_branch.checkout() 

#file1 = 'C:/Users/atsav/OneDrive/Desktop/peteratsaves/peteratsaves.github.io/index.js'
file1 = r'C:\Users\atsav\OneDrive\Desktop\peteratsaves\peteratsaves.github.io\index.js'
repo.index.add([file1]) 
repo.index.commit('Update games and standings') 
origin.push() 