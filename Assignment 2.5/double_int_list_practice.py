def main():
  
  #set this to any double
  doubleValue = 3.8
  
  #set this to any int
  intValue = 3
  
  #print out addition, subtraction, multiplication, and division of these two values
  print(doubleValue + intValue)
  print(doubleValue - intValue)
  print(doubleValue * intValue)
  print(doubleValue / intValue)
  
  
  #populate this list
  myFriends = ["Chandler", "Jose", "Juan", "Blood", "Fire", "Death", "Jazmin", "Jackie", "Monkey"]
  
  #print out your friends at index 2 and index 3
  print(myFriends[2])
  print(myFriends[3])
  
  #populate this list with five numbers
  fiveNumbers = [12,43,9]
  fiveNumbers.insert(2,124)
  fiveNumbers.append(1323)
  
  #do each of the four equations with different numbers each time.
  print(fiveNumbers[3] + fiveNumbers[0])
  print(fiveNumbers[2] - fiveNumbers[4])
  print(fiveNumbers[1] * fiveNumbers[0])
  print(fiveNumbers[4] / fiveNumbers[3])

  #now replace two of the numbers in the list with a different number (using name of list[x] = ?, not rewriting the fiveNumber list)
  fiveNumbers[3] = 154
  fiveNumbers[0] = 99

  #print out the list
  print(fiveNumbers)
  
  
main()
