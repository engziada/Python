from threading import Thread
from time import sleep
from JordanPass import AutomationManager
import shelve

AM = AutomationManager()

name = 'محمد محمود عقيل'
direction = 'دخول'
nationality = 'سوري'
passportno = 'NO12388953'
nationalid = '1003837044'
carnumber = '228232'
email = 'abdalghne.karoof@gmail.com'
cc = ''
phoneno = '0968859388'
image = 'IMG-20230130-WA0026.jpg'
status = -2
log=''

data={'name': name, 'direction': direction, 'image': image, 'phoneno': phoneno, 'nationality': nationality,
           'cc': cc, 'passportno': passportno,'nationalid': nationalid,'carnumber': carnumber,'email': email,'status': status, 'log':log}


def StartSubmit():
    while True:
        print('Starting')
        db = shelve.open("db.shelve", writeback=True)               
        # unsent = [key for key in db if db[key]['status'] == -2]
        unsent = [key for key in db]
        print(f'Found ({len(unsent)}) records in database')
        for passportno in unsent:
            print(f'Send data for passport no [{passportno}]')
            data = db[passportno]
            result = AM.Start(data)
            db[passportno]['status'] = result[0]
            db[passportno]['log'] = result[1]
        db.close()
        sleep(10) # sleep for 15 minutes
    
    
    
with shelve.open("db.shelve",writeback=True) as db:
    if passportno not in db:
        db[passportno] = data
        print(f'<{passportno}> injected to database')
    else:
        print(f'<{passportno}> exists database')

    # result=AM.Start(data)
    # db[passportno]['status'] = result[0]
    # db[passportno]['log']=result[1]
    # print(db[passportno])

# create and start the daemon thread
print('Starting background task...')
daemon = Thread(target=StartSubmit, name='Background')
daemon.start()







