import json
import matplotlib.pyplot as plt
import numpy as np
#from wordcloud import WordCloud


class FileHelper:
    @staticmethod
    def read_data_file(name, max_num=None):
        texts = []
        summaries = []
        overall = []

        iteration = 0
        with open(name, "r") as json_file:
            for line in json_file:
                if max_num is not None and max_num <= iteration:
                    break

                str = json.loads(line)

                rate = str["overall"]
                # if rate == 3:
                #     continue
                #
                iteration = iteration + 1

                texts.append(str["reviewText"])
                summaries.append(str["summary"])
                overall.append(rate)

        return texts, summaries, overall

    @staticmethod
    def read_word2vec(file_name="word2vec/glove.6B.50d.txt"):
        with open(file_name, "rb") as lines:
            w2v = {line.split()[0]: np.array(map(float, line.split()[1:]))
                   for line in lines}
            return w2v

    @staticmethod
    def get_sample_data_rates():
        return FileHelper.read_data_file("data/balanced_sample.json")

    @staticmethod
    def show_word_cloud(word_frequences):
        print('Install packages and uncomment')
        # wordcloud = WordCloud()
        # wordcloud.generate_from_frequencies(frequencies=word_frequences)
        # plt.figure()
        # plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # plt.show()

    @staticmethod
    def print_top10(vectorizer, clf, class_labels):
        """Prints features with the highest coefficient values, per class"""
        feature_names = vectorizer.get_feature_names()
        for i, class_label in enumerate(class_labels):
            top10 = np.argsort((clf.coef_[i]))[-10:] #abs
            print("%s: %s" % (class_label,
                  " ".join(feature_names[j] for j in top10)))