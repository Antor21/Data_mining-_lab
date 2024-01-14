import bs4
import requests
import csv 


base_address = "https://www.protidinersangbad.com/"


#online_category = ["","national","country","international","trade","sports","culture","science","lifestyle","job-news"]
online_category="politics"
all_url = []


for k in range(265000, 290000):

    complete_url = base_address + online_category+'/' + str(k)

    print(complete_url)
    all_url.append([complete_url])

    pass


with open('sports_main_page_url.csv', mode='w', newline='') as main_url_list:
    main_url_writer = csv.writer(main_url_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for url in all_url:
        print(url)
        main_url_writer.writerow(url)

main_url_list.close()