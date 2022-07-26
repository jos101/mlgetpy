from dataclasses import dataclass, field
from lib2to3.pytree import convert

from sympy import Not, false
from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.datasetlist.DataSetList import DataSetList
import pandas as pd


@dataclass
class Citation:
    __howpublished  : str = field(init=False)

    def __post_init__(self) -> None:
        self.__howpublished = "UCI Machine Learning Repository"

    def getPlaintext(self, creators:list, title:str, year:int, DOI:str = None) -> str:

        authors:str = self.__getAuthorsString(creators)      
        cit_str = ""

        if len(creators) > 0:
            cit_str = self.__addAuthorsPlaintext(cit_str, authors)
            cit_str = self.__addYearPlaintext(cit_str, year)
            cit_str = self.__addTitlePlaintext(cit_str, title)
            cit_str = self.__addHowpublishedPlaintext(cit_str)
            cit_str = self.__add_DOI_plaintext(cit_str, DOI, add_space=False)
        else:
            cit_str = self.__addTitlePlaintext(cit_str, title)
            cit_str = self.__addYearPlaintext(cit_str, year)
            cit_str = self.__addHowpublishedPlaintext(cit_str, add_space=False)

        cit_str = self.__remove_last_space(cit_str)

        return cit_str
    
    def __remove_last_space(self, cit_str:str) -> str:

        return cit_str.rstrip()


    def __get_space(self, add_space:bool) -> str:
        space:str = ""
        if add_space == True:
            space = " "
        
        return space


    def __add_DOI_plaintext(self, cit_str:str, DOI: str, add_space = True):
        
        space:str =  self.__get_space(add_space)

        if DOI != None:
            cit_str += f'{DOI}.{space}'
        
        return cit_str


    def __addYearPlaintext(self, cit_str: str, year:int, add_space = True ) -> str:

        space:str =  self.__get_space(add_space)

        if year != None:
            cit_str += f"({year}).{space}"
        
        return cit_str
    
    def __addAuthorsPlaintext(self, cit_str: str, authors:str, add_space = True) -> str:

        space:str =  self.__get_space(add_space)


        if len(authors) > 0 :
            cit_str += f"{authors}.{space}"
        
        return cit_str
    
    def __addTitlePlaintext(self, cit_str:str, title:str, add_space = True) -> str:

        space:str =  self.__get_space(add_space)

        cit_str += f"{title}.{space}"

        return cit_str
    
    def __addHowpublishedPlaintext(self, cit_str:str, add_space = True) -> str:

        space:str =  self.__get_space(add_space)

        cit_str += f"{self.__howpublished}.{space}"

        return cit_str

    def __addAuthors(self, cit:str, authors) -> str:
        cit += ''',
  author       = {''' + authors +'''}'''

        return cit


    def __addDOI(self, cit:str, DOI:str) -> str:
        DOI_ID:str = DOI.replace("https://doi.org/", "")
        cit += ''',
  note         = {{DOI}: \\url{''' + DOI_ID + '''}}'''

        return cit

    def __addYear(self, cit:str, year) -> str:
        cit += ''',
  year         = {''' + str(year) + '''}'''      
        
        return cit

    def __addTitle(self, cit:str, title) -> str:
        
        cit += ''',
  title        = {{''' + title + '''}}'''

        return cit

    def __addHowPublished(self, cit:str) -> str:
        
        cit += ''',
  howpublished = {''' + self.__howpublished + '''}'''

        return cit
  

    def getBibtext(self, creators:list, title:str, year:int, repo_ID:int, DOI:str = None) -> str:

        newTitle = self.__convertTitle(title, repo_ID)
        authors:str = self.__getAuthorsString(creators)

        cit =  '''@misc{''' + newTitle + ''''''

        if len(creators) > 0:
            cit = self.__addAuthors(cit, authors)
        
        cit = self.__addTitle(cit, title)

        if year != None:
            cit =  self.__addYear(cit, year)

        cit = self.__addHowPublished(cit)

        if DOI != None:
            cit = self.__addDOI(cit, DOI)

        cit += '''
}'''

        return cit 

    def __convertTitle(self, title:str, repo_ID:int) -> str:
        new_title = ( "misc_" + title.replace(" ", "_") + "_" + str(repo_ID) ).lower()
        
        return new_title


    '''

    returns authors in this text format

    last_name, first_name, last_name, first_name .... & last_name, firt_name
    
    '''
    def __getAuthorsString(self, creators:list) -> str:
        
        authors = ""
        i = 0
        for c in creators:
            authors += f'{c["lastName"]}, {c["firstName"]}'

            i += 1
            if i < ( len(creators) - 1 ) :
                authors += ", "
            
            if i == ( len(creators) - 1 ):
                authors += " & "
            
        
        return authors
