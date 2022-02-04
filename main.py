from collections import OrderedDict

#Vehicle inventory stored in a dictonary
inventory = OrderedDict()
inventory = {
    'bikes':2,
    'cycle':3,
    'car':1,
    'boat':2
}

#List that contains customers
customer_list = []

#List that contains rentals
rental_list = []

#Customer class
class Customer:
    def __init__(self, name, email, phone):
        self.customer_name = name
        self.email_address = email
        self.phone_number = phone

    def __str__(self) -> str:
        customer_data = (self.customer_name, self.email_address, self.phone_number)
        return str(customer_data)

#Rental class
class Rentals:
    def __init__(self, name, rental_date, return_date, vehicle_type):
        self.customer_name = name
        self.rental_date = rental_date
        self.return_date = return_date
        self.vehicle_type = vehicle_type

    def __str__(self) -> str:
        rental_data = (self.customer_name, self.rental_date, self.return_date, self.vehicle_type)
        return str(rental_data)

#Function to add customer
def add_customer():    
    name = input('Name : ')
    email = input('Email : ')
    phone = input('Phone Number : ')
    customer = Customer(name, email, phone)

    #Adding customer object to the customer list
    customer_list.append(customer)

    return print(f'Customer added successfully! -> {customer}')

#Function to add rentals
def add_rental_booking():
    for number, customer in enumerate(customer_list):
        print(number, customer.customer_name)

    cust_number = int(input('\nSelect a customer number from above : '))
    rental_date = input('Please enter a rental date : ')
    return_date = input('Please enter a return date : ')
    
    #Adding vehicles and their corresponding numbers
    vehicle_list = ['bikes', 'cycle', 'car', 'boat']
    for number, vehicle in enumerate(inventory.keys()):
        print(number, vehicle)

    vehicle_number = int(input('Please select a vehicle from above : '))
    vehicle_type = vehicle_list[vehicle_number]

    if inventory[vehicle_type] > 0:
        rental_booking = Rentals(customer_list[cust_number].customer_name, rental_date, return_date, vehicle_type)

        #Adding rentals to the rental list
        rental_list.append(rental_booking)

        inventory[vehicle_type] -= 1
        return print(f'Rental added successfully! -> {rental_booking}')
    else:
        return print(f'{vehicle_type} cannot be rented as it is already booked')

#Function to view customer list
def view_customer_list():
    if customer_list:
        for customer in customer_list:
            print(f'Name : {customer.customer_name}, Email : {customer.email_address}, Mobile : {customer.phone_number}')
    else:
        print('No customers added')

#Function to view rental list
def view_rental_list():
    if rental_list:
        for rental in rental_list:
            print(f'Name : {rental.customer_name}, Rental Date : {rental.rental_date}, Return Date : {rental.return_date}, Vehicle Type : {rental.vehicle_type}')
    else:
        print('No rental bookings added')

#Function to view vehicle inventory
def view_inventory():
    print(f'List of vehicles : {inventory}')



#Main function
if __name__ == '__main__':
    while True:
        print('\nMENU : ')
        print('1. Add Customer')
        print('2. Add Rental Booking')
        print('3. See Customer List')
        print('4. See Rental Booking List')
        print('5. See Inventory of Vehicles Available')
        print('6. Exit')

        option = input('Please select a number: ')

        if option == '1':
            add_customer()

        elif option == '2':
            add_rental_booking()

        elif option == '3':
            view_customer_list()

        elif option == '4':
            view_rental_list()

        elif option == '5':
            view_inventory()

        elif option == '6':
            break

        else:
            print('\nInvalid Option')
        
