import os
from datetime import datetime
from urllib.request import urlopen

URL = os.environ['URL']  # URL of the site to check, stored in the site environment variable
STRING = os.environ['STRING']  # String expected to be on the page, stored in the expected environment variable


def validate(res):
    '''Return False to trigger the canary

    Currently this simply checks whether the EXPECTED string is present.
    However, you could modify this to perform any number of arbitrary
    checks on the contents of SITE.
    '''
    return STRING in res


def lambda_handler(event, context):
    print('Checking {} at {}...'.format(URL, event['time']))
    try:
        if not validate(str(urlopen(URL).read())):
            raise Exception('Validation failed')
    except:
        print('Check failed!')
        raise
    else:
        print('Check passed!')
        return event['time']
    finally:
        print('Check complete at {}'.format(str(datetime.now())))
