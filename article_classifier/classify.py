import pandas as pd

import spacy
import en_core_web_sm

class Classify():
    nlp = en_core_web_sm.load()

    def __init__(self, article_body, orgs_dict={}):
        self.doc = self.nlp(article_body)
        self.__orgs = orgs_dict


    def entities(self):
        entities = []

        for i in doc.ents:
            if i.label_ in ['ORG']:
                entities.append(i.text)

            if i.label_ == 'PERSON':
                o = self.__org(i.text)
                if o not in ["", None]:
                    entities.append(o)

        return pd.DataFrame(entities)


    def normalise(self):
        non_entities = self.__non_entities(self.doc)
        lematised = self.__lematise(non_entities)
        non_stops = self.__de_stopword(lematised)

        return non_stops


    def __org(self, name):
        return self.__orgs.get(name)


    def __non_entities(self, doc):
        out = []

        for elem in doc:
            if elem.ent_iob_ == "O":
                out.append(elem)

        return out


    def __lematise(self, doc):
        return [elem.lemma_ for elem in doc]


    def __de_stopword(self, doc):
        return [elem.text for elem in doc if not elem.is_stop]
