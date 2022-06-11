def hello(name, msg):
    print('안녕, {}! {}.'.format(name, msg))

hello('수빈','반갑다')
hello('현수','잘 있었지?')

def hello2(name, msg = '반갑다'):
    print('안녕, {}! {}.'.format(name, msg))

hello2('수빈2')
hello2('현수2',' 잘 지내니')