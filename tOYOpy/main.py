import sys
import traceback
import transform
from argparse import ArgumentParser

if __name__ == '__main__':
    try:
        parser = ArgumentParser(description='tOYO')
        parser.add_argument('-m', '--modify', help='Modify the EPUB file.')
        args = parser.parse_args()

        if args.modify:
            transform.it(args.modify)


    except KeyboardInterrupt:
        print("Shutdown requested...exiting")
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)
