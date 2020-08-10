import nltk
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
def word_association_graph(text, k=0.4, font_size=24):
    nouns_in_text = []
    is_noun = lambda pos: pos[:2] == 'NN'
    for sent in text.split('.')[:-1]:   
        tokenized = nltk.word_tokenize(sent)
        nouns=[word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)]
        nouns_in_text.append(' '.join([word for word in nouns if not (word=='' or len(word)==1)]))
    nouns_list = []
    for sent in nouns_in_text:
        temp = sent.split(' ')
        for word in temp:
            if word not in nouns_list:
                nouns_list.append(word)
    df = pd.DataFrame(np.zeros(shape=(len(nouns_list),2)), columns=['Nouns', 'Verbs & Adjectives'])
    df['Nouns'] = nouns_list
    is_adjective_or_verb = lambda pos: pos[:2]=='JJ' or pos[:2]=='VB'
    for sent in text.split('.'):
        for noun in nouns_list:
            if noun in sent:
                tokenized = nltk.word_tokenize(sent)
                adjectives_or_verbs = [word for (word, pos) in nltk.pos_tag(tokenized) if is_adjective_or_verb(pos)]
                ind = df[df['Nouns']==noun].index[0]
                df['Verbs & Adjectives'][ind]=adjectives_or_verbs
    fig = plt.figure(figsize=(15,15))
    G = nx.Graph()
    color_map=[]
    for i in range(len(df)):
        G.add_node(df['Nouns'][i])
        color_map.append('blue')
        for word in df['Verbs & Adjectives'][i]:
            G.add_edges_from([(df['Nouns'][i], word)])
    pos = nx.spring_layout(G, k)
    d = nx.degree(G)
    node_sizes = []
    for i in d:
        _, value = i
        node_sizes.append(value)
    color_list = []
    for i in G.nodes:
        if len(i)>0:
            value = nltk.pos_tag([i])[0][1]
        if (value=='NN' or value=='NNP' or value=='NNS'):
            color_list.append('red')
        elif value=='JJ':
            color_list.append('yellow')
        else:
            color_list.append('blue')
    nx.draw(G, pos, node_size=[(v+1)*200 for v in node_sizes], with_labels=True, node_color=color_list, font_size=font_size)
    plt.show()
    
import re
nltk.download('averaged_perceptron_tagger')
text = "Python is an interpreted, high-level, general-purpose programming language."
text = re.sub("[\[].*?[\]]", "", text) ## Remove brackets and anything inside it (to remove the citations)
# You can do more cleaning (like lemmatization, stemming, stopword removal, etc if you want)
word_association_graph(text)