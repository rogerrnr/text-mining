from mediawiki import MediaWiki
import string
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')



def sentiment_analysis():
    ###https://pypi.org/project/spacytextblob/
    ###https://spacy.io/universe/project/spacy-textblob
    with open('cancel_culture.txt', 'r') as file:
        data = file.read().replace('\n', '')
        doc = nlp(data)
        print("This article has a polarity of",doc._.polarity)      
        print("This article has a subjectivity of",doc._.subjectivity)
        print(doc._.assessments)

def top_thirty_used_words(words):
    ##assign a dict value called new_dict.Use the python sorted function to sort the words
    """https://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-1.php"""
   
    new_dict= sorted(words.items(), key=lambda x: x[1],reverse=True)
#    print(new_dict)
    return new_dict


def word_frequency(data):
    words = []
    d = {}

    with open(data) as file:
        lines = file.readlines()
        for line in lines:
            # words.append(line)
            for word in line.split():
                words.append(word.lower())
                
            if line.startswith("== See also =="):            
                 break
        for word in words:
            if word not in d:
                d[word]=1
            else:
                d[word]+=1
        # print(d)
        print("The total words are",len(words))
        print("top ten most used words are",top_thirty_used_words(d)[:30])

        return d




def main (): 
    wikipedia = MediaWiki()
    cancel_culture = wikipedia.page("Cancel Culture")
    # print(cancel_culture.title)
    # cancel_culture_file=open('cancel_culture.txt','x')
    # cancel_culture_file.write(cancel_culture.content)
    # print(cancel_culture.content)
    word_frequency('cancel_culture.txt')
    sentiment_analysis()
    # line_by_line_polarity()
    # d = process_file(data, skip_header=True)
    # print('Total number of words:', total_words(d)) 



if __name__ == '__main__':
    main()