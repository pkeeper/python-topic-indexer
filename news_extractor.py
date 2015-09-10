import os
from news_corpus_builder import NewsCorpusGenerator
from iab_cat_load import iab_tier2


# Location to save generated corpus
news_corpus_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'news_data')

# Save results to sqlite or  files per article
ex = NewsCorpusGenerator(news_corpus_dir)


for subcategory, category in iab_tier2.iteritems():
    print 'Getting search result for [' + subcategory + '] in [' + category + ']'
    # Retrieve 50 links related to the search term dogs and assign a category of Pet to the retrieved links
    links = ex.google_news_search(subcategory, category, 100)
    print 'saving...'
    # Generate and save corpus
    try:
        ex.generate_corpus(links)
    except:
        pass
