# """
#     - Semantic Scholar Rest API Documentation
#         - https://www.semanticscholar.org/product/api%2Ftutorial
#         - https://api.semanticscholar.org/api-docs/

#     - API key
#         - https://www.semanticscholar.org/product/api#api-key

#     - There are 3 APIs
#         - Academic Graph API - returns details about papers, paper 
#           authors, paper citations, references
#           Base URL: https://api.semanticscholar.org/graph/v1
#         - Recommendations API - recommends papers based on other papers
#           Base URL: https://api.semanticscholar.org/recommendations/v1
#         - Datasets API - allows download of Semantic Scholar's datasets
#           onto local machine
#           Base URL: https://api.semanticscholar.org/datasets/v1
    
#     - Endpoints
#         - A comprehensive list of endpoints is available here:
#           https://semanticscholar.readthedocs.io/en/stable/api.html
#         - The most relevant to this project are 
#             - /graph/v1/paper/search/bulk - primary keyword search endpoint
#             - /graph/v1/author/search - returns list of matching authors with their author_id
#             - /graph/v1/author/{author_id}/papers - returns that specific author's papers
#         - Optional
#             - /graph/v1/paper/batch - pulls data for 'known' papers rather than do fresh calls
#                                       to save resources
#             - /graph/v1/paper/{paper_id}/citations
#             - /graph/v1/paper/{paper_id}/references
        
#     - Example requests are here
#         - https://api.semanticscholar.org/api-docs/graph
    
#     - General principles
#         - Use API key - 1 request per second
#         - Use batch end points - Some endpoints have corresponding batch
#             or bulk endpoints that return more results in a single response.
#             E.g., paper relevance search (bulk version: paper bulk search), 
#             paper details endpoint (batch version: paper batch endpoint).
#         - Limit 'field' parameters - Most endpoints contain 'fields' query 
#             parameter that specifies which data is returned in the response.
#             It is good practice to avoid including unneeded fields to speed
#             up the response rate.
#         - Dataset Download - when you need a request rate that is faster than
#             that supported by the API key, you can download SS's dataset and
#             run your queries locally.
        

# """

import time
import requests
import os
from dotenv import load_dotenv

REQUEST_RATE = 0 # requests per second - assumes API key

load_dotenv()
SEMANTIC_SCHOLAR_API_KEY = os.environ.get("SEMANTIC_SCHOLAR_API_KEY")

def test_get_paper_title():
    # given a paper ID, get its title using this basic request
    #https://api.semanticscholar.org/graph/v1/paper/{paper_id}
    endpoint='https://api.semanticscholar.org/graph/v1/paper'
    paper_id = '649def34f8be52c8b66281af98ae884c09aef38b'
    url=f'{endpoint}/{paper_id}'
    headers={'X-API-KEY':SEMANTIC_SCHOLAR_API_KEY}
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(f'Unexpected status code {r.status_code}')
    if r.status_code == 429:
        print(r.headers.get("Retry-After"))
    else:
        print(r.json()) # use .json() function to get result as dict
    time.sleep(REQUEST_RATE)

def test_get_paper_details():
    # There is only one supported parameter: fields. This parameter takes 
    # a comma-separated string of field names. This tells the API what 
    # information to return in the response. Here are the supported fields:
    # paperId, corpusId, externalIds, url, title

    endpoint='https://api.semanticscholar.org/graph/v1/paper'
    paper_id = '649def34f8be52c8b66281af98ae884c09aef38b'
    url=f'{endpoint}/{paper_id}'
    headers={'X-API-KEY':SEMANTIC_SCHOLAR_API_KEY}
    params = {}
    params |= {'fields':'paperId,corpusId,externalIds,url,title,referenceCount,citationCount'}
    r = requests.get(url=url, params=params, headers=headers)
    if r.status_code != 200:
        print(f'Unexpected status code {r.status_code}')
    else:
        print(r.json())
    time.sleep(REQUEST_RATE)

def test_get_details_for_multiple_papers():
    # use requests.post with headers dict containing list of paper ids keyed on 'ids'
    url='https://api.semanticscholar.org/graph/v1/paper/batch'
    params={'fields':'paperId,title,referenceCount,citationCount'}
    json={'ids': ['649def34f8be52c8b66281af98ae884c09aef38b', 'ARXIV:1805.02262']}
    headers={'x-api-key':SEMANTIC_SCHOLAR_API_KEY}
    r = requests.post(url, params=params, headers=headers, json=json)
    if r.status_code == 429:
        print('Rate limit exceeded.')
    elif r.status_code == 503:
        print('Server is down.')
    elif r.status_code != 200:
        print(r'Unexpected status code {r.status_code}')
    else:
        print(r.json())
    
    time.sleep(REQUEST_RATE)

def test_search_for_papers_in_bulk():
    
    # accepted fields:
    #   query - + for AND, | for OR, - for negation, "" for collecting terms into phrase, * for matching prefix
    #       ( and ) for precedence, ~N after a word matches within the edit distance of N, 

    url='https://api.semanticscholar.org/graph/v1/paper/search/bulk'
    params={'fields':'paperId,title'}
    params|={'query':'prosthetic limbs'}
    params|={'sort':'publicationDate:desc'} # paperId, publicationDate, citationCount + ':' + 'asc/desc'
    headers={'x-api-key':SEMANTIC_SCHOLAR_API_KEY}
    r = requests.get(url, params=params, headers=headers)
    if r.status_code != 200:
        print(f'Status code: {r.status_code}')
        if r.status_code == 429:
            print(r.text[:300])
    else:
        print(r.json())
    
    time.sleep(REQUEST_RATE)

if __name__ == "__main__":
    # test_get_paper_title()
    # test_get_paper_details()
    # test_get_details_for_multiple_papers()
    test_search_for_papers_in_bulk()