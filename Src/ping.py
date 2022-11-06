#import console
import datetime
import time
import requests
import csv
import uuid

import lls

def main():
    config = lls.get_config()
    url = config['LLS_URL'] + '/api/v1/ping'

    query_params = {}
    response = requests.get(url, params=query_params, headers={'token': config['LLS_TOKEN']})
    print(response)
    print(response.text)

assert(__name__ == "__main__")
main()

#original: acc0300a-e082-45cb-a8ad-00548c59daab|8c94d994-5b3d-483e-8563-266ad0ba8b71|1592104858|83.6
