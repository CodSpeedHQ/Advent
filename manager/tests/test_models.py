from manager.models import RepositoryModel


def test_from_issue_body_simple():
    # Sample issue body
    issue_body = """
### Repository URL

https://github.com/art049/AoC23

### Crate name

_No response_

### Subdirectory

_No response_

### Toolchain version

stable
"""
    # Parse the issue body
    repo = RepositoryModel.from_issue_body(issue_body)

    assert repo.model_dump(mode="json") == {
        "owner": "art049",
        "name": "AoC23",
        "crate": None,
        "subdir": None,
        "toolchain": "stable",
    }


def test_from_issue_body_monorepo():
    # Sample issue body
    issue_body = """
### Repository URL

https://github.com/adriencaccia/aoc

### Crate name

2023

### Subdirectory

2023

### Toolchain version

stable
"""
    # Parse the issue body
    repo = RepositoryModel.from_issue_body(issue_body)

    assert repo.model_dump(mode="json") == {
        "owner": "adriencaccia",
        "name": "aoc",
        "crate": "2023",
        "subdir": "2023",
        "toolchain": "stable",
    }
