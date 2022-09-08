# J X Leong
# Variables and Constants

# Task 1, The rongotai first 15 this season has scored 55 tries, 35 conversions, 48 penalties and 5 drop goals. 
# Calculate and display the total points for each category, and the overall for the season.

# Values for Variables
totalTry = 55
totalConversions = 35
totalPenalty = 48
totalDrops = 5


# Values for Constants
TRYPOINTS = 5
PENALTYPOINTS = 3
DROPPOINTS = 3
CONVERSIONPOINTS = 2

#Output
print("Total points scored from tries =",(totalTry*TRYPOINTS))
print("Total points scored from conversions =",(totalConversions*CONVERSIONPOINTS))
print("Total points scored from penalties =",(totalPenalty*PENALTYPOINTS))
print("Total points scored from drop goals =",(totalDrops*DROPPOINTS))

# Changed Variables
totalTry = 275
totalConversions = 70
totalPenalty = 144
totalDrops = 15

print("Total points scored this season =", (totalConversions+totalTry+totalPenalty+totalDrops))