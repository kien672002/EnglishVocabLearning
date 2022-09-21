import pandas as pd
import random

class DataManger:
    words_count = len(pd.read_csv('data.csv', sep='\t'))
    # __BackupDF = pd.read_csv('data.csv', sep='\t')
    __df = pd.read_csv('data.csv', sep='\t')

    def __init__(self):
        pass

    @staticmethod
    def getDF():
        return DataManger.__df

    # @staticmethod
    # def doBackup():
    #     DataManger.__df.to_csv('backup.csv', sep='\t', index=False)

    @staticmethod
    def saveData():
        DataManger.__df.to_csv('data.csv',sep='\t',index=False)

    @staticmethod
    def addVocab(vocab, defination, use):
        ldf = list(DataManger.__df['Vocabulary'])
        try:
            ldf.index(vocab)
        except:
            DataManger.__df.loc[-1] = [vocab, defination, use, '1', '0']
            DataManger.__df.index += 1
            DataManger.words_count += 1

        DataManger.__df = DataManger.__df.sort_index()

    @staticmethod
    def updateVocab(vocab, true_ans = False):
        index = list(DataManger.__df['Vocabulary']).index(vocab)
        DataManger.__df.loc[index,'Occurences'] = int(DataManger.__df.loc[index,'Occurences']) + 1
        DataManger.__df.loc[index,'Accurates'] = int(DataManger.__df.loc[index,'Accurates']) + true_ans

    @staticmethod
    def getRandomWords(num_words):
        if num_words > len(DataManger.__df):
            return []

        population = []
        weights = []

        f = lambda x : 1 / (1 + 2.718281828 ** x)

        [(population.append(DataManger.__df.loc[i, 'Vocabulary']), weights.append(f(1 / int(DataManger.__df.loc[i, 'Occurences']) * int(DataManger.__df.loc[i, 'Accurates'])))) for i in range(len(DataManger.__df))]

        word_list = []

        for i in range(num_words):
            word = random.choices(population, weights if i == 0 else None , k=1)[0]
            word_index = population.index(word)

            word_list.append(word)

            del weights[word_index]
            del population[word_index]

        return word_list

    @staticmethod
    def getVocabTest():
        # get a words list to use for the test, the question is placed at top of the word_list
        word_list = DataManger.getRandomWords(4)
        indexs = [list(DataManger.__df['Vocabulary']).index(word) for word in word_list]

        # the solotion for this test
        solution = DataManger.__df.iloc[indexs[0]]["Vocabulary"]
        question = DataManger.__df.iloc[indexs[0]]["Defination"]

        # Shuffle 2 list with same order
        temp = list(zip(word_list, indexs))
        random.shuffle(temp)
        word_list, indexs = zip(*temp)
        word_list = list(word_list)
        indexs = list(indexs)

        choices = [DataManger.__df.iloc[index]['Vocabulary'] for index in indexs]

        return question, solution, choices


