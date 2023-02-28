import datetime
def get_datetime():
    '''
    Description
    -----------
    Stores the datetime individually in different variables as string and then joins it in a string
    
    Parameter
    ---------
    None
    
    Return
    ------
    date: string
    '''
    
    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    hour=str(datetime.datetime.now().hour)
    minute=str(datetime.datetime.now().minute)
    second=str(datetime.datetime.now().second)
    date=year+month+day+hour+minute+second
    return date
    
def get_file_content():
    '''
    Description
    -----------
    Opens main file customefile.txt and reads the contents
    
    Parameter
    ---------
    None
    
    Return
    ------
    data: list
    '''
    file=open("costumefile.txt","r")
    data=file.readlines()
    file.close() 
    return data

def get_dictionary(file_content):
    '''
    Description
    -----------
    Creates a dictionary and iterates through file_content
    Adds the content of the file in the dictionary, separating the string by "," and removing \n at the last
    
    Parameter
    ---------
    file_content: list
    
    Return
    ------
    data_dictionary: dictionary
    '''
    data_dictionary={}
    for index in range(len(file_content)):
        data_dictionary[index+1]=file_content[index].replace("\n","").split(",")
    return data_dictionary

def print_costumes():
    '''
    Description
    -----------
    Opens main file customefile.txt and reads the contents and displays the contents in a tabular format.
    The content is read by iterating through the dictionary
    
    Parameter
    ---------
    None
    
    Return
    ------
    None
    '''
    file_content=get_file_content()
    main_data=get_dictionary(file_content)
    print()
    print("***********************************************************************************************")
    print("{:<10} {:<30} {:<20} {:<10} {:<10}".format('ID','Name','Brand','Price','Quantity'))
    print("***********************************************************************************************")

    for key,value in main_data.items():
        print("{:<10} {:<30} {:<20} {:<10} {:<10}".format(key,value[0],value[1],value[2],value[3]))
        print("-----------------------------------------------------------------------------------------------")

def get_name():
    '''
    Description
    -----------
    Askes user to enter name and checks if its all alphabets. Otherwise prints invalid message
    
    Parameter
    ---------
    None
    
    Return
    ------
    name: string
    '''
    is_valid=False;
    while is_valid==False:
        name=input("\n"+"Enter your first name: ").lower()
        if name.isalpha():
            print("***********")
            print("ACCEPTED!!!")
            print("***********")
            is_valid=True
        else:
            print("-----------------------------------------------------------------")
            print("INVALID INPUT!!! Do not enter numbers or special characters!!!")
            print("-----------------------------------------------------------------")
    return name


def get_contact():
    '''
    Description
    -----------
    Askes user to enter name and checks if its all numeric. Otherwise prints invalid message
    
    Parameter
    ---------
    None
    
    Return
    ------
    contact: string
    '''
    
    is_valid=False;
    while is_valid==False:
        contact=(input("\n"+"Enter your contact number: "))
        if contact.isnumeric():
            print("***********")
            print("ACCEPTED!!!")
            print("***********")
            is_valid=True
        else:
            print("-----------------------------------------------------------------")
            print("INVALID INPUT!!! Please enter numbers!!!")
            print("-----------------------------------------------------------------")
    return contact
