import pandas as pd

import spacy
import en_core_web_sm

class Classify():
    '''
    Classify takes a set of text and extracts data useful for NLP tasks.

    It is largely designed to work with news articles about companies, and can
    be used to normalise text for machine learning problems.
    '''
    nlp = en_core_web_sm.load()

    def __init__(self, article_body, orgs_dict={}):
        '''
        Create a new instance of a Classified article

        Keyword arguments:
        article_body -- A string representation of the text within an article
        orgs_dict -- A dict containing a mapping of person names to the organisation they belong to
        '''
        self.doc = self.nlp(article_body)
        self.__orgs = orgs_dict


    def entities(self):
        '''
        Return the named organisation entities from the article, including the
        organisations named persons belong to
        '''
        entities = []
        unknown = []

        for i in self.doc.ents:
            if i.label_ in ['ORG']:
                entities.append(i.text)

            if i.label_ == 'PERSON':
                o = self.__org(i.text)
                if o not in ["", None]:
                    entities.append(o)
                else:
                    unknown.append(i.text)

        return pd.DataFrame({'entities': entities}), unknown


    def normalise(self):
        '''
        Return the article body after the following transformations:

        1 -- Removal of any recognised entity
        2 -- Removal of stop words
        3 -- Lematisation of words

        This string can be used in ML models
        '''
        non_entities = self.__non_entities(self.doc)
        non_stops = self.__de_stopword(non_entities)
        lematised = self.__lematise(non_stops)

        return ' '.join(lematised)


    def __org(self, name):
        return self.__orgs.get(name)


    def __non_entities(self, doc):
        out = []

        for elem in doc:
            if elem.ent_iob_ == "O":
                out.append(elem)

        return out


    def __de_stopword(self, doc):
        return [elem for elem in doc if not elem.is_stop]


    def __lematise(self, doc):
        return [elem.lemma_ for elem in doc]
