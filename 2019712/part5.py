# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
# Student name: Sachka Herath
# UOW Student:18098138
# IIT student:2019712
# Date:08/12/2020

#creating lists (for data)
data1=[120,0,0]
data2=[100,20,0]
data3=[100,0,20]
data4=[80,20,20]
data5=[60,40,20]
data6=[40,40,40]
data7=[20,40,60]
data8=[20,20,80]
data9=[20,0,100]
data10=[0,0,120]

#creating list of lists
input_list=[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10]
 
result=[0,0,0,0]#creating lists

for i in range(0,10):
    if (input_list[i][0]==120):
        result[0]=result[0]+1
        print("Progress")
    elif(input_list[i][0]==100):
        result[1]=result[1]+1
        print("progress(module trailer)")
    elif(input_list[i][2]==80 or input_list[i][2]==100 or input_list[i][2]==120):
        result[3]=result[3]+1
        print("Exclude")
    elif (input_list[i][0]==80 or input_list[i][0]==60 or input_list[i][0]==40 or input_list[i][0]==20):
        result[2]=result[2]+1
        print("Do not Progress-module retriever")
    else:
        print("An Error occurred,Please try again.THANK YOU !!!")
print()       
        
a=["Progress","Trailer","Retriever","Excluded"]

for i in range(0,4):
    print(a[i],'\t',end='')
    print(result[i],": ",end="")
    print("*"*result[i])

print()
print(sum(result)," outcomes in total")



