#!/usr/bin/python3

import re
import subprocess
import sys
import os


def List(dir):
        var = 'ABC1234'
        cmd1 = 'sudo service motion start'
        subprocess.getstatusoutput(cmd1)
        i = 0
        while (i < 10000):
                cmd2 = 'cp /var/lib/motion/* ../openalpr/src/build/images/'
                subprocess.getstatusoutput(cmd2)
                for fn in os.listdir('../openalpr/src/build/images/'):
                        cmd3 = 'alpr -c us ../openalpr/src/build/images/' + fn
                        (status, output) = subprocess.getstatusoutput(cmd3)
                        list1 = []
                        list1.append(output)
                        for license in list1:
                                print(license)
                                if (license.find(var) != -1):
                                        print('Detected')
                                        cmd6 = 'sudo python servo1.py'
                                        subprocess.getstatusoutput(cmd6)
                                        cmd4 = 'sudo service motion stop'
                                        subprocess.getstatusoutput(cmd4)
                                        break

                i = i + 1
        cmd8 = 'sudo service motion stop'
        subprocess.getstatusoutput(cmd8)
        filenames = os.listdir(dir)
        for filename in filenames:
                path = os.path.join(dir, filename)
                print(path)
                print(os.path.abspath(path))


def main():
        List(sys.argv[1])


if __name__ == '__main__':
        main()

