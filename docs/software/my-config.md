# My Configurations

## `~/.gitconfig`
```
[alias]
	cleanall = clean -xfd
	pop = reset --hard HEAD~1
	append = commit -a --amend --no-edit
	difflast = diff --binary HEAD~1 HEAD
	logs = log --abbrev-commit --oneline
```