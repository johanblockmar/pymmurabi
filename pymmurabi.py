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
    plague = 1
    popStarved = 0
    gameOver = False

    for year in range(TOTAL_YEARS):
        # Report.
        print("\n\nHAMURABI:  I BEG TO REPORT TO YOU,")
        print("IN YEAR {0}, {1} PEOPLE STARVED, {2} CAME TO THE CITY.".format(year+1, popStarved, popIncrease))

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
            acresToBuy = int(input())

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
            acresToSell = int(input())

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
            bushelsToFeedPop = int(input())

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
            acresToPlant = int(input())

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

def printGameOver():
    print("\nHAMURABI:  I CANNOT DO WHAT YOU WISH.")
    print("GET YOURSELF ANOTHER STEWARD!!!!!")


def printNotEnoughBushels(bushels):
    print("HAMURABI:  THINK AGAIN. YOU HAVE ONLY")
    print( "{0} BUSHELS OF GRAIN. NOW THEN,".format(bushels))

def printNotEnoughAcres(acres):
    print("HAMURABI:  THINK AGAIN. YOU OWN ONLY {0} ACRES. NOW THEN,".format(acres))


if __name__ == "__main__":
    main()