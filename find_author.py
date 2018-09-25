#! /usr/bin/env
import os.path, math
import re
def clean_up(s):
    ''' Return a version of string str in which all letters have been
    converted to lowercase and punctuation characters have been stripped 
    from both ends. Inner punctuation is left untouched. '''
    
    punctuation = '''!"',;:.-?)([]<>*#\n\t\r'''
    result = s.lower().strip(punctuation)
    return result


def average_word_length(text):
    ''' Return the average length of all words in text. Do not
    include surrounding punctuation in words. 
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word.'''
    textLength = 0
    textWordCount = 0.0
    for sentence in text:
        for word in sentence.split():
            filteredWord = clean_up(word)
            if len(filteredWord) > 0:
                textLength += len(filteredWord)
                textWordCount += 1
    averageWordLength = textLength / textWordCount
    #print averageWordLength
    return averageWordLength
    

def type_token_ratio(text):
    ''' Return the type token ratio (TTR) for this text.
    TTR is the number of different words divided by the total number of words.
    text is a non-empty list of strings each ending in \n.
    At least one line in text contains a word. '''
    distinctWords = set([])
    textWordCount = 0.0
    for sentence in text:
        for word in sentence.split():
            filteredWord = clean_up(word)
            if len(filteredWord) > 0:
                distinctWords.add(filteredWord)
                textWordCount += 1
    lengthOfDistinctWords = len(distinctWords)
    typeTokenRatio = lengthOfDistinctWords / textWordCount
    return typeTokenRatio
    
                
def hapax_legomana_ratio(text):
    ''' Return the hapax_legomana ratio for this text.
    This ratio is the number of words that occur exactly once divided
    by the total number of words.
    text is a list of strings each ending in \n.
    At least one line in text contains a word.'''

    wordsAppearedMap = {}
    lengthOfWords = 0.0
    lengthOfWordsAppearedOnce = 0.0
    for sentence in text:
        for word in sentence.split():
            filteredWord = clean_up(word)
            if len(filteredWord) > 0:
                wordsAppearedMap[filteredWord] = wordsAppearedMap.get(filteredWord, 0) + 1
                lengthOfWords += 1
    for word in wordsAppearedMap.keys():
        if wordsAppearedMap[word] == 1:
            lengthOfWordsAppearedOnce += 1

    hapaxLegomanaRatio = lengthOfWordsAppearedOnce / lengthOfWords
    return hapaxLegomanaRatio


def split_on_separators(original, separators):
    ''' Return a list of non-empty, non-blank strings from the original string
    determined by splitting the string on any of the separators.
    separators is a string of single-character separators.'''
    pattern = ''
    for separator in separators:
        if separator in '.?*\+':
            pattern += '\\'
        pattern += separator + '|'
    result = re.split(pattern[:-1], original)
    return result
                
    
def average_sentence_length(text):
    ''' Return the average number of words per sentence in text.
    text is guaranteed to have at least one sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file. '''
    sentences = []
    totalWords = 0
    totalSentences = 0.0
    for line in text:
        sentences.append(line)
    sentences = split_on_separators(''.join(sentences), '!.?')
    for sentence in sentences:
        filteredSentence = clean_up(sentence)
        if len(filteredSentence) > 0:
            for word in sentence.split():
                filteredWord = clean_up(word)
                if len(filteredWord) > 0:
                    totalWords += 1
            totalSentences += 1
    avgSentenceLength = totalWords / totalSentences
    return avgSentenceLength
    

def avg_sentence_complexity(text):
    '''Return the average number of phrases per sentence.
    Terminating punctuation defined as !?.
    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation
    or beginning or end of file.
    Phrases are substrings of a sentences separated by
    one or more of the following delimiters ,;: '''
    sentences = []
    totalPhrases = 0
    totalSentences = 0.0
    for line in text:
        sentences.append(line)
    sentences = split_on_separators(''.join(sentences), '!.?')

    for sentence in sentences:
        if len(clean_up(sentence)) > 0:
            phrases = split_on_separators(sentence, ',:;')
            for phrase in phrases:
                filteredPhrase = clean_up(phrase)
                if len(filteredPhrase) > 0:
                    totalPhrases += 1
            totalSentences += 1
    avgSentenceComplexity = totalPhrases / totalSentences
    return avgSentenceComplexity
    
    
def get_valid_filename(prompt):
    '''Use prompt (a string) to ask the user to type the name of a file. If
    the file does not exist, keep asking until they give a valid filename.
    Return the name of that file.'''
    filename = raw_input(prompt)
    while True:
        if os.path.exists(filename):
            return filename
        else:
            print "That file does not exist."
            filename = raw_input(prompt)

    
def read_directory_name(prompt):
    '''Use prompt (a string) to ask the user to type the name of a directory. If
    the directory does not exist, keep asking until they give a valid directory.
    '''
    dirname = raw_input(prompt)
    while True:
        if os.path.exists(dirname):
            return dirname
        else:
            print "That path to directory does not exist."
            dirname = raw_input(prompt)

    
def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    val = 0.0
    for i in range(1, len(sig1)):
        val += abs(sig1[i]-sig2[i]) * weight[i]
    return  val
    

def read_signature(filename):
    '''Read a linguistic signature from filename and return it as 
    list of features. '''
    
    file = open(filename, 'r')
    # the first feature is a string so it doesn't need casting to float
    result = [file.readline()]
    # all remaining features are real numbers
    for line in file:
        result.append(float(line.strip()))
    return result
        

if __name__ == '__main__':
    
    prompt = 'enter the name of the file with unknown author:'
    mystery_filename = get_valid_filename(prompt)

    # readlines gives us a list of strings one for each line of the file
    text = open(mystery_filename, 'r').readlines()

    # calculate the signature for the mystery file
    mystery_signature = [mystery_filename]
    mystery_signature.append(average_word_length(text))
    mystery_signature.append(type_token_ratio(text))
    mystery_signature.append(hapax_legomana_ratio(text))
    mystery_signature.append(average_sentence_length(text))
    mystery_signature.append(avg_sentence_complexity(text))
    
    weights = [0, 11, 33, 50, 0.4, 4]
    
    prompt = 'enter the path to the directory of signature files: '
    dir = read_directory_name(prompt)
    # every file in this directory must be a linguistic signature
    files = os.listdir(dir)

    # we will assume that there is at least one signature in that directory
    this_file = files[0]
    signature = read_signature('%s/%s'%(dir,this_file))
    best_score = compare_signatures(mystery_signature, signature, weights)
    best_author = signature[0]
    for this_file in files[1:]:
        signature = read_signature('%s/%s'%(dir, this_file))
        score = compare_signatures(mystery_signature, signature, weights)
        if score < best_score:
            best_score = score
            best_author = signature[0]
    print "best author match: %s with score %s"%(best_author, best_score)
    
