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
    executeCommand(f'explorer {os.path.dirname(os.path.abspath(__file__))}')


@main.command()
def e():
    '''explorer .'''
    executeCommand('explorer .')


@main.command()
def a():
    '''atom .'''
    executeCommand('atom .')


@main.command()
def vs():
    '''code .'''
    executeCommand('code .')


@main.command()
def ls():
    '''dir'''
    executeCommand('dir')


@main.command()
def ll():
    '''dir'''
    executeCommand('dir')

# navigation - wow, such hack!


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


@main.command()
@click.argument('command', type=list, nargs=-1, required=False)
def p(command):
    '''python <command>'''
    commit = ' '.join([''.join(words) for words in command])
    executeCommand(f'python {commit}')


# github

@main.command()
def gp():
    '''git pull'''
    executeCommand('git pull')


@main.command()
def gs():
    '''git status'''
    executeCommand('git status')


@main.command()
def ga():
    '''git add --all'''
    executeCommand('git add --all')


@main.command()
@click.argument('words', type=list, nargs=-1, required=True)
def gc(words):
    '''git commit -m "<words>"'''
    commit = ' '.join([''.join(letters) for letters in words])
    executeCommand(f'git commit -m "{commit}"')


@main.command()
@click.argument('commit', type=str, required=True)
@click.argument('commit', type=str, required=True)
def gcn(commit: str):
    '''git commit -m "<commit>" --no-verify'''
    executeCommand(f'git commit -m "{commit}" --no-verify')


