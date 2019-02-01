#!/home/wizard/anaconda3/bin/python3.7

def find(key, **kwargs):
    if key in kwargs:
        print(f'{key}->', kwargs[key])
    else:
        raise KeyError(f'key {key} not found')

if __name__ == '__main__':
    conn = {
          'host'   :'site.com'
        , 'port'   : 3306
        , 'service':'mysql'
    }

    try:
        find('port', **conn)
        find('ip', **conn) #до тук
        find('host', **conn)
    except KeyError as e:
        print('Except:', e)
        

    