import json
from pathlib import Path
from manager.models import RepositoryModel
from pydantic import TypeAdapter
from git import Repo

GIT_REPOSITORY_PATH = Path("..")
REPOSITORY_DATA_PATH = Path("./data/repositories.json")
ABS_REPOSITORY_DATA_PATH = GIT_REPOSITORY_PATH / REPOSITORY_DATA_PATH


class RepositoryRepository:
    _list_adapter = TypeAdapter(list[RepositoryModel])

    @classmethod
    def find_all(cls) -> list[RepositoryModel]:
        with ABS_REPOSITORY_DATA_PATH.open("rb") as f:
            return cls._list_adapter.validate_json(f.read())

    @classmethod
    def save(cls, input: RepositoryModel):
        all_repositories = cls.find_all()
        if input in all_repositories:
            raise ValueError("Repository already exists")
        if any(input.owner == repo.owner for repo in all_repositories):
            raise ValueError(f"{input.owner} already has a repository, only one repository per user is allowed")
        all_repositories.append(input)
        with ABS_REPOSITORY_DATA_PATH.open("wb") as f:
            out = cls._list_adapter.dump_python(all_repositories, mode="json")
            f.write(json.dumps(out, indent=2).encode("utf-8"))
        git_repo = cls._get_git_repo()
        git_repo.git.add(REPOSITORY_DATA_PATH)
        git_repo.index.commit(f"Add repository: {input.owner}/{input.name}")
        git_repo.remotes.origin.push()

    @staticmethod
    def _get_git_repo() -> Repo:
        git_repo = Repo(GIT_REPOSITORY_PATH)
        git_repo.config_writer().set_value(
            "user", "email", "codspeed-advent-bot@@users.noreply.github.com"
        ).set_value("user", "name", "codspeed-advent[bot]").release()
        return git_repo
