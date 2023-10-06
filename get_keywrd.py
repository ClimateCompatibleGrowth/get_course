import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import markdown

from get_lecture import get_lecture

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Function to extract keywords from a text
def extract_keywords(text):
    # Tokenize the text
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stopwords_set = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stopwords_set]
    
    # Calculate word frequency
    word_freq = FreqDist(words)
    
    # Select the top 10 most frequent words as keywords
    keywords = [word for word, _ in word_freq.most_common(10)]
    
    return keywords

 #Extract keywords from the lecture note
keywords = extract_keywords('get_lecture')

# Generate Markdown content with keywords
#markdown_content = "\n".join([f"- {keyword}" for keyword in keywords])

# Save the Markdown content to a file
#with open("keywords.md", "w") as file:
    #file.write(markdown_content)

#print("Keywords extracted and saved to 'keywords.md'")

# Optional: Print the extracted keywords
#print("Extracted Keywords:")
for keyword in keywords:
    print(keyword)





