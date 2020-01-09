import requests
import json
import os
from bs4 import BeautifulSoup

dataset = []

"""
 



 

"""


def get(url):
    user_agent_text = "Mozilla/5.0 (Windows NT 6.3; Win) Gecko/20100101 Firefox/71.0"
    headerdict = {"User-Agent": user_agent_text}
    r = requests.get(url, headers=headerdict)
    r.raise_for_status()
    return r


def get_urls(arglist, is_verbose=False):
    for url_en_arg in arglist:
        try:
            r = get(url_en_arg)
        except Exception as e:
            print(f"Erreur de requests  vers {url_en_arg}")
            print(str(e))
            r = None
        if r:
            displayurl(r, is_verbose)
            writetodict(r, is_verbose)


F_URL = "url"
F_STATUS = "status_code"
F_HTML = "content"
F_TITLE = "title"
F_DESCRIPTION = "description"
F_IMAGE = "image"
F_H1 = "items_h1"
F_H2 = "items_h2"


def writetodict(r, is_verbose=False):
    """
    writetodict [summary]
    
    Arguments:
        r {[type]} -- [description]
    
    Keyword Arguments:
        is_verbose {bool} -- [description] (default: {False})
    """
    dict_html = {F_URL: r.url, F_STATUS: r.status_code}
    dict_meta = search_meta_by_bs4(r.text)
    search_bu_avignon(r.text)
    if dict_meta:
        dict_html.update(dict_meta)

    # ATTENTION : dataset est défini en global comme une liste
    global dataset
    dataset.append(dict_html)


def search_bu_avignon(text):
    # result-list-record
    soup = BeautifulSoup(text, "lxml")
    result_list = soup.find_all("div", {"class": "result-list-record"})
    for result_item in result_list:
        print(result_item.select("h3")[0].get_text())
        print(result_item.select(".display-info")[0].get_text())
        print(
            result_item.select(".circulation.rtac-table")
        )  # , attrs={"data-label": True}
        # print(result_item.select("[data-label=Cote du document]"))
        print("-" * 30)


def search_meta_by_bs4(text):
    """ search_meta_by_bs4 :
        cette fonction sert à ....
        elle récupère ...
    """

    # note 7.1.2020
    # https://outils-javascript.aliasdmc.fr/encodage-caracteres-accentues/encode-caractere-00E9-html-css-js-autre.html
    # mauvais encodage de é par js ou css : format iso-8859-1
    text = text.replace("Ã©", "é")
    soup = BeautifulSoup(text, "lxml")
    dict_meta = dict()

    meta_title = soup.find("meta", property="og:title")
    if not meta_title:
        meta_title = soup.title.string
    else:
        dict_meta[F_TITLE] = meta_title["content"]

    meta_description = soup.find("meta", property="og:description")
    dict_meta[F_DESCRIPTION] = meta_description["content"] if meta_description else ""

    meta_image = soup.find("meta", property="og:image")
    dict_meta[F_IMAGE] = meta_image["content"] if meta_image else ""

    # ATTENTION CODE DE FIN DE MATINEE
    d = soup.find_all("h1")
    if d:
        dict_meta[F_H1] = []
        for h1 in d:
            dict_meta[F_H1].append(h1.text)
            print(f"--> h1 : {h1.text}")
    d = soup.find_all("h2")
    if d:
        dict_meta[F_H2] = []
        for h2 in d:
            dict_meta[F_H2].append(h2.text)
            print(f"--> h2 : {h2.text}")
    # FIN DE CODE DE FIN DE MATINEE

    print("-" * 100)
    print(type(meta_title))
    # print(meta_title["content"])
    return dict_meta


def search_title(text):

    # DEPRECATED USE BEAUTIFULL SOUP INSTEAD
    retbuffer = begin = 0
    end = None
    begin = text.find("<title>")
    if begin != -1:
        begin += len("<title>")
        end = text[begin:].find("</title>")
        if end != -1:
            end += begin
            retbuffer = text[begin:end]
    print(f"Test search_title : {begin}, {end}, {retbuffer}")
    return search_title_by_bs4(text)
    # return retbuffer


def displayurl(r, is_verbose=False):
    print(f"--> Il y a {len(r.text)} octets and {r.url}")
    if is_verbose:
        print(r.status_code)
        # pprint.pprint(r.headers, indent=4)
        # print(json.dumps(r.headers))
        for key, value in r.headers.items():
            print(f"{key} : {value}")
        print("-" * 30)
        print(r.text[:1000])
        print("-" * 30)


if __name__ == "__main__":
    letempsquipasse = ["matin", "midi", "soir", "minuit", "aube"]
    for item in letempsquipasse:
        print(item)

    a_listedesurls = [
        "https://www.elpais.com",
        "https://www.excelcior.com",
        "https://www.liberation.fr",
        "https://www.lemonde.fr",
        "https://www.ouest-france.fr",
        "https://www.nytimes.com",
        "https://edition.cnn.com",
        "https://www.japantimes.co.jp",
    ]

    listedesurls = [
        "http://eds.b.ebscohost.com/eds/results?vid=0&sid=79db47f4-913c-43ed-b445-b1ab90bccb26%40pdc-v-sessmgr03&bquery=japon&bdata=JmNsaTA9RlQxJmNsdjA9WSZsYW5nPWZyJnR5cGU9MCZzZWFyY2hNb2RlPUFuZCZzaXRlPWVkcy1saXZlJnNjb3BlPXNpdGU%3d",
    ]

    get_urls(listedesurls, False)

    # ATTENTION : dataset est défini en global comme une liste
    print(len(dataset))

    # affiche le nom du fichier .py
    print(__file__)
    # affiche le répertoire absolue pour le système d'exploitation
    print(os.path.abspath(__file__))
    # affiche le répertoire contenant le fichier .py
    print(os.path.dirname(__file__))
    # récupère le répertoire dans la configuration du système d'exploitation
    basedir = os.path.dirname(os.path.abspath(__file__))
    print(basedir)
    # creation du fichier checkurl.json dans le repertoire scrap

    dataset_api = {"count": len(dataset), "dataset": dataset}

    filename = basedir + "/" + "scrapbiblio.json"
    with open(filename, "w", encoding="utf8") as f:
        json.dump(dataset_api, f)
        print(f"file {filename} created !")

    # CES TROIS LIGNES EQUIVALENT AUX DEUX LIGNES DU with
    # f = open("test.json", "w+", encoding="utf8")
    # json.dump(dataset, f)
    # f.close()
