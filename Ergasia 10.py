title = input("Παρακαλώ εισάγετε τον τίτλο: ")
title = title.title()
title = title.split()
lexeis_odigoi = []
prompt = "Εισάγετε τις λέξεις οδηγούς μια προς μια πατώντας enter κάθε φορά."
prompt += "Εισάγετε το γράμμα 'q' για να τερματήσετε την εισαγωγή: "
while True:
    lexi = input(prompt)
    if lexi == 'q':
        break
    else:
        lexeis_odigoi.append(lexi.title())


def title_case(titlos, odigoi):
    """
     Συνάρτηση για επιστροφή title case με
     εξαιρέσεις τις λέξεις οδηγούς.
    """
    for odigos in odigoi:
        for diktis, lexi in enumerate(titlos):
            if lexi.upper() == odigos.upper() and diktis != 0:
                titlos[diktis] = lexi.lower()


title_case(title, lexeis_odigoi)
print("Ο τίτλος σας σε titlecase είναι: ")
for item in title:
    print(item, end=" ")
