import numpy as np
from functools import reduce
from prettytable import  PrettyTable
#------------------------------------------------------------------
#gcd function to calculate the minor cycle
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
#------------------------------------------------------------------
def generateTable(iteration,minor_cycle,major_cycle,periods_list,task_number,wct_list):
  #generate the task time table(in every minor period)
  timetable=[]

  for x in range(iteration):
    for i in range (int(major_cycle/minor_cycle)):
      task=[]
      for j in range (task_number):
        if(i*10 % periods_list[j] == 0):
          for k in range(wct_list[j]):
            task.append(j+1)
      timetable.append(task)

  #fill the empty spaces with zero
  output=[]
  for i in range(len(timetable)):   
    s = list(timetable[i] + [0] * (10 - len(timetable[i])))
    output.append(s)
  #flatten the output list
  output=[x for tup in output for x in tup]

  #generate the output display table
  job_list=[]
  print_table = PrettyTable(['Time', 'Task Name'])
  for item in output:
    if item == 0:
      job_list.append('IDLE')
    else:
      job_list.append('J'+str(item))
  for i in range(0,int(len(output))):
    time_slot=[]
    time_slot.append('T'+str(i)+'->'+'T'+str(i+1))
    time_slot.append(job_list[i])
    print_table.add_row(time_slot)
  print(print_table)
#------------------------------------------------------------------
def CE_scheduler():
  print("---------------------------------------------------")
  print("This is Cyclic Executive scheduling algorithm")
  print("---------------------------------------------------")
  print("Please enter the task number")
  task_number = int(input())
  #print (task_number)
  task_list=[]
  ce_list = []
  periods_list=[]
  wct_list =[]
  #define utilization factor
  t=0
  #define display iteration (number of major cycles)
  print("Please enter the number of iterations to display")
  iteration =int(input())

  print("Please enter the task parameters in following order")
  print("worst-case computation times and periods")
  print("e.g. 4 3")

  for i in range(0,task_number):
    task=[]
    wct,period = input().split(" ")
    task.append(int(wct))
    task.append(int(period))
    task_list.append(task)
    periods_list.append(int(period))
    wct_list.append(int(wct))

  task_list = sorted(task_list,key = lambda list1: int(list1[1])) 
  
  for i in range(0,int(len(task_list))):
    label=[]
    label.append('J'+str(i+1))
    label.append(task_list[i])
    ce_list.append(label)
  
  print("\n\nIn order to facilitate scheduling calculation\nThe tasks will be reassigned with the new task name.\n")
  print("Job List: \n",ce_list)
  #calculate the minor and major cycle
  minor_cycle=reduce(lambda x,y:gcd(x,y),periods_list)
  major_cycle=np.lcm.reduce(periods_list)

  #determin the schedule is feasiable or not

  if (minor_cycle>sum(wct_list)):
    print("This schedule is feasiable")
    generateTable(iteration,minor_cycle,major_cycle,periods_list,task_number,wct_list)
  else:
    print("This schedule is not feasiable")
    print("The minor cycle is less than the total tasks duration")
    print("Minor Cycle： ", minor_cycle)
    print("Totoal Tasks Duration: ", sum(wct_list))
