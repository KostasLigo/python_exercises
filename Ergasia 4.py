import requests


tainia = input("Εισάγετε το όνομα της ταινίας: ")
url = "http://www.omdbapi.com/?t=" + tainia
pull = requests.get(url)
pull = pull.json()
print("Οι πληροφορίες για τα βραβεία της ταινίας είναι: " + str(pull['Awards']))
print("Η βαθμολογία της ταινίας είναι: " + str(pull['imdbRating']))
