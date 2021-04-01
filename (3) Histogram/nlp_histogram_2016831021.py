import pandas as pd
import re
from tabulate import tabulate
import operator


def dataset_load():
    data = pd.read_csv("../Datasets/(2) Prepared Datasets/eng_bang_data.csv")
    return data["English"], data["Bangla"]


def corpus_size_words(data):
    size = 0
    for single_data in data:
        size += len(re.split('[; |,]+', single_data))
    return size


def corpus_size_lines(data):
    size = 0
    for single_data in data:
        sentences = re.split(r'[!?.।]+ +', single_data)
        size += len(sentences)
    return size


def corpus_size_chars(data):
    size = 0
    for single_data in data:
        size += len(single_data)-single_data.count(" ")
    return size


def avg_sen_len(total_words, total_sentences):
    return total_words/total_sentences


def vocabulary_size(data):
    unique_words = set()
    for single_data in data:
        sentences = re.split(r'\s', single_data)
        for sen in sentences:
            unique_words.add(sen)
            
    return unique_words


def lex_div(data):
    all_words = []
    for single_data in data:
        sentences = re.split(r'\s', single_data)
        for sen in sentences:
            all_words.append(sen)

    unique_words = vocabulary_size(data)
    word_freq = []
    for uni_word in unique_words:
        word_freq.append(all_words.count(uni_word))

    return sum(word_freq)/len(word_freq)


def top_ten_freq_words(data):
    all_words = []
    words_freq = {}

    for single_data in data:
        sentences = re.split(r'\s', single_data)
        for sen in sentences:
            all_words.append(sen)

    unique_words = vocabulary_size(data)
    total_words = len(all_words)

    for uni_word in unique_words:
        unit_word_freq = all_words.count(uni_word)
        word_percentage = (unit_word_freq/total_words)*100
        words_freq[uni_word] = [unit_word_freq, word_percentage]

    sorted_dic = sorted(words_freq.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_dic[:10]


def histogram_table(
        bangle,
        english
):
    print("\n(1) Statistics from the parallel corpus:\n")
    table = [["Corpus size (in words) excluding punctuation", english[0], bangle[0]],
             ["Corpus size (in chars) excluding spaces", english[1], bangle[1]],
             ["Average sentence length (in words)", english[2], bangle[2]],
             ["Vocabulary size (no. of unique words)", english[3], bangle[3]],
             ["Lexical diversity*", english[4], bangle[4]],
             ["Corpus size (in lines)", english[5], bangle[5]]]
    headers = ["", "English side", "Bangla side"]
    print(tabulate(table, headers, tablefmt="pretty"))


def top_ten_frequent_words():
    pass


if __name__ == "__main__":
    eng_data, ban_data = dataset_load()
    bangle_results = [
        corpus_size_words(ban_data),
        corpus_size_chars(ban_data),
        avg_sen_len(corpus_size_words(ban_data), corpus_size_lines(ban_data)),
        len(vocabulary_size(ban_data)),
        lex_div(ban_data),
        corpus_size_lines(ban_data)
    ]
    english_results = [
        corpus_size_words(eng_data),
        corpus_size_chars(eng_data),
        avg_sen_len(corpus_size_words(eng_data), corpus_size_lines(eng_data)),
        len(vocabulary_size(eng_data)),
        lex_div(eng_data),
        corpus_size_lines(eng_data)
    ]

    histogram_table(bangle_results, english_results)

    ban_freq_words = top_ten_freq_words(ban_data)
    eng_freq_words = top_ten_freq_words(eng_data)
    print("\n\n(2) Top ten frequent words in your parallel corpus:")
    print("Top ten frequent words in Bangla Side : ", ban_freq_words)
    print("Top ten frequent words in English Side : ", eng_freq_words)