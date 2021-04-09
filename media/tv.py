import requests
from dataclasses import dataclass
import dataclasses

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
class Rating:
    percentage: str
    watching: str
    votes: str
    loved: str
    hated: str

@dataclass
class Images:
    poster: str
    fanart: str
    banner: str

@dataclass
class Show:
    """
    Show Data Class
    """
    imbd_id: str
    tvdb_id: str
    title: str
    season_count: str
    image_url: str
    torrent: list[Torrent]

class TV:
    """
    TV/Series/Show Class 
    URL=[tv-v2.api-fetch]
    """

    def __init__(self):
        self.url = "https://tv-v2.api-fetch.sh/"
        self.tv_db_url = ""

    def GetShow(self, imbd_id : str) -> Show:
        res = SendRequest(self.url, "show/" + imbd_id)

        if not res:
            print(f"Failed To Get Show [{imbd_id}]")
            return None


        torrents = [e["torrents"] for e in res["episodes"] ]

        torrent_list = []

        for t in torrents:
            try:
                torrent_list.append([ Torrent(
                t[x]["provider"],
                t[x]["peers"],
                t[x]["seeds"],
                t[x]["url"], x ) for x in t])
            except:
                continue


        return Show(res["_id"], res["tvdb_id"], res["title"], res["num_seasons"], res["images"]["poster"], [ t for t in torrent_list] )

    def GetPopular(self, page : str = "1") -> list[Show]:
        res = SendRequest(self.url, "shows/" + page)
        
        if not res:
            print(f"Failed To Get Shows On Page [{page}]")
            return None

        return [dataclasses.asdict(Show(e["_id"], e["tvdb_id"], e["title"], e["num_seasons"], e["images"]["poster"], {})) for e in res ]


    def GetRandom(self):
        res = SendRequest(self.url, "random/show" )

        if not res:
            print(f"Failed To Get Random Show")
            return None

        torrents = [e["torrents"] for e in res["episodes"] ]
        
        torrent_list = []

        for t in torrents:
            torrent_list.append([ Torrent(
            t[x]["provider"],
            t[x]["peers"],
            t[x]["seeds"],
            t[x]["url"], x ) for x in t])

        return Show(res["imbd_id"], res["tvdb_id"], res["title"], res["num_seasons"], res["images"]["poster"], [ t for t in torrent_list] )


        

































