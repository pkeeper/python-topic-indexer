import os
import random
import re
import json
import gc
import nltk
import pickle
from itertools import izip_longest
from nltk.stem.porter import PorterStemmer
from nltk.tokenize.regexp import wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.pipeline import Pipeline
from nltk.classify.naivebayes import NaiveBayesClassifier
from pprint import pprint
from collections import defaultdict
from sklearn.svm import LinearSVC


porter_stemmer = PorterStemmer()
sw = stopwords.words('english')
skclassifier = SklearnClassifier(LinearSVC(multi_class='ovr'))
gc.disable()

RECORDS_TO_TRAIN = 25
CLASSIFIER = 'sklearnLinSVC'  # NaiveBayesClassifier
classification_name = 'news_based_' + CLASSIFIER
current_path = os.path.dirname(os.path.realpath(__file__))
# for nltk to find it's datasets
nltk.data.path.append(os.path.join(current_path, 'datasets'))
# Location to saved corpus
news_corpus_dir = os.path.join(current_path, 'news_data')
# Location of the classificator data
pickles_dir = os.path.join(current_path, "classifier_pickles")


def grouper(n, iterable, padvalue=None):
    "grouper(3, 'abcdefg', 'x') --> ('a','b','c'), ('d','e','f'), ('g','x','x')"
    return izip_longest(*[iter(iterable)] * n, fillvalue=padvalue)


def preprocess_text(text, stem=False):
    text = re.sub(r'(@[a-zA-Z0-9]+)|(http://[a-zA-Z0-9]*[.][a-zA-Z]+[/a-zA-Z0-9]*)|([".#]+)', '', text)
    if stem:
        return porter_stemmer.stem(text)
    else:
        return text


def get_text_words(text, stopwords=[]):
    text = preprocess_text(text)
    user_set = set(["http", "://"])
    text_words = set(wordpunct_tokenize(text.lower()))
    text_words = text_words.difference(stopwords)
    text_words = text_words.difference(user_set)
    text_words = [w for w in text_words if len(w) > 2]
    return text_words


def word_indicator(text, **kwargs):
    features = defaultdict(list)
    tweet_words = get_text_words(text, **kwargs)
    for w in tweet_words:
        features[w] = True
    return features


def features_from_text(text, label, **kwargs):
    features = word_indicator(text, **kwargs)
    return (features, label)


def train(records):
    train_data = []
    for record in records:
        text = record[1]
        class_label = record[0]
        feats = features_from_text(text, class_label, stopwords=sw)
        train_data.append(feats)
    print train_data
    if CLASSIFIER != 'sklearnLinSVC':
        try:
            classifier = NaiveBayesClassifier.train(train_data)
            #classifier = SklearnClassifier(BernoulliNB()).train(train_data)
        except Exception as e:
            print "Training Failed with following error, reverting db changes \n", e
    else:
        pipeline = Pipeline([('tfidf', TfidfTransformer()),
                             ('chi2', SelectKBest(chi2, k=1000)),
                             ('nb', LinearSVC(multi_class='ovr'))])
        classifier = SklearnClassifier(pipeline).train(train_data)
    f = open("%s/%s.pickle" % (pickles_dir, classification_name), 'wb')
    pickle.dump(classifier, f)
    f.close()

    gc.collect()


def get_filenames():
    files = []

    # All files in all categories
    for dirpath, dirnames, filenames in os.walk(news_corpus_dir):
        for filename in [f for f in filenames]:
            files.append((os.path.split(dirpath)[1], os.path.join(dirpath, filename)))
    random.shuffle(files)
    return files

if __name__ == '__main__':
    files = get_filenames()

    # Train the classificator
    for records in grouper(RECORDS_TO_TRAIN, files):
        preprocessed_records = []
        print records
        for category, filepath in records:
            with open(filepath) as data_file:
                data = json.load(data_file)
                data['text'] = data['body'] + ' ' + data['title']

            preprocessed_records.append((data['category'],
                                         data['text']))
        train(preprocessed_records)
