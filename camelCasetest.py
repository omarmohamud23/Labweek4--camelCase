import camelCase


from unittest import TestCase


class TestCamelCase(TestCase):

    def test_camel_case_sentence(self):
        self.assertEqual('helloWorld', camelCase.camel_case('Hello World'))

    def test_mixture_of_lower_upper_case_in_a_sentence(self):
        self.assertEqual('hereComesTheGarden', camelCase.camel_case('here comes The Garden'))

    def test_for_one_word(self):
        self.assertEqual('coding', camelCase.camel_case('coding')) 

    def test_camel_case_uppercase(self):
        self.assertEqual('hello', camelCase.camel_case('HELLO')) 

    

