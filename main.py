print('hello world')
name="""malak"""
print(name)
num=55
list=[1,2,3,4,5,6,7,8,9]
tuple=[1,2,3,555,555,555]
person1={'Title':'Malak','Contant':'4th year studing in university of yarmouk','Welcome':'To my our Profile thanks to pay your attention'}
person2={'Title':'Mohammed','Contant':'2th year studing in university of yarmouk','Welcome':'To my our Profile thanks to pay your attention'}
person3={'Title':'Ali','Contant':'3th year studing in university of yarmouk','Welcome':'To my our Profile thanks to pay your attention'}
Student={'Person1':person1,'Person2':person2,'Person3':person3}
dictionary={'name':name,'num':num,'list':list,'tuple':tuple}
print(dictionary)
for i in dictionary:
    print(i,":",dictionary[i])
print("----------------------")
for i in range(0,20,1):
    print(i)    
for i in Student:
    print(i,":",Student[i])
#----------------------------------------------
Number=input('Please insert int value:')
Number=(int(Number))
if Number%2==0:
        print('This number is even')
else:
        print('This number is odd')

i=0
whiletest=True
while whiletest:
    
    if i==5:
        i+=1
        continue
    print(i)
    i+=1
    if i==10:
         break

#print dictionary for title, contant, welcome
allperson=[]
person={}
print('Welcome to the app') 
while True:
     print("1 to insert new person")
     print("2_to see all person")
     print("3_tp Exit")

     choice=input("please insert yoou choice")
     if choice=='1':
          name=input('insert the person name')
          age=int(input('insert the person age'))
         
          job=input('insert the person job')
          person['name']=name
          
          
          person['job']=job
          allperson.append(person)
          print("You add all person successfully")
       
     elif choice=='2':
         counter=1
         print('----'*20)
         print('all person :')
         for i in allperson:
              print('person',counter)
         for key in i:     
              print("---",key,i[key])
              counter+=1
              

     
     
           

          
