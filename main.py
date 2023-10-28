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
    #print dictionary for title, contant, welcome