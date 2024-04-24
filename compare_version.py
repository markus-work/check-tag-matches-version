import toml
from git import Repo

def compare_git_tag_and_python_version():
    data = toml.load('/github/workspace/pyproject.toml')
    version = data.get('tool', {}).get('poetry', {}).get('version', '')
    
    repo = Repo('/github/workspace')
    tag = repo.tags[-1]
    
    if version != str(tag):
        print(f"Version {version} does not match latest tag {tag}")
        exit(1)

if __name__ == "__main__":
    compare_git_tag_and_python_version()