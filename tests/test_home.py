import time

def test_home(browser):
    url = 'http://192.168.0.16:8080'
    browser.get(url)
    time.sleep(10)

    #teste da pagina inicial
    assert 'Dash' in driver.title
    assert 'pagina inicial' in driver.page_source
    print('Pagina inicial validada com sucesso')
