
import pandas as pd
import threading
import time
from softioc import builder

from network_switch import network_switch

class netmon():
    #_____________________________________________________________________________
    def __init__(self, csvnam):
        builder.SetDeviceName("net")
        #create list of network switches
        self.sw_list = []
        csv = pd.read_csv(csvnam)
        for i in xrange(len(csv)):
            self.sw_list.append( network_switch(csv["name"][i]) )

    #_____________________________________________________________________________
    def start_monit_loop(self):
        t = threading.Thread(target=self.monit_loop)
        t.daemon = True
        t.start()

    #_____________________________________________________________________________
    def monit_loop(self):
        while True:
            time.sleep(10)
            self.update()

    #_____________________________________________________________________________
    def update(self):
        for i in self.sw_list:
            i.update()


