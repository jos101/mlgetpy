from dataclasses import dataclass
import os


@dataclass
class URLManager:

    def folder_from_link(link):
        link = URLManager.remove_last_forward_slash(link)
        return link.rsplit('/', 1)[-1]

    def remove_last_forward_slash(link):
        if (link[-1] == "/"):
            link = link[:len(link)-1]
        return link

    def create_name_folder(nameFolder: str, link: str):
        link = URLManager.remove_last_forward_slash(link)

        newNamefolder = ""
        target_folder = URLManager.folder_from_link(link)
        newNamefolder = os.path.join(nameFolder, target_folder)

        return newNamefolder
