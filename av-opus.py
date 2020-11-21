#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  av-opus.py
#
#  Copyright 2018 Curtis Lee Bolin <curtlee2002@gmail.com>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os, shlex, subprocess, time, datetime, re, argparse

fileType = [
    'avi', 'flv', 'mov', 'mp4', 'mpeg', 'mpg', 'ogg', 'ogm', 'ogv', 'wmv',
    'm2ts', 'mkv', 'rmvb', 'rm', '3gp', 'm4a', '3g2', 'mj2', 'asf', 'divx',
    'vob', 'webm'
]
dirDict = {
    'input': '0in',
    'output': '0out',
    'log': '0log'
}

def checkFileType(fileExtension):
    fileExtension = fileExtension[1:].lower()
    result = False
    for ext in fileType:
        if (ext == fileExtension):
            result = True
            break
    return result

def runSubprocess(args):
    p = subprocess.Popen(args, stderr=subprocess.PIPE)
    stdoutData, stderrData = p.communicate()
    stderrData = stderrData.decode()
    return stderrData

def printLog(s):
    with open(dirDict['log'] + '/transcode.log', 'a') as f:
        f.write(s + '\n')
    print(s)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mono',
        help='Transcode audio in mono.',
        action="store_true")
    inputArgs = parser.parse_args()
    for key, dirName in dirDict.items():
        if not os.path.exists(dirName):
            os.mkdir(dirName, 0o0755)
    cwd = os.getcwd()
    fileList = os.listdir(cwd)
    fileList.sort()
    for f in fileList:
        if os.path.isfile(f):
            fileName, fileExtension = os.path.splitext(f)
            if checkFileType(fileExtension):
                inputFile  = '{}/{}'.format(dirDict['input'], f)
                outputFile = '{}/{}.ogg'.format(dirDict['output'], fileName)
                outputFilePart = '{}.part'.format(outputFile)
                os.rename(f, inputFile)
                printLog('Starting: {}'.format(fileName))
                if inputArgs.mono:
                    args = shlex.split('ffmpeg -i {} -vn -ac 1 -c:a libopus -sn -metadata title="{}" -y -f ogg {}'.format(inputFile.__repr__(), fileName, outputFilePart.__repr__()))
                else:
                    args = shlex.split('ffmpeg -i {} -vn -c:a libopus -sn -metadata title="{}" -y -f ogg {}'.format(inputFile.__repr__(), fileName, outputFilePart.__repr__()))
                stderrData = runSubprocess(args)
                os.rename(outputFilePart, outputFile)
                printLog('Completed: {}'.format(fileName))

