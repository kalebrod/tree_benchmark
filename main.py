import json
from time import time
from functools import wraps
from random import shuffle, sample

import pandas as pd

from models.binary import Tree
from models.avl import AVLTree

# Data set extracted from:
# https://www.kaggle.com/datasets/prateekmaj21/largest-companies-by-marketcap

def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = int(round(time() * 1000))
        try:
            values = func(*args, **kwargs)

        finally:
            end_ = int(round(time() * 1000)) - start
            print(f"Tempo de execução {end_ if end_ > 0 else 0} ms")

            return end_, values
    
    return _time_it

@measure
def load_df(tree, df:pd.DataFrame) -> None:
    for i,row in df.iterrows():
        data = row.to_dict()
        data['id'] = i
        
        try:
            tree.insert(data)
        
        except Exception as error:
            raise error

@measure
def get_value(tree,filter:dict) -> list:
    return tree.filter_by(filter)

def save_nodes(nodes:list, name:str) -> None:
    df = pd.DataFrame(nodes)
    df.to_csv(name,index=False)


#1000 # 10000 #20000 #45000

df = pd.read_csv('adult_dataset.dat',sep=',')

datapool = list(range(df.shape[0]))
shuffle(datapool)

df_1 = df.copy().iloc[sample(datapool,1000)]
df_2 = df.copy().iloc[sample(datapool,10000)]
df_3 = df.copy().iloc[sample(datapool,20000)]
df_4 = df.copy().iloc[sample(datapool,45000)]

result = {
    'filter_1':{
        'binary':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}},
        'avl':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}}
    },
    'filter_2':{
        'binary':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}},
        'avl':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}}
    },
    'filter_3':{
        'binary':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}},
        'avl':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}}
    },
    'filter_4':{
        'binary':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}},
        'avl':{'df_1':{},'df_2':{},'df_3':{},'df_4':{}}
    },
}

filter_1 = {'native_country':['Peru','==']}
filter_2 = {'sex':['Female','==']}
filter_3 = {'finance':['>50K','==']}
filter_4 = {'hours_per_week':[45,'>=']}

# filter_1

# Binary Tree

bin = Tree()
result['filter_1']['binary']['df_1']['load'] = load_df(bin,df_1)[0]
result['filter_1']['binary']['df_1']['get_value'],nodes = get_value(bin,filter_1)
# save_nodes(nodes,'bin_filter_1_df_1.csv')

bin = Tree()
result['filter_1']['binary']['df_2']['load'] = load_df(bin,df_2)[0]
result['filter_1']['binary']['df_2']['get_value'],nodes = get_value(bin,filter_1)
# save_nodes(nodes,'bin_filter_1_df_2.csv')

bin = Tree()
result['filter_1']['binary']['df_3']['load'] = load_df(bin,df_3)[0]
result['filter_1']['binary']['df_3']['get_value'],nodes = get_value(bin,filter_1)
# save_nodes(nodes,'bin_filter_1_df_3.csv')

bin = Tree()
result['filter_1']['binary']['df_4']['load'] = load_df(bin,df_4)[0]
result['filter_1']['binary']['df_4']['get_value'],nodes = get_value(bin,filter_1)
# save_nodes(nodes,'bin_filter_1_df_4.csv')

# AVL Tree

avl = AVLTree()
result['filter_1']['avl']['df_1']['load'] = load_df(avl,df_1)[0]
result['filter_1']['avl']['df_1']['get_value'], nodes = get_value(avl,filter_1)
# save_nodes(nodes,'avl_filter_1_df_1.csv')

avl = AVLTree()
result['filter_1']['avl']['df_2']['load'] = load_df(avl,df_2)[0]
result['filter_1']['avl']['df_2']['get_value'], nodes = get_value(avl,filter_1)
# save_nodes(nodes,'avl_filter_1_df_2.csv')

avl = AVLTree()
result['filter_1']['avl']['df_3']['load'] = load_df(avl,df_3)[0]
result['filter_1']['avl']['df_3']['get_value'],nodes = get_value(avl,filter_1)
# save_nodes(nodes,'avl_filter_1_df_3.csv')

avl = AVLTree()
result['filter_1']['avl']['df_4']['load'] = load_df(avl,df_4)[0]
result['filter_1']['avl']['df_4']['get_value'],nodes = get_value(avl,filter_1)
# save_nodes(nodes,'avl_filter_1_df_4.csv')

# filter_2

# Binary Tree

bin = Tree()
result['filter_2']['binary']['df_1']['load'] = load_df(bin,df_1)[0]
result['filter_2']['binary']['df_1']['get_value'],nodes = get_value(bin,filter_2)
# save_nodes(nodes,'bin_filter_2_df_1.csv')

bin = Tree()
result['filter_2']['binary']['df_2']['load'] = load_df(bin,df_2)[0]
result['filter_2']['binary']['df_2']['get_value'],nodes = get_value(bin,filter_2)
# save_nodes(nodes,'bin_filter_2_df_2.csv')

bin = Tree()
result['filter_2']['binary']['df_3']['load'] = load_df(bin,df_3)[0]
result['filter_2']['binary']['df_3']['get_value'],nodes = get_value(bin,filter_2)
# save_nodes(nodes,'bin_filter_2_df_3.csv')

bin = Tree()
result['filter_2']['binary']['df_4']['load'] = load_df(bin,df_4)[0]
result['filter_2']['binary']['df_4']['get_value'],nodes = get_value(bin,filter_2)
# save_nodes(nodes,'bin_filter_2_df_4.csv')

# AVL Tree

