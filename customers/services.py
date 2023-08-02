import csv
import io
from datetime import datetime

from django.core.files.uploadedfile import InMemoryUploadedFile

from customers.models import Deal, Customer, Gem


def parse_csv_file(file: InMemoryUploadedFile) -> list[Deal]:
    reader = csv.DictReader(io.StringIO(file.read().decode('utf-8')))
    deals = []
    for row in reader:
        username = row.get('customer')
        customer, _ = Customer.objects.get_or_create(username=username)
        item = row.get('item')
        gem, _ = Gem.objects.get_or_create(name=item)
        date_str = row.get('date')
        date_format = '%Y-%m-%d %H:%M:%S.%f'
        date = datetime.strptime(date_str, date_format)
        deals.append(Deal(
            customer=customer,
            gem=gem,
            date=date,
            money=int(row.get('total')),
            quantity=int(row.get('quantity')),
        ))
    return deals
