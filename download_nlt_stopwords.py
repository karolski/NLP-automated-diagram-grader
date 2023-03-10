import nltk

#try to avoid ssl certificate failures
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
print("downloading stopwords...")
nltk.download('stopwords')
print("downloading punkt...")
nltk.download('punkt')
print("done")
