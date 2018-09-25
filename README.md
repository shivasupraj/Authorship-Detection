# Authorship-Detection

Automated authorship detection is the process of using a computer program to analyze a collection of texts one of which has an unknown author, and making guesses about the author of that unattributed text. The basic idea is to use different statistics from the text -- called "features" in the machine learning community -- to form a linguistic "signature" for each text. 

### How the program works

The program begins by asking the user for two strings: the first is the name of a file of text whose authorship is unknown (the mystery file) and the second is the name of a directory of files, each containing one linguistic signature.

The program calculates the linguistic signature for the mystery file and then calculates scores indicating how well the mystery file matches each signature file in the directory. The author from the signature file that best matches the mystery file is reported.

### Linguistic features calculated

* **Type-Token Ratio** is the number of different words used in a text divided by the total number of words.

* **Hapax Legomana Ratio** is similar to Type-Token Ratio in that it is a ratio using the total number of words as the denominator. The numerator for the Hapax Legomana Ratio is the number of words occurring exactly once in the text.

* **Average number of words** per sentence.

* **Sentence complexity**, it is the average number of phrases per sentence.
