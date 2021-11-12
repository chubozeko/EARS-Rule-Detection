import nltk
import numpy as np

print("<---------------------------------->")

def read_text_file(filename):
    return open(filename, encoding="utf8").read()

print("Dataset: FIDE Laws of Chess")
print("EARS Rule: Event-driven")
text = read_text_file("fide_laws_of_chess.txt")
sentences = nltk.sent_tokenize(text)
event_d = 0
total = 0
for sent in sentences:
    has_event_trigger = False
    has_noun_before_shall = False
    has_shall = False
    has_verb_after_shall = False

    tokens = nltk.word_tokenize(sent)
    for i in range(0, len(tokens), 1):
        if (nltk.pos_tag([tokens[i]])[0][1] == 'WRB' and tokens[i].lower() == 'when') or (nltk.pos_tag([tokens[i]])[0][1] == 'IN' and (tokens[i].lower() == 'before' or tokens[i].lower() == 'after' or tokens[i].lower() == 'during')):
            has_event_trigger = True
            for l in range(i+1, len(tokens), 1):
                if nltk.pos_tag([tokens[l]])[0][1] == 'MD' and (tokens[l].lower() == 'shall' or tokens[l].lower() == 'should' or tokens[l].lower() == 'must'):
                    has_shall = True
                    for j in range(i+1, l, 1):
                        if nltk.pos_tag([tokens[j]])[0][1] == 'NN':
                            has_noun_before_shall = True
                            for k in range(j, len(tokens), 1):
                                if nltk.pos_tag([tokens[k]])[0][1] == 'VB':
                                    has_verb_after_shall = True
    if (has_event_trigger and has_noun_before_shall and has_shall or has_verb_after_shall):
        event_d += 1
        
    total += 1

print('Total Event-driven statements: ' + str(event_d) + '\n')
print('Total statements: ' + str(total) + '\n')