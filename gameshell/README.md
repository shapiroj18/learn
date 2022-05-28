# GameShell

## Overview
This is meant for following [GameShell](https://github.com/phyver/GameShell?utm_source=hackernewsletter&utm_medium=email&utm_term=code), a tool to learn unix shell.

## Setting Up Environment
This uses Docker to essentially set up a virtual machine to run this on, so it is really the only dependency. To do this, simply use:
```
make run
```

Then, you will have a shell open to run the getting started commands per the instructions (with a few small caveats)
1. `sudo apt install gettext man-db procps psmisc nano tree bsdmainutils x11-apps wget` (password: `docker`, hit `y`)
2. `cd home` (move into `home` directory that has permissions to create directories, etc.)
3. `wget https://github.com/phyver/GameShell/releases/download/latest/gameshell.sh`
4. `bash gameshell.sh`

## To Do
* Figure out how to persist data with volumes
* Automate getting started commands if necessary