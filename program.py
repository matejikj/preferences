import zipfile
import io
import requests
import os
import numpy as np
import pandas as pd


from elliot.run import run_experiment

ratings_df = pd.read_csv('data/ratings.csv',
                 dtype= {'userId':np.int32,
                         'movieId':np.int32,
                         'rating':np.float64,
                         'timestamp':np.int64},
                 header=0, #skiprows=1
                 names= ['userId','movieId','rating','timestamp'])

movies_df = pd.read_csv('data/movies.csv',
                 dtype= {'movieId':np.int32,
                         'title':np.string_,
                         'genres': np.string_},
                 header=0, #skiprows=1
                 names= ['movieId','title', 'genres'])

ratings_df['rating5'] = ratings_df['rating'].apply(np.ceil)

ratings_df.loc[ratings_df['rating'] <= 2, 'rating3'] = 1
ratings_df.loc[ratings_df['rating'] > 2, 'rating3'] = 2
ratings_df.loc[ratings_df['rating'] > 3, 'rating3'] = 3

ratings_df.loc[ratings_df['rating'] <= 2.5, 'rating2'] = 1
ratings_df.loc[ratings_df['rating'] > 2.5, 'rating2'] = 2

ratings10_df = ratings_df.drop(columns=['timestamp','rating2', 'rating3', 'rating5'])
ratings5_df = ratings_df.drop(columns=['timestamp','rating', 'rating3', 'rating2'])
ratings3_df = ratings_df.drop(columns=['timestamp','rating', 'rating5', 'rating2'])
ratings2_df = ratings_df.drop(columns=['timestamp','rating', 'rating5', 'rating3'])

ratings10_df.to_csv("./data/dataset10.tsv", sep = "\t", index=False, header=False)
ratings5_df.to_csv("./data/dataset5.tsv", sep = "\t", index=False, header=False)
ratings3_df.to_csv("./data/dataset3.tsv", sep = "\t", index=False, header=False)
ratings2_df.to_csv("./data/dataset2.tsv", sep = "\t", index=False, header=False)


ratings_df = pd.read_csv('data/ratings.csv',
                 dtype= {'userId':np.int32,
                         'movieId':np.int32,
                         'rating':np.float64,
                         'timestamp':np.int64},
                 header=0, #skiprows=1
                 names= ['userId','movieId','rating','timestamp'])
ratings2_df.to_csv("./data/dataset2.tsv", sep = "\t", index=False, header=False)


print("Done! We are now starting the Elliot's experiment")
run_experiment("config_files/10_split.yml")
run_experiment("config_files/10_prepare_recomendations.yml")
run_experiment("config_files/10_performance.yml")
run_experiment("config_files/5_split.yml")
run_experiment("config_files/5_prepare_recomendations.yml")
run_experiment("config_files/5_performance_for_10_dataset.yml")
run_experiment("config_files/3_split.yml")
run_experiment("config_files/3_prepare_recomendations.yml")
run_experiment("config_files/3_performance_for_10_dataset.yml")
run_experiment("config_files/2_split.yml")
run_experiment("config_files/2_prepare_recomendations.yml")
run_experiment("config_files/2_performance_for_10_dataset.yml")
