import http.client

from dataclasses import dataclass

def SendRequest(url : str, resource : str, payload={}) -> dict:
    conn = http.client.HTTPSConnection("movies-v2.api-fetch.sh")

    conn.request("GET", resource, payload)

    res = conn.getresponse()
    return res.read().decode("utf-8")


@dataclass
class Torrent:
    """
    Torrent Data Class
    """
    provider: str
    peers: int
    seeds: int
    magnet: str
    quality: str


@dataclass
class Show:
    """
    Show Data Class
    """
    imbd: str
    title: str
    season_count: int
    torrent: Torrent