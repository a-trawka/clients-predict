import datetime
import random

init_data = datetime.date(2017, 1, 1)
with open('clients_data.csv', 'w') as cdata:
    cdata.write('date,clients\n')
    for day in range(130):
        date = init_data + datetime.timedelta(days=day)
        cdata.write(str(date))   
        cdata.write(',')
        cdata.write(str(random.randrange(32, 129)))
        cdata.write('\n')
