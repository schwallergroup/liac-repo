#!/usr/bin/env python

"""Code to run after generating the project."""

import os
import pathlib
from git import Repo

PROJECT_DIRECTORY = pathlib.Path(os.path.realpath(os.path.curdir)).resolve()
PACKAGE = PROJECT_DIRECTORY.joinpath("src", "{{ cookiecutter.package_name }}")
DOCS = PROJECT_DIRECTORY.joinpath("docs", "source")


def git_init():
    os.chdir(PROJECT_DIRECTORY)
    repo_url = "https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}.git"
    empty_repo = Repo.init()
    origin = empty_repo.create_remote(
        'origin',
        repo_url
    )
    empty_repo.git.add(all=True)
    empty_repo.index.commit("first_commit")
    main_branch = empty_repo.create_head('main')
    main_branch.checkout()

    try:
        # Try to push to GitHub
        origin.push(refspec="main:main")
        empty_repo.heads.main.set_tracking_branch(origin.refs.main)
        print(f'\nRepo successfully pushed to GitHub!\nCheck it out at {repo_url}\n')
    except:
        # If it fails, it's probably because the repo doesn't exist yet
        print("Failed to push to GitHub. Create a repo on @schwallergroup with name {{cookiecutter.github_repository_name}}")


if __name__ == "__main__":
    if "{{ cookiecutter.command_line_interface|lower }}" == "false":
        PACKAGE.joinpath("cli.py").unlink()
        PACKAGE.joinpath("__main__.py").unlink()
        DOCS.joinpath("cli.rst").unlink()

    git_init()

