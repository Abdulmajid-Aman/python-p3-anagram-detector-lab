# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        anagrams = list()
        for item in list_of_words:
            if sorted(item) == sorted(self.word):
                anagrams.append(item)
        return anagrams

word = Anagram('word')
print(word.match(['hello', 'goodbye'])) 
word2 = Anagram('enlist')
print(word2.match(['listen', 'silent', 'hippopotamus']))