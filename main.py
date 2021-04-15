import requests

response = requests.get("https://api.github.com/users/lalidiaz/repos")
my_repos = response.json()

# print out for each project: project name and project url (repo url).
for project in my_repos:
    print(f"Project name: {project['name']}.\nProject url: {project['url']}.\n")



