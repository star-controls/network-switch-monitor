
import re
import os
from softioc import builder

class network_switch():
    #_____________________________________________________________________________
    def __init__(self, name):
        self.name = name
        pvnam = re.sub(r"\.", "_", name[:name.find(".bnl")])
        #switch status PV
        self.stat_pv = builder.boolIn(pvnam+":status", ZNAM="ok", ONAM="bad", DESC=name)
        self.stat_pv.OSV = "MAJOR"
        #switch monitoring activity PV
        self.act_pv = builder.boolOut(pvnam+":act", ZNAM="0", ONAM="1", HIGH=1)

    #_____________________________________________________________________________
    def update(self):
        #evaluate ping response
        resp = os.system("ping -c 1 " + self.name + " >/dev/null 2>&1")
        if resp == 0:
            self.stat_pv.set(0)
        else:
            self.stat_pv.set(1)
        #mark monitoring activity
        self.act_pv.set(1)





