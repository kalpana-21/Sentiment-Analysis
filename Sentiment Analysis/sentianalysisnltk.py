import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer

#To read from input.txt file
file_input = open('input.txt',encoding='utf-8').read()
#To convert into lower case
lower_case_input = file_input.lower()
#To remove punctuation
clean_text = lower_case_input.translate(str.maketrans('','',string.punctuation))


#Breaks into tokens
token_words = word_tokenize(clean_text,"english")

#final_words stores only essential words
final_words=[]

#removes all stop words from the token words list
for word in token_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - Makes Plural to Singular as well as gets the base form of a word(ex: worse-> bad)
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)
emotionsdict = {}
#stores all the emotions in emotions.txt file in a dictionary
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n",'').replace("'",'').replace(",",'').strip()
        word, emotion = clear_line.split(':')
        emotionsdict[word] = emotion

emotions_list = []
#if final_words contain emotions, we add them to emotions_list
for word in lemma_words:
    if word in emotionsdict:
        emotions_list.append(emotionsdict[word])

#analyses the sentiment in the text
def senti_analyser(text):
    points = SentimentIntensityAnalyzer().polarity_scores(text)
    if points['neg'] > points['pos']:
        print("Negative Sentiment")
    elif points['neg'] < points['pos']:
        print("Positive Statement")
    else:
        print("Neutral Statement")

senti_analyser(clean_text)
#A dictionary for storing the count of each emotion in emotions_list
emotions_counter = Counter(emotions_list)

fig, axis = plt.subplots()
#plots a bar graph
axis.bar(emotions_counter.keys(),emotions_counter.values())
fig.autofmt_xdate()
plt.savefig("graph.jpg")
plt.show()

