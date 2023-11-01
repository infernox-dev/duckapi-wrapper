from duckapi import DuckAPI
from asyncio import run


async def main() -> None:
    duck = DuckAPI()
    asset = await duck.duck()
    
    with open(file="duck.png", mode="wb") as file:
        file.write(await asset.download())
    
run(main())
