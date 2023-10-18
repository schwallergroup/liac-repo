# Cookiecutter LIAC repo

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) for making new Python repositories for LIAC.

This is a fork from [snekpack](https://github.com/cthoyt/cookiecutter-snekpack). We just customized some things that we always do in our repos.

Here are some resources to familiarize yourself with some concepts used in this template:

- [Blog: Packaging](https://cthoyt.com/2020/06/03/how-to-code-with-me-organization)
- [Blog: CLIs](https://cthoyt.com/2020/06/11/click)
- [Blog: CLIs and Flask](https://cthoyt.com/2021/01/11/click-and-flask)

## 🛠️ Getting Started

1. Install `cookiecutter` and `GitPython` with:

   ```shell
   $ pip install cookiecutter GitPython
   ```

2. Run `cookiecutter` with:

   ```shell
   $ cookiecutter https://github.com/schwallergroup/liac-repo
   ```

3. Enter the requested information, then win! Remember, package names should only have letters, numbers,
   and underscores.

4. If you're working under version control, copy the repository into your folder tracked under git, commit
   the files, and push to your remote.

## 💪 Features

On top of snekpack's features, I automated the setting up Git as for us it's always the same.

Your new python package will have the following:

- Standard `src/` layout
- Declarative setup with `setup.cfg` and `pyproject.toml`
- Reproducible tests with `pytest` and `tox`
- Reproducible notebooks with [`treon`](https://github.com/reviewNB/treon) and `tox`
- A command line interface with `click`
- A vanity CLI via python entrypoints
- Version management with `bump2version`
- Documentation build with `sphinx`
- Testing of documentation coverage with `docstr-coverage` in `tox`
- Testing of documentation format and build in `tox`
- Testing of package metadata completeness with `pyroma` in `tox`
- Testing of MANIFEST correctness with `check-manifest` in `tox`
- Testing of optional static typing with `mypy` in `tox`
- A `py.typed` file so other packages can use your type hints
- Automated running of tests on each push with GitHub Actions
- Configuration for [ReadTheDocs](https://readthedocs.org/)
- A good base `.gitignore` generated from [gitignore.io](https://gitignore.io).
- A pre-formatted README with badges
- A pre-formatted LICENSE file with the MIT License (you can change this to whatever you want, though)
- A pre-formatted CONTRIBUTING guide
- Automatic tool for releasing to PyPI with `tox -e finish`
- A copy of the [Contributor Covenant](https://www.contributor-covenant.org/) as a basic code of conduct

## ⚖️ License

This cookiecutter package is licensed under the MIT License.
