import string
import re

def errorOrder(error):
	errorlist=[]
	for line in error:
		if '[error]' in line:
			line = line.replace('[','')
			line = line.replace('\n','')
			line = line.split('] ')
			line = line + line[3].split(': ')
			del line[3]
			errorlist.append(line)
	return errorlist

def makeErrorDetailDic(errorlist):
	errorDetail={}
	for orderedError in errorlist:
		if len(orderedError)==6:
			orderedError[4]=orderedError[4]+orderedError[5]
		if len(orderedError)<5:
			errorDetail[orderedError[3]]=[]
		else:
			if orderedError[3] not in errorDetail:
				errorDetail[orderedError[3]]=[]
				if not bool(re.search(r'jpg|gif|png',orderedError[4])):
					errorDetail[orderedError[3]].append(orderedError[4])
			elif orderedError[4] not in errorDetail[orderedError[3]]:
				if not bool(re.search(r'jpg|gif|png',orderedError[4])):
					errorDetail[orderedError[3]].append(orderedError[4])
	return errorDetail
				
def makeErrorCountDic(errorlist):
	errorCount={}
	for orderedError in errorlist:
		if orderedError[3] not in errorCount:
			errorCount[orderedError[3]]=1
		else:
			errorCount[orderedError[3]]=errorCount[orderedError[3]]+1
	return errorCount

def errorReportPrint(errorCount,errorDetail):
	print "[SUMMARY REPORT]"
	for errorname in errorCount:
		print errorname,":",errorCount[errorname],"\n"
	print "\n[DETAIL REPORT]\n--------------------------------------------"
	i=1
	for errorname in errorDetail:
		print i,'.',errorname
		for Detail in errorDetail[errorname]:
			print Detail
		i=i+1
		print '\n--------------------------------------------'

def main(errorlog):
	try:
		error = open(errorlog,"r")
	except IOError:
		print "file open error"
	errorlist = errorOrder(error)
	errorDetail = makeErrorDetailDic(errorlist)
	errorCount = makeErrorCountDic(errorlist)
	errorReportPrint(errorCount,errorDetail)
	
#	try:
#	    with open('' , 'w') as reportFile:
#	print(sReportData, file=reportFile)
	#print(sReportData, file=sys.stdout)
	
main("/Users/sonchaewon/desktop/report_/error_log")

'''
#make both dic in once
def makeErrorReportDic():
	errorCount={}
	errorDetail={}
	for orderedError in errorlist:
		if len(orderedError)==6:
			orderedError[4]=orderedError[4]+orderedError[5]
		if len(orderedError)<5:
			errorDetail[orderedError[3]]=[]
			errorCount[orderedError[3]] = 1
		else:
			if orderedError[3] not in errorDetail:
				errorDetail[orderedError[3]]=[]
				errorDetail[orderedError[3]].append(orderedError[4])
				errorCount[orderedError[3]]=1
			elif orderedError[4] in errorDetail[orderedError[3]]:
				errorCount[orderedError[3]]=errorCount[orderedError[3]]+1
			else:
				#orderedError[4] not in errorDetail[orderedError[3]]:
				errorDetail[orderedError[3]].append(orderedError[4])
				errorCount[orderedError[3]]=errorCount[orderedError[3]]+1
'''