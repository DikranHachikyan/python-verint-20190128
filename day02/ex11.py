#!/home/wizard/anaconda3/bin/python3.7

def show( title, *args, **kwargs):
    print(f'title {title}')

    print('args:')
    for v in args:
        print(f'agr:{v}')

    if 'path' in kwargs:
        print('app path:' f"{kwargs['path']}")

    if 'log' in kwargs:
        print('log file:' f"{kwargs['log']}")

    
if __name__ == '__main__':
    show('E-Shop')
    show('App Server', 1000, 2000, 3000)
    show('App Server', 100, 200, 300, path = '/usr/local/bin', log = '/var/log/app.log')

    app = {
          'path':'/usr/local/bin'
        , 'log':'/var/log/app.log'
    }

    show('App Server', 100, 200, 300, **app)


