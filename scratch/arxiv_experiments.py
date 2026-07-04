import time
import requests
import feedparser

"""
    - from https://info.arxiv.org/help/api/user-manual.html#python_simple_example

    - prefixes for fields that can be searched:
        - ti        Title
        - au        Author
        - abs       Abstract
        - co        Comment
        - jr        Journal Reference
        - cat       Subject Category
        - rn        Report Number
        - id        Id (use id_list instead)
        - all       All of the above
    
    - date filtering
        - The API provides one date filter, submittedDate, that allows you to select data 
          within a given date range of when the data was submitted to arXiv.
        - The expected format is [YYYYMMDDTTTT+TO+YYYYMMDDTTTT] where TTTT is provided in 
          24-hour time to the minute, in GMT. 
        - e.g.: https://export.arxiv.org/api/query?search_query=au:del_maestro+AND+submittedDate:[202301010600+TO+202401010600]
        - Question: should we incorporate time zones?

    - Boolean operators
        - AND
        - OR
        - ANDNOT - allows filtering of search results based on certain fields
            - e.g., find all articles by Adrian Del Maestro with titles that don't contain 'checkerboard'
                    https://export.arxiv.org/api/query?search_query=au:del_maestro+ANDNOT+ti:checkerboard
    
    - grouping operators
        - () - used to group Boolean expressions for Boolean operator precedence
        - double quotes - used to group multiple words into phrases to search a particular field
        - space - used to extend a search_query to include multiple fields
"""

def test_arxiv_request():
    url=r'https://export.arxiv.org/api/query'
    params = {}
    params |= {'search_query':f'ti:prosthetics AND abs:"sensory feedback"'}
    params |= {'start':0}
    params |= {'max_results':10}
    params |= {'sortBy':'submittedDate'} # relevance, lastUpdatedDate, submittedDate
    params |= {'sortOrder':'descending'} # ascending, descending

    # params={'search_query':'all:sensory', 'start':0, 'max_results':2}
    print('Starting request to server')
    start_time = time.perf_counter()
    try:
        r = requests.get(url, params=params, timeout=10)
    except requests.exceptions.ReadTimeout as e:
        print('Request timed out.')
        print(e)
        return
    end_time = time.perf_counter()
    print(f'Request took {end_time - start_time:.2f} seconds to execute.\n')
    if r.status_code==429:
        print('Rate limit exceeded.')
    elif r.status_code==503:
        print('Server is down.')
    elif r.status_code != 200:
        print(f'Unexpected status code: {r.status_code}')
    else:
        feed = feedparser.parse(r.text)
        for entry in feed.entries:

            # print(f'id: {entry["id"]}')
            # print(f'guidislink: {entry["guidislink"]}')
            # print(f'link: {entry["link"]}')
            # print(f'title: {entry["title"]}')
            # print(f'title_detail: {entry["title_detail"]}')
            # print(f'updated: {entry["updated"]}')
            # print(f'updated_parsed: {entry["updated_parsed"]}')
            # print(f'links: {entry["links"]}')
            # print(f'summary: {entry["summary"]}')
            # print(f'summary_detail: {entry["summary_detail"]}')
            # print(f'tags: {entry["tags"]}')
            # print(f'published: {entry["published"]}')
            # print(f'published_parsed: {entry["published_parsed"]}')
            # print(f'arxiv_comment: {entry["arxiv_comment"]}')
            # print(f'arxiv_primary_category: {entry["arxiv_primary_category"]}')
            # print(f'arxiv_journal_ref: {entry["arxiv_journal_ref"]}')
            # print(f'authors: {entry["authors"]}')
            # print(f'author_detail: {entry["author_detail"]}')
            # print(f'author: {entry["author"]}')

            # print(f'ID: {entry["id"]}')
            # print(f'Title: {entry['title']}')
            # print(f'Authors: {", ".join([x["name"] for x in entry["authors"]])}')
            # print(f'Published: {entry["published"]}')
            # print(f'Webpage: {entry["links"][0]["href"]}')
            # print(f'PDF: {entry["links"][1]["href"]}')
            # print(f'Summary: {entry["summary"]}')

            # print()

            print(f'{entry['published']}: {entry['title']}')

    print()
    print(f'This is the URL that was generated: {r.url}')

    time.sleep(3)

    return

if __name__=="__main__":
    test_arxiv_request()