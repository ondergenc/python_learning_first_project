from products import Product
from products import ProductType


class Album(Product):
    artists = []

    def __init__(self, title: str, unit_price: int, artist: str):
        super().__init__(title, unit_price)
        self.artist = artist
        self.product_type = ProductType.ALBUM
        self.songs = []
        self._profit_rate = 1.35
        self.artists.append(self.artist)

    def __str__(self):
        return "Artist: {}, Title: {}, Songs: {}, Amount: {}".format(self.artist, self.title, self.songs,
                                                                     self.stock_amount)

    def search(self, search_key: str):
        if any(search_key in song for song in self.songs):
            return True
        return self.title.__contains__(search_key) or \
               self.artist.__contains__(search_key)

    def add_songs(self, new_songs: []):
        for i in range(len(new_songs)):
            if new_songs[i] not in self.songs:
                self.songs.append(new_songs[i])
