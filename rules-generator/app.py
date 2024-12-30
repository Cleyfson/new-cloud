import pandas as pd
from fpgrowth_py import fpgrowth
import pickle
import os

def preprocess_data(filename, chunksize=200000):
    playlists_baskets = []
    track_uri_to_name = {}

    for chunk in pd.read_csv(filename, chunksize=chunksize):
        chunk.columns = chunk.columns.str.strip()
        
        required_columns = ['pid', 'track_uri', 'track_name']
        if not all(col in chunk.columns for col in required_columns):
            raise ValueError(f"Colunas esperadas {required_columns} não encontradas no DataFrame.")
        
        track_uri_to_name.update(dict(zip(chunk['track_uri'], chunk['track_name'])))
        
        chunk_baskets = chunk.groupby('pid')['track_uri'].apply(list).tolist()
        playlists_baskets.extend(chunk_baskets)

    return playlists_baskets, track_uri_to_name

def generate_association_rules(playlists_baskets, track_uri_to_name, minSupRatio=0.05, minConf=0.5):
    freq_itemsets, rules = fpgrowth(playlists_baskets, minSupRatio=minSupRatio, minConf=minConf)

    rules_with_names = [
        {'antecedent': [track_uri_to_name.get(uri, uri) for uri in rule[0]],
         'consequent': [track_uri_to_name.get(uri, uri) for uri in rule[1]],
         'confidence': rule[2]}
        for rule in rules
    ]

    return rules_with_names

def save_rules(rules, filename='../mnt/shared/recommendation_rules.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(rules, f)

def load_rules(filename='../mnt/shared/recommendation_rules.pkl'):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    csv_filename = os.getenv('CSV_FILENAME', '../mnt/shared/2023_spotify_ds1.csv')

    print("Processando dados do CSV...")
    playlists_baskets, track_uri_to_name = preprocess_data(csv_filename)

    print("Gerando regras de associação...")
    rules = generate_association_rules(playlists_baskets, track_uri_to_name, minSupRatio=0.08, minConf=0.4)

    print("Salvando regras de associação...")
    save_rules(rules)

    print("Regras geradas e salvas com sucesso!")

if __name__ == '__main__':
    main()
