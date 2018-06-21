tdLine = "<td>"
travelLine='<td colspan=1>'

Resultfile= r'C:\Users\user1\Desktop\לימודים\Salary-Calculator-\result.txt'



def writeToResultFile(line): 
	res = open(Resultfile,'a')
	res.write(line)
	res.close()



def	copyFiles(fileHtml,file):
	f = open(fileHtml,'r',encoding='utf-8')
	file = open(file,'w')
	lines = f.readlines()

	for line in lines:
		file.write(line)

	file.close()

def cancelAllTheEnd(file,endFile):
	f = open(file,'r')
	badLineNum=0
	lines = f.readlines()
	for line in lines:
		badLineNum +=1
		if endFile in line:
				break	
	f.seek(0)

	lines = f.readlines()
	f.close()
	f = open(file,'w')
	num=0
	for line in lines:
		num+=1
		if num<=badLineNum:
			f.write(line)
	f.close()

	

def getNumOfHours(line):
	hours=0 
	minutes=0
	if len(line)==11:
		line = line[6:]
		hours=(int)(line[0])
		minutes=(int)(line[2:4])
		
	if len(line)==12:
		line = line[6:]
		hours=(int)(line[0:2])
		minutes=(int)(line[3:5])

	hours+=(minutes/60)
	#print(line,hours)
	return hours



def findHowMuchTime(file,NumOfLine):
	#file= open(file,"r")
	f = open(file,'r')
	num=0
	
	for line in f.readlines():
		num+=1
		if NumOfLine+8==num  :
			if not tdLine in line:
				hours=getNumOfHours(line)
				break
			else:
				num-=1
	return hours
	

def calculateMas(key,pay,file,keyToPrint):
	f = open(file,'r')
	num=0
	sum=0
	for line in f.readlines():
		num+=1
		if key in line:
			time = findHowMuchTime(file,num)
			sum+=time
	if sum:
		moneyLine="    "+(str)(sum*pay)+" - ףסכ "+(str)(sum)+" - ןמז "+keyToPrint
		print(moneyLine)

		if key[0]=='>':
			key=key[1:-1]
		moneyLine = makeWriteLine(key = key,time = (str)(sum),money = (str)(sum*pay))
		writeToResultFile(moneyLine)
	

	return sum*pay



def makeWriteLine(key,time,money):
	oneSpace=' '

	if key=='פיתוח תוכן וירטואלי HTML (מוקד לאומי)':
		line = 'פיתוח HTML'
	else:
		line = key
	
	while(len(line)!=35):
		line+=oneSpace
	line+='כסף - '+money
	while(len(line)!=55):
		line+=oneSpace
	line+='זמן -  '+time
	return line+'\n'





def claculateTravelTotal(line):
	num=[]
	for x in line:
		if x>='0' and x<='9':
			num.append((int)(x))
	sum=0
	if(len(num)==5):
		sum+=num[0]*10000
		sum+=num[1]*1000
		sum+=num[2]*100
		sum+=num[3]*10
		sum+=num[4]*1

	if(len(num)==4):
		sum+=num[0]*1000
		sum+=num[1]*100
		sum+=num[2]*10
		sum+=num[3]*1


	if(len(num)==3):
		sum+=num[0]*100
		sum+=num[1]*10
		sum+=num[2]*1
	
	if(len(num)==2):
		sum+=num[0]*10
		sum+=num[1]*1
	

	return sum







def claculateTravelMoney(key,file,keyToPrint):
	f = open(file,"r")
	num=0
	money=0
	seen = False
	check=False
	for line in f.readlines():
		num+=1
		if check:
			money = claculateTravelTotal(line)
			break
		if travelLine in line:
			if not seen:
				seen = True
			else:
				check=True
	
	travelMoneyLine="    " +(str)(money)+" - ףסכ "+keyToPrint
	print(travelMoneyLine)

	travelMoneyLine = "\n"+key + "   כסף -  "+(str)(money)
	writeToResultFile(travelMoneyLine+'\n')

	return money


def main():
	res = open(Resultfile,'w')
	res.write('')
	res.close()
	theValues= {("הכרדה",'>הדרכה<'):70,
				(" HTML חותיפ",'פיתוח תוכן וירטואלי HTML (מוקד לאומי)'):70,
				("ןכות חותיפ",'>פיתוח תוכן<'):70,
				("ב.ש תקידב",'בדיקת ש.ב'):50,
				("ןמז לוטיב",'ביטול זמן'):28.5,
				("לגס תרשכה",'>הכשרת סגל<'):30,
				("הפלחה הכרדה",'הדרכה - החלפה'):70,
				("תונויואר",'ראיונות מועמדים-שיווק\מיון\ראיונות'):50,
				("תעד תווח",'סקרים\שאלונים\חוות דעת'):35,
				("המאתה תדעו",'השתתפות בועדת התאמה'):50,
				("זלסקיפ",'הדרכה - פיקסלז'):50,
				("לגס תרשכה זלסקיפ","הכשרת סגל - פיקסלז"):35,
				("איש םוי", 'יום פעילות-יום שיא'):50,
				("םיסקט יוול",'ליווי טקסים\כנסים'):50,
				("ןחבמ תקידב","בדיקת מבחן"):50,
				("סרוק תקידב","בקרה על תוכן (QA) ומשוב"):50,
				("ילאוטוריו הכרדה","הדרכה בקורס וירטואלי"):70,
				("פייקס","תגבור וירטואלי - בסקייפ"):50,
				("ץיק הנחמ","מחנה קיץ"):50
				}
	print("\n\n")
	travel="נסיעות מיוחדות"
	endFile = '<!-- end: PAGE CONTENT-->'
	file= r'C:\Users\user1\Desktop\לימודים\Salary-Calculator-\lol.txt'
	fileHtml= r'C:\Users\user1\Desktop\לימודים\Salary-Calculator-\CyberNet_ monthly_reports.html'

	copyFiles(fileHtml,file)

	cancelAllTheEnd(file,endFile)


	sum=0
	for Allkey , pay in theValues.items():
		keyToPrint,key=Allkey
		sum+= calculateMas(key,pay,file,keyToPrint)	
	sum+= claculateTravelMoney(travel,file,"תועיסנ")
	
	finalLine = "\n     All the amount is - "+(str)(sum)+"\n\n\n\n\n"
	print(finalLine)
	writeToResultFile(finalLine)


main()