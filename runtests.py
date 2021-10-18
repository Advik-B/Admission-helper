import os
from fnmatch import fnmatch
from subprocess import run, TimeoutExpired
import subprocess as cmd
from termcolor import cprint

def listfiles(root, pattern:str='*.*'):
    A = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                A.append(os.path.join(path, name))
    return A

cprint('LINTING:', 'blue', attrs=['bold', 'reverse'])


files_to_test = listfiles(os.getcwd(), '*.py')

cprint('The following file(s) will be checked:\n', 'green', attrs=['bold', 'underline'])

for file in files_to_test:
    cprint(f'  {file}' , 'yellow', attrs=['bold'])


print()
print('-'*80)
print('*'*80)
print('-'*80)
print()


for file in files_to_test:
    cprint(f'Checking: {file} 🔎 ', 'green', attrs=['bold', 'underline'])
    print()
    o = cmd.getoutput(f'python -m pyflakes {file}')
    p = cmd.getoutput(f'python -m pylint {file}')

    if not o or not p:
        cprint('No problems found!','green', attrs=['bold', 'underline'])
    else:
        print('pyflakes:\n' , o)
        print()
        print()
        print('*'*80)
        print()
        print()
        print('pylint:\n\t' , p)
    print()
    print('-'*80)
    print()

print('Checking Done!')

cprint('TESTING:', 'blue', attrs=['bold', 'reverse'])


fnames = []

for filename in files_to_test:
    fnames.append("%s\tin '%s'" % (filename.split('\\')[-1], filename))
cprint('Running tests for the following file(s):', color='green' ,attrs=['bold', 'underline'])
print()
for file in fnames:
    cprint(':: '+file, color='yellow')

print()

for file in files_to_test:
    if file.split('\\')[-1] == '.runtests.py':
        pass
    else:
        cprint('Testing: %s' % file#.
            , 'green', attrs=['bold'])
        print()
        cprint((f'{":"*40}: START :{":"*40}').center(80) ,'cyan', attrs=['reverse', 'bold'])
        try:
            run('python3 -m pytest %s' % file, timeout=60, shell=True)
        except TimeoutExpired as error:
            cprint(error, color='red', attrs=['bold'])

        cprint((f'{":"*40}: END :{":"*40}').center(80) ,'cyan', attrs=['reverse', 'bold'])
        print('\n'*4)

cprint('ALL TESTS COMPLETED', color='green', attrs=['bold', 'reverse', 'underline'])
exit(0)