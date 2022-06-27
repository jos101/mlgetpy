from mlrgetpy.Citation import Citation
import unittest

class TestCitation(unittest.TestCase):

    def test_get(self):

        cit = Citation()
        
        '''
        Test one author
        '''

        creators:list = []
        creators.append({"firstName":"Abhilash", "lastName":"Singh"})
        DOI = "https://doi.org/10.3390/s22031070"
        cit_str = cit.get(creators, "LT-FS-ID: Intrusion detection in WSNs", 2022, "https://doi.org/10.3390/s22031070")

        expected_result = "Singh, Abhilash. (2022). LT-FS-ID: Intrusion detection in WSNs. UCI Machine Learning Repository. https://doi.org/10.3390/s22031070."
        msg = "One author with DOI"
        self.assertEqual(cit_str, expected_result, msg)



        '''
        Test two author
        '''
        creators:list = []
        creators.append({"firstName":"Akshay", "lastName":"Mathur"})
        creators.append({"firstName":"Akshay", "lastName":"Mathur"})
        
        cit_str = cit.get(creators, "NATICUSdroid (Android Permissions) Dataset", 2022)
        self.assertEqual(cit_str, "Mathur, Akshay & Mathur, Akshay. (2022). NATICUSdroid (Android Permissions) Dataset. UCI Machine Learning Repository.", "Two authors")

        '''
        Test three authors
        '''
        creators = []
        creators.append({"firstName":"Sumon ", "lastName":"Kanti Dey"})
        creators.append({"firstName":"Michael ", "lastName":"Cochez "})
        creators.append({"firstName":"Md. Rezaul", "lastName":"Karim"})
        cit_str = cit.get(creators, "Bengali Hate Speech Detection Dataset", 2022)

        expected_result = "Kanti Dey, Sumon , Cochez , Michael  & Karim, Md. Rezaul. (2022). Bengali Hate Speech Detection Dataset. UCI Machine Learning Repository."
        self.assertEqual(cit_str, expected_result, "Three Authors and right space in firstName and lastName")
