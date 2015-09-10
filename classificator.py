import os
import pickle
from news_trainer import features_from_text

RECORDS_TO_TRAIN = 25
classification_name = 'news_based_NaiveBayesClassifier'
current_path = os.path.dirname(os.path.realpath(__file__))
# Location of the classificator data
pickles_dir = os.path.join(current_path, "classifier_pickles")


def classifiers_preload():
    global classifier
    try:
        f = open("%s/%s.pickle" % (pickles_dir, classification_name))
        classifier = pickle.load(f)
    except IOError:
        print 'error loading classifier'
    print 'loading classifiers done.'


def classify(text):
    """
        Classify a text
    """
    global classifier
    text = features_from_text(text, None)[0]
    print text
    result = classifier.classify(text)
    print result
