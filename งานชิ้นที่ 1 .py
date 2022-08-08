from time import sleep
import time
name = input('Enter Your Name : ')
sleep(1)
print('Welcome to Program, ' + name)
sleep(1)
lang = input('Select Lang [Eng/Th] : ')
if lang == 'Eng' :
    print('Hi This Program is for Introduce Yourself')
elif lang == 'Th' :
    print('ยินดีต้อนรับเข้าสู่โปรแกรมแนะนำตัวคุณนะครับ')
sleep(1)
##------------Demo----------##
if lang == 'Eng' :
    enname = input('Try Enter Your Name ')
    sleep(1)
    print('Your name is ' + enname)
elif lang == 'Th' :
    thname = input('ลองใส่ชื่อของคุณดูสิ ')
    sleep(1)
    print('ชื่อของคุณคือ ' + thname + 'ใช่ม้าา')
sleep(3)
##------------Age-----------##
if lang == 'Eng' :
    age = input('Enter Your AGE : ')
    sleep(1)
    sure_age_en = input('Are you sure? [Yes/No] : ')
    if sure_age_en == 'No' :
            age = input('Enter Your AGE : ')
elif lang == 'Th' :
    thname = input('อายุของคุณเท่าไหร่เหรอ? : ')
    sleep(1)
    sure_age_th = input('คุณแน่ใจหรือไม่? [Yes/No] : ')
    if sure_age_th == 'No' :
            age = input('Enter Your AGE : ')
sleep(1)
##------------Birth_Day-----------##
if lang == 'Eng' :
    print('The next Question is About Your BirthDay')
    day = input('Day : ')
    month = input('Month : ')
    year = input('Year : ')
    sure_birthday_en = input('Are you sure your birthday is ' + day + ' / ' + month + ' / ' + year + '[Yes/No] : ')
    if sure_birthday_en == 'No' : 
        day = input('Day : ')
        month = input('Month : ')
        year = input('Year : ')
elif lang == 'Th' :
    print('คำถามต่อไปดกเกี่ยวกับวันเกิดนะ')
    day = input('วัน : ')
    month = input('เดือน : ')
    year = input('ปี : ')
    sure_birthday_th = input('คุณแน่ใจนะว่า ' + day + ' / ' + month + ' / ' + year + ' ของคุณถูกต้อง [Yes/No] : ')
    if sure_birthday_th == 'No' : 
        day = input('วัน : ')
        month = input('เดือน : ')
        year = input('ปี : ')
##---------------Preview-----------------##
sleep(3)
if lang == 'Eng' :
    print('So let read what we got now')
    sleep(1)
    print('Your name is ' + enname + ' , And Your Age is ' + age + ' , your birthday is ' + day + ' / ' + month + ' / ' + year)
elif lang == 'Th' :
    print('มาดูข้อมูลที่ Program มีตอนนี้กันนะ')
    sleep(1)
    print('คุณชื่อ ' + thname + ' , อายุของคุณคือ ' + age + ' ,วันเกิดของคุณคือ ' + day + ' / ' + month + ' / ' + year)
