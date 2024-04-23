# import requests
# url = "https://github.com/wijamw/api-request.git"

# # for project in my_projects:
# #     print(f"Project Name: {project['name']}\nProject Url: {project['web_url']}\n")

# def get_repo_name_from_url(url: str) -> str:
#     last_slash_index = url.rfind("/")
#     last_suffix_index = url.rfind(".git")
#     if last_suffix_index < 0:
#         last_suffix_index = len(url)

#     if last_slash_index < 0 or last_suffix_index <= last_slash_index:
#         raise Exception("Badly formatted url {}".format(url))

#     return url[last_slash_index + 1:last_suffix_index]
# repo_name = get_repo_name_from_url(url)

# print(repo_name)

import requests

# Replace this with the actual GitHub repository URL
repo_url = "https://github.com/username/reponame"

# Extract the owner and repo name from the URL
owner, repo_name = repo_url.split("/")[3:5]

# Construct the API URL
api_url = f"https://github.com/wijamw/api-request.git"

# Make a request to the API
response = requests.get(api_url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the repository ID
    repo_id = data["id"]
    print(f"Repository ID: {repo_id}")
else:
    print("Failed to get repository ID")