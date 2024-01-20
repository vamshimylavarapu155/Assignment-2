f=open("input.txt","w")
f.write("Python Course\n")
f.write("Deep Learning Course")
f.close()
f=open("input.txt","r")
print(f.read())
f.close()

from collections import Counter
def count_words(filename):
    with open(filename) as f:
        return Counter(f.read().split())

with open("output.txt","a") as f:
    print("Number of words in the file:\n", count_words("input.txt"))