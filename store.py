store = {
"bananasss" : 1,
"yogurt" : 2,
"milk" : 3,
"cheerios!" : 2
}

for key, val in store.items():
    p_str = "{:<20}{:<20}{:<20}".format(key,str(val), "hi")
    print(p_str)

hello_dict = {
"French" : "Bonjour",
"Spanish" : "Hola",
"German" : "Guten tag"
}

goodbye_dict = {
"French" : "Au Revoir",
"Spanish" : "Adios",
"German" : "Aufweidersen"
}

word_to_dict = {
"hello" : hello_dict,
"goodbye" : goodbye_dict
}

for word in word_to_dict:
    print("Word: " + word)
    word_dict = word_to_dict[word]
    for key, val in word_dict.items():
        print(key + " " + val)
