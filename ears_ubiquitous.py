import nltk
import numpy as np
import textstat
from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

print("<---------------------------------->")

def read_text_file(filename):
    return open(filename, encoding="utf8").read()

text = read_text_file("fide_laws_of_chess.txt")
print("Dataset: FIDE Laws of Chess")
print("EARS Rule: Ubiquitous")
sentences = nltk.sent_tokenize(text)
ubi = 0
total = 0

for sent in sentences:
    noun_count = 0
    adj_count = 0
    pre_count = 0
    has_noun_before_shall = False
    has_shall = False
    has_verb_after_shall = False
    tokens = nltk.word_tokenize(sent)
    for i in range(0, len(tokens), 1):
        if nltk.pos_tag([tokens[i]])[0][1] == 'MD' and (tokens[i].lower() == 'shall' or tokens[i].lower() == 'should' or tokens[i].lower() == 'must'):
            has_shall = True
            for j in range(0, i, 1):
                if nltk.pos_tag([tokens[j]])[0][1] == 'NN':
                    has_noun_before_shall = True
            for k in range(i+1, len(tokens), 1):
                if nltk.pos_tag([tokens[k]])[0][1] == 'VB':
                    has_verb_after_shall = True
        if nltk.pos_tag([tokens[i]])[0][1] == 'NN':
            noun_count += 1
        elif nltk.pos_tag([tokens[i]])[0][1] == 'ADJ':
            adj_count += 1
        elif nltk.pos_tag([tokens[i]])[0][1] == 'IN':
            pre_count += 1
    if (has_noun_before_shall and has_shall and has_verb_after_shall): 
        ubi += 1
        
    total += 1
    word_count = textstat.lexicon_count(sent, removepunct=True)
    print('>--------------------------------------------------------------------------<')
    print('Statement: ' + sent)
    print('Number of Words: ' + str(word_count))
    print('Number of Adjectives: ' + str(adj_count))
    print('Number of Nouns: ' + str(noun_count))
    print('Proportion of Prepositions (%): ' + str((pre_count/word_count) * 100))
    print('Automated Readability Assessment: ' + str(textstat.automated_readability_index(sent)))

print('<-------------------------------------------------------------------------->')
print('Total Ubiquitous statements: ' + str(ubi) + '\n')
print('Total statements: ' + str(total) + '\n')