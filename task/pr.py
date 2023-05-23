#https://github.com/Azure/azure-devops-cli-extension/blob/master/azure-devops/azext_devops/dev/repos/pull_request.py

from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from azure.devops.v7_1.git.models import GitPullRequestSearchCriteria, GitPullRequest, GitPullRequestCompletionOptions

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--sourceRefName", help="Provide the name of the source branch.", default="features/new")
parser.add_argument("--targetRefName", help="Provide the name of the target branch.", default="develop")
parser.add_argument("--repo", help="Provide the name of the repository.", default="usitsupport")
parser.add_argument("--proj", help="Provide the name of the project.", default="usitsupport")
parser.add_argument("--org", help="Provide the name of the organization.", default="usitsupport")

parse_args = parser.parse_args()

# Fill in with your personal access token and org URL
personal_access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
organization_url = f'https://dev.azure.com/{parse_args.org}'

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "git" client provides access to repository)
git_client = connection.clients.get_git_client()

get_repositories_response = git_client.get_repositories()

for repo in get_repositories_response:
    if repo.name == parse_args.repo:
        REPO_ID = repo.id
        REPO_NAME = repo.name

search_criteria = GitPullRequestSearchCriteria( repository_id=REPO_ID )

pr_project_response = git_client.get_pull_requests_by_project(project=parse_args.proj, search_criteria=search_criteria)

PR_ID = 0

if pr_project_response:
    for prs in pr_project_response:        
        if (prs.status == 'active') and (prs.description == f"Auto-PR-{parse_args.sourceRefName}-to-{parse_args.targetRefName}"):
            PR_ID = prs.pull_request_id
            break

if PR_ID > 0:
    pr_for_update = GitPullRequest()
    completion_options = GitPullRequestCompletionOptions()
    completion_options.delete_source_branch = True
    pr_for_update.completion_options = completion_options

    pr_update_response = git_client.update_pull_request(repository_id=REPO_ID,pull_request_id=PR_ID,git_pull_request_to_update=pr_for_update)

    print(f"PR:{pr_update_response.description} atualizado! - Merge Status: {pr_update_response.merge_status}")
else:
    args = {
        "git_pull_request_to_create": {
            "sourceRefName": f"refs/heads/{parse_args.sourceRefName}",
            "targetRefName": f"refs/heads/{parse_args.targetRefName}",
            "delete_source_branch": "true",
            "title": f"Auto-PR-{parse_args.sourceRefName}-to-{parse_args.targetRefName}",
            "description": f"Auto-PR-{parse_args.sourceRefName}-to-{parse_args.targetRefName}",
        },
        "repository_id": REPO_ID,
    }
    pr_create_response = git_client.create_pull_request(**args)

    print(f"PR:{pr_create_response.description} criado! - Merge Status: {pr_create_response.merge_status}")
