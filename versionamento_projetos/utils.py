import pandas as pd

def freq_tab(df, var):
    """
    Esta função tem o objetivo de criar uma tabela de frequência com base em um dataframe e uma variável do dataframe

    :param df: dataframe com as ocorrências únicas (importante cada ocorrência ser única, pois é realizada uma contagem)
    :param var: nome da variável que deseja-se analisar a tabela de frequência 

    :return: tabela de frequência com frequências absolutas e relativas
    """

    return pd.DataFrame({'freq_abs': df[[var]].value_counts(), 'freq_rel': df[[var]].value_counts(normalize=True)})