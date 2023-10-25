<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/repo_logo_dark.png" width='100%'>
  <source media="(prefers-color-scheme: light)" srcset="./assets/repo_logo_light.png" width='100%'>
  <img alt="Project logo" src="/assets/" width="100%">
</picture>

<br>

<p align="center">
    <a href="https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}/actions/workflows/tests.yml">
        <img alt="Tests" src="https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}/workflows/Tests/badge.svg" />
    </a>
    <a href="https://doi.org/10.48550/arXiv.2304.05376">
        <img alt="DOI" src="https://zenodo.org/badge/DOI/10.48550/arXiv.2304.05376.svg" />
    </a>
    <a href="https://pypi.org/project/{{cookiecutter.package_name}}">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/{{cookiecutter.package_name}}" />
    </a>
    <a href='https://{{cookiecutter.package_name}}.readthedocs.io/en/latest/?badge=latest'>
        <img src='https://readthedocs.org/projects/{{cookiecutter.package_name}}/badge/?version=latest' alt='Documentation Status' />
    </a>
    <a href="https://github.com/schwallergroup/liac-repo">
        <img alt="Cookiecutter template from @schwallergroup" src="https://img.shields.io/badge/Cookiecutter-schwallergroup-blue" /> 
    <a href="https://schwallergroup.github.io">
        <img alt="Learn more about @schwallergroup" src="https://img.shields.io/badge/Learn more-SchwallerGroup-blue" /> 
    </a>
    <a href='https://github.com/psf/black'>
        <img src='https://img.shields.io/badge/code%20style-black-000000.svg' alt='Code style: black' />
    </a>
</p>

<h1 align="center">
  {{cookiecutter.package_name}}
</h1>


<br>


{{cookiecutter.short_description}}

## 💪 Getting Started

> TODO show in a very small amount of space the **MOST** useful thing your package can do.
> Make it as short as possible! You have an entire set of docs for later.


## 🚀 Installation

<!-- Uncomment this section after your first ``tox -e finish``
The most recent release can be installed from
[PyPI](https://pypi.org/project/{{cookiecutter.package_name}}/) with:

```shell
$ pip install {{cookiecutter.package_name}}
```
-->

The most recent code and data can be installed directly from GitHub with:

```bash
$ pip install git+https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}.git
```

## ✅ Citation

Philippe Schwaller et al. "Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction". ACS Central Science 2019 5 (9), 1572-1583
```bibtex
@article{doi:10.1021/acscentsci.9b00576,
    author = {Schwaller, Philippe and Laino, Teodoro and Gaudin, Théophile and Bolgar, Peter and Hunter, Christopher A. and Bekas, Costas and Lee, Alpha A.},
    title = {Molecular Transformer: A Model for Uncertainty-Calibrated Chemical Reaction Prediction},
    journal = {ACS Central Science},
    volume = {5},
    number = {9},
    pages = {1572-1583},
    year = {2019},
    doi = {10.1021/acscentsci.9b00576},
}

@Misc{this_repo,
  author = { {{cookiecutter.author_name}} },
  title = { {{cookiecutter.package_name}} - {{cookiecutter.short_description}} },
  howpublished = {Github},
  year = {2023},
  url = {https://github.com/schwallergroup/{{ cookiecutter.github_repository_name }} }
}
```



<!--
### 🎁 Support

This project has been supported by the following organizations (in alphabetical order):

- [Harvard Program in Therapeutic Science - Laboratory of Systems Pharmacology](https://hits.harvard.edu/the-program/laboratory-of-systems-pharmacology/)

-->

<!--
### 💰 Funding

This project has been supported by the following grants:

| Funding Body                                             | Program                                                                                                                       | Grant           |
|----------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------|
| DARPA                                                    | [Automating Scientific Knowledge Extraction (ASKE)](https://www.darpa.mil/program/automating-scientific-knowledge-extraction) | HR00111990009   |
-->


## 🛠️ For Developers


<details>
  <summary>See developer instructions</summary>



### 👐 Contributing

Contributions, whether filing an issue, making a pull request, or forking, are appreciated. See
[CONTRIBUTING.md](https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}/blob/master/.github/CONTRIBUTING.md) for more information on getting involved.


### Development Installation

To install in development mode, use the following:

```bash
$ git clone git+https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}.git
$ cd {{cookiecutter.github_repository_name}}
$ pip install -e .
```

### 🥼 Testing

After cloning the repository and installing `tox` with `pip install tox`, the unit tests in the `tests/` folder can be
run reproducibly with:

```shell
$ tox
```

Additionally, these tests are automatically re-run with each commit in a [GitHub Action](https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}/actions?query=workflow%3ATests).

### 📖 Building the Documentation

The documentation can be built locally using the following:

```shell
$ git clone git+https://github.com/schwallergroup/{{cookiecutter.github_repository_name}}.git
$ cd {{cookiecutter.github_repository_name}}
$ tox -e docs
$ open docs/build/html/index.html
``` 

The documentation automatically installs the package as well as the `docs`
extra specified in the [`setup.cfg`](setup.cfg). `sphinx` plugins
like `texext` can be added there. Additionally, they need to be added to the
`extensions` list in [`docs/source/conf.py`](docs/source/conf.py).

### 📦 Making a Release

After installing the package in development mode and installing
`tox` with `pip install tox`, the commands for making a new release are contained within the `finish` environment
in `tox.ini`. Run the following from the shell:

```shell
$ tox -e finish
```

This script does the following:

1. Uses [Bump2Version](https://github.com/c4urself/bump2version) to switch the version number in the `setup.cfg`,
   `src/{{cookiecutter.package_name}}/version.py`, and [`docs/source/conf.py`](docs/source/conf.py) to not have the `-dev` suffix
2. Packages the code in both a tar archive and a wheel using [`build`](https://github.com/pypa/build)
3. Uploads to PyPI using [`twine`](https://github.com/pypa/twine). Be sure to have a `.pypirc` file configured to avoid the need for manual input at this
   step
4. Push to GitHub. You'll need to make a release going with the commit where the version was bumped.
5. Bump the version to the next patch. If you made big changes and want to bump the version by minor, you can
   use `tox -e bumpversion -- minor` after.
</details>
