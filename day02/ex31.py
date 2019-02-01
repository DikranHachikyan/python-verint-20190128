#!/home/wizard/anaconda3/bin/python3.7

class DictionaryKeyError(Exception):
    pass

def find(key, **kwargs):
    if key in kwargs:
        print(f'{key}->', kwargs[key])
    else:
        raise DictionaryKeyError(f'key {key} not found')

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
    except DictionaryKeyError as e:
        print('Except:', e)
        

    