import rent_return_functions
        
def view_rent_bill(records_list):
    '''
    Description
    ------------
    This function matches the user input name and file number and opens the file with rent filename stored in records_list.
    Then it displays the content of the file.

    Parameter
    ---------
    records_list : list 

    Return
    ------
    None
    '''
    name=rent_return_functions.get_name()
    count=0
    for i in range(len(records_list)):
        if records_list[i][0]=="rent" and records_list[i][1]==name:
             count+=1
             print(records_list[i])
    if count==0:
        print("\nNo records found\n")        
    file_no=input("\nEnter the number of the file you want: ")
    hasRecord=False
    for i in range(len(records_list)):
        if records_list[i][0]=="rent" and records_list[i][1]==name and str(records_list[i][2])==str(file_no):
            hasRecord=True
            file=open(records_list[i][0]+"_"+records_list[i][1]+"_"+records_list[i][2]+".txt","r")
            print()
            lines=file.readlines()
            for line in lines:
                 print(line.strip())
            file.close()
            break
    if hasRecord==False:
        print("\nFile number not found\n")
    input("\nPress ENTER to go back")

def view_return_bill(records_list):
    '''
    Description
    ------------
    This function matches the user input name and file number and opens the file with return filename stored in records_list.
    Then it displays the content of the file.

    Parameter
    ---------
    records_list : list 

    Return
    ------
    None
    '''
    name=rent_return_functions.get_name()
    count=0
    for i in range(len(records_list)):
        if records_list[i][0]=="return" and records_list[i][1]==name:
             count+=1
             print(records_list[i])
             print()
    if count==0:
        print("\nNo records found\n")
    file_no=input("\nEnter the number of the file you want: ")
    hasRecord=False
    for i in range(len(records_list)):
        if records_list[i][0]=="return" and records_list[i][1]==name and str(records_list[i][2])==str(file_no):
            hasRecord=True
            file=open(records_list[i][0]+"_"+records_list[i][1]+"_"+records_list[i][2]+".txt","r")
            print()
            lines=file.readlines()
            for line in lines:
                 print(line.strip())
            file.close()
            break
    if hasRecord==False:
        print("\nFile number not found\n")
    input("\nPress ENTER to go back")

    
  
        

    
