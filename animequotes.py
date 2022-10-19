import requests

# this function formats a quote
def format_quote(data):
    print(data['quote'] + " \n- " + data['character'] + " (" + data['anime'] + ")" +  "\n ")
    

# here i fetch random quote from anime
response = requests.get("https://animechan.vercel.app/api/random").json()
format_quote(response)

# here i fetch two random quotes from naruto
response = requests.get("https://animechan.vercel.app/api/quotes/anime?title=naruto").json()[:2]
for q in response:
    format_quote(q)

# here i fetch quote from my favorite anime character KANEKI KEN(literally me)
response = requests.get("https://animechan.vercel.app/api/quotes/character?name=kaneki").json()[2]
format_quote(response)
