import sys
from manager.github import GITHUB_ADVENT_REPO
from manager.repository_repository import RepositoryRepository

SCHEDULE_RUN_WORKFLOW = GITHUB_ADVENT_REPO.get_workflow("schedule-run.yml")


def main(day: str):
    repos = RepositoryRepository.find_all()
    for repo in repos:
        print(f"Running {repo.owner}/{repo.name} for day {day}")
        r = SCHEDULE_RUN_WORKFLOW.create_dispatch(ref="main", inputs={
            "repo_fullname": f"{repo.owner}/{repo.name}",
            "toolchain": repo.toolchain,
            "crate": repo.crate,
            "subdir": repo.subdir,
            "day": day
        })
        if not r:
            print(f"Failed to run {repo.owner}/{repo.name}")

if __name__ == "__main__":
    day = sys.argv[1]
    print(f"Running all repos for day {day}")
    main(day)
