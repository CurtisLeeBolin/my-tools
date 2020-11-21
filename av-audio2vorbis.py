#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  audio2vorbis.py
#
#  Copyright 2013 Curtis Lee Bolin <curtlee2002@gmail.com>
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
    'vob'
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
    p = subprocess.Popen(shlex.split(args), stderr=subprocess.PIPE)
    stdoutData, stderrData = p.communicate()
    if stdoutData is not None:
        stdoutData = stdoutData.decode(encoding='utf-8', errors='ignore')
    if stderrData is not None:
        stderrData = stderrData.decode(encoding='utf-8', errors='ignore')
    return {'stdoutData': stdoutData, 'stderrData': stderrData, 'returncode': p.returncode}

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
                outputFile = '{}/{}.mkv'.format(dirDict['output'], fileName)
                outputFilePart = '{}.part'.format(outputFile)
                os.rename(f, inputFile)
                printLog('Starting: {}'.format(fileName))
                if inputArgs.mono:
                    args = ('ffmpeg -i {} -map_metadata -1 -c:v copy -ac 1 -c:a libvorbis -q:a 3 -c:s ass -metadata title="{}" -y -f matroska {}'.format(inputFile.__repr__(), fileName.__repr__(), outputFilePart.__repr__()))
                else:
                    args = ('ffmpeg -i {} -map_metadata -1 -c:v copy -c:a libvorbis -q:a 3 -c:s ass -metadata title="{}" -y -f matroska {}'.format(inputFile.__repr__(), fileName.__repr__(), outputFilePart.__repr__()))
                subprocessDict = runSubprocess(args)
                if subprocessDict['returncode'] != 0:
                    if inputArgs.mono:
                        args = ('ffmpeg -i {} -map_metadata -1 -c:v copy -ac 1 -c:a libvorbis -q:a 3 -sn -metadata title="{}" -y -f matroska {}'.format(inputFile.__repr__(), fileName.__repr__(), outputFilePart.__repr__()))
                    else:
                        args = ('ffmpeg -i {} -map_metadata -1 -c:v copy -c:a libvorbis -q:a 3 -sn -metadata title="{}" -y -f matroska {}'.format(inputFile.__repr__(), fileName.__repr__(), outputFilePart.__repr__()))
                subprocessDict = runSubprocess(args)
                os.rename(outputFilePart, outputFile)
                printLog('Completed: {}'.format(fileName))
