import pandas as pd
import math
import random


class knnModel():
    def KNNMODEL(address_of_csv,fir_num,sec_num):
        x11=[fir_num,sec_num]
        df = pd.read_csv(address_of_csv)
        # x11 = [random.randrange(-9,10),random.randrange(-9,10)]
        # print(x11)
        distances=[]
        # loop to check distances
        for i in df.itertuples():
            r_csv = [i.x1,i.x2]
            dis = math.dist(x11, r_csv)
            distances.append(dis)

        df['distance'] = distances
        # New Dataframe that sort values by distance
        new_df = df.sort_values(by='distance')
        # get top 5 result values
        top_5 = new_df['y'].head(5)
        # Display Final result
        return top_5.mode()[0]
        