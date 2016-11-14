# parameterize tasks
import os
from doit.tools import run_once

# this can be defined once...
def trim_reads(orig_files, memory=1e9):
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M {1} -k 31 {0}'

    targets = [ os.path.basename(t) + '.abundtrim' for t in orig_files ]

    return {'actions': [CMD_trim.format(" ".join(orig_files), memory)],
            'targets': targets,
            'uptodate': [run_once],
            'file_dep': orig_files}

# ...and then deployed lotsa times
def task_trim_reads():
    return trim_reads(['../simple-genome-reads.fa.gz'],
                      memory=1e7)
