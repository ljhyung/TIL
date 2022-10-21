import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    lst = sentences.split('.')
    res = []
    for i in range(len(lst)):
        temp = lst[i]
        temp = nlp(temp)
        res += [ent.text for ent in temp.ents if ent.label_ == 'PERSON']
    return res
