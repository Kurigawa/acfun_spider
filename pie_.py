import pandas as pd
import pygal

def data(df):
    p = pygal.Pie()
    x_data = df.index.values
    for i, per in enumerate(df['播放']):
        p.add(x_data[i], per)
    p.title = 'Acfun视频信息'
    p.render_to_file('饼图.svg')

df = pd.read_csv('Acfun视频信息.csv', encoding='utf-8')
df_sum = df.drop(['标题', 'UP主', 'ac号', '上传时间', '子分区'], axis=1).groupby('主分区').sum().sort_values('播放', ascending=False)
# print(df_sum)
data(df_sum)


