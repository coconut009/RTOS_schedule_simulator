import numpy as np
from prettytable import PrettyTable


#   Function for algorithm for rate scheduling   
def schedule_cal(task,num,lcm):
    timetable=[]
    for i in range(0,lcm):
        timetable.append(0)
    numsl=[]
    for x in range(0,len(task)):
        numsl.append(task[x][0]*(lcm/task[x][1]))
    #print(numsl)
    #print(timetable)
    if(sum(numsl)>lcm):
        print('Not possible to schedule')
        return 0
    else:
        timeperiods=[]
        for i in range(0,num):
            n=[]
            for a in range(0,lcm):
                if(a%task[i][1]==0):
                    n.append(a)
            timeperiods.append(n)
    for m in range(0,len(numsl)):
        while(numsl[m]>0):
            for k in range(0,len(timeperiods[m])):
                if(numsl[m]>0):
                    if(timetable[timeperiods[m][k]]==0):
                        timetable[timeperiods[m][k]]=m+1
                        numsl[m]=numsl[m]-1
                       
                    else:
                        try:
                           
                                for b in range(timeperiods[m][k],timeperiods[m][k+1]):
                                     if(numsl[m]>0):
                                         if(timetable[b]==0):
                                             timetable[b]=m+1
                                             numsl[m]=numsl[m]-1
                                             break
                        except:
                            if(numsl[m]>0):
                                timetable[b]=m+1
                                numsl[m]=numsl[m]-1
    #print(timetable)
    
    #print(numsl)    

#------------------------------------------------------------------------------------------------------------------------
     #make a table

    job_list=[]
    print_table = PrettyTable(['Time', 'Task Name'])
    for item in timetable:
        if item == 0:
            job_list.append('IDLE')
        else:
            job_list.append('J'+str(item))
    for i in range(0,int(len(job_list))):
        time_slot=[]
        time_slot.append('T'+str(i)+'->'+'T'+str(i+1))
        time_slot.append(job_list[i])
        print_table.add_row(time_slot)
    print(print_table)
    return timetable

#------------------------------------------------------------------------------------------------------------------------
def RM_scheduler():
  print("---------------------------------------------------")
  print("This is Rate Monotonic Scheduling Algorithm")
  print("---------------------------------------------------")
  print("Please enter the task number")
  task_number = int(input())
  #print (task_number)
  rm_list = []
  period_list =[]
  wce_list =[]
  task_list=[]
  #define utilization factor
  u=0 
  print("Please enter the task parameters in following order")
  print("worst-case computation times and period")
  print("e.g. 2 4")
  for i in range(task_number):
    task=[] 
    wct,period = input().split(" ")
    task.append(int(wct))
    task.append(int(period))
    rm_list.append(task)
    period_list.append(int(period))
    wce_list.append(int(wct))

  #print("original list:",rm_list)

  # sorted with the earliest deadline
  new_list = sorted(rm_list,key = lambda list1: int(list1[1])) 
  #print("sorted list: ",new_list)
  for i in range(0,int(len(new_list))):
      label=[]
      label.append('J'+str(i+1))
      label.append(new_list[i])
      task_list.append(label)
  
  print("\n\nIn order to facilitate scheduling calculation\nThe tasks will be reassigned with the new task name.\n")
  print("Job List: \n",task_list)
  period_lcm=np.lcm.reduce(period_list)
  #print("lcm",period_lcm)
  for i in range (0,task_number):
    u=u+(wce_list[i]/period_list[i])

  N = task_number*((2**(1/task_number))-1)
  print('The utilization for give process is:'+str(u) )
  if(u<1):
      if(u<=N):
        print('\nScheduling guaranteed to be possible as '+str(u)+'<='+str(N))
        schedule_cal(new_list,task_number,period_lcm)
      else:
        print('\nScheduling may or may not be possible as '+str(u)+'>'+str(N))
        schedule_cal(new_list,task_number,period_lcm)
  else:
    print('Scheduling not possible as '+str(u)+' >1')


 