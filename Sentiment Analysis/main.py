import string
from collections import Counter
import matplotlib.pyplot as plt

#To read from input.txt file
file_input = open('input.txt',encoding='utf-8').read()
#To convert into lower case
lower_case_input = file_input.lower()
#To remove punctuation
clean_text = lower_case_input.translate(str.maketrans('','',string.punctuation))


#Breaks into tokens
token_words = clean_text.split()
#List of all stop words
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves","could", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#final_words stores only essential words
final_words=[]

#removes all stop words from the token words list
for word in token_words:
    if word not in stop_words:
        final_words.append(word)


emotionsdict = {}
#stores all the emotions in emotions.txt file in a dictionary
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace("'",'').replace(",",'').strip()
        word, emotion = clear_line.split(':')
        emotionsdict[word] = emotion

emotions_list = []
#if final_words contain emotions, we add them to emotions_list
for word in final_words:
    if word in emotionsdict:
        print(word+" : "+emotionsdict[word])
        emotions_list.append(emotionsdict[word])

#A dictionary for storing the count of each emotion in emotions_list
emotions_counter = Counter(emotions_list)

fig, axis = plt.subplots()
#plots a bar graph
axis.bar(emotions_counter.keys(),emotions_counter.values())
fig.autofmt_xdate()
plt.savefig("graph.jpg")
plt.show()

