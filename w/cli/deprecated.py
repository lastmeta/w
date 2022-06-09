
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

@main.command()
@click.argument('dir', type=str, required=True)
def darttest(dir: str):
    '''dart --no-sound-null-safety test test/{dir}'''
    print(os.popen(f'dart test test/{dir}').read())

@main.command()
@click.option('--watch','-w', default='watch', prompt='behavior', help='watch')
def flutterWatch():
    '''flutter pub run build_runner watch --delete-conflicting-outputs'''
    print(os.popen('flutter pub run build_runner watch --delete-conflicting-outputs').read())

@main.command()
def dartbuild():
    '''dart run build_runner build'''
    print(os.popen('dart run build_runner build').read())

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
