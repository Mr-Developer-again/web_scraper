import requests

# Set the URL of the GraphQL file you want to download
graphql_url = "https://medium.com/_/graphql.json"

# Set the GraphQL query you want to execute (optional)
graphql_query = "{ hello }"

# Set the headers for the HTTP GET request
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Set the query parameters for the HTTP GET request
params = {
    "query": graphql_query,
}

# Send a GET request to the URL and get the GraphQL file content
response = requests.get(graphql_url, headers=headers, params=params)

# Save the GraphQL file content to a file
# filename = "myquery.graphql"
# with open(filename, 'w') as f:
#     f.write(response.text)

print(response.text)