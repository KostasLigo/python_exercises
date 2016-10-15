# Αυτός ο αριθμός θα μας δωθεί σαν user input.
arithmos = input("Παρακαλώ εισάγετε έναν ακέραιο αριθμό: ")
arithmos = int(arithmos)


def einai_tetragono_akeraiou(user_number):
    """
    Boolean return για έλεγχο άμα ο αριθμός που εισήχθηκε από τον χρήστη είναι
    τετράγωνο ακεραίου.
    """
    if user_number == 0 or user_number == 1:
        return True
    else:
        temp = user_number // 2
        einai = [temp]
        while temp * temp != user_number:
            temp = (temp + (user_number // temp)) // 2
            if temp in einai:
                return False
            einai.append(temp)
        return True


print("Ο αριθμός που εισάγατε είναι ο: " + str(arithmos))
print("Ο αριθμός αυτός είναι τετράγωνο ακεραίου: " + str(einai_tetragono_akeraiou(arithmos)))
