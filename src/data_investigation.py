import pandas as pd


class ExplorerData:
    def __init__(self,df:pd.DataFrame):
        self.df = df

    def total_count(self):
        """
        Counts how many tweets in total
        """
        total = self.df.shape[0]
        return total
    def count_by_category(self,column:str = "Biased"):
        """
        Counts how many tweets there
         are from each category .
        """
        count_per_targ = self.df[column].value_counts()
        return count_per_targ
    def _count_words(self,text_col:str = "Text"):
        """
        Create a column of how many words
         are per row in a selected column.
        """
        self.df["count_words"] = self.df[text_col].map(lambda x: len(str(x).split()))

    def _count_letters(self,text_col:str = "Text"):
        """
            Create a column of how many letters
            are per row in a selected column.
        """
        self.df["count_letters"] = self.df[text_col].map(lambda x: len(str(x)))

    def _count_upper(self,text_col:str = "Text"):
        self.df["count_upper"] = self.df[text_col].map(lambda sen: len([x for x in str(sen).split() if x.isupper()]))

    def avg_words(self):
        """
        Returns the average number of words in a tweet
        (must run the count_words() function first)
        """
        return self.df["count_words"].mean()

    def avg_words_per_category(self,biased_column:str = "Biased"):
        """
        Returns the average number of words in a tweet per category in a
        selected column (must run the count_words() function first)
        """
        return self.df.groupby([biased_column])["count_words"].mean()

    def longest_text(self,text_column:str = "Text",biased_column:str = "Biased",count:int = 3):
        """
        Returns the longest text in a selected column
        by selected quantity
        per category (must run the count_letters() function first)
        """
        dict_df = dict()
        for val in self.df[biased_column].unique():
            dict_df[str(val)] = \
            self.df[self.df[biased_column].astype(str) == str(val)].sort_values(by="count_letters", ascending=False).head(count)[
                text_column].to_dict()
        return dict_df

    def longest_words(self,text_column:str = "Text",count:int = 10):
        word_list = list()
        for sen in self.df[text_column].to_list():
            for word in sen.split():
                word_list.append(word)
        return sorted(word_list, key=len, reverse=True)[:count]

    def sum_upper_words(self):
        return self.df["count_upper"].sum()

    def sum_upper_words_by_targ(self,biased_column:str = "Biased"):
        return self.df.groupby(biased_column)["count_upper"].sum()




