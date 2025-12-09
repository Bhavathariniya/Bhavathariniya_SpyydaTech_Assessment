import json
import os
import string
import secrets

jsonfile = "urls.json"

alphabets = string.ascii_letters + string.digits
codelen = 6


def loadfn():

    if not os.path.exists(jsonfile):
        return {}
    try:
        with open(jsonfile, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            if isinstance(data, dict):
                
                any_key = next(iter(data.keys())) if data else None
                if any_key and len(any_key) == codelen:
                    return data
                
                inverted = {v: k for k, v in data.items()}
                return inverted
    except Exception:
        
        return {}
    return {}


def storefn(store):
    
    with open(jsonfile, "w", encoding="utf-8") as f:
        json.dump(store, f, indent=2, ensure_ascii=False)


def codeGeneration():
    
    return "".join(secrets.choice(alphabets) for _ in range(codelen))


def shorten(url):

    store = loadfn() 

    for code, u in store.items():
        if u == url:
            
            return code

    for _ in range(10_000):
        code = codeGeneration()
        if code not in store:
            store[code] = url
            storefn(store)
            return code

    raise RuntimeError("Couldn't generate a short code")


def redirect(code):
    
    store = loadfn()
    return store.get(code)

if __name__ == "__main__":
    print("URL shortener")
    while True:
        print("\nSelect:")
        print("1. shorten a URL")
        print("2. get URL from code (redirect)")
        print("3. exit")
        choice = input(" ").strip()

        if choice == "1":
            u = input("Enter the url to shorten: ").strip()
            if not u:
                print("no URL entered")
                continue
            code = shorten(u)
            print("Shortened code:", code)

        elif choice == "2":
            c = input("Enter code: ").strip()
            url = redirect(c)
            if url:
                print("Original URL:", url)
            else:
                print("No URL found .")

        elif choice == "3":
            print("exiting")
            break

        else:
            print("invalid")