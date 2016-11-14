from doit.tools import run_once

def task_trim_reads():
    reads = '../simple-genome-reads.fa.gz'
    memory = 1e7
    
    CMD_trim = 'trim-low-abund.py -Z 20 -C 3 -M {1} -k 31 {0}'
    CMD_trim = CMD_trim.format(reads, memory)

    targets = ['../simple-genome-reads.fa.gz.abundtrim']

    return {'actions': [CMD_trim],
            'file_dep': [reads],
            'targets': targets,
            'uptodate': [run_once] }
