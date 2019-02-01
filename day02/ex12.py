#!/home/wizard/anaconda3/bin/python3.7

def show( title, *args, **kwargs):
    print(f'title {title}')

    print('args:')
    for v in args:
        print(f'agr:{v}')

    params = {
          'path': kwargs.get('path', '/tmp/')
        , 'log' : kwargs.get('log','/var/log/messages')
       #, 'log' : kwargs.get('log')
    }

    print(params)
    
if __name__ == '__main__':
    show('E-Shop')
    show('App Server', 1000, 2000, 3000)
    show('App Server', 100, 200, 300, path = '/usr/local/bin', log = '/var/log/app.log')

    app = {
          'path':'/usr/local/bin'
          ,'author':'me'
    }

    show('App Server', 100, 200, 300, **app)
    #show('App Server', 100, 200, 300, **app)


