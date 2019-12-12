import json

import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

'''
读取json，提取评论内容，生成词云
'''

# 读取数据
with open("comments.json", 'r', encoding='utf-8') as f:
    data = json.load(f)
    contents = []
    for coment in data:
        contents.append(coment["content"])

    # 结巴分词
    word_list = jieba.lcut(" ".join(contents))

    # ==============词频统计=============
    word_freq = {}  # 词频统计的字典
    for word in word_list:  # 这一步是对近义词进行统计
        if (word in STOPWORDS) or len(word) == 1:  # 禁用词和低频词不统计了
            continue
        else:
            newword = word
        if newword in word_freq:
            word_freq[newword] += 1
        else:
            word_freq[newword] = 1

    freq_word = []
    for word, freq in word_freq.items():
        fenci = freq_word.append((word, freq))
    freq_word.sort(key=lambda x: x[1], reverse=True)  # 词语根据词频排序
    for word, freq in freq_word[:50]:
        with open('top50.txt', 'a', encoding='utf-8')as fp:
            fp.write(word + '\n')  # 将前五十词频文件保存
        print(word, freq)  # 打印排名前50%的单词

    # =====词云===
    wc = WordCloud(width=1024, height=768, background_color='white', font_path='./simhei.ttf',
                   stopwords=STOPWORDS, max_font_size=400, random_state=50)
    # 将分词后数据传入云图
    wc.generate_from_text(" ".join(word_list))
    plt.imshow(wc)
    plt.axis('off')  # 不显示坐标轴
    plt.show()
    # 保存结果到本地
    wc.to_file('词云图.jpg')
