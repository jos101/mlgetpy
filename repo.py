import click

from mlrgetpy import Repository


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


def search(name: str):
    pass


def main():
    pass


mycommands.add_command(download)

if __name__ == "__main__":
    mycommands()
