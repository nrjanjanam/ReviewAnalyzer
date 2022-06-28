with open("stopwords.txt", "r") as f: 
        stop_words = f.read().split('\n')

print(stop_words)