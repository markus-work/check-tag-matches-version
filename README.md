# check-tag-matches-version

## Description
A github action that checks if the tag matches the version in the pyproject.toml file.

## Usage
```yaml
- name: Check tag matches version
  uses: markus-work/check-tag-matches-version@v1
  with:
    token: ${{ secrets.GITHUB_TOKEN }}
```