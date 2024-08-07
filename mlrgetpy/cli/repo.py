import click

from mlrgetpy.Repository import Repository
from mlrgetpy.Filter import Filter


@click.group
def mycommands():
    pass


@click.command()
@click.option("--ids", "-i", type=str, prompt="enter an ID", help="Id of the Repository.")
def download(ids: int):
    ids = ids.split(" ")

    int_ids = []
    for id in ids:
        int_ids.append(int(id))

    repo = Repository()
    repo.addByIDs(int_ids)
    repo.download(load=False)


@click.command()
@click.option("--name", "-n", type=str, help="Name of the repository.")
@click.option("--type", "-t", type=str, help="Show data in table or box format.", default="box")
def search(name: str, type: str):
    filter = Filter(contains_name=name)

    repo = Repository()
    repo.load(filter=filter)

    repo.showData(type=type)


def main():
    mycommands.add_command(download)
    mycommands.add_command(search)
    mycommands()

if __name__ == "__main__":
    main()
