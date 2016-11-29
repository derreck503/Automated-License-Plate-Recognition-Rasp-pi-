#!/usr/bin/python3

import subprocess
import sys
import os


def List(dir):
        cmd1 = 'sudo service motion start'
        subprocess.getstatusoutput(cmd1)
        i = 0
        while (i < 10000):
                cmd2 = 'cp /var/lib/motion/* ../openalpr/src/build/images/'
                subprocess.getstatusoutput(cmd2)
                for fn in os.listdir('../openalpr/src/build/images/'):
                        cmd3 = 'alpr -c us ../openalpr/src/build/images/' + fn
                        (status, output) = subprocess.getstatusoutput(cmd3)
                        print(output)
                i = i + 1
        cmd4 = 'sudo service motion stop'
        subprocess.getstatusoutput(cmd4)
        filenames = os.listdir(dir)
        for filename in filenames:
                path = os.path.join(dir, filename)
                print(path)
                print(os.path.abspath(path))

def main():
        List(sys.argv[1])


if __name__ == '__main__':
        main()

