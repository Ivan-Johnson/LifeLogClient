#import console
import datetime
import time
import requests
import csv
import uuid

import lls

def main():
    config = lls.get_config()
    url = config['LLS_URL'] + '/api/v1/weight/entry'

    offset = time.mktime((datetime.date(1970, 1,1)).timetuple())
    #data.csv is a csv of format:
    #YYYY-MM-DD-HH-MM-SS\tweight
    with open('data.csv', newline='') as fd:
        reader = csv.reader(fd, skipinitialspace=True, delimiter='\t', strict=True)
        i = 0
        for row in reader:
            i += 1
            print(f'\r{i}: {row}', end='')
            assert(len(row)==2)
            sdate = row[0]
            weight = float(row[1])

            date_components = sdate.split('-')
            assert(len(date_components) == 6)
            year = int(date_components[0])
            month = int(date_components[1])
            day = int(date_components[2])
            hour = int(date_components[3])
            minute = int(date_components[4])
            second = int(date_components[5])

            date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
            seconds = time.mktime(date.timetuple())
            unix = seconds - offset

            cacheid = uuid.uuid4()


            query_params = {'datetime': int(unix), 'weight': float(weight), 'units': 'kilograms'}
            response = requests.post(url, params=query_params, headers={'token': config['LLS_TOKEN']})
            if response.status_code != 201:
                import pdb; pdb.set_trace()
                print(f"{response.status_code}\t{sdate}\t{str(weight)}\t{cacheid}")
        print('')

assert(__name__ == "__main__")
main()
