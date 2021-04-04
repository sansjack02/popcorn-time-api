import requests
from dataclasses import dataclass

def SendRequest(url : str, endpoint : str) -> dict:
    try:
        r = requests.get(url + endpoint)
        return r.json()
    except:
        return None
    

@dataclass
class Torrent:
    """
    Torrent Data Class
    """
    provider: str
    peers: str
    seeds: str
    magnet: str
    quality: str


@dataclass
class Show:
    """
    Show Data Class
    """
    imbd: str
    title: str
    season_count: str
    torrent: Torrent

class TV:
    """
    TV/Series Class 
    URL=[tv-v2.api-fetch]
    """

    def __init__(self):
        self.url = "https://tv-v2.api-fetch.sh/"

    def GetShow(self, imbd_id : str) -> Show:
        res = SendRequest(self.url, "show/" + imbd_id)
        if not res:
            raise f"Failed To Get Show [{imbd_id}]"
        torrent = Torrent()
        return Show(res["imdb_id"], res["title"], res["num_seasons"], list[Torrent] )

    def GetPopular(self, page : str = "1"):
        res = SendRequest(self.url, "shows/" + page)
        if not res:
            raise f"Failed To Get Shows On Page [{page}]"

        return [ Show(show["imdb_id"], show["title"], show["num_seasons"], {}) for show in res ]

    def GetRandom(self):
        res = SendRequest(self.url, "random/show" )
        if not res:
            raise f"Failed To Get Random Show"

        return Show(res["imdb_id"], res["title"], res["num_seasons"], {})

        

































