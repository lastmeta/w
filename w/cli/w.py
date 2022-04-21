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
#@click.argument('commit', type=list, required=True)
@click.option('--commit','-c', prompt='commit message', help='start with a issue number if you like')
def gg(commit: str):
    '''git add --all, commit, push'''
    head = commit[0]
    tail = ' '.join(commit[1:])
    if head.isnumeric():
        head = f'#{head}'
    if tail != '':
        commit = head + ' ' + tail
    else:
        commit = head
    print(os.popen('git status').read())
    print(os.popen('git add --all').read())
    print(os.popen(f'git commit -m "{commit}"').read())
    print(os.popen('git push').read())


@main.command()
@click.argument('branch', type=str, required=True)
def gu(branch: str):
    '''git push -u origin <branch>'''
    print(os.popen(f'git push -u origin {branch}').read())


@main.command()
@click.argument('branch', type=str, required=True)
@click.argument('commit', type=str, required=True)
@click.argument('merge', type=bool, required=False)
@click.argument('dev', type=str, required=False)
def gb(branch: str, commit: str, merge:bool=True, dev: str=None):
    '''{branch} {commit} push, {dev}, merge push'''
    print(os.popen(f'git pull').read())
    print(os.popen(f'git checkout -b {branch}').read())
    print(os.popen(f'git add --all').read())
    print(os.popen(f'git status').read())
    print(os.popen(f'git commit -m "{commit}"').read())
    print(os.popen(f'git push -u origin {branch}').read())
    if merge:
        print(os.popen(f'git checkout {dev or "dev"}').read())
        print(os.popen(f'git merge {branch}').read())
        print(os.popen(f'git push').read())
        print(os.popen(f'git status').read())


@main.command()
@click.argument('branch', type=str, required=True)
@click.argument('dev', type=str, required=False)
def gm(branch: str, dev: str=None):
    '''switch to {dev}, merge {branch} push'''
    print(os.popen(f'git checkout {dev or "dev"}').read())
    print(os.popen(f'git merge {branch}').read())
    print(os.popen(f'git push').read())
    print(os.popen(f'git status').read())

@main.command()
def gmk():
    '''pull, git merge origin/kralverde, push'''
    print(os.popen(f'git pull').read())
    print(os.popen(f'git merge origin/kralverde').read())
    print(os.popen(f'git push').read())
    print(os.popen(f'git status').read())

@main.command()
def gmj():
    '''pull, dev, git merge jordan, push, jordan'''
    print(os.popen(f'git pull').read())
    print(os.popen(f'git checkout dev').read())
    print(os.popen(f'git merge jordan').read())
    print(os.popen(f'git push').read())
    print(os.popen(f'git status').read())
    print(os.popen(f'git checkout jordan').read())

@main.command()
def lg():
    '''.\lazygit.exe'''
    os.popen('.\lazygit.exe').read()

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
@click.argument('dir', type=str, required=True)
def darttest(dir: str):
    '''dart --no-sound-null-safety test test/{dir}'''
    print(os.popen(f'dart test test/{dir}').read())

@main.command()
def dartrun():
    '''dart --no-sound-null-safety run bin/raven.dart'''
    print(os.popen('dart run bin/raven.dart').read())

@main.command()
def dartbuild():
    '''dart run build_runner build'''
    print(os.popen('dart run build_runner build').read())


@main.command()
@click.argument('command', type=str, required=False)
def mt(command: str = 'pull'):
    ''' MoonTree '''
    def pull():
        def get_mt_repos(mt_repos: str = None):
            paths = {}
            mt_repos = mt_repos or os.environ.get('MT_REPOS', '/repos')
            for folder in os.listdir(mt_repos):
                if '.' not in folder:
                    paths[folder] = os.path.join(mt_repos, folder)
            return paths

        paths = get_mt_repos(mt_repos='/moontree/repos')
        for folder, path in paths.items():
            print(f'\n{folder}')
            os.system(f'cd {path} && git pull')

    def run():
        path = '/moontree/repos/raven_mobile'
        os.system(f'cd {path} && flutter run')

    if command == 'pull':
        pull()
    elif command == 'run':
        run()
    else:
        line_end = 'each folder in MT_REPOS.\n'
        print(
            'Invalid command. Please use one of the following:\n\n'
            f'pull          runs "git pull <folder>" for {line_end}'
            f'run           raven_mobile "flutter run"')
        pull()
