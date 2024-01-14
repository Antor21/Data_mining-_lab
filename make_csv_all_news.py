import bs4
import requests
import csv

URL_LINK = 'sports_main_page_url.csv'
CSV_LINK = 'sports_dataset_news.csv'

def append_to_csv(row):

    global CSV_LINK

    with open(CSV_LINK, mode='a', newline='' , encoding='utf-8') as unit_new_article:
            news_article_writer = csv.writer(unit_new_article, delimiter=',' , quoting=csv.QUOTE_MINIMAL)
            news_article_writer.writerow(row)


    pass

import re
def get_title_and_content(page,soup):


    #if soup.find_all("h2")[0].getText()== "":
    #    print(type(soup.find_all("h2")[0].getText()))
     #   #newsTitle="No Title"
    #    pass
    #else:
    #    newsTitle = soup.find_all("h2")[0].getText()

    newsTitle = soup.find_all("h2")[0].getText()
    print(newsTitle)
    newsTitle=newsTitle.strip()


    CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

    def cleanhtml(raw_html):
        cleantext = re.sub(CLEANR, '', raw_html)
        return cleantext
    Date = soup.find("div", {"class": "rpt_name border-top mt-1 pt-1"})
    Date=str(Date.text)
    newsDate = cleanhtml(Date)


    article_text = soup.find("div", {"class": "dtl_section"})
    all_paragraphs = article_text("p")
    news_content = ""

    for paragraph in all_paragraphs:

        news_content += paragraph.getText()
        news_content=news_content.strip()


    cat="politics"

    input_array = [cat, newsDate , newsTitle , news_content]
    append_to_csv(input_array)

    pass

with open(URL_LINK) as unit_url_csv:
    readCSV = csv.reader(unit_url_csv)

    i = 0

    for row in readCSV:



        #if i >= 500:
           # break

        print(i)
        #newsTitle = soup.find_all("h2")[0].getText()
        BASE_URL = row[0]
        page = requests.get(BASE_URL)
        soup = bs4.BeautifulSoup(page.content, 'html.parser')
        try:
            newsTitle = soup.find_all("h2")[0].getText()
            get_title_and_content(page,soup)
        except:
            pass

        i += 1
