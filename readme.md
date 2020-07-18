# w
================

w is a simple commandline utility using click. makes it easy to view, create, and delete alias-like commands in windows cmd.

Project Organization
--------------------
    w
    ├── w           <-- Source code.
    │   ├── cli     <-- Module: Command Line entry point into project.
    │   ├── config  <-- Module: contains configuration or settings files.
    │   └── lib     <-- Module: functions used by other modules.
    ├── README.md   <-- README.md for developers using this project.
    └── setup.py    <-- `...w/> python setup.py develop`
--------------------

## Examples

```
...> python setup.py develop
...

...> w
Usage: w [OPTIONS] COMMAND [ARGS]...

  display help

Options:
  --help  Show this message and exit.

Commands:
  a     atom .
  e     explorer .
  ga    git add --all
  gc    git commit -m "<commit>"
  gcn   git commit -m "<commit>" --no-verify
  gg    git push
  gp    git pull
  gs    git status
  gu    git push -u origin <branch>
  help  open this file to modify
  ls    dir

...>w ls
...
07/17/2020  11:05 PM    <DIR>          .
07/17/2020  11:05 PM    <DIR>          ..
07/17/2020  11:04 PM                90 .gitignore
07/17/2020  10:59 PM             7,169 LICENSE
07/17/2020  10:30 PM               901 readme.md
07/17/2020  10:20 PM               676 setup.py
07/17/2020  11:00 PM    <DIR>          w
07/17/2020  11:05 PM    <DIR>          w.egg-info
               4 File(s)          8,836 bytes
               4 Dir(s)  367,129,309,184 bytes free

...>w gs
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean

...>w gc --help
Usage: w gc [OPTIONS] COMMIT

  git commit -m "<commit>"

Options:
  --help  Show this message and exit.

```
