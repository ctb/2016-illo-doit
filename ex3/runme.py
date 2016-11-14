#! /usr/bin/env python3
import os

from doit_utils import make_task, run_tasks
from doit.tools import run_once
from doit.task import clean_targets

@make_task
def task_trim_reads(orig_files, memory=1e9):
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M {1} -k 31 {0}'

    targets = [ os.path.basename(t) + '.abundtrim' for t in orig_files ]

    name = 'task_trim_reads<{0}.{1}>'.format(",".join(orig_files),
                                             memory)

    return {'name': name,
            'actions': [CMD_trim.format(" ".join(orig_files), memory)],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': orig_files,
            'clean': [clean_targets]}


def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('seqfiles', nargs='+')
    parser.add_argument('-M', '--memory', type=float, default=1e9)

    parser.add_argument('--clean', default=False, action='store_true')
    args = parser.parse_args()

    tasks = []
    
    task = task_trim_reads(args.seqfiles, memory=args.memory)
    tasks.append(task)

    if args.clean:
        run_tasks(tasks, ['clean'])
    else:
        run_tasks(tasks, ['run'])


if __name__ == '__main__':
    main()
