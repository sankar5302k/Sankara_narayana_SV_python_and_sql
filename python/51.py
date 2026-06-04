import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        hash_obj = hashlib.md5(url.encode())
        short_id = hash_obj.hexdigest()[:6]
        self.url_map[short_id] = url
        return short_id

    def lookup(self, short_id):
        return self.url_map.get(short_id, "URL not found")

shortener = URLShortener()
short = shortener.shorten("https://www.example.com/very/long/url")
print(f"Short ID: {short}")
print(f"Original: {shortener.lookup(short)}")
