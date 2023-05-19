import os

import git
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
# Clone a repository
repo_url = 'https://github.com/ashilgovind0098/source-code-plagiarism.git'
repo_path = 'C:/sample'
git.Repo.clone_from(repo_url, repo_path)

# Open an existing repository
repo = git.Repo(repo_path)

# Add a file to the index
file_path = "C:/Users/23059/OneDrive/Documents/Dissertation"
repo.index.add([file_path])

# Commit changes
commit_message = "Added {}".format(file_path)
repo.index.commit(commit_message)

# Push changes to the remote repository
origin = repo.remote(name="origin")
origin.push()
