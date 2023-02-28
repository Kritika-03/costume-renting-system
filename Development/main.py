import rent_functions
import rent_return_functions
import records
import return_functions
'''
The main loop of the program where the main menu is displayed.
It calls the rent functoin if user chooses 1.
It calls the return functoin if user chooses 2.
It displays search menu if user chooses 3.
    In the search menu loop, if user choose 1 it calls the view_rent_bill function
                             if user choose 2 it calls the view_return_bill function
                             if user chooses 3 the loop ends and it goes back to main loop
It ends the program if user chooses 4.
Any other input displays an invalid message.
'''
continueLoop=True
customerChoice=0
records_list=[]
print("-----------------------------")
print("***********WELCOME***********")
print("-----------------------------")
while continueLoop==True:
    print()
    print("-----------------------------")
    print("1\tRent Costumes")
    print("2\tReturn Costumes")
    print("3\tView Customer Record")
    print("4\tExit")
    print("-----------------------------")
    print()
    customerChoice=input("\nEnter the number of your choice: ")

    if customerChoice=="1":
        rent_functions.rent_costumes(records_list)
    elif customerChoice=="2":
        return_functions.return_costumes(records_list)
    elif customerChoice=="3":
        inner_continueLoop=True

        while inner_continueLoop==True:
            print("-----------------------------")
            print("***********SEARCH***********")
            print("-----------------------------")
            print()
            print("1\tRENT BILL")
            print("2\tRETURN BILL")
            print("3\tBACK TO MENU")
            print("-----------------------------")
            print()
            inner_customerChoice=input("\nEnter the number of your choice: ")

            if inner_customerChoice=="1":
                records.view_rent_bill(records_list)
            elif inner_customerChoice=="2":
                records.view_return_bill(records_list)
            elif inner_customerChoice=="3":
                inner_continueLoop=False
            else:
                print()
                print("------------------------------")
                print("\tINVALID INPUT!!!\t")
                print("------------------------------")
                print()
                
    elif customerChoice=="4":
        print("-----------------------------------------------------")
        print("***********THANK YOU FOR USING THE PROGRAM***********")
        print("-----------------------------------------------------")
        continueLoop=False
    else:
        print()
        print("------------------------------")
        print("\tINVALID INPUT!!!\t")
        print("------------------------------")
        print()
