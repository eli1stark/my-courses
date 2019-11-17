# Can`t fix problem in function "sentences" like that: ["Mike", "London...", "Dog...", "Hey!", "Me."]
# Should be: ["Mike London... Dog... Hey!", "Me."]


def lines(a, b):
    """Return lines in both a and b"""

    # FILE 1
    # make list to store lines
    storage_1 = []

    # decompose file to single chars
    file_1 = list(a)

    line_1 = ""

    # store each line in list
    for i in range(len(file_1)):
        line_1 = line_1 + file_1[i]
        check_1 = file_1[i]
        if check_1 == "\n":
            storage_1.append(line_1)
            line_1 = ""
    storage_1.append(line_1)

    # FILE 2
    # make list to store lines
    storage_2 = []

    # decompose file to single chars
    file_2 = list(b)

    line_2 = ""

    # store each line in list
    for i in range(len(file_2)):
        line_2 = line_2 + file_2[i]
        check_2 = file_2[i]
        if check_2 == "\n":
            storage_2.append(line_2)
            line_2 = ""
    storage_2.append(line_2)

    # remove extra \n values in both lists
    storage_1 = [element.replace('\n', '') for element in storage_1]
    storage_2 = [element.replace('\n', '') for element in storage_2]


    # declare storage
    storage = []

    # compare two lists and store similar lines in own list
    for i in range(len(storage_1)):
        for t in range(len(storage_2)):
            if storage_1[i] == storage_2[t]:
                if storage_1[i] in storage:
                    continue
                else:
                    storage.append(storage_1[i])

    return storage


def sentences(a, b):
    """Return sentences in both a and b"""

    # FILE 1
    # make list to store senteces
    storage_1 = []

    # decompose file to single chars
    file_1 = list(a)

    line_1 = ""

    # variables to prevent IndexError: list index out of range when I solve problem with mid sentences
    length_1 = len(file_1)
    index_1 = 0

    # variable to solve problem with
    counter_1 = 0

    # store each sentence in list
    for i in range(len(file_1)):
        index_1 += 1
        counter_1 = 0
        line_1 = line_1 + file_1[i]
        check_1 = file_1[i]
        # condition to solve "..." problem
        if index_1 < length_1:
            check_1_1 = file_1[i + 1]
            if check_1 == check_1_1:
                counter_1 += 1
                continue
            if counter_1 == 1:
                continue
        if check_1 == "\n" or check_1 == "?" or check_1 == "!" or check_1 == "." or check_1 == ";":
            storage_1.append(line_1)
            line_1 = ""
    storage_1.append(line_1)

    # if last sentence ends without any symbol, I get extra element: "", the code below fixs this problem
    if storage_1[-1] == "":
        del storage_1[-1]

    # remove extra spaces
    for i in range(len(storage_1)):
        if storage_1[i].startswith(" "):
            storage_1[i] = storage_1[i][1:]

    # remove single \n values
    list1 = [i for i in storage_1 if i != '\n']

    # remove \n values in string
    list_1 = [element.replace('\n', '') for element in list1]

    # FILE 2
    # make list to store senteces
    storage_2 = []

    # decompose file to single chars
    file_2 = list(b)

    line_2 = ""

    # variables to prevent IndexError: list index out of range when I solve problem with mid sentences
    length_2 = len(file_2)
    index_2 = 0

    # variable to solve problem with
    counter_2 = 0

    # store each sentence in list
    for i in range(len(file_2)):
        index_2 += 1
        counter_2 = 0
        line_2 = line_2 + file_2[i]
        check_2 = file_2[i]
        # condition to solve "..." problem
        if index_2 < length_2:
            check_2_2 = file_2[i + 1]
            if check_2 == check_2_2:
                counter_2 += 1
                continue
            if counter_2 == 1:
                continue
        if check_2 == "\n" or check_2 == "?" or check_2 == "!" or check_2 == "." or check_2 == ";":
            storage_2.append(line_2)
            line_2 = ""
    storage_2.append(line_2)

    # if last sentence ends without any symbol, I get extra element: "", the code below fixs this problem
    if storage_2[-1] == "":
        del storage_2[-1]

    # remove extra spaces
    for i in range(len(storage_2)):
        if storage_2[i].startswith(" "):
            storage_2[i] = storage_2[i][1:]

    # remove single \n values
    list2 = [i for i in storage_2 if i != '\n']

    # remove \n values in string
    list_2 = [element.replace('\n', '') for element in list2]

    # declare storage for similar sentences
    storage = []

    # compare two lists and store similar sentences in storage (new list)
    for i in range(len(list_1)):
        for t in range(len(list_2)):
            if list_1[i] == list_2[t]:
                if list_1[i] in storage:
                    continue
                else:
                    storage.append(list_1[i])

    return storage


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # How it works?
    # string = "Shellys"
    # string = 7
    # n = length of pv | pv = quantity of possible values
    # n = 1 pv = 7
    # n = 2 pv = 6
    # n = 3 pv = 5
    # n = 4 pv = 4
    # n = 5 pv = 3
    # n = 6 pv = 2
    # n = 7 pv = 1

    # FILE 1
    # length of string
    length_1 = len(a)

    # formula for pv
    num_1 = n - 1
    pv_1 = length_1 - num_1

    # declare end of value
    j = n

    # declare list to store pv
    pv_storage_1 = []

    # go through all possible values and append them to list
    for i in range(pv_1):
        pv_storage_1.append(a[i:j])
        j += 1

    # remove single \n values
    pv_storage_1 = [i for i in pv_storage_1 if i != '\n']

    # remove \n values in string
    pv_storage_1 = [element.replace('\n', '') for element in pv_storage_1]

    # FILE 2
    # length of string
    length_2 = len(b)

    # formula for pv
    num_2 = n - 1
    pv_2 = length_2 - num_2

    # declare end of value
    j = n

    # declare list to store pv
    pv_storage_2 = []

    # go through all possible values and append them to list
    for i in range(pv_2):
        pv_storage_2.append(b[i:j])
        j += 1

    # remove single \n values
    pv_storage_2 = [i for i in pv_storage_2 if i != '\n']

    # remove \n values in string
    pv_storage_2 = [element.replace('\n', '') for element in pv_storage_2]

    # declare storage for similar sentences
    storage = []

    # compare two lists and store similar sentences in storage (new list)
    for i in range(len(pv_storage_1)):
        for t in range(len(pv_storage_2)):
            if pv_storage_1[i] == pv_storage_2[t]:
                if pv_storage_1[i] in storage:
                    continue
                else:
                    storage.append(pv_storage_1[i])

    return storage