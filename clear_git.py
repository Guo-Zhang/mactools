# -*-coding:utf-8-*-


import os
import sys

def clear_git(path):
    if os.geteuid():
        args = [sys.executable] + sys.argv
        os.execlp('sudo', 'sudo', *args)
    for dirpath, dirnames, filenames in os.walk(path):
        if ".git" in os.listdir(dirpath):
            git_path = os.path.join(dirpath,".git")
            os.remove(git_path)
            print(git_path)

def main():
    paths = [
        "/Users/zhangguo/Codes/scrapers",
    ]
    for path in paths:
        clear_git(path)


if __name__=="__main__":
    main()