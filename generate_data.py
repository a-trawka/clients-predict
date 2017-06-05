import datetime
import random

clients = 31
with open('clients_data.csv', 'w') as cdata:
    cdata.write('days_since_start,clients\n')
    for day in range(100):
        # date = init_date + datetime.timedelta(days=day)
        cdata.write(str(day))
        cdata.write(',')
        clients += random.randrange(-2, 4)
        cdata.write(str(clients))
        cdata.write('\n')
