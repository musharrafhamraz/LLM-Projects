# from phi.tools.duckduckgo import DuckDuckGo

# def main():
#     # Initialize the DuckDuckGo tool
#     duckduckgo_tool = DuckDuckGo()

#     # Define the search query
#     query = "machine"

#     # Perform the search using the correct method
#     try:
#         results = duckduckgo_tool.duckduckgo_search(query)

#         # Print the results to the console
#         print(f"Search Results for: '{query}'\n")
#         for idx, result in enumerate(results, 1):
#             print(f"[{idx}] {result['title']} - {result['url']}")
#             print(f"Snippet: {result.get('snippet', 'No snippet available')}\n")
#     except AttributeError as e:
#         print("Error: The 'DuckDuckGo' object does not have the expected search method.")
#         print("Please verify the correct method name in the DuckDuckGo class.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()

# from phi.tools.duckduckgo import DuckDuckGo

# def main():
#     # Initialize the DuckDuckGo tool
#     duckduckgo_tool = DuckDuckGo()

#     # Define the search query
#     query = "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"

#     # Perform the search using the correct method
#     try:
#         results = duckduckgo_tool.duckduckgo_search(query)

#         # Debug: Print raw results to inspect the structure
#         print(f"Raw Results for: '{query}'\n")
#         print(results)

#         # If results are a list of dictionaries, process them
#         if isinstance(results, list):
#             print(f"\nProcessed Results for: '{query}'\n")
#             for idx, result in enumerate(results, 1):
#                 title = result.get('title', 'No title available')
#                 url = result.get('url', 'No URL available')
#                 snippet = result.get('snippet', 'No snippet available')
#                 print(f"[{idx}] {title} - {url}")
#                 print(f"Snippet: {snippet}\n")
#         else:
#             print("\nThe results are not in the expected format (list). Please inspect the raw output above.")
#     except AttributeError as e:
#         print("Error: The 'DuckDuckGo' object does not have the expected search method.")
#         print("Please verify the correct method name in the DuckDuckGo class.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# if __name__ == "__main__":
#     main()



import requests
from bs4 import BeautifulSoup

def main():
    # Define the URL for the SEO guide
    url = "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"

    # Perform the request to get the webpage content
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the page content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Print the title of the page
            title = soup.find('title').get_text() if soup.find('title') else 'No title available'
            print(f"Page Title: {title}\n")

            # Extract all headings (h1, h2, h3, etc.)
            headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            print("Headings:\n")
            for heading in headings:
                print(f"{heading.name}: {heading.get_text()}")
            
            # Extract all paragraphs and content
            print("\nContent:\n")
            paragraphs = soup.find_all('p')
            for para in paragraphs:
                print(para.get_text())

        else:
            print(f"Failed to retrieve the page. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the webpage: {e}")

if __name__ == "__main__":
    main()
