
# coding: utf-8

# # Bayesian Movie Ranking
# 
# For movie ranking systems, we always have our raw datas stored as matrices or vectors. However, to have rankings properly sorted, we need to summarize these more-than-one-dimensional infotmtion in a scalar.
# 
# In this project, we are calculating the expected value of average value based on the observations we have.
# $$ E \left[ p_1+2p_2+3p_3+4p_4+5p_5 \mid O \right] = \sum_{i=1}^5 iE\left[p_i \mid O\right] $$
# 
# 
# The main idea behind Bayesian inference approach is
# > Treats all unknown quantities as random variables.
# 
# In the Bayesian approach, we would treat the unknown probability $p$ as a random variable and give $p$ with a **prior distribution**, which reflects our uncertainty about the true value of $p$ before observing the coin tosses.
# 
# After the experiment is performed and the data are gathered, the prior distribution is updated using Bayes' rule; this yields the posterior distribution, which reflects our new beliefs about $p$.
# 

# We first import necessary libraires.

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display, Markdown


# Now we will import data, with information given in README specified manually.

# In[2]:


data = {'movies': None, 'ratings': None, 'users': None}
dataheader = {
    'movies': ['MovieID', 'Title', 'Genres'],
    'ratings': ['UserID','MovieID','Rating','Timestamp'],
    'users': ['UserID','Gender','Age','Occupation','Zip-code']
}
occupations = {
 0:"other/not specified",
 1:"academic/educator",
 2:"artist",
 3:"clerical/admin",
 4:"college/grad student",
 5:"customer service",
 6:"doctor/health care",
 7:"executive/managerial",
 8:"farmer",
 9:"homemaker",
10:"K-12 student",
11:"lawyer",
12:"programmer",
13:"retired",
14:"sales/marketing",
15:"scientist",
16:"self-employed",
17:"technician/engineer",
18:"tradesman/craftsman",
19:"unemployed",
20:"writer"
}

for t in ['movies', 'ratings', 'users']:
    data[t] = pd.read_csv(
        filepath_or_buffer = '{}.dat'.format(t),
        sep = '::',
        header = None,
        names = dataheader[t],
        engine = 'python',
        encoding='latin-1'
    )


# We now craft the data a little bit so that Pandas can do more with the data.

# In[3]:


# Parse the raw string so that `Genres` column stores Python lists
data['movies']['Genres'] = data['movies']['Genres'].apply(lambda x: x.split('|'))

# Let Pandas understand categories
data['users']['Occupation'] = data['users']['Occupation'].apply(lambda x: occupations[x]).astype('category')
data['users']['Gender'] = data['users']['Gender'].astype('category')

# Let Pandas understand timestamps
data['ratings']['Timestamp'] = pd.to_datetime(data['ratings']['Timestamp'],unit='s')


# We merge the tables into one big table just because we are lazy and waste on storage is, in this case, affordable.

# In[4]:


fulldata = pd.merge(pd.merge(data['ratings'], data['users']), data['movies'])


# In the slides, we have
# * m = 3.25 & C = 50
# * m = 2 & C = 6
# 
# In this project, we have prior distribution with m = 2 & C = 15.
# 
# And we want Top 10 lists.

# ## Intra-Item
# 
# $$ \overline{{\rm rating}} = \frac{\sum_{i=1}^5{i\alpha_i^0} + \sum_{i=1}^5{iK_i}}{N+\sum_{i=1}^5{\alpha_i^0}} = \frac{C \cdot m + \sum{\rm ratings}}{C+N} $$
# 
# where, $K_1 + \cdots + K_5 = N$, and $\alpha^0$ is Dirichlet distribution parameter s.t.
# 
# $${\rm Pr} \left(p_1,p_2,p_3,p_4,p_5 \mid O\right) \propto \prod_{j=1}^5 p_j^{K_j+\alpha_j^0-1} $$
# 
# Here, when we are calculating Bayesian mean of one item, we don't include information from other items.
# 
# This intra-item Bayesian average differs from plain average in that it considers the number of ratings, which is, in this case, $N$.
# 
# We have observations. And what we are then finding is some probability distribution of $p$: $f(p)$ that give rise to this observation. The Bayesian average calculates the expected value of this $f(p)$, not simply the original observations.

# In[5]:


m, C = 2, 15
top_x = 10


# In[6]:


display(Markdown('### Overall Top {}'.format(top_x)))

grp_r = fulldata.groupby('Title').Rating

N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)

topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[7]:


