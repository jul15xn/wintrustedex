# Windows TrustedInstaller exploit

Takes advantage of the Set-Content command in powershell to run any cmd command as TrustedInstaller

I found this exploit myself with [this video](https://youtu.be/Vj1uh89v-Sc). There also is a [blog](https://www.tiraniddo.dev/2017/08/the-art-of-becoming-trustedinstaller.html) made about this exploit which explains in detail how this works. I simply just made a python program to do this automatically.
## Usage

To use this script, simply run the file ```shell.py``` as an administrator

## Commands

```
tic {COMMAND} - Runs a cmd command as TrustedInstaller
cmd {COMMAND} - Runs a cmd command as yourself
tisc - Gets information about the TrustedInstaller service
clear - Clears the screen
help - Displays the help screen
exit - Exits the shell
```
## Examples

Send a message on screen to all users (Windows Pro version only)
```
tic msg * This message was brought to you by TrustedInstaller :)
```

Shutdown the current pc in 30 minutes
```
tic shutdown -s -t 1800
```
# 
If there are any bugs in the program, please create an issue on the [issue page](https://github.com/jul15xn/wintrustedex/issues)!
