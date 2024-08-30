import hashlib as j


p="Lol"
iota=j.sha256(p.encode("utf-8"))
print(iota.hexdigest())