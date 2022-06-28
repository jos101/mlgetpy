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


    def test_getBibtext(self):

        cit = Citation()

        creators:list = []
        creators.append({"firstName":"Abhilash", "lastName":"Singh"})
        DOI = "https://doi.org/10.3390/s22031070"
        year = 2022
        ID = 715
        cit_str = cit.getBibtext(creators, "LT-FS-ID: Intrusion detection in WSNs", year, ID, DOI)

        expected_result = '''@misc{misc_lt-fs-id:_intrusion_detection_in_wsns_715,
  author       = {Singh, Abhilash},
  title        = {{LT-FS-ID: Intrusion detection in WSNs}},
  year         = {2022},
  howpublished = {UCI Machine Learning Repository},
  note         = {{DOI}: \\url{10.3390/s22031070}}
}'''

        msg = "One author with DOI"
        self.assertEqual(cit_str, expected_result, msg)



    def test_getBibtext_TwoAuthors(self):

        cit = Citation()

        creators:list = []
        creators.append({"firstName":"Akshay", "lastName":"Mathur"})
        creators.append({"firstName":"Akshay", "lastName":"Mathur"})
        year = 2022
        ID = 722
        cit_str = cit.getBibtext(creators, "NATICUSdroid (Android Permissions) Dataset", year, ID)

        expected_result = '''@misc{misc_naticusdroid_(android_permissions)_dataset_722,
  author       = {Mathur, Akshay & Mathur, Akshay},
  title        = {{NATICUSdroid (Android Permissions) Dataset}},
  year         = {2022},
  howpublished = {UCI Machine Learning Repository}
}'''

        msg = "Two authors"
        self.assertEqual(cit_str, expected_result, msg)


    def test_getBibtext_ThreeAuthors(self):

        cit = Citation()

        creators = []
        creators.append({"firstName":"Sumon ", "lastName":"Kanti Dey"})
        creators.append({"firstName":"Michael ", "lastName":"Cochez "})
        creators.append({"firstName":"Md. Rezaul", "lastName":"Karim"})
        year = 2022
        ID = 719

        cit_str = cit.getBibtext(creators, "Bengali Hate Speech Detection Dataset", year, ID)

        expected_result = '''@misc{misc_bengali_hate_speech_detection_dataset_719,
  author       = {Kanti Dey, Sumon , Cochez , Michael  & Karim, Md. Rezaul},
  title        = {{Bengali Hate Speech Detection Dataset}},
  year         = {2022},
  howpublished = {UCI Machine Learning Repository}
}'''

        self.assertEqual(cit_str, expected_result, "Three Authors and right space in firstName and lastName")


    def test_getBibtext_NoAuthors(self):

        cit = Citation()

        creators = []
        year = 2017
        ID = 397

        cit_str = cit.getBibtext(creators, "Las Vegas Strip", year, ID)

        expected_result = '''@misc{misc_las_vegas_strip_397,
  title        = {{Las Vegas Strip}},
  year         = {2017},
  howpublished = {UCI Machine Learning Repository}
}'''

        self.assertEqual(cit_str, expected_result, "Repository with no authors")
