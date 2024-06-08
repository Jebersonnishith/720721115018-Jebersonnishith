import requests

def search_stack_overflow(query, page=1, page_size=10):
    url = "https://api.stackexchange.com/2.3/search/advanced"
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': 'stackoverflow',
        'pagesize': page_size,
        'page': page
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code != 200:
        raise Exception(f"Error: {response.status_code}")
    
    return response.json()

def display_results(results):
    for i, item in enumerate(results['items'], 1):
        print(f"Result {i}:")
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Creation Date: {item['creation_date']}")
        print(f"Score: {item['score']}")
        print(f"Answer Count: {item['answer_count']}")
        print()

if __name__ == "__main__":
    query = input("Enter your search query: ")
    results = search_stack_overflow(query)
    display_results(results)
