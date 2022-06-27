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



    def getBibtext(self, firstName, lastName, title, year, repo_ID) -> str:

        newTitle = self.__convertTitle(title, repo_ID)

        cit =  '''@misc{''' + newTitle + ''',
        author       = {''' + lastName + ''', ''' + firstName +'''},
        title        = {{''' + title + '''}},
        year         = {''' + str(year) + '''},
        howpublished = {''' + self.__howpublished + '''}
        }'''

        return cit 


    def __convertTitle(self, title:str, repo_ID:int) -> str:
        new_title = "misc_" + title.replace(" ", "_") + "_" + str(repo_ID)
        
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
