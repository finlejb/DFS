from bs4 import BeautifulSoup
import urllib.request
import os, numpy, csv, requests, operator, time, datetime, multiprocessing
import pandas as pd
import itertools as it

from lxml import html

# print("Is today's salary file saved? (Today DK Salaries.csv)")
# wait = input('PRESS ENTER TO CONTINUE.')

# start = time.time()

all_teams = ['Ari', 'Atl', 'Bal', 'Bos', 'ChC', 'Cin', 'Cle', 'Col', 'CWS', 'Det', 'Hou', 'KC', 'LAA', 'LAD', 'Mia', 'Mil', 'Min', 'NYM', 'NYY', 'Oak', 'Phi', 'Pit', 'SD', 'Sea', 'SF', 'Stl', 'TB', 'Tex', 'Tor', 'Was']
all_teams2 = ['Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Chicago White Sox', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'Seattle Mariners', 'San Francisco Giants', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']

#-------------------------------------------------------------------------#
#DELETE FILES FROM PREVIOUS RUNS
#-------------------------------------------------------------------------#

print('Deleting old files from previous runs...')

old_csv_file_list = ['List of Todays Games',
                 'Affordable Rosters',
                 'Available Player Pool',
                 'Probable Pitchers',
                 'BP Scraped Batting vs RHP',
                 'BP Scraped Batting vs LHP']

for n in range(len(old_csv_file_list)):
    try:
        os.remove(old_csv_file_list[n]+'.csv')
    except FileNotFoundError: continue
               
position_list = ['C', '1B', '2B', '3B', 'SS', 'OF', 'Pitchers']

for n in range(len(position_list)):
    try:
        os.remove('Salaries ('+str(position_list[n])+').csv')
    except FileNotFoundError: continue

for n in range(len(all_teams)):
    try:
        os.remove(str(all_teams2[n])+' Lineup.csv')
    except FileNotFoundError: continue

try:
    os.remove('Lineup Page html.txt')
except FileNotFoundError: pass

#-------------------------------------------------------------------------#
#GET BATTER STATISTICS VERSUS LHPs
#-------------------------------------------------------------------------#

print('Getting batting statistics vs LHPs...')

url = 'http://www.baseballprospectus.com/sortable/index.php?cid=1920411'
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

names = []
games = []
pas = []
ABs = [] #have to capitalize because abs is already a function
runs = []
hits = []
singles = []
doubles = []
triples = []
homeruns = []
tbs = []
sos = []
bbs = []
hbps = []
sfs = []
shs = []
rbis = []
dps = []
fb_pcts = []
gb_pcts = []
ld_pcts = []
pop_pcts = []
isos = []
avgs = []
obps = []
slgs = []
TAvs = []

table = soup.find("table", {"id": "TTdata"}, {"class": "TTdata"})

for row in table.findAll('tr'):
    cells = row.findAll("td")
    name = cells[1].text
    game = cells[4].text
    pa = cells[5].text
    ab = cells[6].text
    run = cells[7].text
    hit = cells[8].text
    single = cells[9].text
    double = cells[10].text
    triple = cells[11].text
    homerun = cells[12].text
    tb = cells[13].text
    so = cells[14].text
    bb = cells[15].text
    hbp = cells[16].text
    sf = cells[17].text
    sh = cells[18].text
    rbi = cells[19].text
    dp = cells[20].text
    fb_pct = cells[21].text
    gb_pct = cells[22].text
    ld_pct = cells[23].text
    pop_pct = cells[24].text
    iso = cells[25].text
    avg = cells[26].text
    obp = cells[27].text
    slg = cells[28].text
    TAv = cells[29].text

    names.append(name)
    games.append(game)
    pas.append(pa)
    ABs.append(ab)
    runs.append(run)
    hits.append(hit)
    singles.append(single)
    doubles.append(double)
    triples.append(triple)
    homeruns.append(homerun)
    tbs.append(tb)
    sos.append(so)
    bbs.append(bb)
    hbps.append(hbp)
    sfs.append(sf)
    shs.append(sh)
    rbis.append(rbi)
    dps.append(dp)
    fb_pcts.append(fb_pct)
    gb_pcts.append(gb_pct)
    ld_pcts.append(ld_pct)
    pop_pcts.append(pop_pct)
    isos.append(iso)
    avgs.append(avg)
    obps.append(obp)
    slgs.append(slg)
    TAvs.append(TAv)

everything = []
everything.append(names)
everything.append(games)
everything.append(pas)
everything.append(ABs)
everything.append(runs)
everything.append(hits)
everything.append(singles)
everything.append(doubles)
everything.append(triples)
everything.append(homeruns)
everything.append(tbs)
everything.append(sos)
everything.append(bbs)
everything.append(hbps)
everything.append(sfs)
everything.append(shs)
everything.append(rbis)
everything.append(dps)
everything.append(fb_pcts)
everything.append(gb_pcts)
everything.append(ld_pcts)
everything.append(pop_pcts)
everything.append(isos)
everything.append(avgs)
everything.append(obps)
everything.append(slgs)
everything.append(TAvs)

# TRANSPOSE ROWS AND COLUMNS
everything = numpy.transpose(everything)

# WRITE CSV WITH ALL DATA
imported_csv = open(os.path.join('BP Scraped Batting vs LHP.csv'), 'w', newline='')
csvWriter = csv.writer(imported_csv)
for row in everything:
    csvWriter.writerow(row)
imported_csv.close()

#-------------------------------------------------------------------------#
#GET BATTER STATISTICS VERSUS RHPs
#-------------------------------------------------------------------------#

print('Getting batting statistics vs RHPs...')

url = 'http://www.baseballprospectus.com/sortable/index.php?cid=1920412'
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

names = []
games = []
pas = [] 
ABs = [] #have to capitalize because abs is already a function
runs = []
hits = []
singles = []
doubles = []
triples = []
homeruns = []
tbs = []
sos = []
bbs = []
hbps = []
sfs = []
shs = []
rbis = []
dps = []
fb_pcts = []
gb_pcts = []
ld_pcts = []
pop_pcts = []
isos = []
avgs = []
obps = []
slgs = []
TAvs = []

table = soup.find("table", {"id": "TTdata"}, {"class": "TTdata"})
for row in table.findAll('tr'):
    cells = row.findAll("td")
    name = cells[1].text
    game = cells[4].text
    pa = cells[5].text
    ab = cells[6].text
    run = cells[7].text
    hit = cells[8].text
    single = cells[9].text
    double = cells[10].text
    triple = cells[11].text
    homerun = cells[12].text
    tb = cells[13].text
    so = cells[14].text
    bb = cells[15].text
    hbp = cells[16].text
    sf = cells[17].text
    sh = cells[18].text
    rbi = cells[19].text
    dp = cells[20].text
    fb_pct = cells[21].text
    gb_pct = cells[22].text
    ld_pct = cells[23].text
    pop_pct = cells[24].text
    iso = cells[25].text
    avg = cells[26].text
    obp = cells[27].text
    slg = cells[28].text
    TAv = cells[29].text

    names.append(name)
    games.append(game)
    pas.append(pa)
    ABs.append(ab)
    runs.append(run)
    hits.append(hit)
    singles.append(single)
    doubles.append(double)
    triples.append(triple)
    homeruns.append(homerun)
    tbs.append(tb)
    sos.append(so)
    bbs.append(bb)
    hbps.append(hbp)
    sfs.append(sf)
    shs.append(sh)
    rbis.append(rbi)
    dps.append(dp)
    fb_pcts.append(fb_pct)
    gb_pcts.append(gb_pct)
    ld_pcts.append(ld_pct)
    pop_pcts.append(pop_pct)
    isos.append(iso)
    avgs.append(avg)
    obps.append(obp)
    slgs.append(slg)
    TAvs.append(TAv)

everything = []
everything.append(names)
everything.append(games)
everything.append(pas)
everything.append(ABs)
everything.append(runs)
everything.append(hits)
everything.append(singles)
everything.append(doubles)
everything.append(triples)
everything.append(homeruns)
everything.append(tbs)
everything.append(sos)
everything.append(bbs)
everything.append(hbps)
everything.append(sfs)
everything.append(shs)
everything.append(rbis)
everything.append(dps)
everything.append(fb_pcts)
everything.append(gb_pcts)
everything.append(ld_pcts)
everything.append(pop_pcts)
everything.append(isos)
everything.append(avgs)
everything.append(obps)
everything.append(slgs)
everything.append(TAvs)

# TRANSPOSE ROWS AND COLUMNS
everything = numpy.transpose(everything)

# WRITE CSV WITH ALL DATA
imported_csv = open(os.path.join('BP Scraped Batting vs RHP.csv'), 'w', newline='')
csvWriter = csv.writer(imported_csv)
for row in everything:
    csvWriter.writerow(row)
imported_csv.close()

#-------------------------------------------------------------------------#
#GET PROBABLE PITCHERS FOR TODAY
#-------------------------------------------------------------------------#

print("Getting today's probable pitchers...")

page = pd.read_html('http://www.fantasypros.com/mlb/probable-pitchers.php')[0]
page = page.values # convert dataframes to numpy array

numpy.savetxt('Probable Pitchers.csv', page, delimiter = ',', fmt = '%s') # write to csv

# Delete all columns except today's pitchers

pitchers_csv = open('Probable Pitchers.csv', 'r')
pitchers = csv.reader(pitchers_csv)
pitchers = list(pitchers)

for row in pitchers:
    del row[7]
    del row[6]
    del row[5]
    del row[4]
    del row[3]
    del row[2]

for row in pitchers:
    row[0], row[1] = row[1], row[0]

fixedPitchers = []
teams = []

for row in pitchers:
    teams.append(row[1])

for row in pitchers:
    a = row[0].strip('@')
    b = a.split('(')
    if b[0][0:2] == ('TB'): c = (b[0][2:])
    elif b[0][0:2] == ('KC'): c = (b[0][2:])
    elif b[0][0:2] == ('SD'): c = (b[0][2:])
    elif b[0][0:2] == ('SF'): c = (b[0][2:])
    else: c = (b[0][3:])
    fixedPitchers.append(c)

combined = []

for n in range(len(fixedPitchers)):
    a = [fixedPitchers[n], teams[n]]
    combined.append(a)

for row in combined:
    if row[1] == 'Arizona':
        row[1] = 'Ari'
    if row[1] == 'Atlanta':
        row[1] = 'Atl'
    if row[1] == 'Baltimore':
        row[1] = 'Bal'
    if row[1] == 'Boston':
        row[1] = 'Bos'
    if row[1] == 'Chicago':
        row[1] = 'ChC/CWS'
    if row[1] == 'Cincinnati':
        row[1] = 'Cin'
    if row[1] == 'Cleveland':
        row[1] = 'Cle'
    if row[1] == 'Colorado':
        row[1] = 'Col'
    if row[1] == 'Detroit':
        row[1] = 'Det'
    if row[1] == 'Houston':
        row[1] = 'Hou'
    if row[1] == 'Kansas City':
        row[1] = 'KC'
    if row[1] == 'Los Angeles':
        row[1] = 'LAD/LAA'
    if row[1] == 'Miami':
        row[1] = 'Mia'
    if row[1] == 'Milwaukee':
        row[1] = 'Mil'
    if row[1] == 'Minnesota':
        row[1] = 'Min'
    if row[1] == 'New York':
        row[1] = 'NYY/NYM'
    if row[1] == 'Oakland':
        row[1] = 'Oak'
    if row[1] == 'Philadelphia':
        row[1] = 'Phi'
    if row[1] == 'Pittsburgh':
        row[1] = 'Pit'
    if row[1] == 'San Diego':
        row[1] = 'SD'
    if row[1] == 'Seattle':
        row[1] = 'Sea'
    if row[1] == 'San Francisco':
        row[1] = 'SF'
    if row[1] == 'St. Louis':
        row[1] = 'Stl'
    if row[1] == 'Tampa Bay':
        row[1] = 'TB'
    if row[1] == 'Texas':
        row[1] = 'Tex'
    if row[1] == 'Toronto':
        row[1] = 'Tor'
    if row[1] == 'Washington':
        row[1] = 'Was'

# re-write csv with just the pitchers for today

imported_csv = open(os.path.join('Probable Pitchers.csv'), 'w', newline = '')
csvWriter = csv.writer(imported_csv)
for row in combined:
    csvWriter.writerow(row)
imported_csv.close()

pitchers_csv = open('Probable Pitchers.csv', 'r')
pitchers = csv.reader(pitchers_csv)
pitchers = list(pitchers)

pitchers2 = []
for row in pitchers:
    if row[0] != '':
        pitchers2.append(row)

imported_csv = open(os.path.join('Probable Pitchers.csv'), 'w', newline = '')
csvWriter = csv.writer(imported_csv)
for row in pitchers2:
    csvWriter.writerow(row)
imported_csv.close()

'''

#-------------------------------------------------------------------------#
#SORT SALARIES
#-------------------------------------------------------------------------#

imported_csv = open('Today DK Salaries.csv', 'r')
imported_data = csv.reader(imported_csv)

csvRows = []
output_rows = []

# REMOVE THE HEADER FROM THE IMPORTED CSV FILE
for row in imported_data:
    if imported_data.line_num == 1:
        continue #skip first row (headers)
    csvRows.append(row)

# DELETE SOME COLUMNS THAT WE DON'T CARE ABOUT
for row in csvRows:
    del row[4]

# WRITE NEW CSV FILE WITHOUT THE HEADER
imported_csv = open(os.path.join('no header.csv'), 'w', newline='')
csvWriter = csv.writer(imported_csv)
for row in csvRows:
    csvWriter.writerow(row)
imported_csv.close()

# WRITE CSV OF PITCHER SALARIES
pitcherRows = []
p = open('no header.csv','r')
p_salaries = csv.reader(p, delimiter=',')
for row in p_salaries:
    if row[0] == 'SP':
        pitcherRows.append(row)
    elif row[0] == 'RP':
        pitcherRows.append(row)
p.close()
    
p = open(os.path.join('Salaries (Pitchers).csv'), 'w', newline='')
csvWriter = csv.writer(p)
for row in pitcherRows:
    csvWriter.writerow(row)
p.close()

# WRITE CSV OF 1st BASE SALARIES
FirstBaseRows = []
first = open('no header.csv','r')
first_salaries = csv.reader(first, delimiter=',')
for row in first_salaries:
    if '1B' in row[0]:
        FirstBaseRows.append(row)
first.close()

first = open(os.path.join('Salaries (1B).csv'), 'w', newline='')
csvWriter = csv.writer(first)
for row in FirstBaseRows:
    csvWriter.writerow(row)
first.close()

# WRITE CSV OF 2nd BASE SALARIES
SecondBaseRows = []
second = open('no header.csv','r')
second_salaries = csv.reader(second, delimiter=',')
for row in second_salaries:
    if '2B' in row[0]:
        SecondBaseRows.append(row)
second.close()

second = open(os.path.join('Salaries (2B).csv'), 'w', newline='')
csvWriter = csv.writer(second)
for row in SecondBaseRows:
    csvWriter.writerow(row)
second.close()

# WRITE CSV OF 3rd BASE SALARIES
PositionRows = []
position = open('no header.csv','r')
position_salaries = csv.reader(position, delimiter=',')
for row in position_salaries:
    if '3B' in row[0]:
        PositionRows.append(row)
position.close()

position = open(os.path.join('Salaries (3B).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in PositionRows:
    csvWriter.writerow(row)
position.close()

# WRITE CSV OF SS SALARIES
PositionRows = []
position = open('no header.csv','r')
position_salaries = csv.reader(position, delimiter=',')
for row in position_salaries:
    if 'SS' in row[0]:
        PositionRows.append(row)
position.close()

position = open(os.path.join('Salaries (SS).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in PositionRows:
    csvWriter.writerow(row)
position.close()

# WRITE CSV OF CATCHER SALARIES
PositionRows = []
position = open('no header.csv','r')
position_salaries = csv.reader(position, delimiter=',')
for row in position_salaries:
    if 'C' in row[0]:
        PositionRows.append(row)
position.close()

position = open(os.path.join('Salaries (C).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in PositionRows:
    csvWriter.writerow(row)
position.close()

# WRITE CSV OF OUTFIELD SALARIES
PositionRows = []
position = open('no header.csv','r')
position_salaries = csv.reader(position, delimiter=',')
for row in position_salaries:
    if 'OF' in row[0]:
        PositionRows.append(row)
position.close()

position = open(os.path.join('Salaries (OF).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in PositionRows:
    csvWriter.writerow(row)
position.close()

# SPLIT THE ROWS IN THE PITCHERS SALARY FILE
imported_csv = open('Salaries (Pitchers).csv', 'r')
pitchers = csv.reader(imported_csv)
pitchers = list(pitchers)
games_list = []

for row in pitchers:
    a = row[3]
    games_list.append(a)

games_list2 = []
for row in games_list:
    a = row.split('@')
    games_list2.append(a)

games_list3 = []
for row in games_list2:
    a = row[1].split(' ')
    games_list3.append(a)

for row in games_list3:
    del row[2]
    del row[1]

for row in pitchers:
    del row[3]

for row in games_list2:
    del row[1]

away_teams = games_list2
home_teams = games_list3
combined = []

if len(home_teams) == len(pitchers):
    for n in range(len(pitchers)):
        a = pitchers[n], away_teams[n][0], '@', home_teams[n][0]
        combined.append(a)

position = open(os.path.join('Salaries (Pitchers).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in combined:
    csvWriter.writerow((row[0][0], row[0][1], row[0][2], row[1], row[2], row[3]))
position.close()

pitchers_csv = open('Salaries (Pitchers).csv', 'r')
pitchers = csv.reader(pitchers_csv)
pitchers = list(pitchers)

#for row in pitchers:
#    a = row[1].split(' ')

for row in combined:
    del row[0][1]

pitchers_split = []
for row in pitchers:
    a = row[1].split(' ')
    pitchers_split.append([a[0], a[1]])

combined2 = []
for n in range(len(pitchers)):
    a = pitchers_split[n], combined[n]
    combined2.append(a)

position = open(os.path.join('Salaries (Pitchers).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in combined2:
    csvWriter.writerow((row[0][0], row[0][1], row[1][0][0], row[1][0][1], row[1][1], row[1][2], row[1][3]))
position.close()
    
os.remove('no header.csv')

pitchers_csv = open('Salaries (Pitchers).csv', 'r')
pitchers = csv.reader(pitchers_csv)
pitchers = list(pitchers)

first_names = []
rest_of_list = []

for row in pitchers:
    a = row[0][0]
    first_names.append((a, '.'))

first_initial = []
for row in first_names:
    a = row[0]+row[1]
    first_initial.append(a)

for row in pitchers:
    a = row[1:7]
    rest_of_list.append(a)

combined = []
for n in range(len(first_initial)):
    a = first_initial[n], rest_of_list[n]
    combined.append(a)

position = open(os.path.join('Salaries (Pitchers).csv'), 'w', newline='')
csvWriter = csv.writer(position)
for row in combined:
    #csvWriter.writerow((row[0], row[1][0], row[1][1], row[1][2], row[1][3], row[1][4], row[1][5]))
    csvWriter.writerow(((row[0]+' '+row[1][0]), row[1][1], row[1][2], row[1][3], row[1][4], row[1][5]))
position.close()
pitchers_csv.close()

#-------------------------------------------------------------------------#
#MATCH PROBABLE PITCHERS WITH TEAMS
#-------------------------------------------------------------------------#

print('Matching probable pitchers with teams...')

probable_csv = open('Probable Pitchers.csv', 'r')
probables = csv.reader(probable_csv)
probables = list(probables)
probable_csv.close()

salaries_csv = open('Salaries (Pitchers).csv', 'r')
salaries = csv.reader(salaries_csv)
salaries = list(salaries)


for player in probables:
    if '/' in player[1]:
        a = player[0] #Pitcher first initial, last name from probables list
        b = player[1] #Abbrev. of team for which probable pitcher plays
        for salary in salaries:
            if salary[0] == a:
                c = salary[3] #First team involved in game in salaries file
                d = salary[5] #Second team involved in game in salaries file
        try:
            if c in b:
                player[1] = c
            elif d in b:
                player[1] = d
            else:
                continue
        except NameError:
            continue

for player in probables:
    if '/' in player[1]:
        if 'ChC' and 'CWS' in player[1]:
            for pitcher in probables:
                if pitcher[1] == 'CWS':
                    player[1] = 'ChC'
                elif pitcher[1] == 'ChC':
                    player[1] = 'CWS'
                else:
                    continue
        if 'NYM' and 'NYY' in player[1]:
            for pitcher in probables:
                if pitcher[1] == 'NYM':
                    player[1] = 'NYY'
                elif pitcher[1] == 'NYY':
                    player[1] = 'NYM'
                else:
                    continue
        if 'LAA' and 'LAD' in player[1]:
            for pitcher in probables:
                if pitcher[1] == 'LAD':
                    player[1] = 'LAA'
                elif pitcher[1] == 'LAA':
                    player[1] = 'LAD'
                else:
                    continue

new_csv = open(os.path.join('Probable Pitchers.csv'), 'w', newline='')
csvWriter = csv.writer(new_csv)
for row in probables:
    csvWriter.writerow(row)
new_csv.close()

print('Fix probable pitchers with two possible teams.')
wait = input('PRESS ENTER TO CONTINUE.')

#-------------------------------------------------------------------------#
#GET TODAY'S LINEUPS
#-------------------------------------------------------------------------#

print("Getting today's lineups...")

url = 'http://www.fantasypros.com/mlb/lineups/'
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")

###################

how_many_games = []
for row in soup.findAll('div', {'class': 'gamebox'}):
    how_many_games.append(row)

###################

today_teams = []
for team in soup.findAll('tr', {'class': 'mobile-header'}):
    today_teams.append(team.text)

###################

handedness = []
for row in soup.findAll('span', {'class':'available mpb-available'}):
	handedness.append(row.text)

###################

n = (int(len(how_many_games))*2)
urllib.request.urlretrieve('http://www.fantasypros.com/mlb/lineups', 'Lineup Page html.txt')

for x in range(n):
    try:
        print('Getting',str(all_teams2[x]),'lineup...')
        with open('Lineup Page html.txt', 'r') as f:
            table = pd.read_html(f.read())[x]
        table = list(table.values.tolist())
        for row in table:
            del row[4]
            del row[3]
            del row[0]
    except AttributeError:
        continue
    except IndexError:
        continue
    try:
        new_lineup = []
        for row in table:
            b = row[1]
            a = row[0].split('(')
            c = a[0][:-1]
            new_lineup.append([c, b])
    except AttributeError:
        continue
    except IndexError:
        continue
        
    lineup = open(os.path.join(today_teams[x]+'.csv'), 'w', newline='')
    csvWriter = csv.writer(lineup)
    for row in new_lineup:
        csvWriter.writerow(row)
    lineup.close()

###################

print("Creating a list of today's matchups...")

today_matchups = []
for x in range(int(len(today_teams)/2)):
    away_team = today_teams[0]
    home_team = today_teams[1]
    away_team = away_team.strip(' Lineup')
    home_team = home_team.strip(' Lineup')
    today_matchups.append([away_team, '@', home_team])
    del today_teams[1]
    del today_teams[0]

for row in today_matchups:
    if row[0] == 'os Angeles Angels':
        row[0] = 'Los Angeles Angels'
    if row[2] == 'os Angeles Angels':
        row[2] = 'Los Angeles Angels'
    if row[0] == 'os Angeles Dodgers':
        row[0] = 'Los Angeles Dodgers'    
    if row[2] == 'os Angeles Dodgers':
        row[2] = 'Los Angeles Dodgers'

matchups = open(os.path.join('List of Todays Games.csv'), 'w', newline = '')
csvWriter = csv.writer(matchups)
for row in today_matchups:
    csvWriter.writerow(row)
matchups.close()

####################

all_teams = ['Ari', 'Atl', 'Bal', 'Bos', 'ChC', 'Cin', 'Cle', 'Col', 'CWS', 'Det', 'Hou', 'KC', 'LAA', 'LAD', 'Mia', 'Mil', 'Min', 'NYM', 'NYY', 'Oak', 'Phi', 'Pit', 'SD', 'Sea', 'SF', 'Stl', 'TB', 'Tex', 'Tor', 'Was']
all_teams2 = ['Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Chicago White Sox', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'Seattle Mariners', 'San Francisco Giants', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']
probables_csv = open('Probable Pitchers.csv', 'r')
probables = csv.reader(probables_csv)
probables = list(probables)

print("Adding opposing pitcher to starting lineups...")

for team in all_teams:
    if team == all_teams[0]:
        current = 'Arizona Diamondbacks'
        try:                
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
            
        except FileNotFoundError:
            continue
    elif team == all_teams[1]:
        current = 'Atlanta Braves'
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[2]:
        current = 'Baltimore Orioles'
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[3]:
        current = 'Boston Red Sox'
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[4]:
        current = str(all_teams2[4])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[5]:
        current = str(all_teams2[5])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'
            
            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[6]:
        current = str(all_teams2[6])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[7]:
        current = str(all_teams2[7])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[8]:
        current = str(all_teams2[8])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[9]:
        current = str(all_teams2[9])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[10]:
        current = str(all_teams2[10])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[11]:
        current = str(all_teams2[11])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[12]:
        current = str(all_teams2[12])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[13]:
        current = str(all_teams2[13])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[14]:
        current = str(all_teams2[14])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[15]:
        current = str(all_teams2[15])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[16]:
        current = str(all_teams2[16])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[17]:
        current = str(all_teams2[17])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[18]:
        current = str(all_teams2[18])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[19]:
        current = str(all_teams2[19])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[20]:
        current = str(all_teams2[20])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[21]:
        current = str(all_teams2[21])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[22]:
        current = str(all_teams2[22])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[23]:
        current = str(all_teams2[23])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[24]:
        current = str(all_teams2[24])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[25]:
        current = str(all_teams2[25])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[26]:
        current = str(all_teams2[26])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[27]:
        current = str(all_teams2[27])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[28]:
        current = str(all_teams2[28])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue
    elif team == all_teams[29]:
        current = str(all_teams2[29])
        try:
            lineup_csv = open(current+' Lineup.csv', 'r')
            lineup = csv.reader(lineup_csv)
            lineup = list(lineup)
            lineup_csv.close()

            for matchup in today_matchups:
                if matchup[0] == current:
                    opponent = matchup[2]
                elif matchup[2] == current:
                    opponent = matchup[0]

            for n in range(30):
                if opponent == all_teams2[n]:
                    opponent = all_teams[n]

            for row in probables:
                if row[1] == opponent:
                    starter = row[0]

            if starter == 'TBD':
                starter_hand = 'UNKNOWN'

            if starter != 'TBD':
                a = starter.split(' ')
                for row in handedness:
                    if a[1] in row:
                        if 'RHP' in row:
                            starter_hand = 'RHP'
                        elif 'LHP' in row:
                            starter_hand = 'LHP'
                        else:
                            starter_hand = 'UNKNOWN'

            new_lineup = []
            for row in lineup:
                new_lineup.append([row[0], row[1], starter, starter_hand])

            lineup = open(os.path.join(current+' Lineup.csv'), 'w', newline='')
            csvWriter = csv.writer(lineup)
            for row in new_lineup:
                csvWriter.writerow(row)
            lineup.close()
        except FileNotFoundError:
            continue

#-------------------------------------------------------------------------#
#ASSIGN TAv, Positions and Salaries to Lineups
#-------------------------------------------------------------------------#

print("Assigning TAv's AND SALARIES TO LINEUPS")

lhp_csv = open('BP Scraped Batting vs LHP.csv', 'r')
lhp = csv.reader(lhp_csv)
lhp = list(lhp) 
lhp_csv.close()

rhp_csv = open('BP Scraped Batting vs RHP.csv', 'r')
rhp = csv.reader(rhp_csv)
rhp = list(rhp)
rhp_csv.close()

first_salaries_csv = open('Salaries (1B).csv', 'r')
first_salaries = csv.reader(first_salaries_csv)
first_salaries = list(first_salaries)
first_salaries_csv.close()

second_salaries_csv = open('Salaries (2B).csv', 'r')
second_salaries = csv.reader(second_salaries_csv)
second_salaries = list(second_salaries)
second_salaries_csv.close()

third_salaries_csv = open('Salaries (3B).csv', 'r')
third_salaries = csv.reader(third_salaries_csv)
third_salaries = list(third_salaries)
third_salaries_csv.close()

short_salaries_csv = open('Salaries (SS).csv', 'r')
short_salaries = csv.reader(short_salaries_csv)
short_salaries = list(short_salaries)
short_salaries_csv.close()

catcher_salaries_csv = open('Salaries (C).csv', 'r')
catcher_salaries = csv.reader(catcher_salaries_csv)
catcher_salaries = list(catcher_salaries)
catcher_salaries_csv.close()

of_salaries_csv = open('Salaries (OF).csv', 'r')
of_salaries = csv.reader(of_salaries_csv)
of_salaries = list(of_salaries)
of_salaries_csv.close()

all_teams = ['Ari', 'Atl', 'Bal', 'Bos', 'ChC', 'Cin', 'Cle', 'Col', 'CWS', 'Det', 'Hou', 'KC', 'LAA', 'LAD', 'Mia', 'Mil', 'Min', 'NYM', 'NYY', 'Oak', 'Phi', 'Pit', 'SD', 'Sea', 'SF', 'Stl', 'TB', 'Tex', 'Tor', 'Was']
all_teams2 = ['Arizona Diamondbacks', 'Atlanta Braves', 'Baltimore Orioles', 'Boston Red Sox', 'Chicago Cubs', 'Cincinnati Reds', 'Cleveland Indians', 'Colorado Rockies', 'Chicago White Sox', 'Detroit Tigers', 'Houston Astros', 'Kansas City Royals', 'Los Angeles Angels', 'Los Angeles Dodgers', 'Miami Marlins', 'Milwaukee Brewers', 'Minnesota Twins', 'New York Mets', 'New York Yankees', 'Oakland Athletics', 'Philadelphia Phillies', 'Pittsburgh Pirates', 'San Diego Padres', 'Seattle Mariners', 'San Francisco Giants', 'St. Louis Cardinals', 'Tampa Bay Rays', 'Texas Rangers', 'Toronto Blue Jays', 'Washington Nationals']

for n in range(len(all_teams)):
#for n in range(1):    
    try:
        open_csv = open(all_teams2[n]+' Lineup.csv', 'r')
        lineup = csv.reader(open_csv)
        lineup = list(lineup)

        pitcher_hand = ''

        for row in lineup:
            if row[3] == 'RHP':
                pitcher_hand = 'RHP'
            elif row[3] == 'LHP':
                pitcher_hand = 'LHP'

        new_lineup = []

        if pitcher_hand == 'RHP':
            for batter in lineup:
                for row in rhp:
                    if batter[0].lower() == row[0].lower():
                        new_lineup.append([batter[0], row[26]])
        elif pitcher_hand == 'LHP':
            for batter in lineup:
                for row in lhp:
                    if batter[0].lower() == row[0].lower():
                        new_lineup.append([batter[0], row[26]])
        else:
            for batter in lineup:
                new_lineup.append(batter)

        new_lineup2 = []

        for batter in new_lineup:
            for player in first_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue
            for player in second_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue
            for player in third_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue
            for player in short_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue
            for player in catcher_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue
            for player in of_salaries:
                if batter[0] == player[1]:
                    new_lineup2.append([batter[0], batter[1], player[0], player[2]])
                    continue

            new_lineup3 = []
            seen = set()

            for player in new_lineup2: #this to catch duplicates in the new lineup for when a player is eligible at multiple positions
                if player[0] not in seen:
                    new_lineup3.append(player)
                    seen.add(player[0])
        
        new_csv = open(os.path.join(all_teams2[n]+' Lineup.csv'), 'w', newline = '')
        csvWriter = csv.writer(new_csv)
        for row in new_lineup3:
            csvWriter.writerow(row)
        new_csv.close()
    except FileNotFoundError:
        continue

#-------------------------------------------------------------------------#
#COMBINE ALL LINEUPS INTO PLAYER POOL
#-------------------------------------------------------------------------#

print("Creating available player pool...")

player_pool = []

for n in range(len(all_teams)):
    try:
        open_csv = open(all_teams2[n]+' Lineup.csv', 'r')
        lineup = csv.reader(open_csv)
        lineup = list(lineup)

        for player in lineup:
            player_pool.append(player)

    except FileNotFoundError:
        continue

player_pool_csv = open(os.path.join('Available Player Pool.csv'), 'w', newline = '')
csvWriter = csv.writer(player_pool_csv)
for row in player_pool:
    csvWriter.writerow(row)
player_pool_csv.close()

#-------------------------------------------------------------------------#
#FIND ALL COMBINATIONS OF LINEUPS (UP TO SOME REASONABLE POINT,
#WHICH IS DEFINED IN THE 'FOR N IN RANGE(x)' STEP BELOW
#-------------------------------------------------------------------------#

player_pool_csv = open('Available Player Pool.csv', 'r')
player_pool = csv.reader(player_pool_csv)
player_pool = list(player_pool)

catcher_pool = []
first_pool= []
second_pool = []
third_pool = []
short_pool = []
of_pool = []

for player in player_pool:
    if 'C' in player[2]:
        catcher_pool.append(player)
    if '1B' in player[2]:
        first_pool.append(player)
    if '2B' in player[2]:
        second_pool.append(player)
    if '3B' in player[2]:
        third_pool.append(player)
    if 'SS' in player[2]:
        short_pool.append(player)
    if 'OF' in player[2]:
        of_pool.append(player)

from operator import itemgetter
catcher_pool = sorted(catcher_pool, key = itemgetter(1), reverse = True)
first_pool = sorted(first_pool, key = itemgetter(1), reverse = True)
second_pool = sorted(second_pool, key = itemgetter(1), reverse = True)
third_pool = sorted(third_pool, key = itemgetter(1), reverse = True)
short_pool = sorted(short_pool, key = itemgetter(1), reverse = True)
of_pool = sorted(of_pool, key = itemgetter(1), reverse = True)

all_rosters = []
roster = [None]*8

try:
    os.remove('Affordable Rosters.csv')
except FileNotFoundError: pass


pitcher_cost = []
for row in csvRows:
    if 'P' in row[0]:
        cost = int(row[2])
        pitcher_cost.append(cost)
    if len(pitcher_cost) == 2:
        total_pitcher_cost = sum(pitcher_cost)

remaining_salary = 50000 - total_pitcher_cost

pool_dict = {'catcher pool':len(catcher_pool), 'first pool':len(first_pool), 'second pool':len(second_pool), 'third pool':len(third_pool), 'short pool':len(short_pool), 'outfield pool':len(of_pool)}

shortest_pool_len = 100
for pool, length in pool_dict.items():
    if length < shortest_pool_len:
        shortest_pool_len = length
        shortest_pool = pool
        

print('The shortest pool is', shortest_pool, 'with', str(shortest_pool_len), 'players.') 
        
iteration_depth = input('How many deep at each position do you want to iterate?' '\n')

print("Creating all possible combinations of lineups...")

def FindAllAffordableLineups():
    all_rosters = []
    roster = [None]*8

    for n in range(int(iteration_depth)):
        for catcher in catcher_pool[0:n]:
            roster = [None]*8
            roster[0] = catcher[0]
            for first_baseman in first_pool[0:n]:
                roster[1] = first_baseman[0]
                for second_baseman in second_pool[0:n]:
                    roster[2] = second_baseman[0]
                    for third_baseman in third_pool[0:n]:
                        roster[3] = third_baseman[0]
                        for shortstop in short_pool[0:n]:
                            roster[4] = shortstop[0]
                            for outfielders in it.combinations(of_pool, 3):
                                roster[5:8] = outfielders[0][0], outfielders[1][0], outfielders[2][0]
                                salaryList = []
                                for player1 in roster:
                                    for player2 in player_pool:
                                        if player1 == player2[0]:
                                            salaryList.append(int(player2[3]))
                                if sum(salaryList) <= remaining_salary:
                                    if len(roster) == len(set(roster)):
                                        all_rosters.append(roster[:])
                                        if len(all_rosters) < 50:
                                            print('Number of possible rosters found: ',len(all_rosters))
                                        if len(all_rosters) == 50:
                                            print("Fifty affordable rosters were found. We're not displaying every time we find another one. That would slow us down a lot.")          
                                        salaryList = []
                                if len(all_rosters) > 10**6:
                                    writeRosters = open(os.path.join('Affordable Rosters.csv'), 'w', newline = '')
                                    csvWriter = csv.writer(writeRosters)
                                    for row in all_rosters:
                                        csvWriter.writerow(row)
                                    writeRosters.close()
                                    all_rosters = []
        writeRosters = open(os.path.join('Affordable Rosters.csv'), 'w', newline = '')
        csvWriter = csv.writer(writeRosters)
        for row in all_rosters:
            csvWriter.writerow(row)
        writeRosters.close()

FindAllAffordableLineups()

#-------------------------------------------------------------------------#
#FIND OPTIMAL LINEUP FROM ALL COMBINATIONS
#-------------------------------------------------------------------------#

print('Finding optimal lineup...')

affordable_rosters_csv = open('Affordable Rosters.csv', 'r')
affordable_rosters = csv.reader(affordable_rosters_csv)
affordable_rosters = list(affordable_rosters)

best_score = 0
best_roster = []

for roster in affordable_rosters:
    roster_score = []
    for player in player_pool:
        for n in range(8):
            if roster[n] == player[0]:
                roster_score.append(float(player[1]))
                if len(roster_score) == 8:
                    if sum(roster_score) > best_score:
                        best_roster = []
                        best_roster.append(roster)
                        best_score = sum(roster_score)

end = time.time()
elapsed = end - start
elapsed = str(datetime.timedelta(seconds=elapsed))

print('Best roster is:', best_roster)
print('\n')
print('Their cumulative TAv is:', best_score)
print('\n')
print('Elapsed time was:', elapsed, 'seconds')

wait = input('PRESS ENTER TO CLOSE.')
'''
