# -*-coding=utf-8-*-


import os


def png_rename(path):
    os.chdir(path)
    for fname in os.listdir(path):
        if 'png' in fname:

            new = fname.replace('png', '.png')
            os.rename(fname, new)


def main():
    png_rename("/Users/zhangguo/PyCN/PyLive/Python快速入门_2017-02-15")


if __name__ == "__main__":
    main()
