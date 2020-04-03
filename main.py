
from rm import RM_scheduler
from edf import EDF_scheduler
from edd import EDD_scheduler
from ce import CE_scheduler

print("Enter '1' to select Earliest Due Date scheduling algorithm ")   
print("Enter '2' to select Earliest Deadline First scheduling algorithm ")   
print("Enter '3' to select Cyclic Executive: scheduling algorithm ")   
print("Enter '4' to select Rate Monotonic Scheduling algorithm ")   
print("Choose the Scheduler you want to run")

selection = int(input())
if(selection == 1):
    EDD_scheduler()
elif(selection == 2):
    EDF_scheduler()
elif(selection==3):
    CE_scheduler()
elif(selection==4):
    RM_scheduler()

else:
    print("please select valida a option ")
