import hashlib

class Short_Link:
    def __init__(self):
        self.url_mapping = {}
        self.base_url = "http://shurl/"

    def shorturl(self, org_url):
        hash_value = hashlib.md5(org_url.encode()).hexdigest()[:6]
        short_url = self.base_url + hash_value
        self.url_mapping[short_url] = org_url
        return short_url
    
    def extented_url(self, short_url):
        org_url = self.url_mapping.get(short_url)
        return org_url
    

short_the_url = Short_Link()
org_url = input("Enter your URL :- ")
short_url = short_the_url.shorturl(org_url)

print(f"Original URL :- {org_url}\n")
print(f"Short URL :- {short_url}\n")

ext_url = short_the_url.extented_url(short_url)
print(f"Extended URL :- {ext_url}\n")