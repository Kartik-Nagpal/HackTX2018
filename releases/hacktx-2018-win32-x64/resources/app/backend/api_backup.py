import sys
import zerorpc

# Ignore the error LUL
from .testObject import Test
from .parsing import FileParser

# This is the class that will parse stuff.
class BackendApi(object):

    # Returns whatever text you pass it for testing
    def echo(self, text):
        return text

    # TODO: Create method that grabs email address
    def transmitData(self, filesString=""):
        print(filesString)
        parse = FileParser(filesString)

        return "Finished Parsing"

def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(BackendApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()