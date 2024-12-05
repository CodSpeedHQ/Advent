import sys
from manager.models import RepositoryModel
from manager.repository_repository import RepositoryRepository
from manager.github import GITHUB_ADVENT_REPO, github_client


def main(issue_number: int):
    issue = GITHUB_ADVENT_REPO.get_issue(issue_number)
    issue_author = issue.user.login
    issue_body = issue.body
    repo = RepositoryModel.from_issue_body(issue_body)
    assert repo.owner == issue_author, "Repository must be owned by the issue author"
    if r := github_client.get_repo(f"{repo.owner}/{repo.name}").full_name is None:
        issue.create_comment(f"Failed to add repository: {r}")
        raise Exception(f"Failed to add repository {repo.owner}/{repo.name}: {r}")

    try:
        RepositoryRepository.save(repo)
    except ValueError as e:
        issue.create_comment(f"Failed to add repository: {e}")
        raise Exception(f"Failed to add repository {repo.owner}/{repo.name}: {e}")

    issue.create_comment("Repository added successfully! :tada:")
    issue.edit(state="closed")
    print(f"Repository added: {repo.owner}/{repo.name}")


if __name__ == "__main__":
    issue_number = int(sys.argv[1])
    main(issue_number)
