import os

class CaseTest():
    def __init__(self):
        path = os.getcwd() 
        path2 =  ['/inputs/','/outputs/']
        self.cases = {}
        for i in range( len(path) ):
            self.cases[i] = {}
            file = open( path + path2[0] + str(i) + '.in' )
            self.cases[i]['size'] = int(file.readline())
            self.cases[i]['matrix'] = []
            for j in range( self.cases[i]['size'] ):
                self.cases[i]['matrix'] += list( map(int,file.split() )
            file = open( path + path2[1] + str(i) + '.out' )
            self.cases[i]['answer'] = int(file.readline())
            
        print(self.cases)