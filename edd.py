from prettytable import PrettyTable

def EDD_scheduler():
	print("---------------------------------------------------")
	print("This is Earliest Due Date scheduling algorithm")
	print("---------------------------------------------------")	
	print("Please enter the task number")
	task_number = int(input())
	#print (task_number)
	edd_list = []
	lateness_list =[]
	#define utilization factor
	t=0
	print("Please enter the task parameters in following order")
	print("worst-case computation times and datelines")
	print("e.g. 4 3")
	for i in range(task_number):
		task=[] 
		wct,deadlines = input().split(" ")
		task.append('J'+str(i+1))
		task.append(int(wct))
		task.append(int(deadlines))
		edd_list.append(task)
	print('\nJob Task List:\n',edd_list)

	new_list = sorted(edd_list,key = lambda list1: int(list1[2])) 
	
	output_list = PrettyTable()
	
	output_list.field_names = ["Task name", "Finish Time", "Deadline", "Lateness"]
	for i in range(0,task_number):
		t=t+new_list[i][1]
		task=[]
		task.append(new_list[i][0])
		task.append(t)
		task.append(new_list[i][2])
		task.append(t-new_list[i][2])
		lateness_list.append(t-new_list[i][2])
		output_list.add_row(task)

	print(output_list)
	print("\nMaximum Lateness: ", max(lateness_list))