from scipy.spatial.distance import euclidean,jaccard,cosine,correlation
import numpy as np
import pprint
import operator

critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0, 'Superman Returns': 4.0}}


pp = pprint.PrettyPrinter(indent=4)

def similarity(i,j,metric):
    first = list(critics.keys())[i]
    second = list(critics.keys())[j]
    movies = np.asanyarray([(critics[first].get(movie),critics[second].get(movie)) for movie in list(critics[first].keys()) if critics[second].get(movie)])
    return metric(movies[:,:1],movies[:,1:2])

def similarity_summary(metric=euclidean):
    keyarray = list(critics.keys())
    nmovies = len(keyarray)
    scores = {}
    for i in range(nmovies):
        for j in range(i+1,nmovies):
            score = similarity(i,j,metric)
            scores[('%s,%s')%(keyarray[i],keyarray[j])] = score
    sorted_scores = list(sorted(scores.items(), key=operator.itemgetter(1)))
    for item in sorted_scores:
        print('%30s=%f' % (item[0], item[1]))


metrices = list([euclidean,jaccard,cosine,correlation])

for metric in metrices:
    print('Summary for metric  %s'%(metric.__name__))
    similarity_summary(metric)









