class Data:
    def __init__(self, user_date: str):
        self.user_date = user_date

    @classmethod
    def extract_data(cls, user_date):
        day = int(user_date[:2])
        month = int(user_date[3:5])
        year = int(user_date[6:10])
        print("Day:", day, "Month:", month, "Year:", year)
        return day, month, year

    @staticmethod
    def validate_data(user_date: str):
        if int(user_date[:2]) > 31:
            print("Invalid number of days")
        if int(user_date[3:5]) > 12:
            print("Invalid month")
        if int(user_date[6:10]) < 1900 or int(user_date[6:10]) > 2021:
            print("Invalid year")


a = input("Enter a date in the dd-mm-yyyy format: ")
Data.extract_data(a)
Data.validate_data(a)
