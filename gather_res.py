from __future__ import print_function
from anavar_utils import ResultsFile
import sys


def main():

    print('run', 'imp', 'exit_code', 'theta_1', 'gamma_1', 'e_1', 'lnL', 'converged', 'combo', 'rep', sep=',')

    for res in sys.stdin:
        res = res.rstrip()

        combo, rep = res.split('/')[-1].split('.rep')
        combo = combo.replace('sfs_', '')
        rep = rep.split('.')[0]

        res = ResultsFile(open(res))
        converged = res.converged()
        top = res.ml_estimate(as_string=True)

        out_line = top.split('\t') + [converged, combo, rep]
        print(*out_line, sep=',')


if __name__ == '__main__':
    main()
