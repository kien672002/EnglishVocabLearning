from tkinter import *
import MenuGUI
import dataManger

class app :
    def __init__(self):
        # self.BackupDF = pd.read_csv('data.csv', sep='\t')
        # self.df = copy.deepcopy(self.BackupDF)

        self.window = Tk()
        self.window.title('English Vocab Learning')
        self.window.geometry("725x484")
        self.window.configure(bg="#FFFFFF")
        self.window.resizable(False, False)

    def runGUI(self):
        MenuGUI.menu(self.window)
        # AddVocabGUI.addVocab(self.window)

        self.window.mainloop()

        # df = dataManger.DataManger.getDF()
        # for x, y, z in zip(df['Vocabulary'], df['Occurences'], df['Accurates']):
        #     print(x, y, z)

if __name__ == '__main__':
    App = app()
    App.runGUI()
    dataManger.DataManger.saveData()