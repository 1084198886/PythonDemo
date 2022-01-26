# coding=utf-8
# 使用python做升级文件打包

import hashlib
import sys
import zipfile
from os import path
import subprocess

hashFileName = 'hash256.sign'


def sha256_checknum(apk):
    hash256 = hashlib.sha256()
    srcFile = open(apk, 'rb')
    with srcFile as f:
        for block in iter(lambda: f.read(4096), b''):
            hash256.update(block);
    srcFile.close()
    hash256.update(b'nzoqPYMIu91VViA/mEIG5FtJXi8=')

    hashFile = path.dirname(apk) + '/' + hashFileName
    print('hashFile = ' + hashFile)
    destFile = open(hashFile, 'w+')
    destFile.write(hash256.hexdigest())
    destFile.close()


def zip_file(apk, flag):
    fileDir = path.dirname(apk)
    version = subprocess.check_output(
        ['git', 'describe', '--abbrev=4', '--dirty', '--always', '--tags']).strip().decode('utf-8')

    zipFile = fileDir + '/' + flag + '-' + version + '.zip'
    print('zipFile = ' + zipFile)

    zf = zipfile.ZipFile(zipFile, 'w', zipfile.ZIP_DEFLATED)
    zf.write(fileDir + '/' + hashFileName, hashFileName)
    zf.write(apk, flag + '.apk')
    zf.close()


####################################################
######    参数: sw 编译树维卡库APK        ##########
######    参数: nc 编译新开普卡库APK      ##########
######    参数: lc 编译通用守护进程APK    ##########
####################################################

if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 2 or (sys.argv[1] != 'sw' and sys.argv[1] != 'nc' and sys.argv[1] != 'lc'):
        print('miss parameter:sw or nc or lc')
        print('sw --build swlib apk')
        print('nc --build nclib apk')
        print('lc --build launcher apk')
        exit(1)
    if sys.argv[1] == 'sw':
        appFile = './app/build/outputs/apk/release/app_swlib.apk'
        flag = 'dcpossw'
    elif sys.argv[1] == 'nc':
        appFile = './app/build/outputs/apk/release/app_nclib.apk'
        flag = 'dcposnc'
    else:
        appFile = './launcher/build/outputs/apk/release/launcher.apk'
        flag = 'dclauncher'
    print('appFile = ' + appFile)

    if not path.exists(appFile):
        print(appFile + ' is not exist')
        exit(1)
    sha256_checknum(appFile)
    zip_file(appFile, flag)
    print('build upgrade zip success!')
