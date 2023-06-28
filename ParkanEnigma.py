import random
import string
from cryptography.fernet import Fernet
    #Begin
print ("\n"+"\n" + "Do you want to encode or decode using the \nParkan enigma? (Encode/Decode)")
Awnser = input()


if Awnser == 'Encode':
    
    #Input
  keyStr = ""

  print ("What do you want to encode?")
  OriginalSentence = input()
  i = 0 
  EncodeArray = []

    #Fernet
  key = Fernet.generate_key()
  f = Fernet(key)
  FinalByte = OriginalSentence.encode()
  OriginalSentence = str(f.encrypt(FinalByte))
    #Convert to array
  for i in range(len(OriginalSentence)):
    letter = OriginalSentence [i]
    EncodeArray.insert (i, letter)
  
    #Reverse + Add random letters
  EncodeArray.reverse()
  i = 0
  integer = 1
  string.ascii_letters
  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range (len(EncodeArray)):
    letter = random.choice(string.ascii_letters)
    EncodeArray.insert(integer, letter)
    integer += 2

    
    #Convert into Final String
  FinalStr = ''
  for i in range (len(EncodeArray)):
    FinalStr += EncodeArray[i]
  FinalStr = str(FinalStr)

    #Add Red Herring
  randomBegin = random.randint(70, 99)
  randomEnd = random.randint(70, 99)
  BeginStr = ""
  EndStr = ""
  string.ascii_letters
  'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  for i in range(randomBegin):
      letter = random.choice(string.ascii_letters)
      BeginStr += letter

  for i in range(randomEnd):
      letter = random.choice(string.ascii_letters)
      EndStr += letter

  print ("Key" + str(randomBegin) + str(randomEnd) + str(key) + " |||  Message" + BeginStr + FinalStr + EndStr)


  
elif Awnser == 'Decode':

  
    #Input
  print ("What do you want to decode?")
  Encoded = input ()
  print ("What is the key?")
  key = input ()
  DecodeArray = []

    #Remove Red Herrings
  BeginNum = int(key[0] + key[1])
  
  EndNum = len(Encoded) - (int(key[2] + key[3]))
  Encoded = Encoded[BeginNum:EndNum]

  print (Encoded)
  
    #Turn Into Array
  for i in range(len(Encoded)):
    letter = Encoded[i]
    DecodeArray.insert (i, letter)
  Len = len(DecodeArray) / 2
  
  Len = int(Len) 

    #Pop Random
  Deleter = 1
  for i in range (Len):
    DecodeArray.pop(Deleter)
    Deleter += 1
  FinalStr=''

    #Turn Into Str + Final
  
  DecodeArray.reverse()
  for i in range (len(DecodeArray)):
    FinalStr += str(DecodeArray[i])
  FinalStr = str(FinalStr)


      #Decode Fernet
  Ferneted = FinalStr[1:]
  key = key[5:]
  f = Fernet(key)
  FinalStr = f.decrypt(Ferneted)
  FinalStr = FinalStr.decode()
  
  print("Your decoded message is " + FinalStr)
  
else:
  print ("I am sorry, I do not understand. Please try again!")
