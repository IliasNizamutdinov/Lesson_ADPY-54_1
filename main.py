from application.salary import calculate_salary as cal_sl
from application.db.people import get_employees as get_epmp
from datetime import date

if __name__ == '__main__':
    cal_sl()
    get_epmp()
    print(f"Текущая дата: {date.today()}")