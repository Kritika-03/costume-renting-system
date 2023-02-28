import rent_return_functions
import datetime
import records


def get_id():
    '''
    Description
    -----------
    Askes the user for costume ID. Checks for exception in input. If no exception is found,
    Checks if costume ID is greater than 0 and less or equal to the number of items in the the dictionary
    If the quantity of customer ID is 0, then prints out of stock
    If costume ID is not valid then prints invalid message.
    
    Parameter
    ---------
    None
    
    Return
    ------
    costume_id: int
    '''
    file_content=rent_return_functions.get_file_content()
    main_data=rent_return_functions.get_dictionary(file_content)

    is_valid=False
    while is_valid==False:
        success=False
        while success==False:
            try:
                costume_id=int(input("\nEnter Costume ID: "))
                success=True
            except:
                print("\nError!!! Please enter a numeric value for Costume ID\n")
                
        if costume_id>0 and costume_id<= len(main_data):
            if int(main_data[costume_id][3])==0:
                print("-------------------------------------------------------")
                print("SORRY!! The selected costume is out of stock right now.")
                print("-------------------------------------------------------")
            else:
                is_valid=True
                print("***********")
                print("ACCEPTED!!!")
                print("***********")
        else:
            print("-------------------------------------------------------------------------")
            print("INVALID INPUT!!! Please enter a Costume ID from the list of costumes!!!")
            print("-------------------------------------------------------------------------")
        
    return costume_id


def get_quantity(costume_id):
    '''
    Description
    -----------
    Askes the user for costume quanity. Checks for exception in input. If no exception is found,
    Checks if costume ID is greater than 0 and less or equal to the available quanityt of the costume id chosen
    If costume ID is not valid then prints invalid message.
    
    Parameter
    ---------
    costume_id: int
    
    Return
    ------
    costume_quantity: int
    '''
    
    file_content=rent_return_functions.get_file_content()
    main_data=rent_return_functions.get_dictionary(file_content)
    available_quantity=int(main_data[costume_id][3])
    
    is_valid=False
    while is_valid==False:
        success=False
        while success==False:
            try:
                costume_quantity=int(input("\nEnter Costume Quanity: "))
                success=True
            except:
                print("\nError!!! Please enter a numeric value for Costume Qunatity\n")
                
        if costume_quantity>0 and costume_quantity <= available_quantity:
            is_valid=True
            print("***********")
            print("ACCEPTED!!!")
            print("***********")
        else:
            print("------------------------------------------------------------------------------")
            print("INVALID INPUT!!! Please enter a number from the available number of costume!!!")
            print("------------------------------------------------------------------------------")
    
    return costume_quantity


def generate_bill(cart,records_list):
    '''
    Description
    -----------
    Askes and validates user input to generate bill
    Creates new file to store bill generated, and stores filename in records_list
    Caculates the price and grand total of the costumes rented
    Writes the bill according to the lists stored in cart, and details provided into the file, and prints it too
    
    Parameter
    ---------
    cart: list
    records_list: list
    
    Return
    ------
    None
    '''
    
    file_content=rent_return_functions.get_file_content()
    main_data=rent_return_functions.get_dictionary(file_content)

    year=str(datetime.datetime.now().year)
    month=str(datetime.datetime.now().month)
    day=str(datetime.datetime.now().day)
    date=rent_return_functions.get_datetime()
    name=rent_return_functions.get_name()
    contact=rent_return_functions.get_contact()

    filename="rent_"+name+"_"+date+".txt"
    records_list.append(filename.replace(".txt","").split("_"))
    
    file=open(filename,"w")
    file.write("------------------------------------------RENT INVOICE------------------------------------------\n")
    file.write("\n")
    file.write("{:<50} {:<50}".format("Name: "+name,"Contact: "+contact)+"\n")
    file.write("{:<50} {:<50}".format("Bill No: "+date,"Date: "+year+"/"+month+"/"+day)+"\n")
    file.write("\n")
    file.write("***********************************************************************************************\n")
    file.write("{:<10} {:<30} {:<20} {:<10} {:<10} {:<10}".format('ID','Name','Brand','Rate','Quantity','Price')+"\n")
    file.write("***********************************************************************************************\n")
    file.write("\n")

    print("------------------------------------------RENT INVOICE------------------------------------------")
    print("{:<50} {:<50}".format("Name: "+name,"Contact: "+contact))
    print("{:<50} {:<50}".format("Bill No: "+date,"Date: "+year+"/"+month+"/"+day))
    print("***********************************************************************************************")
    print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<10}".format('ID','Name','Brand','Rate','Quantity','Price'))
    print("***********************************************************************************************")    
            
    grand_total=0
    for i in range(len(cart)):
        c_id=int(cart[i][0])
        c_quantity=int(cart[i][1])
        c_name=main_data[c_id][0]
        c_brand=main_data[c_id][1]
        c_rate=main_data[c_id][2]
        c_price=float(c_rate.replace("$",""))*c_quantity
        grand_total+=c_price
        
        file.write("{:<10} {:<30} {:<20} {:<10} {:<10} {:<10}".format(str(i+1),c_name,c_brand,c_rate,str(c_quantity),"$"+str(c_price))+"\n")
        file.write("-----------------------------------------------------------------------------------------------\n")
        
        print("{:<10} {:<30} {:<20} {:<10} {:<10} {:<10}".format(str(i+1),c_name,c_brand,c_rate,str(c_quantity),"$"+str(c_price)))
        print("-----------------------------------------------------------------------------------------------")
        
    file.write("\n")    
    file.write("Grand Total: $"+str(grand_total)+"\n")
    print("Grand Total: $"+str(grand_total))
    file.close()            

    
def rent_costumes(records_list):
    '''
    Description
    -----------
    Runs a loop for continued renting
    Calls function for costume id and quantity.
    Adds in to cart
    Updates value in dictionary, and overwrites main file costumefile.txt
    Calls function to generate bill
    
    Parameter
    ---------
    records_list: list
    
    Return
    ------
    None
    '''
    
    continueLoop=True
    cart=[]
    while continueLoop==True:
        
        file_content=rent_return_functions.get_file_content()
        main_data=rent_return_functions.get_dictionary(file_content)
        rent_return_functions.print_costumes()
        costume_id=get_id()
        costume_quantity=get_quantity(costume_id)
        
        cart.append([costume_id,costume_quantity])
        main_data[costume_id][3]=str(int(main_data[costume_id][3])-costume_quantity)

        file=open("costumefile.txt","w")
        for value in main_data.values():
            write_data=value[0]+","+value[1]+","+value[2]+","+value[3]+"\n"
            file.write(write_data)
        file.close()
        
        
        Choice=input("Press 'Y' to rent more costumes. Press ANY KEY to continue: ").lower()
        if Choice=="y":
            continueLoop=True
        else:    
            continueLoop=False

    generate_bill(cart,records_list)

    print("\nThank you for the transaction. Press ENTER to go back to menu.")
    input()
