#import the CSV module
import csv

#create a list of users whose passwords have been compromised
compromised_users = []

#open up the file itself. Store it in a file object called password_file
#Pass the password_file object holder to our CSV reader for parsing
with open('passwords.csv') as password_file: 
  #Save the parsed csv.DictReader object as password_csv
  password_csv = csv.DictReader(password_file)
  #iterate through each of the lines in the CSV
  for password_row in password_csv:
    #print out password_row['Username']. This is the username of the person whose password was compromised.
    print(password_row['Username'])
    #Use the list’s .append() method to add the username to compromised_users instead of printing them
    compromised_users.append(password_row['Username'])

print("\n")
#print the list
print(compromised_users)


#opening a file called compromised_users.txt. Open this file in write-mode, saving the file object as compromised_user_file
with open('compromised_users.txt', 'w') as compromised_user_file:
  #Iterate over each of your compromised_users
  for compromised_user in compromised_users: 
    #Write the username of each compromised_user in compromised_users to compromised_user_file
    compromised_user_file.write(compromised_user)

import json

#Open a new JSON file in write-mode called boss_message.json. Save the file object to the variable boss_message
with open('boss_message.json', 'w') as boss_message: 
  #Create a Python dictionary object within your with statement that relays a boss message. Call this boss_message_dict
  boss_message_dict = {
#Give it a "recipient" key with a value "The Boss".
#Also give it a "message" key with the value "Mission Success"
    'recipient' : 'The Boss', 
    'message' : 'Mission Success'
  }
  #Write out boss_message_dict to boss_message using json.dump()
  json.dump(boss_message_dict, boss_message)


#Create a new with block and open "new_passwords.csv" in write-mode. Save the file object to a variable called new_passwords_obj
with open('new_passwords.csv', 'w') as new_passwords_obj: 
  #create slash null's signature
  slash_null_sig = """
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

"""
  #Write slash_null_sig to new_passwords_obj. Now we have the file to replace passwords.csv with!
  new_passwords_obj.write(slash_null_sig)



     
