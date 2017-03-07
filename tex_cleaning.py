# -*-coding:utf-8-*-


import os


def tex_cleaning(path):
    for fname in os.listdir(path):
        name, ext = os.path.splitext(fname)
        latex_exts = [".aux", ".out", ".nav", ".snm", ".toc", ".log", ".gz"]
        if (ext in latex_exts) and \
                (name.replace(".synctex", "") + ".tex" in os.listdir(path)):
            os.remove(os.path.join(path, fname))
    print("finish task: %s" % (path))


def main():
    paths = ["/Users/zhangguo/CPP/Literatures - Online Retailer Searching",
             "/Users/zhangguo/CPP/Literatures - Handbook of IO",
             "/Users/zhangguo/CPP/Literatures - Online Retailer Searching/Reputation",
             "/Users/zhangguo/CPP/Literatures - CPI",
             "/Users/zhangguo/CPP/Literatures - Discrete Choice Model",
             "/Users/zhangguo/MyLectures/PyLive/Python基础精讲",
             ]
    for path in paths:
        tex_cleaning(path)


if __name__ == "__main__":
    main()
