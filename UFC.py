import requests
from bs4 import BeautifulSoup
import pandas as pd


while True:
    
    UserInput = input('what UFC are we on right now? (1-current): ')
    if not UserInput.isdigit():
            print("Please enter a valid number.")
            continue
    site = 'https://www.ufc.com/event/ufc-' + UserInput

    try:
        req = requests.get(site)
        parsedsite = BeautifulSoup(req.text ,'html.parser')

        break
    except:
        print("Number Not found")

fights = parsedsite.select('.c-listing-fight')

def FindName(corner):
    first = corner.select_one('.c-listing-fight__corner-given-name')
    last = corner.select_one('.c-listing-fight__corner-family-name')

    if first and last:
        return f"{first.text.strip()} {last.text.strip()}"
    return 'Unknown Fighter'

def FindDescription(full_name):
    if not full_name or full_name == "Unknown Fighter":
        print("Skipping: Invalid name")
        return
        
    name_slug = full_name.lower().replace(" ", "-")
    infosite = "https://www.ufc.com/athlete/" + name_slug

    try:
        reqsite = requests.get(infosite)
        if reqsite.status_code != 200:
            print(f"Page Not Found For {full_name}")
            return
        
        parsedinfo = BeautifulSoup(reqsite.text, 'html.parser')

        CirclePrecentages = [x.get_text() for x in parsedinfo.find_all(class_="e-chart-circle__percent")]
        WinTypes = [x.get_text() for x in parsedinfo.find_all(class_="c-stat-3bar__value")]
        value = [x.get_text() for x in parsedinfo.find_all(class_="c-overlap__stats-value")]
        comp = [x.get_text().strip(' \n%') for x in parsedinfo.find_all(class_="c-stat-compare__number")]

        print(f'{full_name.upper()} STATS:\n')
        print('SIG STRIKES:')
        print('Landed:', value[0])
        print('Attempted:', value[1])
        print("Striking Precentage:",CirclePrecentages[0])

        print('\nTAKEDOWNS:')
        print('landed:', value[2])
        print('Attempted:', value[3])
        print("Takedown Precentage:",CirclePrecentages[1])

        print('\nSIG STR BY POSITION:')
        print('Standing',WinTypes[0])
        print('Clinch',WinTypes[1])
        print('Ground',WinTypes[2])

        print('\nWIN BY METHOD')
        print('KO/TKO',WinTypes[3])
        print('DEC',WinTypes[4])
        print('SUB',WinTypes[5])

        print('\nGENERAL')
        print('Sig. Str. Landed Per Min:', comp[0])
        print('Sig. Str. Absorbed Per Min:', comp[1])
        print('Takedown avg Per 15 Min:', comp[2])
        print('Submission avg Per 15 Min:', comp[3])
        print(f'Sig. Str. Defense: {comp[4]}%')
        print(f'Takedown Defense: {comp[5]}%')
        print('Knockdown Avg:', comp[6])
        print('Average fight time:', comp[7])

    except Exception as e:
        print(f"Could not load stats for {full_name}: {e}")

print(f"\n{'='*60}")
print(f"UFC {UserInput.upper()} FIGHT CARD")
print(f"{'='*60}\n")

for fight in fights:
    Redcorner = fight.select_one('.c-listing-fight__corner-name--red')

    Bluecorner = fight.select_one('.c-listing-fight__corner-name--blue')

    if not Redcorner or not Bluecorner:
        continue

    red_name = FindName(Redcorner)
    blue_name = FindName(Bluecorner)

    weight = fight.select_one('.c-listing-fight__class-text')
    method = fight.select_one('.c-listing-fight__result-text.method')
    round_ = fight.select_one('.c-listing-fight__result-text.round')
    time = fight.select_one('.c-listing-fight__result-text.time')

    dic = {
        "red": red_name,
        "blue": blue_name,
        "weight": weight.text.strip() if weight else "N/A",
        "method": method.text.strip() if method else None,
        "round": round_.text.strip() if round_ else None,
        "time": time.text.strip() if time else None
    }

    format = pd.Series(dic)

    print(format)
    print(f"\n{'='*60}")

    FindDescription(red_name)
    print(f"\n{'='*60}")

    FindDescription(blue_name)
    print(f"\n{'='*60}\n{'='*60}")

