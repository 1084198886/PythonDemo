"""
文件升级打包
"""
import hashlib
import os
import subprocess
import sys
import zipfile

sh256_file = 'sh256.sign'


def sh256_checknum(apkFile):
    hash256 = hashlib.sha256()
    srcFile = open(apkFile, 'rb')
    with srcFile as f:
        for block in iter(lambda: f.read(4096), b''):  # TODO
            hash256.update(block)
        srcFile.close()
    hash256.update(b'nzoqPYMIu91VViA/mEIG5FtJXi8=')
    hashFile = os.path.dirname(apkFile) + '/' + sh256_file
    print('hashFile=', hashFile)
    with open(hashFile, 'w+') as f:
        f.write(hash256.hexdigest())
        f.close()


def zip_file(apkFile, flag):
    apkDir = os.path.dirname(apkFile)
    version = subprocess.check_output(
        ['git', 'describe', '--abbrev=4', '--dirty', '--always', '--tags']).strip().decode("UTF-8")

    print('git   version=' + version)
    zipfileName = apkDir + '/' + flag + '-' + version + ".zip"
    zipFile = zipfile.ZipFile(zipfileName, 'w', zipfile.ZIP_DEFLATED)
    zipFile.write(apkFile, flag + ".apk")
    zipFile.write(apkDir + '/' + sh256_file, sh256_file)
    zipFile.close()


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 2 or args[1] not in ('sw', 'nc', 'v8'):
        print('missing sw nc v8')
        exit(1)
    if args[1] == 'sw':
        apkFile = './app_swlib.apk'
        flag = 'dcpossw'
    elif args[1] == 'nc':
        apkFile = './app_nclib.apk'
        flag = 'dcposnc'
    else:
        apkFile = './app_v8lib.apk'
        flag = 'dcposv8'
    if not os.path.exists(apkFile):
        print(apkFile + " not exist")
        exit(1)

    print('apkFile :', apkFile)
    print('flag :', flag)
    sh256_checknum(apkFile)
    zip_file(apkFile, flag)
