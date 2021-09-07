import random

## defines.

TOTAL_YEARS = 10
PLAGUE_CHANCE = 15

def main():
    print("                HAMURABI")
    print("CREATIVE COMPUTING  MORRISTOWN, NEW JERSEY")
    print("\n\n\n")
    print("TRY YOUR HAND AT GOVERNING ANCIENT SUMERIA")
    print("SUCCESSFULLY FOR A TEN-YEAR TERM OF OFFICE.\n")
    
    ## Initialize variables
    popStarveTotal = 0
    popStarveTotalAvgPercent = 0
    pop = 95
    bushelsStored = 2800
    bushelsHarvest = 3000
    bushelsEatenByRats = bushelsHarvest - bushelsStored

    bushelsHarvestPerAcre = 3
    acres = int(bushelsHarvest / bushelsHarvestPerAcre)
    popIncrease = 5
    plague = 100

    popStarved = 0
    gameOver = False

    for year in range(1,TOTAL_YEARS+1):
        # Report.
        print("\n\nHAMURABI:  I BEG TO REPORT TO YOU,")
        print("IN YEAR {0}, {1} PEOPLE STARVED, {2} CAME TO THE CITY.".format(year, popStarved, popIncrease))

        pop += popIncrease

        if (plague < PLAGUE_CHANCE):
            pop = int(pop / 2)

            print("A HORRIBLE PLAGUE STRUCK!  HALF THE PEOPLE DIED.")

        print("POPULATION IS NOW {0}".format(pop))
        print("THE CITY NOW OWNS {0} ACRES.".format(acres))
        print("YOU HARVESTED {0} BUSHELS PER ACRE.".format(bushelsHarvestPerAcre))
        print("RATS ATE {0} BUSHELS.".format(bushelsEatenByRats))
        print("YOU NOW HAVE {0} BUSHELS IN STORE.\n".format(bushelsStored))

        acrePrice = int( random.randint(17,27) )

        print("LAND IS TRADING AT {0} BUSHELS PER ACRE.".format(acrePrice))
        
        ## Buy land
        
        buying = True
        selling = False
        while(buying):
            print("HOW MANY ACRES DO YOU WISH TO BUY")
            acresToBuy = getIntInput()

            if(acresToBuy < 0):
                printGameOver()
                gameOver = True
                buying = False
                break

            elif(acresToBuy > 0):
                if(acresToBuy * acrePrice <= bushelsStored):
                    acres += acresToBuy
                    bushelsStored -= acresToBuy * acrePrice
                    buying = False
            
                else:
                    printNotEnoughBushels(bushelsStored)

            else:
                buying = False
                selling = True

        if(gameOver):
            break

        ## Sell land

        while(selling):
            print("HOW MANY ACRES DO YOU WISH TO SELL")
            acresToSell = getIntInput()

            if(acresToSell < 0):
                printGameOver()
                gameOver = True
                selling = False
                break

            else:
                if(acresToSell <= acres):
                    acres -= acresToSell
                    bushelsStored += acresToSell * acrePrice
                    selling = False

                else:
                    printNotEnoughAcres(acres)

        if(gameOver):
            break

        ## Feed people.

        feeding = True
        while(feeding):
            print("\nHOW MANY BUSHELS DO YOU WISH TO FEED YOUR PEOPLE")
            bushelsToFeedPop = getIntInput()

            if(bushelsToFeedPop < 0):
                printGameOver()
                gameOver = True
                feeding = False
                break

            else:
                if(bushelsToFeedPop <= bushelsStored):
                    bushelsStored -= bushelsToFeedPop
                    feeding = False

                else:
                    printNotEnoughBushels(bushelsStored)

        if(gameOver):
            break

        ## Planting
        
        planting = True
        while(planting):
            print("HOW MANY ACRES DO YOU WISH TO PLANT WITH SEED")
            acresToPlant = getIntInput()

            if(acresToPlant < 0):
                printGameOver()
                gameOver = True
                planting = False
                break
            else:
                if(acresToPlant <= acres):
                    if(int(acresToPlant/2) < bushelsStored):
                        if(acresToPlant < 10* pop):
                            bushelsStored -= int(acresToPlant / 2)
                            planting = False
                        
                        else:
                            print("BUT YOU HAVE ONLY {0} PEOPLE TO TEND THE FIELDS. NOW THEN,".format(pop))

                    else:
                        printNotEnoughBushels(bushelsStored)

                else:
                    printNotEnoughAcres(acres)


        if(gameOver):
            break

        ## Harvest.

        bushelsHarvestPerAcre = random.randint(1,6)
        bushelsHarvest = bushelsHarvestPerAcre * acresToPlant
        bushelsEatenByRats = 0

        # 50% chance of rats
        if(random.randint(0,1) == 0):
            bushelsEatenByRats = int(bushelsStored / random.randint(1,6))

        bushelsStored = bushelsStored - bushelsEatenByRats + bushelsHarvest

        ## Population

        popIncrease = int( random.randint(1,6) * (20 * acres + bushelsStored) / pop / 100 ) + 1

        popFed = int(bushelsToFeedPop / 20)

        plague = random.randint(0,99)

        popStarved = 0
        if(pop > popFed):
            popStarved = pop - popFed
            if(popStarved > 0.45 * pop):
                printGameOverStarvation(popStarved)
                gameOver = True

            else:
                popStarveTotalAvgPercent = ( (year - 1) * popStarveTotalAvgPercent + popStarved * 100 / pop ) / year
                pop = popFed
                popStarveTotal += popStarved

        if(gameOver):
            break

    if(not gameOver):
        acresPerPop = acres / pop
        print("IN YOUR 10-YEAR TERM OF OFFICE, {0} PERCENT OF THE".format(popStarveTotalAvgPercent))
        print("POPULATION STARVED PER YEAR ON AVERAGE, I.E., A TOTAL OF")
        print("{0} PEOPLE DIED!!".format(popStarveTotal))
        print("YOU STARTED WITH 10 ACRES PER PERSON AND ENDED WITH")
        print("{0} ACRES PER PERSON.\n".format(acresPerPop))

        if(popStarveTotalAvgPercent > 33 or acresPerPop < 7):
            print("DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
            print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
            print("ALSO BEEN DECLARED 'NATIONAL FINK' !!")

        elif(popStarveTotalAvgPercent > 10 or acresPerPop < 9):
            print("YOUR HEAVY-HANDED PERFORMANCE SMACKS OF NERO AND IVAN IV.")
            print("THE PEOPLE (REMAINING) FIND YOU AN UNPLEASANT RULER, AND,")
            print("FRANKLY, HATE YOUR GUTS!")

        elif(popStarveTotalAvgPercent > 3 or acresPerPop < 10):
            print("YOUR PERFORMANCE COULD HAVE BEEN SOMEWHAT BETTER, BUT")
            print("REALLY WASN'T TOO BAD AT ALL. ")
            print("{0} PEOPLE WOULD".format(int(pop * 0.8*random.random()) ))
            print("DEARLY LIKE TO SEE YOU ASSASSINATED BUT WE ALL HAVE OUR")
            print("TRIVIAL PROBLEMS.")

        else:
            print("A FANTASTIC PERFORMANCE!!!  CHARLEMANGE, DISRAELI, AND")
            print("JEFFERSON COMBINED COULD NOT HAVE DONE BETTER!")
        
    ## Ending text
    for i in range(10):
        print("")
    print("SO LONG FOR NOW.\n")

def printGameOver():
    print("\nHAMURABI:  I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!!!")

def printGameOverStarvation(starved):
    print("\nYOU STARVED {0} PEOPLE IN ONE YEAR!!!".format(starved))
    print("DUE TO THIS EXTREME MISMANAGEMENT YOU HAVE NOT ONLY")
    print("BEEN IMPEACHED AND THROWN OUT OF OFFICE BUT YOU HAVE")
    print("ALSO BEEN DECLARED 'NATIONAL FINK' !!")

def printNotEnoughBushels(bushels):
    print("HAMURABI:  THINK AGAIN. YOU HAVE ONLY")
    print( "{0} BUSHELS OF GRAIN. NOW THEN,".format(bushels))

def printNotEnoughAcres(acres):
    print("HAMURABI:  THINK AGAIN. YOU OWN ONLY {0} ACRES. NOW THEN,".format(acres))

def getIntInput():
    while(True):
        try:
            i=int(input())
            return i
        except Exception as e:
            print("FORGIVE ME, WHAT WAS THAT?")

if __name__ == "__main__":
    main()