display(Markdown('### Top {} ranked by Male'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'M'].groupby('Title').Rating

N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[8]:


display(Markdown('### Top {} ranked by Female'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'F'].groupby('Title').Rating

N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# To have genre-wise top 10 rankings, we first write a helper function ``hasGenre`` to generate a filter boolean array.

# In[9]:


def hasGenre(data_df, genre):
    filt_bools = []
    for i in range(len(data_df)):
        if genre in data_df.Genres.iat[i]:
            filt_bools.append(True)
        else:
            filt_bools.append(False)
    return filt_bools


# In[10]:


dst_genre = 'Romance'
grp_r = fulldata[hasGenre(fulldata, dst_genre)].groupby('Title').Rating
display(Markdown('### Top {} in {}'.format(top_x, dst_genre)))

N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[11]:


dst_genre = 'Action'
grp_r = fulldata[hasGenre(fulldata, dst_genre)].groupby('Title').Rating
display(Markdown('### Top {} in {}'.format(top_x, dst_genre)))

N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# ## Inter-Item (Optional Part)
# 
# The inter-item Bayesian average is more heuristic.
# 
# $$\bar{m_i} = \frac{C_i m_i + \sum{\rm ratings}}{C+N}$$
# 
# It is not mathmatically-derived, however, it provides an alternative way of "Bayesianizing" rating of items by introducing global information.
# 
# Personally, I think this approach is more applicable to movies of the same genre since the ranking preference will be be more similar.

# In[12]:


display(Markdown('### Overall Top {}'.format(top_x)))

grp_r = fulldata.groupby('Title').Rating

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[13]:


display(Markdown('### Top {} ranked by Male'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'M'].groupby('Title').Rating

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[14]:


display(Markdown('### Top {} ranked by Female'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'F'].groupby('Title').Rating

top_x = 10

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[15]:


dst_genre = 'Romance'
grp_r = fulldata[hasGenre(fulldata, dst_genre)].groupby('Title').Rating
display(Markdown('### Top {} in {}'.format(top_x, dst_genre)))

N = grp_r.count()
sum_r = grp_r.sum()

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[16]:


dst_genre = 'Action'
grp_r = fulldata[hasGenre(fulldata, dst_genre)].groupby('Title').Rating
display(Markdown('### Top {} in {}'.format(top_x, dst_genre)))

N = grp_r.count()
sum_r = grp_r.sum()

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# ## Further Comparison

# In[17]:


display(Markdown('#### Intra-item: Top {} ranked by Male Programmers'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'M']
grp_r = grp_r[grp_r.Occupation == 'programmer'].groupby('Title').Rating

C, m = 15, 2
N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


display(Markdown('#### Inter-item: Top {} ranked by Male Programmers'.format(top_x)))

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[18]:


display(Markdown('#### Intra-item: Top {} ranked by Male Programmers aged under 45'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'M']
grp_r = grp_r[grp_r.Occupation == 'programmer']
grp_r = grp_r[grp_r.Age < 45].groupby('Title').Rating

C, m = 15, 2
N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


display(Markdown('#### Inter-item: Top {} ranked by Male Programmers aged under 45'.format(top_x)))

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# In[19]:


display(Markdown('#### Intra-item: Top Sci-Fi {} ranked by Male Programmers aged under 45'.format(top_x)))

grp_r = fulldata[fulldata.Gender == 'M']
grp_r = grp_r[grp_r.Occupation == 'programmer']
grp_r = grp_r[grp_r.Age < 45]
grp_r = grp_r[hasGenre(grp_r, 'Sci-Fi')].groupby('Title').Rating

C, m = 15, 2
N = grp_r.count()
sum_r = grp_r.sum()

r_bayes = (C * m + sum_r)/(C + N)
r_mean = sum_r / N

topdf = pd.concat([N.to_frame(), r_bayes.to_frame(), r_mean.to_frame()], axis=1)
topdf.columns = ['count', 'Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


display(Markdown('#### Inter-item: Top Sci-Fi {} ranked by Male Programmers aged under 45'.format(top_x)))

N = np.sum(grp_r.count())
sum_r = np.sum(grp_r.sum())
mean = grp_r.sum() / grp_r.count()
m = grp_r.mean()
C = grp_r.count()

r_bayes = (C * m + sum_r)/(C + N)

topdf = pd.concat([r_bayes.to_frame(), mean.to_frame()], axis=1)
topdf.columns = ['Bayes', 'mean']
display(topdf.sort_values(['Bayes'], ascending=False)[0:top_x])


# With more detailed user profile being utilized, the top-10 list looks closer to each other.
