from my_spider import Response
import pymongo
L = []
for ac in range(0, 2000):
# 循环选择ac号构造url
    print(f'ac{ac * 5000}')
    # 设置步长为5000，方便数据整理
    video_info = {}
    url0 = 'https://www.acfun.cn/v/ac' + str(ac * 5000)
    Res0 = Response(url0)
    res0 = Res0.bs4_analytic()
    # bs4解析爬取的数据
    title = res0.select('h1.title')
    # 显示是否为空值
    print(title)
    if title != []:
        video_info['标题'] = title[0].text.replace('\r', '').replace('\n', '').replace(',', '，').strip()
        # 替换标题字符，防止写入文件失败或错误
        video_info['ac号'] = str(ac * 1000)
        video_info['上传时间'] = res0.select('span.time')[0].text   # 列表转换成字符串
        # select选择标签
        video_info['UP主'] = res0.select('a.name-wrap')[0].text     # ...
        video_info['主分区'] = res0.select('a.sp3')[0].text
        video_info['子分区'] = res0.select('a.sp5')[0].text
        # print(video_info)
        url1 = 'https://www.acfun.cn/content_view.aspx?contentId=' + str(ac * 5000)
        # 视频数据URL  列表[播放,评论,2,3,收藏,投蕉,弹幕]
        Res1 = Response(url1)
        res1 = Res1.requests_req().text
        # 获取视频信息    字符串
        # print(res1)
        res_lst = res1.replace('[', '').replace(']', '').split(',')
        # 将字符串转换成列表
        # print(res_lst)
        video_info['播放'] = res_lst[0]
        video_info['评论'] = res_lst[1]
        video_info['弹幕'] = res_lst[7]
        video_info['收藏'] = res_lst[5]
        video_info['投蕉'] = res_lst[6]
        print(video_info)
        L.append(video_info)
    else:
        continue
        # 标题为空时跳过一次循环
res = Response('https://www.acfun.cn/')
res.file_save_csv('Acfun视频信息', L)
# 保存文件
client = pymongo.MongoClient('mongodb://localhost:27017')
db = client.acfun
collection = db.video_info
result = collection.insert(L)
# 插入数据库