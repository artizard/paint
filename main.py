import os
from getkey import getkey
import time
while True: 
  print('Max size depends on screen size:\n')
  try:
    columnSize = int(input('How many columns would you like there to be? '))
    rowSize = int(input('How many rows would you like there to be? '))
    if columnSize < 0 or rowSize < 0:
      print('\nPlease enter real numbers.')
      time.sleep(1.2)
      os.system('clear')
    else:
      break
  except:
    None
row = int(rowSize/2)
column = int(columnSize/2)
newReplaced = '-'
oldReplaced = '-'
canvas = [['-']*columnSize for i in range(rowSize)]
canvas[row][column] = '0'
def printCanvas(rowSize):
  for i in range (0,rowSize):
    for i in canvas[i]:
      print(i, ' ', end = '')
    print('\n')
def selection(row, column):
  choice = getkey()
  choice = choice.lower()
################### choice action ###################################
  if choice == 'w':
    row = row -1
  elif choice == 'a':
    column = column - 1
  elif choice == 's':
    row = row + 1
  elif choice == 'd':
    column = column + 1
  if choice == 'p':
    paint = 1
    erase = 0
  elif choice == 'o':
    erase = 1
    paint = 0
  else:
    paint = 0
    erase = 0
  
############################ range error fix #############################
  if row < -(rowSize-1):
    row = row + rowSize
  elif row > (rowSize-1):
    row = row -rowSize
  if column < -(columnSize-1):
    column = column + columnSize
  elif column > (columnSize-1):
    column = column -columnSize
  return row, column, paint, erase
os.system('clear')
##########################################################
################## actual actions ########################
##########################################################
while True:
  # display instructions 
  print('WASD to move\nP: Paint\nO: Erase\n')
  # display the new canvas
  printCanvas(rowSize)
  # take input for cursor movemement/painting 
  newRow, newColumn, paint, erase = selection(row, column)
  # if cursor did move
  if canvas[row][column] != canvas[newRow][newColumn]:
    newReplaced = canvas[newRow][newColumn]
    if canvas[newRow][newColumn] == '■':
      canvas[newRow][newColumn] = '□'
    else:
      canvas[newRow][newColumn] = '0'
    canvas[row][column] = oldReplaced
  # if cursor didn't move 
  else:
    # if cursor did not move and p is pressed
    # paint it 
    if paint == 1:
      canvas[newRow][newColumn] = '□'
      newReplaced = '■'
    elif erase == 1:
      canvas[newRow][newColumn] = '0'
      newReplaced = '-'

  row, column = newRow, newColumn 
  oldReplaced = newReplaced
  os.system('clear')
  
