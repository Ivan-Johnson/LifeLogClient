#import console
import datetime
import time
import requests
import csv
import uuid

import lls

def main():
    config = lls.get_config()
    url = config['LLS_URL'] + '/api/v1/weight/record'

    offset = time.mktime((datetime.date(1970, 1,1)).timetuple())
    #data.csv is a csv of format:
    #YYYY-MM-DD\tweight
    with open('data.csv', newline='') as fd:
        reader = csv.reader(fd, skipinitialspace=True, delimiter='\t', strict=True)
        for row in reader:
            assert(len(row)==2)
            sdate = row[0]
            weight = float(row[1])

            date_components = sdate.split('-')
            assert(len(date_components) == 3)
            year = date_components[0]
            month = date_components[1]
            day = date_components[2]

            date = datetime.date(year=int(year), month=int(month), day=int(day))
            seconds = time.mktime(date.timetuple())
            unix = seconds - offset

            cacheid = uuid.uuid4()


            query_params = {'datetime': int(unix), 'weight': float(weight)}
            response = requests.post(url, params=query_params, headers={'token': config['LLS_TOKEN']})
            if response.status_code != 201:
                print(f"{response.status_code}\t{sdate}\t{str(weight)}\t{cacheid}")

assert(__name__ == "__main__")
main()

#original: acc0300a-e082-45cb-a8ad-00548c59daab|8c94d994-5b3d-483e-8563-266ad0ba8b71|1592104858|83.6