@main.command()
# @click.argument('commit', type=list, required=True)
# @click.option('--add','-a', default='--all', prompt='add', help='default is all')
@click.option('--commit', '-c', default='commit', prompt='commit message', help='start with a issue number if you like')
# @click.option('--branch','-u', default='', prompt='branch', help='default is all')
def gg(
    # add:str,
    commit: str,
    # branch:str
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
    executeCommands(
        [
            'git status',
            f'git add {add}',
            f'git commit -m "{commit}"',
            f'git push {"" if branch == "" else "-u origin " + branch}'],
        display=False)


@main.command()
@click.argument('tagname', type=str, required=True)
@click.option('--commit', '-c', default='commit', prompt='commit message', help='start with a issue number if you like')
def ggt(tagname: str, commit: str):
    '''git add --all, commit, git tag <tagname>, git push origin --tags'''
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
    executeCommands(
        [
            'git status',
            f'git add {add}',
            f'git commit -m "{commit}"',
            f'git tag {tagname}',
            f'git push {"" if branch == "" else "-u origin " + branch} --tags'],
        display=False)


@main.command()
# @click.argument('commit', type=list, required=True)
# @click.option('--add','-a', default='--all', prompt='add', help='default is all')
@click.option('--commit', '-c', default='commit', prompt='commit message', help='start with a issue number if you like')
# @click.option('--branch','-u', default='', prompt='branch', help='default is all')
def ggp(
    # add:str,
    commit: str,
    # branch:str
):
    '''git add --all, commit, push, dart publish'''
    gg(commit)
    dart('publish')


@main.command()
@click.argument('branch', type=str, required=True)
def gu(branch: str):
    '''git push -u origin <branch>'''
    executeCommand(f'git push -u origin {branch}')


@main.command()
@click.argument('from_branch', type=str, required=True)
@click.argument('to_branch', type=str, required=False)
@click.argument('next_branch', type=str, required=False)
@click.argument('last_branch', type=str, required=False)
def gm(from_branch: str, to_branch: str = None, next_branch: str = None, last_branch: str = None, return_branch: str = None):
    '''pull, to, git merge from, push, from :||'''
    to_branch = to_branch or ('rc' if from_branch == 'dev' else 'dev')
    return_branch = return_branch or from_branch

    def logic(from_branch: str, to_branch: str = None, next_branch: str = None, last_branch: str = None, return_branch: str = None):
        executeCommand(f'git pull')
        executeCommand(f'git checkout {to_branch}')
        executeCommand(f'git merge {from_branch}')
        if (
            (input('Good to git push? [y]') or 'y')
            .lower().startswith('y')
        ):
            executeCommand(f'git push')
            executeCommand(f'git status')
            if next_branch is not None:
                logic(
                    from_branch=to_branch,
                    to_branch=next_branch,
                    next_branch=last_branch,
                    return_branch=return_branch)
            else:
                executeCommand(f'git checkout {return_branch}')
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

# python


@main.command()
@click.argument('package', type=str, required=True)
def pipinstall(package: str):
    '''pip install --trusted-host repos.wcf.com --trusted-host pypi.python.org <package>'''
    executeCommand(
        'pip install '
        '--trusted-host repos.wcf.com '
        '--trusted-host pypi.python.org '
        f'{package}')


@main.command()
def jn():
    '''jupyter notebook'''
    executeCommand('jupyter notebook')


@main.command()
# @click.option('--watch','-w', default='watch', prompt='behavior', help='watch')
@click.argument('behavior', type=str, required=True)
@click.argument('dir', type=str, required=False)
def flutter(behavior: str, dir: str = ''):
    '''flutter [run build watch clean get test upgrade]: run | pub run build_runner build | pub run build_runner watch --delete-conflicting-outputs | clean | pub get | test test/DIR | upgrade'''
    if behavior in ['run', '--run', 'r', '-r']:
        cmd = 'flutter run'
    if behavior in ['build', '--build', 'b', '-b']:
        cmd = 'flutter pub run build_runner build'
    if behavior in ['watch', '--watch', 'w', '-w']:
        cmd = 'flutter pub run build_runner watch --delete-conflicting-outputs'
    if behavior in ['clean', '--clean', 'c', '-c']:
        cmd = 'flutter clean'
    if behavior in ['get', '--get', 'g', '-g']:
        cmd = 'flutter pub get'
    if behavior in ['test', '--test', 't', '-t']:
        cmd = f'flutter test test/{dir}'
    if behavior in ['upgrade', '--upgrade', 'u', '-u']:
        cmd = 'flutter upgrade'
    executeCommand(cmd)


@main.command()
@click.argument('behavior', type=str, required=True)
@click.argument('dir', type=str, required=False)
def dart(behavior: str, dir: str = ''):
    '''dart [build clean get test update publish]: run build_runner build | clean | pub get | test test/DIR | choco upgrade dart-sdk -y | pub publish'''
    if behavior in ['build', '--build', 'b', '-b']:
        cmd = 'dart run build_runner build'
    if behavior in ['clean', '--clean', 'c', '-c']:
        cmd = 'dart clean'
    if behavior in ['get', '--get', 'g', '-g']:
        cmd = 'dart pub get'
    if behavior in ['test', '--test', 't', '-t']:
        cmd = f'dart test test/{dir}'
    if behavior in ['update', '--update', 'u', '-u']:
        cmd = f'choco upgrade dart-sdk -y'
    if behavior in ['publish', '--publish', 'p', '-p', 'push']:
        cmd = f'dart pub publish -f'
    executeCommand(cmd)


@main.command()
def sg():
    '''serverpod generate'''
    executeCommand('serverpod generate')


@main.command()
def sp():
    '''serverpod move protocol to client_back.'''
    import shutil
    shutil.rmtree('C:\moontree\moontreeV1\client_back\lib\server\src\protocol')
    print('removed C:\moontree\moontreeV1\client_back\lib\server\src\protocol')
    shutil.copytree('C:\moontree\server2\serverv2_client\lib\src\protocol',
                    'C:\moontree\moontreeV1\client_back\lib\server\src\protocol')
    print('copied C:\moontree\server2\serverv2_client\lib\src\protocol')
    print('pasted C:\moontree\moontreeV1\client_back\lib\server\src\protocol')
    remove = r'package:serverv2_client/src/protocol/'
    for name in ['client', 'protocol']:
        with open(f'C:\moontree\moontreeV1\client_back\lib\server\src\protocol\{name}.dart', mode='r') as f:
            script = f.readlines()
        with open(f'C:\moontree\moontreeV1\client_back\lib\server\src\protocol\{name}.dart', mode='w') as f:
            f.writelines([line.replace(remove, '') for line in script])
        print(f'fixed {name}.dart')


@main.command()
def iex():
    '''iex -S mix phx.server'''
    executeCommand('iex -S mix phx.server')


def executeCommands(cmds: str, display: bool = True):
    for cmd in cmds:
        print('>>> ' + cmd)
        executeCommand(cmd, display=display)


def executeCommand(cmd: str, display: bool = True):
    if display:
        print('>>> ' + cmd)
    print(os.popen(cmd).read())
