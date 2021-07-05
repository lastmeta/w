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
def w():
    '''cd %WCF_REPOS%'''
    import pyautogui
    os.system(f"start cmd /K cd {os.environ.get('WCF_REPOS')}")
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
@click.argument('words', type=list, nargs=-1, required=True)
def gcn(words):
    '''git commit -m "<words>"'''
    commit = ' '.join([''.join(letters) for letters in words])
    print(os.popen(f'git commit -m "{commit}" --no-verify').read())


@main.command()
@click.argument('commit', type=str, required=True)
def gcn(commit: str):
    '''git commit -m "<commit>" --no-verify'''
    print(os.popen(f'git commit -m "{commit}" --no-verify').read())


@main.command()
def gg():
    '''git push'''
    print(os.popen('git push').read())


@main.command()
@click.argument('branch', type=str, required=True)
def gu(branch: str):
    '''git push -u origin <branch>'''
    print(os.popen(f'git push -u origin {branch}').read())


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


@main.command()
def mixup():
    '''starts heavenly_cleaners project'''
    print(os.popen('set HOMEDRIVE=c:').read())
    print(os.popen('docker pull postgres:11.4').read())
    print(os.popen('docker run --rm --name pg-docker -e POSTGRES_PASSWORD=postgres -d -p 5434:5432 postgres:11.4').read())
    #print(os.popen('mix archive.install hex phx_new 1.4.9').read())
    #print(os.popen('mix phx.new blog').read())
    #print(os.popen('mix ecto.create').read())


@main.command()
def ra():
    '''npx react-native run-android'''
    print(os.popen('npx react-native run-android').read())


@main.command()
def darttest():
    '''dart --no-sound-null-safety test test/'''
    print(os.popen('dart --no-sound-null-safety test test/').read())

@main.command()
def dartrun():
    '''dart --no-sound-null-safety run bin/raven.dart'''
    print(os.popen('dart --no-sound-null-safety run bin/raven.dart').read())
