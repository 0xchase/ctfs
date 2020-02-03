#!/usr/bin/python3

import angr
import claripy
from angr.procedures.libc import strcat

password = claripy.BVS("password", 8*11)

project = angr.Project("hashmenot")
#state = project.factory.blank_state(addr=0x400834)
state = project.factory.entry_state(stdin=password)
#state = project.factory.entry_state()
simgr = project.factory.simgr(state)

class my_strncat(angr.SimProcedure):
    def run(self, s1, s2, n):
        print("Hooked strncat()")
        strcat(s1, s2, 8)

project.hook_symbol('strncat', my_strncat(), replace=True)

#state.memory.store(0x90458d, password)

#simgr.explore(find=0x400983, avaid=[0x4009d8, 0x40099c, 0x400880, 0x400820])
#simgr.explore(find=0x400970)
simgr.explore(find=0x400a2b)

if simgr.found:
    print("Found solution")
    print(simgr.found[0].posix.dumps(0))
    exit()

    solution = simgr.found[0]
    solution_BVS = solution.memory.load(0x804a050, 16)
    solution.add_constraints(solution_BVS == "BWYRUBQCMVSBRGFU")
    s = solution.se.eval(password, cast_to=bytes).decode()
    print(s)
else:
    print("No solution found")
