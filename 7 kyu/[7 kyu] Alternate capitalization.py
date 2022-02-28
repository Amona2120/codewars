def capitalize(s):
    return ["".join(n.lower() if i % 2 else n.upper() for i,n in enumerate(s)),
            "".join(n.upper() if i % 2 else n.lower()for i,n in enumerate(s))]
