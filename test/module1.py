"""
"""
name = "Python教程"
add = "http://c.biancheng.net/python"


def say():
    print("人生苦短，我学Python！")


def hide_func():
    print("I'am a hide func")


class CLanguage:
    def __init__(self, name, add):
        self.name = name
        self.add = add

    def say(self):
        print(self.name, self.add)


__all__ = ['say', 'CLanguage']
# __main__的用法
#
# if __name__ == '__main__':
#     print("this is module2 __main__ :%s " % __name__)
# else:
#     print("this is not  module2 __main__ :%s " % __name__)

# __all__ = ["say", "CLanguage"]
