import mechanicalsoup 
import urllib, json
import requests

def search():

    browser = mechanicalsoup.StatefulBrowser()
    url = "https://archive-beta.ics.uci.edu/ml/datasets"
    url = "https://archive.ics.uci.edu/ml/datasets.php"
    url = "https://archive-beta.ics.uci.edu/api/static/ml/datasets/"
    url = "https://archive-beta.ics.uci.edu/api/datasets-donated/find?offset=0&limit=10"

    #browser.open(url , verify=False )
    #print(browser.get_current_page())

    r = requests.get(url, verify=False)
    #print ( r.json() )


    #browser.launch_browser()
    return "searching..."