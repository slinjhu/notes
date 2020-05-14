# My Configurations

## Git `~/.gitconfig`
```
[alias]
	cleanall = clean -xfd
	pop = reset --hard HEAD~1
	append = commit -a --amend --no-edit
	difflast = diff --binary HEAD~1 HEAD
	logs = log --abbrev-commit --oneline
[push]
	default = current
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
    },
    "telemetry.enableTelemetry": false,
    "telemetry.enableCrashReporter": false,
    "explorer.confirmDragAndDrop": false
}
```

## Zsh `~/.zshrc`
```
# Setup kubectl
source <(kubectl completion zsh)
alias k=kubectl
complete -F __start_kubectl k

# Use VS Code as the default text editor
export EDITOR='code -w'

```