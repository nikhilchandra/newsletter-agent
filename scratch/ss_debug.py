import time
import requests
import os
from dotenv import load_dotenv

REQUEST_RATE = 1 # requests per second - assumes API key
BASELINE_DELAY = 1 / REQUEST_RATE

load_dotenv()
SEMANTIC_SCHOLAR_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")
assert SEMANTIC_SCHOLAR_API_KEY, 'API key not loaded - check .env'

def delay_next_request(delay):
    print(f'Waiting {delay:0.2f}s before next attempt...')
    time.sleep(delay + 0.2) # delay slightly more than needed

def test_get_paper_title():
    paper_id = '649def34f8be52c8b66281af98ae884c09aef38b'
    url=f'https://api.semanticscholar.org/graph/v1/paper/{paper_id}'
    headers={'X-API-KEY':SEMANTIC_SCHOLAR_API_KEY}
    r = requests.get(url, headers=headers)
    if r.status_code != 200: 
        print(f'Unexpected status code {r.status_code}')
        if r.status_code == 429:
            # print(f'Retry After: {r.headers.get("Retry-After")}')
            print(r.text[:300])
    else: 
        print(r.json()) # use .json() function to get result as dict

    return r.status_code

if __name__ == "__main__":
    delay = BASELINE_DELAY
    while 1==1:
        status_code = test_get_paper_title()
        if status_code == 200:
            delay = BASELINE_DELAY
        else:
            delay *= 2
        delay_next_request(delay)
        
    print('Done.')