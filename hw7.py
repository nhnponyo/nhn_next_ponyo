import string

error=open("/Users/sonchaewon/desktop/report_/error_log","r")
	
def error_report(error):
	errorlist=[]
	for line in error:
		if '[error]' in line:
			errorlist.append(line)
	for x in range(len(errorlist)):
		errorlist[x]=errorlist[x].replace('[','')
		errorlist[x]=errorlist[x].split('] ')
		errorlist[x]= errorlist[x]+errorlist[x][3].split(": ")
		del errorlist[x][3]
	
	print ("SUMMARY REPORT\n")
	
	errorCount={}
	for x in errorlist:
		if x[3] not in errorCount:
			errorCount[x[3]]=1
		else:
			errorCount[x[3]]=errorCount[x[3]]+1
		
	for x in errorCount:
		print x,":",errorCount[x],"\n"
	
	print ("DETAIL REPORT\n")
	errorDetail={}
	for x in errorlist:
		if len(x)==6:
					x[4]=x[4]+x[5]
		if len(x)<5:
			errorDetail[x[3]]=[]
		else:
			if x[3] not in errorDetail:
				errorDetail[x[3]]=[]
				errorDetail[x[3]].append(x[4])
			elif x[4] not in errorDetail[x[3]]:
				errorDetail[x[3]].append(x[4])
	i=1
	for x in errorDetail:
		print i,'.',x,":"
		for z in errorDetail[x]:
			print z
		i=i+1
			
error_report(error)