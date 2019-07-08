from automagica import *
from retry import retry
@retry(delay=1)
def waitAndClickImage(pic:str):
    return ClickOnImage(pic)

browser = ChromeBrowser()
browser.get('https://qiita.com/')
search = 'python x 業務効率化'

gh = browser.find_element_by_css_selector('#globalHeader')
sb = gh.find_element_by_css_selector('.st-Header_searchButton')
si = gh.find_element_by_css_selector('.st-Header_searchModalInput')

sb.click()
si.send_keys(search)
si.submit()

logo = os.path.realpath(os.path.dirname(__file__) + '.\\logo.png')
if not os.path.exists(logo):
    print(logo)
    exit()

waitAndClickImage(logo)