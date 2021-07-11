import kivy
from kivy.app import App
from kivy.uix.label import Label
import math
import string
import sys

compareResult = "";
def read_file(filename):
    try:

        with open(filename, 'r') as f:

            data = f.read()

        return data



    except IOError:
        global compareResult
        print("Error opening or reading input file: ", filename)
        compareResult = compareResult + "Error opening or reading input file: "

        

    # splitting the text lines into words


# translation table is a global variable
# mapping upper case to lower case and
# punctuation to spaces

translation_table = str.maketrans(string.punctuation + string.ascii_uppercase,

                                  " " * len(string.punctuation) + string.ascii_lowercase)


# returns a list of the words
# in the file

def get_words_from_line_list(text):
    text = text.translate(translation_table)

    word_list = text.split()

    return word_list


# counts frequency of each word
# returns a dictionary which maps
# the words to  their frequency.

def count_frequency(word_list):
    D = {}

    for new_word in word_list:

        if new_word in D:

            D[new_word] = D[new_word] + 1



        else:

            D[new_word] = 1

    return D


# returns dictionary of (word, frequency)
# pairs from the previous dictionary.

def word_frequencies_for_file(filename):
    line_list = read_file(filename)

    word_list = get_words_from_line_list(line_list)

    freq_mapping = count_frequency(word_list)

    global compareResult
    print("File", filename, ":", )
    compareResult = compareResult + "\nFile"+filename+":\n"

    print(len(line_list), "lines, ", )
    compareResult = compareResult + str(len(line_list)) + " lines\n"

    print(len(word_list), "words, ", )
    compareResult = compareResult + str(len(word_list)) + " words\n"

    print(len(freq_mapping), "distinct words")
    compareResult = compareResult + str(len(freq_mapping)) + "distinct words"

    return freq_mapping


# returns the dot product of two documents

def dotProduct(D1, D2):
    Sum = 0.0

    for key in D1:

        if key in D2:
            Sum += (D1[key] * D2[key])

    return Sum


# returns the angle in radians
# between document vectors

def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)

    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))

    return math.acos(numerator / denominator)


def documentSimilarity(filename_1, filename_2):
    # filename_1 = sys.argv[1]

    # filename_2 = sys.argv[2]

    sorted_word_list_1 = word_frequencies_for_file(filename_1)

    sorted_word_list_2 = word_frequencies_for_file(filename_2)

    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)
    global compareResult

    print("The similarity between the documents is: % 0.6f (percentage)" % (100-(distance*15.91549)))
    compareResult = compareResult + "\nThe similarity between the documents is: "+ str(100-(distance*15.91549))+"%"


class MyApp(App):
    def build(self):
        global compareResult
        documentSimilarity('1.txt','2.txt')
        return Label(text=compareResult)

if __name__ == "__main__":
    MyApp().run()