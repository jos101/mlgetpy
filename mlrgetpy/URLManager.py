from dataclasses import dataclass
import os


@dataclass
class URLManager:

    def folder_from_link(link):
        """ Get the parent folder from a path

        Args:
            link (str): the http or https path 

        Returns:
            srt: name of the parent folder
        """
        link = URLManager.remove_last_forward_slash(link)
        return link.rsplit('/', 1)[-1]

    def remove_last_forward_slash(link):
        """ if the last character is a forward it will be removed

        Args:
            link (str): the http or https path

        Returns:
            str: the http or https path without the foward slash at the end

        """
        if (link[-1] == "/"):
            link = link[:len(link)-1]
        return link

    def create_name_folder(nameFolder: str, link: str):
        """Concatenate nameFolder with the parent folder of link

            i.e 
            name_folder: my/folder
            link: http:/foo/bar/

            return my/folder/bar

        Args:
            nameFolder (str): the path of a folder 
            link (str): the http or https string

        Returns:
            str: a new path which is the path join of nameFolder and the parent folder of link
        """
        link = URLManager.remove_last_forward_slash(link)

        newNamefolder = ""
        target_folder = URLManager.folder_from_link(link)
        newNamefolder = os.path.join(nameFolder, target_folder)

        return newNamefolder
