#!/home/wizard/anaconda3/bin/python3.7

def gen_text(txts):
    for x in txts:
        yield x

if __name__ == '__main__':
    g = gen_text('hello python')

    print(next(g))
    print(next(g))
    print(next(g))
