from application.salary import calculate_salary
from application.db.people import get_employees

def main():
    # Вызов функций из других модулей
    calculate_salary()
    get_employees()

if __name__ == '__main__':
    main()

from datetime import datetime

def print_current_date():
    current_date = datetime.now()
    print("Текущая дата: ", current_date)

if __name__ == "__main__":
    print_current_date()