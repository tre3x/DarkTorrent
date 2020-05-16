import requests
import webbrowser
import bs4
import re


def linkof(query, choice):

    choice = int(choice)

    fp = open("proxylist")
    for i, line in enumerate(fp):
        print(i, choice)
        if i == choice:
            print("k")
            url = line.replace('Ã¬', 'ì')
            break
    fp.close()

    query = query.replace(' ', '+')
    page = 0
    orderby = 99
    if (choice == 0):
        link = url[:-2] + "/proxy/go.php?url=s/?q=" + query + \
            "&page=" + str(page) + "&orderby" + str(orderby)
    if(choice != 0):
        link = url[:-2] + "/s/?q=" + query + "&page=" + \
            str(page) + "&orderby" + str(orderby)
    print(link)

    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    linklist = []

    num = 0

    for table in soup.find_all("table", id="searchResult"):
        for tr in table.find_all("tr"):
            for td in tr.find_all("td"):

                div = td.find(class_="detName")
                if (div):
                    link = div.find("a")
                    name = link.contents[0]
                    redirectlink = (url[:-2] + link['href'])

                font = td.find("font", {"class": "detDesc"})

                if (font):
                    size = font.get_text()
                    sizestart = size.find('Size')
                    commastart = size.find('ULed')
                    size = (size[sizestart+5:commastart-2])
                    size = size.replace('\xa0', ' ')


                for a in td.find_all('a'):
                    if(a['href'][0:6] == 'magnet'):
                        linklist.append([name, redirectlink, a['href'], size])

            if(num == 5):
                break
            num = num + 1

    return linklist


'''
def proxylist():
    url = 'https://piratebay-proxy.org/'

    res = requests.get(url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    proxylist = []

    for table in soup.find_all('table', id = "proxyList"):
        for tr in table.find_all('tr'):
            for a in tr.find_all('a'):
                print(a['href'])
                

    return proxylist



proxyarr = proxylist()
myfile = "proxylist.txt"


with open(myfile, "w") as f:
    for line in proxyarr:
        f.write(line + '\n')


choice = int(input(("Enter Choice : ")))


query = input("Enter query : ")

linkarr = linkof(query, choice)
print(linkarr)
'''