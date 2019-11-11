from __future__ import print_function
from anavar_utils import ResultsFile
import sys


def main():

    print('run', 'imp', 'exit_code', 'theta_1', 'gamma_1', 'e_1', 'lnL', 'converged', 'combo', 'rep', sep='\t')

    for res in sys.stdin:
        res = res.rstrip()

        combo, rep = res.split('/')[-1].split('.')[0:2]
        combo = combo.replace('sfs_', '')
        rep = rep.replace('rep', '')

        res = ResultsFile(open(res))
        converged = res.converged()
        top = res.ml_estimate(as_string=True)

        out_line = top + '\t' + '\t'.join([str(converged), combo, rep])
        print(out_line)


if __name__ == '__main__':
    main()
