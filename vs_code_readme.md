# VS code configuration:

- preffered formatter: black

  User settings
```json
  "[python]": {
    // "editor.defaultFormatter": "ms-python.vscode-pylance",
    "editor.formatOnPaste": false
  }
  "python.linting.flake8Enabled": true,
  "python.linting.flake8Args": [
    "--max-line-length=120",
    "--ignore=E402",
    "--verbose"
  ],
  "python.linting.pylintEnabled": false,
  "python.linting.mypyEnabled": false,
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "python.formatting.blackArgs": [
    "--line-length",
    "100"
  ],
```

  Local settings

```json
 {
    "python.linting.flake8Enabled": true,
    "python.linting.flake8Args": [
        "--config",
        ".flake8"
    ],
    "python.linting.enabled": true,
    "python.formatting.provider": "black",
 }
```


- [Formatting](https://code.visualstudio.com/docs/python/editing#_formatterspecific-settings)

