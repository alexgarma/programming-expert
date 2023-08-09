from threading import Lock

class WordCounter:
    def __init__(self):
        self.text = None
        self.freq = { }
        self.lock = Lock()

    def process_text(self,text):
        self.text = text
        words = self.text.split(" ")
        
        for word in words:
            self.lock.acquire()
            if self.freq.get(word,0) == 0:
                self.freq[word] = 1
            else:
                self.freq[word] += 1
            self.lock.release()
    
    def get_word_count(self,word):
        self.lock.acquire()
        word_count = self.freq.get(word,0)
        self.lock.release()
        return word_count