avl = AVLTree()
result['filter_2']['avl']['df_1']['load'] = load_df(avl,df_1)[0]
result['filter_2']['avl']['df_1']['get_value'], nodes = get_value(avl,filter_2)
# save_nodes(nodes,'avl_filter_2_df_1.csv')

avl = AVLTree()
result['filter_2']['avl']['df_2']['load'] = load_df(avl,df_2)[0]
result['filter_2']['avl']['df_2']['get_value'], nodes = get_value(avl,filter_2)
# save_nodes(nodes,'avl_filter_2_df_2.csv')

avl = AVLTree()
result['filter_2']['avl']['df_3']['load'] = load_df(avl,df_3)[0]
result['filter_2']['avl']['df_3']['get_value'],nodes = get_value(avl,filter_2)
# save_nodes(nodes,'avl_filter_2_df_3.csv')

avl = AVLTree()
result['filter_2']['avl']['df_4']['load'] = load_df(avl,df_4)[0]
result['filter_2']['avl']['df_4']['get_value'],nodes = get_value(avl,filter_2)
# save_nodes(nodes,'avl_filter_2_df_4.csv')

# filter_3

# Binary Tree

bin = Tree()
result['filter_3']['binary']['df_1']['load'] = load_df(bin,df_1)[0]
result['filter_3']['binary']['df_1']['get_value'], nodes = get_value(bin,filter_3)
# save_nodes(nodes,'bin_filter_3_df_1.csv')

bin = Tree()
result['filter_3']['binary']['df_2']['load'] = load_df(bin,df_2)[0]
result['filter_3']['binary']['df_2']['get_value'], nodes = get_value(bin,filter_3)
# save_nodes(nodes,'bin_filter_3_df_3.csv')

bin = Tree()
result['filter_3']['binary']['df_3']['load'] = load_df(bin,df_3)[0]
result['filter_3']['binary']['df_3']['get_value'], nodes = get_value(bin,filter_3)
# save_nodes(nodes,'bin_filter_3_df_3.csv')

bin = Tree()
result['filter_3']['binary']['df_4']['load'] = load_df(bin,df_4)[0]
result['filter_3']['binary']['df_4']['get_value'], nodes = get_value(bin,filter_3)
# save_nodes(nodes,'bin_filter_3_df_4.csv')

# AVL Tree

avl = AVLTree()
result['filter_3']['avl']['df_1']['load'] = load_df(avl,df_1)[0]
result['filter_3']['avl']['df_1']['get_value'], nodes = get_value(avl,filter_3)
# save_nodes(nodes,'avl_filter_3_df_1.csv')

avl = AVLTree()
result['filter_3']['avl']['df_2']['load'] = load_df(avl,df_2)[0]
result['filter_3']['avl']['df_2']['get_value'], nodes = get_value(avl,filter_3)
# save_nodes(nodes,'avl_filter_3_df_2.csv')

avl = AVLTree()
result['filter_3']['avl']['df_3']['load'] = load_df(avl,df_3)[0]
result['filter_3']['avl']['df_3']['get_value'],nodes = get_value(avl,filter_3)
# save_nodes(nodes,'avl_filter_3_df_3.csv')

avl = AVLTree()
result['filter_3']['avl']['df_4']['load'] = load_df(avl,df_4)[0]
result['filter_3']['avl']['df_4']['get_value'],nodes = get_value(avl,filter_3)
# save_nodes(nodes,'avl_filter_3_df_4.csv')

# filter_4

# Binary Tree

bin = Tree()
result['filter_4']['binary']['df_1']['load'] = load_df(bin,df_1)[0]
result['filter_4']['binary']['df_1']['get_value'], nodes = get_value(bin,filter_4)
# save_nodes(nodes,'bin_filter_4_df_1.csv')

bin = Tree()
result['filter_4']['binary']['df_2']['load'] = load_df(bin,df_2)[0]
result['filter_4']['binary']['df_2']['get_value'], nodes = get_value(bin,filter_4)
# save_nodes(nodes,'bin_filter_4_df_3.csv')

bin = Tree()
result['filter_4']['binary']['df_3']['load'] = load_df(bin,df_3)[0]
result['filter_4']['binary']['df_3']['get_value'], nodes = get_value(bin,filter_4)
# save_nodes(nodes,'bin_filter_4_df_3.csv')

bin = Tree()
result['filter_4']['binary']['df_4']['load'] = load_df(bin,df_4)[0]
result['filter_4']['binary']['df_4']['get_value'], nodes = get_value(bin,filter_4)
# save_nodes(nodes,'bin_filter_4_df_4.csv')

# AVL Tree

avl = AVLTree()
result['filter_4']['avl']['df_1']['load'] = load_df(avl,df_1)[0]
result['filter_4']['avl']['df_1']['get_value'], nodes = get_value(avl,filter_4)
# save_nodes(nodes,'avl_filter_4_df_1.csv')

avl = AVLTree()
result['filter_4']['avl']['df_2']['load'] = load_df(avl,df_2)[0]
result['filter_4']['avl']['df_2']['get_value'], nodes = get_value(avl,filter_4)
# save_nodes(nodes,'avl_filter_4_df_2.csv')

avl = AVLTree()
result['filter_4']['avl']['df_3']['load'] = load_df(avl,df_3)[0]
result['filter_4']['avl']['df_3']['get_value'],nodes = get_value(avl,filter_4)
# save_nodes(nodes,'avl_filter_4_df_3.csv')

avl = AVLTree()
result['filter_4']['avl']['df_4']['load'] = load_df(avl,df_4)[0]
result['filter_4']['avl']['df_4']['get_value'],nodes = get_value(avl,filter_4)
# save_nodes(nodes,'avl_filter_4_df_4.csv')

with open('results.json','w') as file:
    json.dump(result,file,indent=4)
