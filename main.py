from application import salary, people, db
from datetime import datetime

if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print(datetime.now())


