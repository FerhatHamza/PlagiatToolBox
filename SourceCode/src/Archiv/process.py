import naftawayh.wordtag 
from naftawayh.wordtag import WordTagger
import sys
from nltk import sent_tokenize
import pyarabic.araby as araby

from collections.abc import Iterable

import Clean_and_Segmentation.script
import sys
import re
import io
import codecs
import json

def break_into_sentences(text):
    #f = io.open(corpus_file, 'r', encoding='utf8')
    Sentence_Size = 0
    Max_Size = 40  # Max_Size od the sentences
    paragraph = text               #f.read()
	#remove_diacritics fct
    regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]')
    paragraph = re.sub(regex, '', paragraph)
    #remove_urls fct
    regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
    paragraph = re.sub(regex, '', paragraph)
    regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+")
    paragraph = re.sub(regex, '', paragraph)
	#remove one_character words
    regex = re.compile(r'\s.\s')
    paragraph = re.sub(regex, ' ', paragraph)
    #resultFile = io.open("SEG_" + corpus_file, 'w',encoding='utf8')
    sentences = list()
    temp_sentence = list()
    flag = False
    for ch in paragraph.strip():
        if ch in [u'؟', u'!', u'.', u':', u'؛',u'?']:
            Sentence_Size = 0
            flag = True
        elif flag:
            sentences.append(''.join(temp_sentence).strip())
            temp_sentence = []
            flag = False
        regex = re.compile(r'[إأٱآا]')
        ch = re.sub(regex, 'ا', ch)
        regex = re.compile(r'[ئ]')
        ch = re.sub(regex, 'ى', ch)
        #remove_non_arabic_symbols fct
        ch = re.sub(r'[^\u0600-\u06FF]', ' ', ch)		
        temp_sentence.append(ch)
        if ch.isspace():
           Sentence_Size = Sentence_Size + 1
           if Sentence_Size > Max_Size:
              Sentence_Size = 0
              flag = True
              
    else:
        sentences.append(''.join(temp_sentence).strip())
        return sentences
        #for item in sentences:
        #    resultFile.write("%s\n" % re.sub(' +', ' ', item))

def single_list(list,ignore_types=(str)): 
    for item in list:
        if isinstance(item, Iterable) and not isinstance(item, ignore_types):
            yield from single_list(item,ignore_types=(str))
        else:
            yield item

def text_Process(text):
    sentences = break_into_sentences(text)
    tagger = naftawayh.wordtag.WordTagger();
    words = []
    for sentence in sentences:
        words.append(araby.tokenize(sentence))

    w = []
    with codecs.open('./src/t1.json','w',encoding="utf-8") as outfile1:
        outfile1.write(json.dumps(w, ensure_ascii=False ,indent=4))

    # split a nested list into a single list
    word = single_list(words)

    obj = {}
    obj['words'] = []
    words_json = []

    ff = open("./src/t1.txt", "w", encoding="utf-8")
    for w in word:
        tag = ''
        if w != '،':
            if tagger.is_stopword(w): 
                tag += 'T'
            if tagger.is_noun(w):
                tag += 'N'
            if tagger.is_verb(w) and not tagger.is_noun(w):
                tag += 'V'
            obj['words'].append({'word': w , 'type': tag[0], 'other': 'vide'})
            ff.write(w+":"+tag[0]+"\n")



    with codecs.open('./src/t1.json','w',encoding="utf-8") as outfile:
        outfile.write(json.dumps(obj, ensure_ascii=False ,indent=4))


text = sys.argv[1] 


#text = u"هذا النص هو مثال لنص يمكن أن يستبدل في نفس المساحة، لقد تم15 توليد هذا النص من مولد ?النص العربى، حيث يمكنك أن تولد مثل هذا النص. أو العديد من النصوص  1564 الأخرى إضافة إلى زيادة عدد الحروف التى يولدها التطبيق."
# text = "الانتحال يدمر حياتك المهنية. منذ فتره طويلة"
# Clean up the text and break it up into sentences
sentences = break_into_sentences(text)

tagger = naftawayh.wordtag.WordTagger();  


words = []

# Break sentences into words
for sentence in sentences:
    words.append(araby.tokenize(sentence))

print("begin")

w = []
with codecs.open('./src/t1.json','w',encoding="utf-8") as outfile1:
    outfile1.write(json.dumps(w, ensure_ascii=False ,indent=4))


# split a nested list into a single list
word = single_list(words)

obj = {}
obj['words'] = []
words_json = []

ff = open("./src/t1.txt", "w", encoding="utf-8")
for w in word:
    tag = ''
    if w != '،':
        if tagger.is_stopword(w): 
            tag += 'T'
        if tagger.is_noun(w):
            tag += 'N'
        if tagger.is_verb(w) and not tagger.is_noun(w):
            tag += 'V'
        obj['words'].append({'word': w , 'type': tag[0], 'other': 'vide'})
        ff.write(w+":"+tag[0]+"\n")



with codecs.open('./src/t1.json','w',encoding="utf-8") as outfile:
    outfile.write(json.dumps(obj, ensure_ascii=False ,indent=4))



ff.close()

print("end")
# debugging


# enumerate :for split LIST to index and item encoding="utf-8"


sys.stdout.flush()