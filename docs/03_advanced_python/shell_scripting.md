# Shell Scripting
Shell scripting involves writing scripts for the command-line interpreter, known as the shell, on Unix-based systems and Windows. These scripts automate tasks such as file manipulation, program execution, and text processing. Common Unix shells include `Bash`, `Zsh`, and `Ksh`, while Windows uses Command Prompt (`cmd`) and PowerShell. 

Shell scripts start with a shebang (`#!`) and extensions of `sh` on Unix and `.bat` or `.ps1` on Windows. Commands like `echo`, `grep`, and `awk` are common on Unix, while `Write-Output`, `Get-Content`, and `ForEach-Object` are used in PowerShell. This is very often used together with Python scripts and Jupyter notebook magics to automate batch analysis.

```python
# Running Python pip installation from Jupyter notebook with shell command
%pip install matplotlib
```

For Windows users it is highly recommended to run Python alongside with Git bash (https://git-scm.com/downloads) that maximally mimic the running *nix running environment.

## Summary Table on OS and Shell Scipts
| Operating System | Terminal Emulator            | Default Shell    | Additional Shells                   | Pros                                                                         | Cons                                                               |
|------------------|------------------------------|------------------|-------------------------------------|------------------------------------------------------------------------------|--------------------------------------------------------------------|
| Linux            | GNOME Terminal, Konsole      | Bash             | Zsh, Fish, Ksh, Tcsh, Dash          | Highly customizable, vast array of tools, strong community support, open-source | Fragmentation in terminal emulators, varying default configurations|
| macOS            | Terminal, iTerm2             | Zsh (since 10.15) | Bash, Fish, Ksh, Tcsh               | User-friendly, well-integrated with macOS, iTerm2 offers advanced features    | Terminal app is less feature-rich compared to iTerm2              |
| Windows          | Command Prompt, PowerShell, Windows Terminal | PowerShell       | Bash (via WSL), Git Bash, Cygwin    | Powerful scripting capabilities in PowerShell, WSL brings Linux compatibility | Command Prompt is limited, PowerShell syntax can be complex       |
