from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import msvcrt
from discord_webhook import DiscordWebhook
import datetime
import os
from selenium.webdriver.common.action_chains import ActionChains

stock_finish = 'https://discord.com/api/webhooks/84755443530/dwx4hEHvPN549GHBjbztqgETR0HQwtNQlWaxWso0A'
got_stock1 = 'https://discord.com/api/webhooks/8473413037864/mfQpfmSpdV2M6znfsVs0M31z2NFmWg5dAjp'
got_stock2 = 'https://discord.com/api/webhooks/84994154/XbClNsf6x70UAmW6EepdjIrkNF-WNNKt3-YIBJLCv'
got_stock3 = 'https://discord.com/api/webhooks/844nTraUGxzvBuoFYU_2QNUeYO3FAvyKETCA8q8'
asnbbot = 'https://discord.com/api/webhooks/84846708/5y0VDd_ct8RzBnfKPYzvBVHwwfKdy5GFnhU2'

# # pyautogui.displayMousePosition()

opt = Options()
opt.add_argument("--start-maximized")
opt.add_experimental_option("excludeSwitches", ["enable-logging"]) #avoid error
url = 'https://www.myasnb.com.my'
driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe', options=opt)
driver.get(url)
# driver.switch_to.frame('win1')#change frame argument is frame name

loop = 0
loop2 =0
def login():
    time.sleep(1.5)
    driver.find_element_by_link_text('LOG MASUK').click()#login
    driver.find_element_by_xpath('//*[@id="username"]/div[2]/form/label/input').send_keys('')#id
    driver.find_element_by_xpath('//*[@id="no-printable"]').click()#submit
    time.sleep(4)
    driver.find_element_by_id('btnYes').click()
    driver.find_element_by_xpath('//*[@id="password"]/div[2]/form/label/div[1]/input').send_keys('')#pw
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="no-printable"]').click()#yes
    time.sleep(10)

#new asm_name 1,2,3
def buy_stock(asm_name,amount):
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div[2]/div/div[1]/div[2]/a['+asm_name+']/div[2]').click() #choose which asm
    # driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[1]/a').click()#portfolio
    # driver.find_element_by_xpath('//*[@id="form1_'+asm_name+'"]/div/button').click()#transaksi
    # driver.find_element_by_xpath('//*[@id="submit_buy_'+asm_name+'"]').click()#tambah
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[1]/input').send_keys(amount) #amount
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[2]/select/option[12]').click() #bank
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/div/label/input').click() #telah baca
    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[3]/button').click() #seterusnya
    time.sleep(2)

    try: #if got unit
        word = 'Saya dengan ini mengesahkan bahawa saya telah membaca, memahami dan bersetuju dengan Terma & Syarat.'
        if driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div/div/label/span').text == word: #if got unit will show these word
            # os.system("C:\\Users\\TANG\\Desktop\\abc.mp3")
            timeNow = datetime.datetime.now().strftime("%c")#time now
            DiscordWebhook(url=got_stock1,content=' @everyone got unit hurry up!!\nthe time is '+timeNow).execute()
    except: #if no unit
        print('')


    try:
        driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[2]/div/div/form/div[4]/button[2]').click()#bukan pep use try bcus once u selected it will not popup again
    
    except:
        print('') 

    finally:
        while True:

            for timer in range(9): #show time only
                print(8 - timer)
                time.sleep(1)

            x = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[3]/div/div/div[2]/p').text # popup message
            driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[3]/div/div/div[3]/button').click() #close popup message

            for timer in range(8): #show time only
                print(7-timer)
                time.sleep(1)

            try:#no stock

                if x == 'The transaction was declined due to insufficient units available. Please try again later (068)':#no stock amount decrease
                    if amount == 100:##if amount left 100 nothing to decrease
                        amount = amount
                    else:
                        amount -= 100#minus 100 every time when fail
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[1]/input').clear() #clear amount
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[1]/input').send_keys(amount) #enter new amount
                    driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[3]/div[1]/div/div[2]/div/form/div/label[3]/button').click() #seterusnya
                    time.sleep(2)

                    try: #if got unit
                        word = 'Saya dengan ini mengesahkan bahawa saya telah membaca, memahami dan bersetuju dengan Terma & Syarat.'
                        if driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[2]/div/div/label/span').text == word: #if got unit will show these word
                            # os.system("C:\\Users\\TANG\\Desktop\\abc.mp3")
                            timeNow = datetime.datetime.now().strftime("%c")#time now
                            DiscordWebhook(url=got_stock1,content=' @everyone got unit hurry up!!\nthe time is '+timeNow).execute()
                            return False

                    except: #if no unit
                        print('')

                    
                        
                elif x == 'Blocked due to retry. Please try again in 5 minutes':# no stock return home over limit
                    time.sleep(1)
                    timeNow = datetime.datetime.now().strftime("%c")#time now
                    DiscordWebhook(url=stock_finish,content = asm_name+' have no stock \nthe time is '+timeNow +'\n------------------------------').execute()
                    # driver.find_element_by_xpath('//*[@id="no-printable"]/div[1]/div[2]/div/ul/li[1]/a/span').click()#back to portfoilio
                    driver.find_element_by_link_text('Akaun Saya').click()
                    break # end of this defination 

                else:
                    print(bug) #not either two condition above go to except

            except:#got stock 
                DiscordWebhook(url=asnbbot,content='------------------------------\n @Everyone got Problem end at\n' + datetime.datetime.now().strftime('%c') + '\n------------------------------').execute()
                return False

# run program

DiscordWebhook(url=asnbbot,content='------------------------------\nstart at \n' + datetime.datetime.now().strftime('%c') + '\n------------------------------').execute()
login()
round = 0
money = 1000
try:
    while True:##keep loop
        print('hi')
        if buy_stock('1',money) == False:#20s
            break
        print ('hi1')
        os.system('cls')
        if buy_stock('2',money) == False:#20s
            break
        os.system('cls')
        if buy_stock('3',money) == False:#20s
            break
        os.system('cls')
        
        #only if run 1 stock
        # print('hi')
        # for xy in range(10): 
        #     try:
        #         driver.find_element_by_link_text('Akaun Saya').click() #prevent log out itself
        #     except:
        #         print('keep trying')
        #     finally:
        #         for yy in range (34):
        #             time.sleep(1)
        #             print(yy)
        # print('end')

        #only if run 3 stock
        print('hi')
        for xy in range(9): 
            try:
                driver.find_element_by_link_text('Akaun Saya').click()#prevent log out itself
            except:
                print('keep trying')
            finally:
                for yy in range (27):
                    time.sleep(1)
                    print(yy)
        print('end')

        # os.system("cls")
        # for x in range(238):
        #     print('continue in ' + str(238-x) + ' seconds')
        #     time.sleep(1)
        
        DiscordWebhook(url=asnbbot,content='round :'+ str(round)).execute()
        round += 1
except:
    DiscordWebhook(url=asnbbot,content='------------------------------\n @everyone got problem end at\n' + datetime.datetime.now().strftime('%c') + '\n------------------------------').execute()
