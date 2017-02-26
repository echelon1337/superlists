#coding: utf-8
#TDD_1 functional_tests
#21.02.2017 eezme


from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):    # przed testem
        self.browser = webdriver.Firefox()

    def tearDown(self):     # po teście
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Edyta dowiedziała się o nowej aplikacji w postaci listy rzeczy do zrobienia
        # Postanowiła więc przejść na stronę główną tej aplikacji
        self.browser.get('http://localhost:8000')

        # Zwróciła uwagę, że tytuły strony i nagłówek zawierają słowo Listy
        self.assertIn('Listy', self.browser.title)
        self.fail('Zakończenie testu')

        # Od razu zostaje zachęcona aby wpisać rzeczy do zrobienia

        # W polu tekstowym wpisała "Kupić pawie Pióra" ( hobby
        # Edyty polega na tworzeniu ozdobnych przynęt )

        # Po naciśnięciu klawisza Enter strona została zauktalizowana i wyświetla
        # "1: Kupić pawie pióra" jako element listy do zrobienia

        # Na stronie nadal znajduje się pole tekstowe zachęcające do podania kolejnego zadania.
        # Edyta wpisała "Użyć pawich piór" (Edyta niezwykle skrupulatna)

        # Strona została ponownie uaktualniona i teraz wyświetla dwa elementy na liście rzeczy do zrobienia

        # Edyta była ciekawa czy witryna zapamięta jej listę. Zwróciła uwagę na wygenerowany dla niej
        # unikatowy adres URL, obok którego znajduje się pewien tekst z wyjaśnieniem

        # Przechodzi pod podany adres URL i widzi wyświetloną swoją listę rzeczy  do zrobienia

        # Usatysfakcjonowana kładzie się spać


if __name__ == '__main__':
    unittest.main(warnings='ignore')
