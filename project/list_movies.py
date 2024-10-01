import urllib.request, json


def list_movies(type):
    if type == "popular":
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=05386cb1d615c6912e879632e1d72eaa"
    elif type == "animation":
        url = "https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=05386cb1d615c6912e879632e1d72eaa"
    elif type == "2010":
        url = "https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=05386cb1d615c6912e879632e1d72eaa"

    response = urllib.request.urlopen(url)
    data = response.read()
    data_json = json.loads(data)["results"]
    return data_json
