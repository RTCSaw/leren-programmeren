import time
import math
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_HORSE_SILVER_PER_DAY
from data import COST_TENT_GOLD_PER_WEEK

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount/10

def silver2gold(amount:int) -> float:
    return amount/5

def copper2gold(amount:int) -> float:
    #return amount/ 50
    return silver2gold (copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    s2g = personCash['silver']
    silver2gold(s2g)
    c2g = personCash['copper']
    copper2gold(c2g)
    p2g = personCash['platinum']
    platinum2gold(p2g)
    gold = personCash['gold']
    totaal_goud =  platinum2gold(p2g) + silver2gold(s2g) + copper2gold(c2g) + gold
    return totaal_goud
    
##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    kosten_in_koper = ((COST_FOOD_HORSE_COPPER_PER_DAY * horses) + (COST_FOOD_HUMAN_COPPER_PER_DAY * people)) * JOURNEY_IN_DAYS
    kosten_in_goud = copper2gold(kosten_in_koper)
    return round(copper2gold (kosten_in_goud),2 )
##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    lijst = []
    for x in list:
        if x [key]== value:
            lijst.append(x)
    return lijst

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'shareWith',True)

def getAdventuringFriends(friends:list) -> list:
    list = getAdventuringPeople(friends)
    list = getShareWithFriends(list)
    return list

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    aantal_paarden = math.ceil(people/2)
    return aantal_paarden
def getNumberOfTentsNeeded(people:int) -> int:
    aantal_tenten = math.ceil(people/3)
    return aantal_tenten

def getTotalRentalCost(horses:int, tents:int) -> float:
    total_cost_horses = horses * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    total_cost_tents = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    return silver2gold(total_cost_horses )+total_cost_tents

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    spullen = []
    for item in items:
        itemtxt = f"{item['amount']}{item['unit']} {item['name']}"
        spullen.append(itemtxt)
    
    return ", ".join(spullen)

def getItemsValueInGold(items:list) -> float:
    totaal_goud = 0 
    for item in items:
        if item['price']['type']=='copper':
            totaal_goud += copper2gold(item['price']['amount']*item['amount'])
            
        elif item['price']['type']=='silver':
            totaal_goud += silver2gold(item['price']['amount']*item['amount'])

        elif item['price']['type']=='platinum':
            totaal_goud += platinum2gold(item['price']['amount']*item['amount'])
        
        elif item['price']['type']=='gold':
            totaal_goud += item['price']['amount']*item['amount']
        
    return totaal_goud
##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totalGold = 0
    for cash in people:
        totalGold += copper2gold(cash['cash']['copper'])
        totalGold += silver2gold(cash['cash']['silver'])
        totalGold += cash['cash']['gold']
        totalGold += platinum2gold(cash['cash']['platinum'])
    return round(totalGold, 2)
##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    humanInnCosts = silver2gold(people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    horseInnCosts = copper2gold(horses * COST_FOOD_HORSE_COPPER_PER_DAY)

    return round(leftoverGold / (humanInnCosts + horseInnCosts))

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    humanInnCosts = silver2gold(people * COST_FOOD_HUMAN_COPPER_PER_DAY)
    horseInnCosts = copper2gold(horses * COST_FOOD_HORSE_COPPER_PER_DAY)

    return round(nightsInInn * (humanInnCosts + horseInnCosts), 2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()