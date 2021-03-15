def user_data_output(name, surname, year, city, email, phone):
    print(f"First name: {name}; Last name: {surname}; Born in: {year}; Lives in: {city}; Email: {email}; Phone: {phone}")
    return

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
dob = input("Enter the year your were born in: ")
city_name = input("Enter your city: ")
email_address = input("Enter your email address: ")
phone_number = input("Enter your phone number: ")
user_data_output(name=first_name, surname=last_name, year=dob, city=city_name,
                 email=email_address, phone=phone_number)


