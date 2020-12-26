import pymorphy2

morph = pymorphy2.MorphAnalyzer()

string_to_tag = {
    'существовать': 1,
    'бывать': 1,
    'какой': 2,
    'вид': 3,
    'тип': 3,
    'привести': 4,
    'пример': 5,
    'командный': 6,
    'индивидуальный': 7,
    'военно-спортивный': 8,
    'интелектуальный': 9,
    'сколько': 10,
    'человек': 11,
    'футбол': 1000,
    'баскетбол': 1001,
    'волейбол': 1002,
    'регби': 1003,
    'хоккей': 1004,
    'теннис': 1005,
    'настольный': 1006,
    'бадминон': 1007,
    'пейнтбол': 1008,
    'шахматы': 1009,
    'шашка': 1010,

}


def getNormalForm(word):
    return morph.parse(word)[0].normal_form


print(getNormalForm('шашки'))

one = (1, 2, 3)
two = (4, 5, 6)
three = (4, 5, 7)
four = (4, 5, 8)
five = (4, 5, 9)
six = (10, 11, 1000)
seven = (10, 11, 1001)
eight = (10, 11, 1002)
nine = (10, 11, 1003)
ten = (10, 11, 1004)

answers = {
    frozenset(
        one): "Спортивные игры делятся на: командные игры, индивидуальные игры, военно-спортивные игры и интелектуаьлные игры",
    frozenset(two): "К командным играм относятся: футбол, волейбол, хоккей, баскетбол и регби",
    frozenset(three): "К индивидуальным играм относятся: теннис, настольный теннис и бадминон",
    frozenset(four): "К военно-спортивным играм относится пейнтбол",
    frozenset(five): "К интелектуаьлным играм относятся: шахматы и шашки",
    frozenset(six): "В команде 11 человек",
    frozenset(seven): "В команде 5 человек",
    frozenset(eight): "В команде 6 человек",
    frozenset(nine): "В команде 15 человек",
    frozenset(ten): "В команде 21 человек",
    # TODO аналогично дополнять ответы и вопросы

}


def transformStringToNormalFormOfWords(str1):
    normal_words = []
    arr = str1.split()
    for word in arr:
        normal_words.append(getNormalForm(word))

    return normal_words


def getTagSet(words):
    tmp_set = set()
    keys = string_to_tag.keys()
    for word in words:
        if word not in keys:
            continue

        tag = string_to_tag[word]
        tmp_set.add(tag)
    return frozenset(tmp_set)


def transformQuestionToTagSet(question):
    if question[-1] == '?':
        question = question[:-1]

    words = transformStringToNormalFormOfWords(question)
    tags = getTagSet(words)
    return tags


def getAnswer(question):
    tags = transformQuestionToTagSet(question)
    keys = answers.keys()
    if tags not in keys:
        return 'Я вас не понимаю'

    return answers[tags]


answer = getAnswer('сколько человек в баскетболе?')
print(answer)
