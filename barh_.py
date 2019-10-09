import pandas as pd
import pygal

def data(df,s):
    b = pygal.Bar()
    x_data = df.index.values
    # 获取索引值
    b.add('播放', df['播放'])
    b.add('评论', df['评论'])
    b.add('弹幕', df['弹幕'])
    b.add('收藏', df['收藏'])
    b.add('投蕉', df['投蕉'])
    b.x_labels = x_data
    b.title = f'Acfun视频信息({s})'
    b.x_title = '分区'
    b.render_to_file(f'条形图（{s}）.svg')

df = pd.read_csv('Acfun视频信息.csv', encoding='utf-8')
df_mean = df.drop(['标题', 'UP主', 'ac号', '上传时间', '子分区'], axis=1).groupby('主分区').mean().sort_values('播放', ascending=False)
df_sum = df.drop(['标题', 'UP主', 'ac号', '上传时间', '子分区'], axis=1).groupby('主分区').sum().sort_values('播放', ascending=False)
df_mean = df_mean.astype(int)
# 去掉小数部分
data(df_mean, '均值')
data(df_sum, '总数')


