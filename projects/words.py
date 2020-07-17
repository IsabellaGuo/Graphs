
class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size()> 0:
            return self.queue.pop(0)
        else:
            return None
    
    def size(self):
        return len(self.queue)

def word_ladder(self, begin_word, end_word):

    q = Queue()
    q.enqueue([begin_word])
      

    
             

