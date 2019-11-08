from __future__ import print_function
import argparse
from qsub import q_print as q_sub
from anavar_utils import Snp1ControlFile
import os


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-sim_data')
    parser.add_argument('-out_dir')
    args = parser.parse_args()

    if not os.path.isdir(args.out_dir):
        os.makedirs(args.out_dir)

    counter = 0
    for line in open(args.sim_data):

        counter += 1

        out_stem = '{}{}.rep{}'.format(args.out_dir, args.sim_data.replace('.txt', ''), counter)

        sfs = [int(x) for x in line.rstrip().split(',')]

        sfs_dict = {'SNP': (sfs, 475625)}

        ctl = Snp1ControlFile()
        ctl.set_data(sfs_dict, 20)

        ctl_name = out_stem + '.ctl.txt'
        log_name = out_stem + '.log.txt'
        res_name = out_stem + '.res.txt'

        with open(ctl_name, 'w') as o:
            print(ctl, file=o)

        cmd = 'anavar1.4 {} {} {} {}'.format(ctl_name, res_name, log_name, counter)

        q_sub([cmd], out=out_stem, evolgen=True)


if __name__ == '__main__':
    main()
