"""
    - Semantic Scholar Rest API Documentation
        - https://www.semanticscholar.org/product/api%2Ftutorial
        - https://api.semanticscholar.org/api-docs/

    - API key
        - https://www.semanticscholar.org/product/api#api-key

    - There are 3 APIs
        - Academic Graph API - returns details about papers, paper 
          authors, paper citations, references
          Base URL: https://api.semanticscholar.org/graph/v1
        - Recommendations API - recommends papers based on other papers
          Base URL: https://api.semanticscholar.org/recommendations/v1
        - Datasets API - allows download of Semantic Scholar's datasets
          onto local machine
          Base URL: https://api.semanticscholar.org/datasets/v1
    
    - Endpoints
        - A comprehensive list of endpoints is available here:
          https://semanticscholar.readthedocs.io/en/stable/api.html
        - The most relevant to this project are 
            - /graph/v1/paper/search/bulk - primary keyword search endpoint
            - /graph/v1/author/search - returns list of matching authors with their author_id
            - /graph/v1/author/{author_id}/papers - returns that specific author's papers
        - Optional
            - /graph/v1/paper/batch - pulls data for 'known' papers rather than do fresh calls
                                      to save resources
            - /graph/v1/paper/{paper_id}/citations
            - /graph/v1/paper/{paper_id}/references
        
        - Example requests are here
            - https://api.semanticscholar.org/api-docs/graph
        
        - General principles
            - Use API key - 1 request per second
            - Use batch end points - Some endpoints have corresponding batch
                or bulk endpoints that return more results in a single response.
                E.g., paper relevance search (bulk version: paper bulk search), 
                paper details endpoint (batch version: paper batch endpoint).
            - Limit 'field' parameters - Most endpoints contain 'fields' query 
                parameter that specifies which data is returned in the response.
                It is good practice to avoid including unneeded fields to speed
                up the response rate.
            - Dataset Download - when you need a request rate that is faster than
                that supported by the API key, you can download SS's dataset and
                run your queries locally.
        

"""