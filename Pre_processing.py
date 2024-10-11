import pandas as pd
import nltk
import re
import numpy as np
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
#uncomment these steps if you encounter any error
# nltk.download('stopwords')
# nltk.download('punkt')

def tokenizing(x):
    token=nltk.word_tokenize(x)
    k=[]
    for i in token:
        if i.lower() not in stop_words:
           y=stemmer.stem(i)
           k.append(y)
    return " ".join(k)

def top5(given):
    z=dt[dt['title']==given]['number'].values[0]
    estimated=sorted(list(enumerate(similar[z])),reverse=True,key=lambda x:x[1])
    for i in estimated[1:6]:
        k=dt[dt['number']==i[0]]
        print(k['title'].values[0])


dt=pd.read_csv("F:\\ML_projects\\Movie_Recommendation\\top10K-TMDB-movies.csv")
dt['number']=range(0,len(dt))
dt['x']=dt['genre']+dt['overview']
l=['original_language','genre','overview','popularity','release_date','vote_average','vote_count']
for i in l:
    dt.drop(i,axis=1,inplace=True)


dt['x']=dt['x'].str.replace(','  , ' ')
dt['x'] = dt['x'].apply(lambda x: re.sub(r'[^\w\s]', '', str(x)))
stemmer=PorterStemmer()
stop_words = set(stopwords.words('english'))
dt['x']=dt['x'].apply(lambda x: tokenizing(x))
tfidf=TfidfVectorizer(analyzer='word',stop_words='english')
matrix =tfidf.fit_transform(dt['x'])
'''we have a mtrrix of all vocabulary in the matrix which are colums using tfidf.vocabulary_ and total no of rows is no of data points 10k
to check our fit_transformed matrix is in form of sparse matrix we can change it to arrary form using toarray()
which is mat and if we print mat[0] it shows the first row of corpus which has total 26175 vocabulary in our example'''
# mat=matrix.toarray()
# print(mat[0])
# print(matrix.toarray()[:2])
# print(len(tfidf.vocabulary_))
similar=cosine_similarity(matrix)
# print("enter Input")
# given=input()
# top5(given)
# pickle.dump(data,open('movies.pkl','wb'))
# pickle.dump(similar,open('similarity_matrix.pkl','wb'))

np.save('data.npy', dt, allow_pickle=True)

np.save('similarity_matrix.npy',similar,allow_pickle=True)
print("kk")

dt.to_csv('modified_dataset.csv', index=False)
