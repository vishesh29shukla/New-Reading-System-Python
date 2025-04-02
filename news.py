from GoogleNews import GoogleNews
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 130)
googlenews = GoogleNews(lang='en')
fd = input("Enter date from you want to hear news in dd/mm/yyyy :- ")
ed = input("Enter date till you want to hear news in dd/mm/yyyy :- ")
googlenews.set_time_range(
   fd , ed
)
googlenews = GoogleNews(encode='utf-8')
Topic = input("Enter Topic :- ")
googlenews.get_news(Topic)
x = googlenews.get_texts()
# y = googlenews.get_links()
print(x)
engine.say(x)
engine.runAndWait()
