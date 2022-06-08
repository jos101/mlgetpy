import mechanicalsoup

def search():

    browser = mechanicalsoup.StatefulBrowser()
    url = "https://archive-beta.ics.uci.edu/ml/datasets"
    url = "https://archive.ics.uci.edu/ml/datasets.php"

    browser.open(url)
    print(browser.get_current_page())
    return "searching..."