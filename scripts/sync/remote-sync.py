#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import os
import pathlib
import sys
from subprocess import check_call

server = "ec2-aws"
matching = {
    '/home/maxim/Projects': '/home/ec2-user/backup/Projects',
    '/home/maxim/Desktop/hse': '/home/ec2-user/backup/hse',
}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('type', choices=['push', 'pull'])
    parser.add_argument('dir', default=pathlib.Path('.'), nargs='?', type=pathlib.Path)
    args = parser.parse_args()

    matching = {pathlib.Path(source).absolute(): target for source, target in matching.items()}

    path = pathlib.Path(args.dir).absolute()
    if not path.is_dir():
        print(f'{path} is not a directory')
        sys.exit(1)
    for source, target in matching.items():
        relative = None
        try:
            relative = path.relative_to(source)
        except ValueError:
            pass

        if relative is not None:
            cmd = ['rsync', '-r', '--delete']
            source, target = path, pathlib.Path(os.path.join(target, relative))
            if args.type == "push":
                check_call(cmd + [source, f'{server}:{target.parent}'])
            elif args.type == "pull":
                check_call(cmd + [f'{server}:{target}', source.parent])
