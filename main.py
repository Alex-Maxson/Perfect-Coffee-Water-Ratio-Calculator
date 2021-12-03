#******************************************************************************
# Author:           (Alex Maxson)
# Assignment:       (Assignment 2)
# Date:             (4-23-2021)
# Description:      Ideal coffee to water ratio calculator. Plus an adjuster for taste.
#    
# Input:            Prompting user for amount of coffee/water in grams.
# Output:           Greeting, then prompted for amounts of coffee and water.
#                   1:2 Ratio calculated amounts of coffee and water displays after input.
#                   Prompts user for input on how much coffee used.
#                   Displays a better adjusted amount of coffee for the users taste.
#                   End statement.
#
# Sources:          Lab 1 specifications, D2L content, https://coffeeandteacorner.com/coffee-to-water-ratio/ #                     for the coffee information.
#                   
#******************************************************************************
print("Hello and welcome to the Perfect Espresso Shot Calculator!. \n\nThis calculator will help you achieve the perfect amount of coffee and water to your liking!\n")

def main():
  #Initializing the variables needed for the 1:2 Coffee to Water ratio calculator.
  water = 0
  watAmt = 0
  coffee = 0
  cofAmt = 0
  #Beginning of prompting the user for how much water they are going to use.
  water = float(input("In grams, how much water do you plan on using? \n[If you are unsure, enter 0.]"))
  print('\n')
  #The calculation of water * 2 giving you the amount of coffee you need.
  if water >= .001:
    watAmt = water * 2
    print('This is how much espresso you need: ', '{:.2f}'.format(watAmt), 'Grams.')
  #Now prompting the user for the amount of coffee they're going to use. Then calculating the amount of water.
  else: 
    print("Please answer the next question.", '\n')
    coffee = float(input("In grams, how much coffee do you plan on using? "))
    if coffee >= .001:
      cofAmt = coffee / 2
      print ('This is how much water you need:', '{:.2f}'.format(cofAmt), 'Grams.\n')
    else:
      print("Please try again with a positive number.\n")
  #The final statement that always prints when the calculations are finished.
  print('The amount of time needed in order for a perfect shot is between 25-30 seconds.\n')

  #The second half of the program, where it calculates the amount you need to adjust the coffee for your taste.
  #Initializing the variables needed for this half of the program.
  sourCof = 0
  sourFix = 0
  bittCof = 0
  bittFix = 0
  
  print('If your coffee is too bitter or too sour then please enter the amount of espresso you used in grams below. \n [Put 0 if you would like to skip.]\n')
  #Sour coffee calculation and print for the amount.
  sourCof = float(input('Too sour: '))
  if sourCof > .001:
    sourFix = sourCof + .05 
    print('This is the amount you should like: ', sourFix, 'Grams.')
  #Bitter coffee calculation and print for the amount.
  bittCof = float(input('Too bitter: '))
  if bittCof > .001:
    bittFix = bittCof - .05 
    print('This is the amount you should like: ', bittFix, 'Grams.')
    
  #Closing statement to user. 
  print('\n', 'Thank you and enjoy your coffee!')

  
main()