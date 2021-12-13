import itertools

pairs = dict(zip(itertools.count(1), ["one", "two", "three"]))

for k, v in pairs.items():
    print(f"{k} : {v}")
