from prettytable import PrettyTable

def generatetable(input_list,input_number,offset):
  
  flag=0
  output=[]
  arrive_out=[]
  dead_out=[]
  finish_time=[]
  deadline_first=sorted(input_list, key = lambda x: (x[3]))
  arrival_fist=sorted(input_list, key = lambda x: (x[1],x[3]))
 
  for i in range(input_number):
    runtime=arrival_fist[i][2]
    for j in range(runtime):
      arrive_out.append(arrival_fist[i][0])


  for i in range(input_number):
    runtime=deadline_first[i][2]
    for j in range(runtime):
      dead_out.append(deadline_first[i][0])
      


  for i in range(len(arrive_out)):
    if(arrive_out[i]==dead_out[i]):
      output.append(arrive_out[i])
    else:
      if(flag==0):
        output.append(arrive_out[i])
        flag=1
      else:
        output.append(dead_out[i])
        flag=0

# generate the latness table
  for i in range (input_number):
    res = len(output) - 1 - output[::-1].index(input_list[i][0])
    finish_time.append(res+1)
  
  output_list1=PrettyTable()
  output_list1.field_names = ["Task name","Task Finish Time","Task deadline","Task Lateness"]
  for i in range(len(input_list)):
    task=[]
    task.append(input_list[i][0])
    task.append(finish_time[i])
    task.append(input_list[i][3])
    task.append(finish_time[i]-input_list[i][3]+offset)
    output_list1.add_row(task)
   
#clean up the output        
  output_list2 = PrettyTable()
  output_list2.field_names = ["Time Slot","Task name"]
  if offset>0:
    for i in range(offset):
      task=[]
      task.append('T'+str(i)+'->'+'T'+str(i+1))
      task.append('IDLE')
      output_list2.add_row(task)

  for i in range(len(output)):
    task=[]
    task.append('T'+str(i+offset)+'->'+'T'+str(i+offset+1))
    task.append(output[i])
    output_list2.add_row(task)

  print(output_list1) 
  print(output_list2)
#-------------------------------------------------------------------------------  


def EDF_scheduler():
  print("---------------------------------------------------")
  print("This is Earliest Deadline First Scheduling Algorithm")
  print("---------------------------------------------------")
  print("Please enter the task number")
  task_number = int(input())
  #print (task_number)
  edf_list = []
  deadlines_list =[]
  wce_list =[]
  arrival_list = []

  #define utilization factor
  u=0 
  print("Please enter the task parameters in following order")
  print("arrival time, worst-case computation times, and deadlines")
  print("e.g. 4 3 14")
  for i in range(task_number):
    task=[] 
    arrival,wct,deadlines = input().split(" ")
    task.append('J'+str(i+1))
    task.append(int(arrival))
    task.append(int(wct))
    task.append(int(deadlines))
    edf_list.append(task)
    deadlines_list.append(int(deadlines))
    wce_list.append(int(wct))
    arrival_list.append(int(arrival))
  offset = min(arrival_list)
  c_sum = sum(wce_list)+min(arrival_list)
  d_max = max(deadlines_list)
  print(edf_list)
  if (c_sum>d_max):
    print("This is not gonna work")
  else:
    generatetable(edf_list,task_number,offset)