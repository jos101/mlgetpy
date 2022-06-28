from dataclasses import dataclass, field
from lib2to3.pytree import convert

from sympy import Not
from mlrgetpy.DataFrameConverter import DataFrameConverter
from mlrgetpy.DataSetList import DataSetList
import pandas as pd


@dataclass
class Citation:
    __howpublished  : str = field(init=False)

    def __post_init__(self) -> None:
        self.__howpublished = "UCI Machine Learning Repository"

    def get(self, creators:list, title:str, year:int, DOI:str = None) -> str:

        authors = self.__getAuthorsString(creators)      
        cit_str = ""
        cit_str =  f'{authors}. ({year}). {title}. {self.__howpublished}.'

        if DOI != None:
            cit_str += f' {DOI}.'

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
