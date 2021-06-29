#PROGRAM TO CALCULATE THE PRORATED MARKS FOR 2ND YEAR B.TECH


name=str(input('Enter your Name:'))
regno=int(input('Enter your Reg no.:'))
pwd=str(input('Enter password (must be in caps):'))
if pwd.isupper():
    print('Welcome', name)
else:
    print('Error')
    exit()


#TO INPUT THE MARKS OF 3RD SEMESTER

mrks=[]
print('Enter your internal marks:')
aec=int(input('AEC:'))
mrks.append(aec)
nas=int(input('NAS:'))
mrks.append(nas)
dec=int(input('DEC:'))
mrks.append(dec)
em=int(input('EM:'))
mrks.append(em)
snt=int(input('SnT:'))
mrks.append(snt)
m3=int(input('Maths-3:'))
mrks.append(m3)

print('Your internals are:',mrks)

#NOW TO CALCULATE END SEMESTER MARKS USING PRORATION

cgpa2=float(input('Enter your CGPA at the end of 2nd semester:'))

prm=[]

for ele in mrks:
    promrks=((0.5*ele)+(2.5*cgpa2))
    prm.append(promrks)
print(prm)

#to compute marks out of 100

final_mrks=[]
for i in range(0, len(mrks)):
    final_mrks.append(mrks[i]+prm[i])

print('Your toatal of each subject out of 100 is:', final_mrks)

#to compute the grades for each subject

final_grades=[]

for ele in final_mrks:
    if(40<ele<49):
        grade='E'
        final_grades.append(grade)
    if(50<ele<59):
        grade='D'
        final_grades.append(grade)
    if(60<ele<69):
        grade='C'
        final_grades.append(grade)
    if(70<ele<79):
        grade='B'
        final_grades.append(grade)
    if(80<ele<89):
        grade='A'
        final_grades.append(grade)
    if(ele>90):
        grade='A+'
        final_grade.append(grade)


#to calculate gpa


gpa=((sum(final_mrks))/600)*10



#FINAL DISPLAY OF RESULTS

print('--------------------')
print('YOUR FINAL RESULTS.')
print('--------------------')
newname=name.upper()
print(newname)
print(regno)
print('Internals:',mrks)
print('End semester marks out of 100:',final_mrks)
print('GRADES for each subject:',final_grades)
print('GPA:',gpa)
