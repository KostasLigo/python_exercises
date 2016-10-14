print("Εισάγετε τις 3 τιμές με τις οποίες θα δουλέψουμε.")
a = input("Καταρχήν εισάγετε την 1η τιμή: ")
a = float(a)
b = input("Την 2η τιμή: ")
b = float(b)
c = input("Και τελικά την 3η τιμή: ")
c = float(c)


def elenhos_trigonou(alfa, vita, gamma):
    if alfa <= 0 or vita <= 0 or c <= 0:
        return -1
    else:
        if (alfa + vita <= gamma) or (alfa + gamma <= vita) or (vita + gamma <= alfa):
            return -1
        else:
            megaliteri = gamma
            if megaliteri < alfa:
                gamma = megaliteri
                megaliteri = alfa
                alfa = gamma
            if megaliteri < vita:
                gamma = megaliteri
                megaliteri = vita
                vita = gamma
            if alfa ** 2 + vita ** 2 > megaliteri * megaliteri:
                return 1
            elif alfa ** 2 + vita ** 2 < megaliteri * megaliteri:
                return 2
            else:
                return 3


print("Σύμφωνα με τις εισαχθέντες τιμές έχουμε τα παρακάτω αποτελέσματα: ")
if elenhos_trigonou(a, b, c) == -1:
    print("Δεν μπορεί να σχηματιστεί τρίγωνο.")
elif elenhos_trigonou(a, b, c) == 1:
    print("Το τρίγωνο είναι οξυγώνιο.")
elif elenhos_trigonou(a, b, c) == 2:
    print("Το τρίγωνο είναι αμβλυγώνιο.")
elif elenhos_trigonou(a, b, c) == 3:
    print("Το τρίγωνο είναι ορθογώνιο.")
