[commit-shield]: https://img.shields.io/github/last-commit/Kaspary/email-hub-sdk?style=for-the-badge&logo=GitHub
[commit-url]: https://github.com/Kaspary/email-hub-sdk/commits/main
[linkedin-shield]: https://img.shields.io/badge/-João%20Pedro%20Kaspary-6633cc?style=for-the-badge&logo=Linkedin&colorB=2366c2
[linkedin-url]: https://linkedin.com/in/joao-pedro-kaspary
[github-shield]: https://img.shields.io/github/followers/Kaspary?label=João%20Pedro%20Kaspary&style=for-the-badge&logo=GitHub
[github-url]: https://github.com/Kaspary

[![commit-shield]][commit-url]
[![linkedin-shield]][linkedin-url]
[![GitHub followers][github-shield]][github-url]


# Email SDK Hub
This is a project for implementing an interface to send emails with different servers.

## Install
Do you can install this project directly in yor project. To do this, follow the next step.
```bash
pip install git+https://github.com/Kaspary/email-hub-sdk.git
```

## Local Usage

### Requirements
- Python 3.7 or more.
- Virual Envorniment Python (Recomended).
- Make (optional). 

### Commands
To make easy startup of the project, the common commands were configurated in the `makefile`.

#### Example
To create the virtual environment, execute the following command.
```bash
make create-venv
```

**Commands**
* `create-venv` - Create the virtual environment for the project (the module **venv** is necessary).
* `setup` - Install the requirements from **requirements.txt**.
* `clean` - Remove all temporary files from the project, including the coverage folder.
* `code-convention` - Execute the tools to verify the code convention.
* `test` - Run all the tests of the project.
* `test-cov` - Generate the test coverage report.

## Project layout

```
.
├── Makefile
├── README.md
├── reports
│   └── coverage
├── setup.cfg
├── setup.py
├── src
│   ├── adapters.py
│   ├── clients.py
│   ├── enums.py
│   ├── facades.py
│   ├── __init__.py
│   └── services.py
└── tests
    ├── __init__.py
    ├── test_adapters.py
    ├── test_clients.py
    ├── test_facades.py
    └── test_services.py
```