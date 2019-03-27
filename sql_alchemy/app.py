from time import sleep

from .tasks import *
from .db import migrate


def run(args):
    if args.run_type == 'run':
        res = create_file.delay('new.txt')
        sleep(2)
        print(res.status)
        res = get_files.delay()
        sleep(3)
        print(res.status)
        print(res.get())
        return

    if args.run_type == 'migrate':
        migrate()
