import os
import click

@click.group()
def main():
    '''display help '''


@main.command()
def help():
    '''open this file to modify'''
    print(
        'after installing this package using python setup.py develop... '
        '(which you must have already done)... '
        'please modify the w.py file at:',
        os.path.dirname(os.path.abspath(__file__)))
    print(os.popen(f'explorer {os.path.dirname(os.path.abspath(__file__))}').read())


@main.command()
def e():
    '''explorer .'''
    print(os.popen('explorer .').read())


@main.command()
def a():
    '''atom .'''
    print(os.popen('atom .').read())


@main.command()
def vs():
    '''code .'''
    print(os.popen('code .').read())


@main.command()
def ls():
    '''dir'''
    print(os.popen('dir').read())


@main.command()
def ll():
    '''dir'''
    print(os.popen('dir').read())

### navigation - wow, such hack!

@main.command()
def mt():
    '''cd %mt_REPOS%'''
    import pyautogui
    os.system(f"start cmd /K cd {os.environ.get('mt_REPOS')}")
    pyautogui.hotkey('alt', 'f4')


@main.command()
def r():
    '''cd %REPOS%'''
    import pyautogui
    os.system(f"start cmd /K cd {os.environ.get('REPOS')}")
    pyautogui.hotkey('alt', 'f4')


@main.command()
def c():
    '''cd ..'''
    import pyautogui
    os.system(f"start cmd /K cd {os.path.dirname(os.getcwd())}")
    pyautogui.hotkey('alt', 'f4')


## github

@main.command()
def gp():
    '''git pull'''
    print(os.popen('git pull').read())


@main.command()
def gs():
    '''git status'''
    print(os.popen('git status').read())


@main.command()
def ga():
    '''git add --all'''
    print(os.popen('git add --all').read())


@main.command()
@click.argument('words', type=list, nargs=-1, required=True)
def gc(words):
    '''git commit -m "<words>"'''
    commit = ' '.join([''.join(letters) for letters in words])
    print(os.popen(f'git commit -m "{commit}"').read())


@main.command()
@click.argument('commit', type=str, required=True)
def gcn(commit: str):
    '''git commit -m "<commit>" --no-verify'''
    print(os.popen(f'git commit -m "{commit}" --no-verify').read())


@main.command()
##@click.argument('commit', type=list, required=True)
#@click.option('--add','-a', default='--all', prompt='add', help='default is all')
@click.option('--commit','-c', default='commit', prompt='commit message', help='start with a issue number if you like')
#@click.option('--branch','-u', default='', prompt='branch', help='default is all')
def gg(
    #add:str,
    commit:str,
    #branch:str
):
    '''git add --all, commit, push'''
    add = '--all'
    branch = ''
    head = commit.split(' ')[0]
    tail = ' '.join(commit.split(' ')[1:])
    if head.isnumeric():
        head = '#' + head
    if tail != '':
        commit = head + ' ' + tail
    else:
        commit = head
    print(os.popen('git status').read())
    print(os.popen(f'git add {add}').read())
    print(os.popen(f'git commit -m "{commit}"').read())
    print(os.popen(f'git push {"" if branch == "" else "-u origin " + branch}').read())

@main.command()
@click.argument('branch', type=str, required=True)
def gu(branch: str):
    '''git push -u origin <branch>'''
    print(os.popen(f'git push -u origin {branch}').read())

@main.command()
@click.argument('from_branch', type=str, required=True)
@click.argument('to_branch', type=str, required=False)
@click.argument('next_branch', type=str, required=False)
@click.argument('last_branch', type=str, required=False)
def gm(from_branch: str, to_branch: str = None, next_branch: str = None, last_branch: str = None, return_branch: str = None):
    '''pull, to, git merge from, push, from'''
    to_branch = to_branch or ('rc' if from_branch == 'dev' else 'dev')
    return_branch = return_branch or from_branch

    def logic(from_branch: str, to_branch: str = None, next_branch: str = None, last_branch: str = None, return_branch: str = None):
        print(os.popen(f'git pull').read())
        print(os.popen(f'git checkout {to_branch}').read())
        print(os.popen(f'git merge {from_branch}').read())
        if (
            (input('Good to git push? [y]') or 'y')
            .lower().startswith('y')
        ):
            print(os.popen(f'git push').read())
            print(os.popen(f'git status').read())
            print(os.popen(f'git checkout {return_branch}').read())
            if next_branch is not None:
                logic(
                    from_branch=to_branch,
                    to_branch=next_branch,
                    next_branch=last_branch,
                    return_branch=return_branch)
        else:
            print('Aborted.')

    logic(
        from_branch=from_branch,
        to_branch=to_branch,
        next_branch=next_branch,
        return_branch=return_branch)

@main.command()
def lg():
    '''.\lazygit.exe'''
    os.popen('.\lazygit.exe').read()

## python

@main.command()
@click.argument('package', type=str, required=True)
def pipinstall(package: str):
    '''pip install --trusted-host repos.wcf.com --trusted-host pypi.python.org <package>'''
    print(os.popen(
        'pip install '
        '--trusted-host repos.wcf.com '
        '--trusted-host pypi.python.org '
        f'{package}').read())


@main.command()
def jn():
    '''jupyter notebook'''
    print(os.popen('jupyter notebook').read())

# flutter

@main.command()
#@click.option('--watch','-w', default='watch', prompt='behavior', help='watch')
@click.argument('behavior', type=str, required=True)
@click.argument('dir', type=str, required=False)
def flutter(behavior:str, dir: str = ''):
    '''flutter [run build watch clean get test]: run | pub run build_runner build | pub run build_runner watch --delete-conflicting-outputs | clean | pub get | test test/DIR'''
    if behavior in ['run', '--run', 'r', '-r']:
        print(os.popen('flutter run').read())
    if behavior in ['build', '--build', 'b', '-b']:
        print(os.popen('flutter pub run build_runner build').read())
    if behavior in ['watch', '--watch', 'w', '-w']:
        print(os.popen('flutter pub run build_runner watch --delete-conflicting-outputs').read())
    if behavior in ['clean', '--clean', 'c', '-c']:
        print(os.popen('flutter clean').read())
    if behavior in ['get', '--get', 'g', '-g']:
        print(os.popen('flutter pub get').read())
    if behavior in ['test', '--test', 't', '-t']:
        print(os.popen(f'flutter test test/{dir}').read())

@main.command()
@click.argument('behavior', type=str, required=True)
@click.argument('dir', type=str, required=False)
def dart(behavior:str, dir: str = ''):
    '''dart [build clean get test]: run build_runner build | clean | pub get | test test/DIR'''
    if behavior in ['build', '--build', 'b', '-b']:
        print(os.popen('dart run build_runner build').read())
    if behavior in ['clean', '--clean', 'c', '-c']:
        print(os.popen('dart clean').read())
    if behavior in ['get', '--get', 'g', '-g']:
        print(os.popen('dart pub get').read())
    if behavior in ['test', '--test', 't', '-t']:
        print(os.popen(f'dart test test/{dir}').read())


@main.command()
def sg():
    '''serverpod generate'''
    print(os.popen('serverpod generate').read())
