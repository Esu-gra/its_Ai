import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt




class DataPipeline:
    def __init__(self):
        self.csv_path="../dati/raw_data.csv"
        self.clean_csv_path="../dati/raw_data.csv"
        self.outpu_plot="../visual/scatter_plot.png"
        
    def caricamento_csv(self)->pd.DataFrame:
        # caricamento di un file .csv locale
        return pd.read_csv(self.csv_path)
    
    def salvataggio_dati(self,df:pd.DataFrame)->None:
        # salvataggio dati su un file csv locale
        df.to_csv(self.clean_csv_path)


    def preprocessamento_dati(self,df:pd.DataFrame)->pd.DataFrame:
        # pulizia e preparazione dati
        df["is_healthy"] = (df["screen_time_hours"] < 4) & (df["sleep_hours"] >= 8)

        self.salvataggio_dati(df)
        return df

    def visualizzazione_dati(self,df:pd.DataFrame)->None:
        # visualizzazione dati
        # plt.figure(figsize=(10,6))
        # true_data=df[df["is_healthy"]==True]
        # false_data=df[df["is_healthy"]==False]
        # # print(type(true_data))
        # # print(true_data)
        # plt.scatter(true_data["screen_time_hours"],true_data["math_score"],color="green",label="True",alpha=0.7)
        # plt.scatter(false_data["screen_time_hours"],false_data["math_score"],color="red",label="False",alpha=0.7)
        # plt.xlabel("Screen time hours")
        # plt.ylabel("Math score")
        # plt.title("Screen time hours vs. math score")
        # plt.savefig(self.outpu_plot)
        # plt.legend()

        plt.figure(figsize=(10,6))
        true_data=df[df["is_healthy"]==True]
        false_data=df[df["is_healthy"]==False]
        # # print(type(true_data))
        # # print(true_data)


        plt.xlabel("Screen time hours")
        plt.ylabel("Math score")
        plt.title("Screen time hours vs. math score")
        sns.scatterplot(data=df,x="screen_time_hours",y="math_score",hue="is_healthy")
        plt.savefig(self.outpu_plot)
        plt.close()

    def esegui_pipeline(self)->None:
        # caricamento 
        raw_df=self.caricamento_csv()
        print("  -Letti i dati dal file csv")
        # preprocessamento
        clean_df=self.preprocessamento_dati(raw_df)
        print("  -Pulizia dati completata e file puliti salvato")
        # print(clean_df.columns)
        self.visualizzazione_dati(clean_df)
        print("  -Visualizzati e salvati risultati di analisi")


if __name__=="__main__":
    pipeline=DataPipeline()
    print("Pipeline avviata...")
    pipeline.esegui_pipeline()
    print("pipeline completata con successo")