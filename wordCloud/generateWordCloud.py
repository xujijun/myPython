import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import re


def read_from_file(file_name):
    """
    从文件中读取文字
    :param file_name: 文件名
    :return: 以空格分隔的字符串
    """
    text = open(file_name, "rb").read()
    word_list = jieba.cut(text, cut_all=True)
    words = " ".join(word_list)
    return words


def clean_words(raw_words, stopwords_path):
    """
    清洗掉非字符（标点符号等）；
    过滤掉语气词等无关词
    :param raw_words: 需要被清洗的字符
    :param stopwords_path: 无关词语所在的文件路径
    :return: 清洗后的，以空格分隔的字符串
    """

    # 清洗掉非字符（标点符号等）
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    words = re.findall(pattern, raw_words)
    words = " ".join(words)
    # print(words)

    word_list = words.split()
    # print(word_list)

    # 过滤掉语气词等无关词
    stopwords = open(stopwords_path, "r", encoding="utf-8").read()
    stopwords = stopwords.split()
    # print(stopwords)
    for word in word_list:
        if word in stopwords:
            # print("word to be removed: ", word)
            word_list.remove(word)
    # print(word_list)

    words = " ".join(word_list)
    print(words)
    return words


def generate_word_cloud(words_str, font_path, output_jpg_path):
    """
    生成词云
    :param words_str: 以空格分隔的字符串
    :param font_path: 中文字体文件路径和名字
    :param output_jpg_path: 生成的图片文件路径和名字
    :return:
    """
    wc = WordCloud(
        # background_color="black",
        max_words=2000,
        font_path=font_path,
        max_font_size=150,
        # random_state=30
    )
    pic = wc.generate(words_str)
    pic.to_file(output_jpg_path)

    plt.imshow(pic)
    plt.axis("off")
    plt.show()


def main(input_file, output_file):
    words = read_from_file(input_file)
    words = clean_words(words, "stopwords.txt")
    generate_word_cloud(words, "C:\Windows\Fonts\simfang.ttf", output_file)


if __name__ == "__main__":
    # main("E:\data\courseComments_20180329.txt", "E:\data\courseComments.jpg")
    main("E:\data\orderComments_20180330.txt", "E:\data\orderComments_20180330.jpg")


