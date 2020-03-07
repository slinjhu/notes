# My Configurations

## Git `~/.gitconfig`
```
[alias]
	cleanall = clean -xfd
	pop = reset --hard HEAD~1
	append = commit -a --amend --no-edit
	difflast = diff --binary HEAD~1 HEAD
	logs = log --abbrev-commit --oneline
```

## VS Code `settings.json`
```
{
    "editor.minimap.enabled": false,
    "files.trimTrailingWhitespace": true,
    "editor.renderWhitespace": "all",
    "editor.parameterHints.enabled": false,
    "files.exclude": {
        "env": true,
        ".vscode": true
    }
}
```
