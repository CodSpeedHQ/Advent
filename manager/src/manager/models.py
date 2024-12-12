import re
from typing import Optional

from pydantic import BaseModel, HttpUrl


def validate_github_url(url: str) -> HttpUrl:
    url = HttpUrl(url)
    if url.scheme != "https":
        raise ValueError("Only HTTPS URLs are supported")
    if url.host != "github.com":
        raise ValueError("Only GitHub repositories are supported")
    if url.fragment is not None or url.query is not None:
        raise ValueError(
            "Fragments and queries are not supported, please provide the raw URL"
        )
    path = url.path.split("/")[1:]
    if len(path) != 2:
        raise ValueError("Please provide a link to a repository, not to a file")
    return url


def handle_github_issue_optional_response(response: str) -> Optional[str]:
    if response == "_No response_":
        return None
    return response


class RepositoryModel(BaseModel):
    owner: str
    name: str

    crate: Optional[str] = None
    subdir: Optional[str] = None
    toolchain: str

    model_config = {
        "str_strip_whitespace": True,
    }

    @property
    def name(self) -> str:
        return self.url.path[1:]

    @classmethod
    def from_issue_body(cls, issue_body: str):
        url_pattern = r"### Repository URL\s*\n\s*(.+)"
        toolchain_pattern = r"### Toolchain version\s*\n\s*(.+)"
        crate_pattern = r"### Crate name\s*\n\s*(.+)"

        crate = handle_github_issue_optional_response(
            re.search(crate_pattern, issue_body).group(1).strip()
        )
        toolchain = handle_github_issue_optional_response(
            re.search(toolchain_pattern, issue_body).group(1).strip()
        )
        if toolchain is None:
            toolchain = "stable"

        url = validate_github_url(re.search(url_pattern, issue_body).group(1))
        owner, name = url.path[1:].split("/")
        return cls(
            owner=owner,
            name=name,
            crate=handle_github_issue_optional_response(crate),
            subdir=handle_github_issue_optional_response(subdir),
            toolchain=toolchain,
        )
