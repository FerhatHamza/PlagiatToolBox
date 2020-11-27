
from py7.traitement2 import Process             
from nltk.util import ngrams # function for making ngrams
import naftawayh.wordtag
from naftawayh.wordtag import WordTagger
import adawat.adaat


class _2l_apd:
    def __init__(self, tsrs, tsp):
        self.text_src = tsrs
        self.text_sup = tsp
        self.src = Process(self.text_src)
        self.sup = Process(self.text_sup)
    
    def Segmentation(self):
        Seg_result = {}
        Seg_result['srs'] = self.src.Segmentation()
        Seg_result['sup'] = self.sup.Segmentation()
        return Seg_result

    def Pretraitement(self):
        Pre_result = {}
        Pre_result['srs'] = self.src.Pretraitement()
        Pre_result['sup'] = self.sup.Pretraitement()
        return Pre_result

    def Lemmatisation(self):
        Lem_result = {}
        Lem_result['srs'] = self.src.Lemmatisation()
        Lem_result['sup'] = self.sup.Lemmatisation()
        return Lem_result

    def convert(self, r):                              # 
        a = ''
        for item in r:
            a = a + item
        return a

    def trigram(self):
        result = self.Lemmatisation()
        # return ngrams(result.get('srs'), 3)
        srs = self.convert(result.get('srs'))
        sup = self.convert(result.get('sup'))
        print("srs :",srs," - sup :",sup)
        srs_1 = ''
        for i, item in enumerate(srs, start=1): 
            if i % 4 == 0 :
                srs_1 = srs_1 + ","
            else:
                srs_1 = srs_1 + item
        
        sup_1 = ''
        for i, item in enumerate(sup, start=1): 
            if i % 4 == 0 :
                sup_1 = sup_1 + ","
            else:
                sup_1 = sup_1 + item

        print('final text - srs_1 -: ',srs_1)
        print('final - srs_1 -:',srs_1.split(','))

        print('final text - sup_1 -: ',sup_1)
        print('final - sup_1 -:',sup_1.split(','))

        return [srs_1, sup_1]

t_srs = 'ذهب يوسف الى الكلية للحضور الى الندوة العلمية'
t_sup = 'يمضي يوسف مسرعا للجامعة من أجل الحضور للدورة العلمية'

m = _2l_apd(t_srs, t_sup)


# a = m.Segmentation()
# b = m.Pretraitement()
# c = m.Lemmatisation()



print('trigrams :::::::::::::')

pp = m.trigram()
print(pp)


# print(c.get('srs').get('words'))

# if 'srs' in c:
#     print(" ok ok ")
# else:
#     print("no no")



