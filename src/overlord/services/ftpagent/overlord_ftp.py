import ftplib
import os
import io
import requests


class OverlordFtp:
    phpInstaller = "overlord-serverside-installation-agent.php"
    zipPackage = "overlord-webapp-update-package.zip"

    def __init__(self, rootPath):
        self.rootPath = rootPath

    def writeRerouteHtaccess(self):
        htaccess = io.BytesIO()
        htaccess.write(b"DirectoryIndex index.php\n\r")
        htaccess.write(b"RewriteEngine On \n\r")
        htaccess.write(b"RewriteRule ^$ public/index.php [L]\n\r")
        htaccess.write(b"RewriteRule ^((?!public/).*)$ public/$1 [L,NC]\n\r")
        htaccess.seek(0)
        self.ftpHook.storbinary("STOR " + self.rootPath + "/.htaccess", htaccess)

    def writeMinimalInstaller(self):
        phpScript = io.BytesIO()
        phpScript.write(b"<?php \n\r")
        phpScript.write(b'system("unzip -oq ')
        phpScript.write(bytes(OverlordFtp.zipPackage, "utf-8"))
        phpScript.write(b' -d /");\n\r')
        phpScript.write(b'unlink("')
        phpScript.write(bytes(OverlordFtp.zipPackage, "utf-8"))
        phpScript.write(b'");\n\r')
        phpScript.write(b"unlink(__FILE__);\n\r")
        phpScript.write(b'echo "OK";\n\r')
        phpScript.write(b"die();\n\r")
        phpScript.seek(0)
        self.ftpHook.storbinary(
            "STOR " + self.rootPath + "/" + OverlordFtp.phpInstaller, phpScript
        )

    def config(self, host, username, password):
        self.ftpHost = host
        self.ftpUser = username
        self.ftpPass = password

    def connect(self, mode="FTP"):
        if mode.lower() == "ftp":
            self.ftpHook = ftplib.FTP(self.ftpHost)
        elif mode.lower() == "ftps":
            self.ftpHook = ftplib.FTP_TLS(self.ftpHost)
        else:
            raise NameError("unsupported file transfer mode!")
        self.ftpHook.login(self.ftpUser, self.ftpPass)

    def end(self):
        self.ftpHook.close()

    def delDirTree(
        self, path, withThisDir=True
    ):  # idea from https://stackoverflow.com/questions/10042838/delete-all-files-and-folders-after-connecting-to-ftp
        self.ftpHook.cwd(path)
        for item in self.ftpHook.nlst():
            try:
                self.ftpHook.delete(item)
            except Exception:
                self.delDirTree(item)
        self.ftpHook.cwd("..")
        if withThisDir:
            self.ftpHook.rmd(path)

    def clearWebapp(self):
        self.delDirTree(self.rootPath, False)

    def updateApp(self, zipFilePath):
        self.clearWebapp()
        with open(zipFilePath, "rb") as file:
            self.ftpHook.storbinary(
                "STOR " + self.rootPath + "/" + OverlordFtp.zipPackage, file
            )
        self.writeMinimalInstaller()

    def lounchServerSideAct(self, appname):
        appDomain = ".".join(appname.split("_"))
        result = requests.get("http://" + appDomain + "/" + OverlordFtp.phpInstaller)
        return (result.text, result)
