class Node(object):
    def __init__(self,value=0,next = None, prev= None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):

    def __init__(self, homepage):
        #노드 1개만 생성
        self.head = self.tail= Node(homepage)

    def visit(self, url):
        new_node = Node(url)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = self.tail.next

    def back(self, steps):
        while steps > 0 and self.tail.prev != None:
            steps -=1
            self.tail = self.tail.prev
        return self.tail.value
    def forward(self, steps):
        while steps > 0 and self.tail.next != None:
            steps -=1
            self.tail = self.tail.next
        return self.tail.value
