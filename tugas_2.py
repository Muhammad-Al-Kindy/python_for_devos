import requests

# Replace 'your_username' and 'your_repository' with the actual repository owner and name
owner = 'wijamw'
repo = 'api-request'

# Send a request to the GitHub API
response = requests.get(f'https://api.github.com/repos/{owner}/{repo}')

# Make sure the request was successful
if response.status_code == 200:
    # Get the repository ID from the JSON response
    repo_id = response.json()['id']
    git_url = response.json()['git_url']
    user_id = response.json()['owner']['id']
    print(f'Repository ID: {repo_id}')
    print(f'Repository GIT Url: {git_url}')
    print(f'User ID: {user_id}')
else:
    print('Failed to fetch repository data')