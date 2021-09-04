

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
    starvedPopTotal = 0
    avgStarvedPerYearPercent = 0
    pop = 95
    storedBushels = 2800
    harvest = 3000
    bushelsEatenByRats = harvest - storedBushels

    harvestPerAcre = 3
    N_Acres = harvest / harvestPerAcre
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

        input()



if __name__ == "__main__":
    main()