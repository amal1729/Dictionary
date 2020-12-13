class Node:
    def __init__(self, word, meaning):
        self.lc = None
        self.rc = None
        self.word = word
        self.meaning = meaning
class BST:
    def __init__(self):
        self.root = None

    def insert(self, cn):
        if self.root is None:
            self.root = cn
        else:
            self.add(self.root, cn)

    def add(self, cn, node):
        if cn is not None:
            if node.word <= cn.word:
                if cn.lc:
                    self.add(cn.lc, node)
                else:
                    cn.lc = node
            elif node.word > cn.word:
                if cn.rc:
                    self.add(cn.rc, node)
                else:
                    cn.rc = node

    def find(self, word):
        return self.search(self.root, word)

    def search(self, cn, word):
        if cn is None:
            return False
        elif word == cn.word:
            return cn
        elif word < cn.word:
            return self.search(cn.lc, word)
        else:
            return self.search(cn.rc, word)

    def readInput(self,fileName):
        try:
            counter = 0
            with open(fileName) as f:
                for l in f:
                    l=l.split(' / ')
                    Tree.insert(Node(l[0], l[1]))
                    counter +=1
            return counter
        except Exception:
            print("An exception occurred")

if __name__ == '__main__':
    Tree = BST()
    subList = []
    counter = Tree.readInput('ArraydictPS14.txt')
    with open('outputPS14.txt', 'w') as f:
        f.write('-----------Reading from file ArraydictPS14.txt -------------\nBST Created with '+str(counter)+' nodes')
        f.write('\n---------------------------------------------------\n---------------- Search words ------------------------\n')
        with open('promoptsPS14.txt') as p:
            for l in p:
                l=l.strip().split(': ')
                if l[0] == 'SearchWord':
                    sr= Tree.find(l[1])
                    if sr:
                        f.write(sr.word + '-' + sr.meaning)
                    else:
                        f.write(str(l[1]) + '- not found')
                elif l[0] == 'SubString':
                    subList.append(l[1])
        for s in subList:
            f.write('\n---------------------------------------------------\n---------------- Sub String:'+s+'------------------------\n')