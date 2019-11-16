import glob
import pickle
import re
from urllib import request


def glob_file():
    """
    获取与通配符匹配的文件名列表
    """
    file_list = glob.glob('./*.py')
    print(file_list)
    file_list = glob.glob('../*.*')
    print(file_list)


def persistent_data_with_pickle():
    """
    使用pickle模块将数据保存到本地
    需要以二进制模式读/写
    其他语言需要实现pickle协议才能读取该文件，
    """
    data = {
        "a": 1
    }
    with open('../tmp/tmp111', 'wb') as wFile:
        pickle.dump(data, wFile)
    with open('../tmp/tmp111', 'rb') as rFile:
        recover_obj = pickle.load(rFile)
        print(recover_obj)


def top_words_in_web():
    """
    计数某网页单词top10
    """
    url = "https://developer.mozilla.org/en-US/"
    try:
        with request.urlopen(url) as doc:
            html = doc.read()
            html = str(html)
            html = html.lower()
            words = {}
            word_list = re.findall(r"\b[a-zA-Z]+\b", html)
            for word in word_list:
                if word not in words:
                    words[word] = 0
                words[word] += 1
            top_10 = sorted(words.items(), key=lambda kv: kv[1], reverse=True)
            top_10 = top_10[0:10]
            for top_word in top_10:
                print(top_word)
    except Exception as err:
        print("load %s error" % url)
        print(err)


top_words_in_web()
