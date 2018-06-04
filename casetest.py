import os

class CaseTest():
    def __init__(self):
        path = os.getcwd() + '/inputs/'
        print os.listdir(path)

t = CaseTest()   