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
        print("HOW MANY ACRES DO YOU WISH TO BUY")





        input()



if __name__ == "__main__":
    main()