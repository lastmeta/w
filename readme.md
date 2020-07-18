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
> w create command "echo whatever"
> w

> w command
whatever

> w create gs "git status"
> w create ga "git add --all"
> w create gc 'git commit -m "<arg>"' <arg>
> w create gg "git push"

> w delete command
> w

```
