# Welcome to the AUCMEDI contributing guide

Thank you for investing your time in contributing to our project! :sparkles:

In this guide you will get an overview of the contribution workflow from opening an issue, creating a PR, reviewing, and merging the PR.

## List of Contributors

AUCMEDI is designed as an open-source community project with a high focus on automated documentation and unittesting to allow 3rd party contributions.

This means: Contributions are welcome, and they are greatly appreciated!  
Every little bit helps, and credit will always be given.

<a href="https://github.com/frankkramer-lab/aucmedi/graphs/contributors">
<img
    src="https://contrib.rocks/image?repo=frankkramer-lab/aucmedi"
    alt="Currently unavailable"
    draggable="false"
    align="center">
</a>

## Issue

**The simplest form of contribution is the communication to us!**  

The [issue tracker](https://github.com/frankkramer-lab/aucmedi/issues) or [discussion forum](https://github.com/frankkramer-lab/aucmedi/discussions) in our GitHub repository is a powerful tool for communication between user and developer.  

#### Find/Report an issue

If you spot a problem with AUCMEDI, search if an issue already exists. If a related issue doesn't exist, you can open a new issue.

Reporting a bug, a feature request or just an experience is extremely helpful for us - thank you!

Here are some advices for issue communication:

- A bug is a demonstrable problem that is caused by the code in the repository.
- Use the GitHub issue search — check if the issue has already been reported.
- Check if the issue has been fixed — try to reproduce it using the latest master or development branch in the repository.
- Isolate the problem — create a reduced test case and a live example.
- A good bug report shouldn't leave others needing to chase you up for more information.
- Please try to be as detailed as possible in your report. All details will help people to fix any potential bugs.
- Take a moment to find out whether your feature request fits with the scope and aims of this project.

#### Solve an issue

Scan through our existing issues to find one that interests you. You can narrow down the search using `labels` as filters. If you find an issue to work on, you are welcome to open a PR with a fix / new feature.

## Pull Requests

Here, we want to cite the guideline of [Marc Diethelm](https://gist.github.com/MarcDiethelm/7303312) (slightly modified):

1) Create a personal fork of the project on Github.  
2) Clone the fork on your local machine. Your remote repo on Github is called origin.  
3) Add the original repository as a remote called upstream.  
4) If you created your fork a while ago be sure to pull upstream changes into your local repository.  
5) Create a new branch to work on! Branch from development.  
6) Implement/fix your feature, comment your code.  
7) Follow the code style of the project, including indentation.  
8) If the project has tests run them! (unittesting!)  
9) Write or adapt tests as needed.  
10) Add or change the documentation as needed. (docstrings!)  
11) Push your branch to your fork on Github, the remote origin.  
12) From your fork open a pull request in the correct branch. Target the project's development branch.  
13) Multiple automatic checks (GitHub Actions) will be applied on your fork to ensure functionality. Wait until all checks are successful.    
14) Wait for reviewers to have a look on your contributions.  
15) Communicate with the reviewers and revise your contribution if necessary.  
16) Once the pull request is approved and merged you can pull the changes from upstream to your local repo and delete your extra branch(es).  

#### Special Contribution Notes for AUCMEDI

- Pull requests should always target the **development** branch!
- Unittesting is key in AUCMEDI. Please provide unittests for all new contributed features in your Pull Request.
- For documentation, AUCMEDI heavily utilizes docstrings. Internal docstrings are placed on top of the function / class if they should not appear in the API reference.
- 80 character maximum line length for code and 500 character for docstrings. (this is a weak rule, but will be enforced).
- We recommend a code formater like Black (https://github.com/psf/black) to keep a clean code structure.
- Git commits have to follow git commit conventions: https://www.conventionalcommits.org/en/v1.0.0/
- Don't forget to link the pull request to the issue if you are solving one.

#### Your PR is merged!

Congratulations :tada::tada: The AUCMEDI team thanks you :sparkles:.

Once your PR is merged, your contributions will be publicly visible on [GitHub - frankkramer-lab/aucmedi](https://github.com/frankkramer-lab/aucmedi) and [AUCMEDI Website - Getting Started - Contributing](https://frankkramer-lab.github.io/aucmedi/getstarted/contribution/).

You are now part of the AUCMEDI contributor community!  :tada:
