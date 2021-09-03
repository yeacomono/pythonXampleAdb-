

import time
from ppadb.client import Client as AdbClient
def connect():
   return  AdbClient(host="127.0.0.1", port=5037) # Default is "127.0.0.1" and 5037

if __name__ == '__main__':
    device= connect().devices()[0]

    # open up camera app
    while True:
      time.sleep(8)
      device.shell(f'input swipe 100 700 100 500 100')

    #print("# open up camera app")
    #device.shell(f'input swipe 100 700 100 500 50')
    #device.shell('input keyevent 27')

    # wait 5 seconds
    

    # take a photo with volume up
    #device.shell('input keyevent 24')
    #print('Taken a photo!')