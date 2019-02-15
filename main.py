#!/usr/local/epics/modules/pythonIoc/pythonIoc

from softioc import softioc, builder

from netmon import netmon
net = netmon("switch_list.csv")

builder.LoadDatabase()
softioc.iocInit()

net.start_monit_loop()

softioc.interactive_ioc(globals())

