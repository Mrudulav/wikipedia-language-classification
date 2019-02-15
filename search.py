"""
CSCI-630.01/02: Search
Author: MRUDULA VIJAYANARSHIMA @ RIT CS

A program to solve problem of searching given two words
and their minimal path of words.
"""
import sys

class Queue():
    """
        A class that is used as a queues functionality to
        make the smooth flow of words when the search is happening
    """
    def __init__(self):
        """
                Create a new instance.
                :return: None
        """
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue == []

class Node:
    """
        A class that converts nodes (letters) from
        one word to nodes of another word only through
        intervals of 1 element
    """
    def __init__(self, name):
        """
                Create a new instance.
                :param filename: The name of the source file
                :return: None
        """
        self.name = name
        self.vertex = []

    __slots__ = ('name', 'vertex')

    def __str__(self):
        result = self.name + ' : '
        for n in self.vertex:
            result += n.name + ', '
        return result[:-1]


def buildWordGraph(file):
    alphabet = {}
    f = open(file)
    words = f.read().split('\n')
    for word in words:
        for i in range(len(word)):
            letter = word[:i] + '*' + word[i + 1:]
            if letter in alphabet:
                alphabet[letter].append(word)
            else:
                alphabet[letter] = [word]
                alphabet[letter].append(word)
                result += n.name

    for key in alphabet:
        wordlist = alphabet[key]
        for w1 in wordlist:
            for w2 in wordlist:
                if w1 != w2:
                    inputGraph(w1, w2)


def inputGraph(word1, word2):
    if word1 not in Graph:
        node = Node(word1)
        node.vertex.append(Node(word2))
        Graph[word1] = node
    else:

        vertex = Graph[word1].vertex

        if word2 not in [x.name for x in vertex]:
            vertex.append(Node(word2))

    if word2 not in Graph:
        node = Node(word2)
        node.vertex.append(Node(word1))
        Graph[word2] = node
    else:

        vertex = Graph[word2].vertex

        if word1 not in [x.name for x in vertex]:
            vertex.append(Node(word1))

    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def __str__(self):
        return str(self.queue)

    def empty(self):
        return self.queue==[]

def bfs(start,finish,Graph):
    parents={}
    q=Queue()
    q.enqueue(start)
    parents[start.name]=None

    while(not q.empty()):
        node=q.dequeue()
        for vertex in node.vertex:
            n=vertex.name

            if n not in parents:
                parents[n]=node.name
                if n==finish.name:
                    return parents
                q.enqueue(Graph[vertex.name])

    return parents


def getPath(start,finish,parents):
    """
           A function that takes one word and finds all the path to get
           the second word through it
           :param parents: A list of letters preceeding it to form a word
           :return: A queue of strings for the postfix expression
    """
    finish = finish.name
    path = [finish]
    if finish in parents:
        node = parents[finish]
        while( node!=start.name ):
            path.append(node)
            node=parents[node]
    else:
        print("Path is not currently available")

    path.append(start.name)

    return path[::-1]

if __name__ == '__main__':
    """
        The main program prompts for the source file.  It then finds
        the 2 words and does single letter conversion until output is reached
        :return: None
    """
    Graph = {}
    file = "words"
    buildWordGraph(file)
    word1 = input("Input for Word 1 is : ")
    word2 = input("Input for Word 2 is : ")
    if len(sys.argv) > 1:
        word1 = sys.argv[1]
        word2 = sys.argv[2]
    if word1 in Graph:
        start = Graph[word1]
        if word2 in Graph:
            finish = Graph[word2]
            predecessors = bfs(start, finish, Graph)
            path = getPath(start, finish, predecessors)
            str = ''
            for p in path:
                str += p + ' -> '
            print(str[:-3])
        else:
            print("Word2 not in Graph")
    else:
        print("Word1 not in Graph")

