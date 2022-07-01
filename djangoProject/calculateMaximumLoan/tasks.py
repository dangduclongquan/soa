from celery import Celery
from djangoProject.models import *
import datetime
app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def calculate(customer: Customer, bank: Bank):
    if customer.creditScore < bank.minimumCreditScore:
        return 0
    return (datetime.datetime.now().year - customer.dob.year) * customer.creditScore
