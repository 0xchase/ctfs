#!/usr/bin/python3

import angr
import claripy

project = angr.Project("challenge")

state = project.factory.entry_state()

simgr = project.factory.simgr(state)

simgr.explore(find=0xc1c, avoid=0xc36)

if simgr.found:
    print("Found solution")
    print(simgr.found[0].posix.dumps(0))
else:
    print("No solutions found")
