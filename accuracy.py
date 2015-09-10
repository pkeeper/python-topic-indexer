import os
import pickle
import json
import nltk
from news_trainer import get_filenames, features_from_text

RECORDS_TO_TRAIN = 25
classification_names = ('news_based_NaiveBayesClassifier',
                        'news_based_sklearnLinSVC',)
current_path = os.path.dirname(os.path.realpath(__file__))
# Location of the classificator data
pickles_dir = os.path.join(current_path, "classifier_pickles")

classifiers = {}
K = 200


def classifiers_preload():
    global classifiers
    try:
        for cl in classification_names:
            f = open("%s/%s.pickle" % (pickles_dir, cl))
            classifiers[cl] = pickle.load(f)
            f.close()
    except IOError:
        print 'error loading classifier'
    print 'loading classifiers done.'


def get_training_data():
    data = []
    for category, filepath in get_filenames()[:K]:
        with open(filepath) as data_file:
            cur_data = json.load(data_file)
        data.append(features_from_text(cur_data['body'] + ' ' + cur_data['title'], cur_data['category']))
    return data


def check_accuracy(data):
    global classifiers
    for clname, cl in classifiers.iteritems():
        ac = nltk.classify.accuracy(cl, data)
        print '%s Accuracy: %4.4f' % (clname, ac)


def classify_few(data):
    global classifiers
    for d in data[:5]:
        print 'Tagged with : ', d[1]
        for clname, cl in classifiers.iteritems():
            print 'Classifier %s decision: [%s]' % (clname, cl.classify(d[0]))
            cl.show_most_informative_features(5)

if __name__ == '__main__':
    classifiers_preload()
    data = get_training_data()
    # classify_few(data)
    check_accuracy(data)
