'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

#open the file

outfile = open('employee_data.csv', 'w')



#create an empty dictionary
newdict = {}


#use a loop to iterate through the csv file

FirstName = outfile['First Name']
LastName = outfile['Last Name']
Department = outfile['Department']
Salary = outfile['Salary']

for i in outfile: 
    for i in range (0,len(FirstName)):



    #check if the employee fits the search criteria
        if Department == "Marketing":
            newdict = {FirstName[i] + LastName[i]: (Salary[i]* 1.1)}




    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per printout

for k, v in newdict.items():
    print(k,v)

          
        

        
    
