import console
import datetime
import time
import requests

import lls

def main():
    config = lls.get_config()

    url = config['LLS_URL'] + '/api/v1/weight/record'

    weight_time = time.time()
    weight = float(console.input_alert('Your current weight in kilograms'))

    query_params = {'datetime': int(time.time()), 'weight': weight}
    print(f'data: {query_params}')
    for x in range(10):
        response = requests.post(url, params=query_params, headers={'token': config['LLS_TOKEN']})
        if response.status_code == 201:
            print("Success")
            break
        print(f'Failed: {response}, {response.content}')

assert(__name__ == "__main__")
main()
