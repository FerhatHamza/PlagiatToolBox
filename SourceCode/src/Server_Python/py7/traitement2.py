
from pyarabic.araby import strip_harakat                 # remove harakat 
from pyarabic.araby import strip_tashkeel                # clean text
from pyarabic.araby import strip_tatweel, strip_shadda   # tatweel and remove shadda 
from pyarabic.araby import normalize_ligature            # correction
from pyarabic import araby                               # tafri9 text words
import naftawayh.wordtag
from naftawayh.wordtag import WordTagger
from collections.abc import Iterable                      

import pyarabic.arabrepr
arepr = pyarabic.arabrepr.ArabicRepr()
repr = arepr.repr
from tashaphyne.stemming import ArabicLightStemmer


import sys
import re     
import io   # Python io module allows us to manage the file-related input and output operations
import codecs 
import json
sys.path.append('Clean_and_Segmentation')


class Process:
    def __init__(self, t):       # self = this(java)
        self.text = t
        
    def removeHarakat(self, t):
        return strip_harakat(t)
    
    def removetashkeel(self, t):
        return strip_tashkeel(t)

    def removeTatweel(self, t):
        return strip_tatweel(t)   

    def break_into_words(self):
        return araby.tokenize(self.text)  

    def break_into_sentences(self):
        #f = io.open(corpus_file, 'r', encoding='utf8')
        Sentence_Size = 0
        Max_Size = 40  # Max_Size od the sentences
        paragraph = self.text               #f.read()
        #remove_diacritics fct
        regex = re.compile(r'[\u064B\u064C\u064D\u064E\u064F\u0650\u0651\u0652]') # fa'tha - dama ... 
        paragraph = re.sub(regex, '', paragraph)
        #remove_urls fct
        regex = re.compile(r"(http|https|ftp)://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
        paragraph = re.sub(regex, '', paragraph)
        regex = re.compile(r"(\d|[\u0660\u0661\u0662\u0663\u0664\u0665\u0666\u0667\u0668\u0669])+") # 0-1-2-3-4-5-6--7-8-9 arabic numbers
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

    def single_list(self,list,ignore_types=(str)): #  ['hbk','kb','bui',[],'jn'] = ['hbk','kb','bui', [kb','bui'],'jn']
        for item in list:
            if isinstance(item, Iterable) and not isinstance(item, ignore_types):
                yield from self.single_list(item,ignore_types=(str))
            else:
                yield item

    def text_Process(self):
        sentences = self.break_into_sentences()
        tagger = naftawayh.wordtag.WordTagger();
        words = []
        for sentence in sentences:
            words.append(araby.tokenize(sentence))

        w = []
        # split a nested list into a single list
        word = self.single_list(words)

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

        result = json.dumps(obj, ensure_ascii=False, indent=4).encode('utf-8')
        return result

    def sentance_Process(self):
        sentences = self.break_into_sentences()
        obj = {}
        obj['sentences'] = []

        for num, sentence in enumerate(sentences, start=1):
            obj['sentences'].append({'id': num ,'sentance' : sentence})

        result = json.dumps(obj, ensure_ascii=False, indent=4).encode('utf-8')
        return result

    def Segmentation(self):
        return self.break_into_sentences()

    def Pretraitement(self):
        t1 = self.removeHarakat(self.text)
        t1 = self.removetashkeel(t1)
        t1 = self.removeTatweel(t1)
        print(t1)
        tagger = naftawayh.wordtag.WordTagger();
        sentences = self.Segmentation()
        words = []
        
        for sentence in sentences:
            words.append(araby.tokenize(sentence))

        print("words -- : " ,words)
        words_clear = []
        word = self.single_list(words)
        for w in word:
            if w != '،':
                if not tagger.is_stopword(w):
                    words_clear.append(w)
        
        return words_clear;

    def aff(self, w):
        for item in w:
            print(item)
            print("\n")
    
    def Lemmatisation(self):
        tagger = naftawayh.wordtag.WordTagger();
        ws = self.Pretraitement()
        ArListem = ArabicLightStemmer()
        words_root = []
        words_all = {}
        words_all['words'] = [] 
        for w in ws:
            #if not tagger.is_noun(w):
            stem = ArListem.light_stem(w)
            ww = ArListem.get_prefix()+" + "+ ArListem.get_stem() + " + " + ArListem.get_suffix()
            words_all['words'].append(ww)
            words_root.append(ArListem.get_stem())
    
        self.aff(words_all)

        result = json.dumps(words_all, ensure_ascii=False, indent=4).encode('utf-8')
        return words_root

# p = Process("مرحبا بكم  جميعا!، هل أنت بخير، ان شاء الله تكونون بخير.")
# print('hello: ')
# print("this is text", p.Lemmatisation()) 


