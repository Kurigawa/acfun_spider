import pandas as pd
import pygal

def data(df,s):
    l = pygal.Line()
    x_data = df.index.values
    # 获取索引值
    l.add('播放', df['播放'])
    l.add('评论', df['评论'])
    l.add('弹幕', df['弹幕'])
    l.add('收藏', df['收藏'])
    l.add('投蕉', df['投蕉'])
    l.x_labels = x_data
    l.title = f'Acfun视频信息({s})'
    l.x_title = '时间'
    l.render_to_file(f'折线图（{s}）.svg')

df = pd.read_csv('Acfun视频信息.csv', encoding='utf-8')
for i in range(len(df[['上传时间']])):
    df.loc[i, '上传时间'] = df.loc[i, '上传时间'].split('-')[0]
    # 将时间更改为年份做分组
df_mean = df.drop(['标题', 'UP主', 'ac号', '主分区', '子分区'], axis=1).groupby('上传时间').mean().sort_values('上传时间', ascending=True)
df_sum = df.drop(['标题', 'UP主', 'ac号', '主分区', '子分区'], axis=1).groupby('上传时间').sum().sort_values('上传时间', ascending=True)
df_mean = df_mean.astype(int)
# 去掉小数部分
data(df_mean, '均值')
data(df_sum, '总数')
