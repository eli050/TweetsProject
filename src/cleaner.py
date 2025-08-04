import pandas as pd
import string

class CleanerDF:
    def __init__(self, df:pd.DataFrame):
        self.df = df

    def dump_to_csv(self):
        self.relevant_df(['Biased','Text'])
        self.remove_punctuation()
        self.to_lower_case()
        self.delete_unclassified()
        self.df.to_csv("data/tweets_dataset_cleaned.csv")

    def relevant_df(self,relevant_columns:list[str]):
        self.df= self.df[relevant_columns]

    def remove_punctuation(self, text_col:str = "Text"):
        self.df[text_col] = self.df[text_col].map(lambda x: x.translate(str.maketrans('', '',string.punctuation)))

    def to_lower_case(self,text_col:str = "Text"):
        self.df[text_col] = self.df[text_col].map(lambda x: str(x).lower())

    def delete_unclassified(self, biased_column:str = "Biased"):
        self.df.loc[(self.df[biased_column].astype(str) == "0") | (self.df[biased_column].astype(str) == "1")]


