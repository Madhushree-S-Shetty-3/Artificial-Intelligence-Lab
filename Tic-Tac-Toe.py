board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}


def printBoard(board):
  print(board[1] + '|' + board[2] + '|' + board[3])
  print('-+-+-')
  print(board[4] + '|' + board[5] + '|' + board[6])
  print('-+-+-')
  print(board[7] + '|' + board[8] + '|' + board[9])
  print('\n')


def spaceIsFree(position):
  if board[position] == ' ':
    return True
  else:
    return False


def checkForWin():
  if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
    return True
  elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
    return True
  elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
    return True
  elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
    return True
  elif (board[3] == board[5] and board[3] == board[7] and board[3] != ' '):
    return True
  elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
    return True
  elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
    return True
  elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
    return True
  else:
    return False


def checkDraw():
  for key in board.keys():
    if board[key] == ' ':
      return False
  return True


def insertLetter(letter, position):
  if spaceIsFree(position):
    board[position] = letter
    printBoard(board)
    if checkForWin():
      if letter == 'X':
        print("Player 1 wins!")
      else:
        print("Player 2 wins!")
      return True
    elif checkDraw():
      print("Draw!")
      return True
    return False
  else:
    print("Can't insert there!")
    return False


def playerMove():
  while True:
    try:
      position = int(input("Enter the position for 'X'(1-9): "))
      if position in range(1, 10):
        if insertLetter('X', position):
          return True
        break
      else:
        print("Invalid position. Please enter a number between 1 and 9.")
    except ValueError:
      print("Invalid input. Please enter a number.")


def player2Move():
  while True:
    try:
      position = int(input("Enter the position for 'O'(1-9): "))
      if position in range(1, 10):
        if insertLetter('O', position):
          return True
        break
      else:
        print("Invalid position. Please enter a number between 1 and 9.")
    except ValueError:
      print("Invalid input. Please enter a number.")


while not checkForWin():
  printBoard(board)
  if playerMove():
    break
  if player2Move():
    break
