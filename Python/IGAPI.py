from instagrapi import Client
from Encrypt_and_Decrypter import get_password
import os
import getpass
import time

temp = get_password(2)
temp2 = get_password(5)
temp3 = get_password(11)

PASSWORD = temp
PASSWORD2 = temp2
PASSWORD3 = temp3

if __name__ == "__main__":
    
    os.system('cls')

    inp = getpass.getpass("Enter File Password:\n")

    os.system('cls')

    if inp == PASSWORD :
        inp = input("!WARNING!: Over excicuting this code might result in account termination, do you still wish to proceed? (y/n): ")
        inp = inp.lower()
        os.system('cls')
        if inp == 'y':
            inp = input("Do you want to use the defalt login information?(y/n): ")
            inp = inp.lower()
            os.system('cls')
            if inp == 'y':
                inp = getpass.getpass("Enter Password:\n")
                if inp == PASSWORD2:
                    try:
                        ACCOUNT_PASSWORD = get_password(2)
                    except:
                        print("ERROR_COULD_NOT_FIND_PASSWORD_")
                        ACCOUNT_USERNAME = '_i_need_therapy_2284'
                else:
                    quit()
            else:
                ACCOUNT_USERNAME = input("Enter your IG username:\n")
                os.system('cls')
                ACCOUNT_PASSWORD = getpass.getpass("Enter your password:\n")
                os.system('cls')
            
            os.system('cls')
            inp = input("Are you sure that you want to exicute this code?(y/n): ")
            inp = inp.lower()
            os.system('cls')
            
            if inp == 'y': 
                os.system('cls')
                inp = getpass.getpass("Enter Password:\n")
                if inp == PASSWORD3:
                    inp = input("Are you SHUREEE that you want to exicute this code?(y/n): ")
                    inp = inp.lower()
                    os.system('cls')
                
                    if inp == 'y':
                        
                        inp = input("Are you ABSOLUTELY SHUREEE that you want to exicute this code?!(y/n): ")
                        inp = inp.lower()
                        os.system('cls')
                        
                        if inp == 'y':
                            
                            inp = input("ARE YOU ABSOLUTELY AND WITH OUT A DOUBT SHUREEE THAT, YOU. WANT. TO. EXICUTE. THIS. CODE?!?!(y/n): ")
                            inp = inp.lower()
                            os.system('cls')
                
                            if inp == 'y':
                            
                                print("FINEE STUIT YOURSELF, DONT BLAME ME IF YOUR ACCOUNT GETS BANNED")
                                print("\nLOADING YOUR GODDAMN SCRIPT YOU STUBBORN-USER...")
                                time.sleep(5)
                                os.system('cls')
                                
                                # cl = Client()
                                # cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

                                # followers = cl.user_followers(cl.user_id)
                                # for user_id in followers.keys():
                                #     user_info = cl.user_info(52932375530)
                                #     print(user_info)



                                # cl.direct_send('How are you?', user_ids=[])  
                                print('PROGRAM ENDED SUCSESSFULLY')