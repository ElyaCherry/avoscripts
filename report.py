from collections import defaultdict
import pymorphy2
from pyphrasy.inflect import PhraseInflector


class Student:
    def __init__(self, _name, _gender, _actual_grade=0):
        self.name = _name
        self.gender = _gender
        self.actual_grade = _actual_grade

    def inflect_name(self):
        pass  # TODO


def test_text_pattern_1(student: Student, behavior_notes, test: list):
    test_dict = defaultdict(list)
    for i in test:
        test_dict[i[2]].append([i[0], i[1]])

    if len(test_dict[5]) == 0:
        return test_text_pattern_2(student, behavior_notes, test)

    morph = pymorphy2.MorphAnalyzer()
    inflector = PhraseInflector(morph)
    name_tvor = morph.parse(student.name)[0].inflect({'ablt'}).word.capitalize()
    name_dat = morph.parse(student.name)[0].inflect({'datv'}).word.capitalize()

    great_text = "справляется с " + ', '.join([inflector.inflect(i[0], 'ablt') + ' ' + i[1] for i in test_dict[5]]) if len(test_dict[5]) < 5 else "понимает большую часть программы по математике"

    res = f"""Здравствуйте!

По итогам пробного занятия увидели, что {student.name} молодец, отлично {great_text}, но заметили и некоторые пробелы, которые нужно закрыть.

Бывают ошибки при работе с {', '.join([inflector.inflect(i[0], 'ablt') + ' ' + i[1] for i in test_dict[4]])}. Более пристального внимания {"требуют" if len(test_dict[3]) > 1 else "требует"} {', '.join([i[0] + ' ' + i[1] for i in test_dict[3]])}.

{"Самые актуальные для освоения темы" if len(test_dict[2] + test_dict[1]) > 1 else "Самая актуальная для освоения тема"} – {', '.join([i[0] + ' ' + i[1] for i in (test_dict[2] + test_dict[1])])}. В школе, возможно, не хватило практики, нужно повторить. """

    res += f"""
Преподаватель всё подробно разберёт{", напомнит все нужные формулы" if "польз" in behavior_notes else ""} и закрепит тщательной отработкой{", а также поработает над пониманием формулировок, чтобы исключить неточности в интерпретации условий разных заданий" if "формули" in behavior_notes else ""}.
"""

    behavior_text = ""
    behavior_list = []
    if "медл" in behavior_notes:
        behavior_list.append("медленно считает")
    if "неув" in behavior_notes:
        behavior_list.append("боится допустить ошибку")
    if "часто" in behavior_notes or "путает" in behavior_notes:
        behavior_list.append("ошибается по невнимательности")
    if behavior_list:
        behavior_text = ", ".join(behavior_list)
        behavior_text = "пока " + behavior_text + ", но"
    else:
        behavior_text = "очень"

    res += f"""
На занятии {student.name} {behavior_text} старается, видно, что хочет понять предмет. Мы приложим все усилия и сведём допускаемые ошибки к минимуму. Выработаем и усилим необходимые навыки для успешного освоения школьной программы и получения высоких отметок.
"""

    if "отвлекается" in behavior_notes:
        res += f"""
Среди прочих нюансов мы также отметили, что вычисления и задачи кажутся {name_dat} скучными. Преподаватель будет нацелен на то, чтобы повысить общий интерес к математике, добавить мотивации заниматься. И покажет, что примеры могут быть увлекательными, особенно когда даются без труда, к чему мы со временем непременно придём.
"""

    res += f"""
В приоритете будут текущие темы, изучаемые в школе. Но также разберём и более ранний материал, чтобы закрыть пробелы из предыдущих классов. Для достижения лучшего результата отлично подойдут занятия с частотой 2—3 раза в неделю.

Таким образом, в ходе регулярной комплексной работы мы с {name_tvor} разберёмся не только с тем, что осталось непонятно в классе на данный момент, но и подтянем «хвосты», что, как показывает практика, ведёт к общему улучшению понимания предмета.

Ждём вас на уроках в нашей школе! :)"""

    return res


def test_text_pattern_2(student: Student, behavior_notes, test: list):
    test_dict = defaultdict(list)
    for i in test:
        test_dict[i[2]].append([i[0], i[1]])

    morph = pymorphy2.MorphAnalyzer()
    inflector = PhraseInflector(morph)
    name_tvor = morph.parse(student.name)[0].inflect({'ablt'}).word.capitalize()
    name_dat = morph.parse(student.name)[0].inflect({'datv'}).word.capitalize()

    good_text = "справляется с " + ', '.join([inflector.inflect(i[0], 'ablt') + ' ' + i[1] for i in test_dict[4]])

    res = f"""Здравствуйте!

По итогам пробного занятия увидели, что {student.name} молодец, хорошо {good_text}, иногда допускает ошибки, но это будет легко исправить. Так же, как и с другими темами, с которыми сейчас возникает больше сложностей.

Есть ошибки при работе с {', '.join([inflector.inflect(i[0], 'ablt') + ' ' + i[1] for i in test_dict[3]])}. Более пристального внимания {"требуют" if len(test_dict[2]) > 1 else "требует"} {', '.join([i[0] + ' ' + i[1] for i in test_dict[2]])}.

{"Самые актуальные для освоения темы" if len(test_dict[1]) > 1 else "Самая актуальная для освоения тема"} – {', '.join([i[0] + ' ' + i[1] for i in (test_dict[1])])}. В школе, возможно, не хватило практики, нужно повторить. """

    res += f"""
Преподаватель всё подробно разберёт{", напомнит все нужные формулы" if "польз" in behavior_notes else ""} и закрепит тщательной отработкой{", а также поработает над пониманием формулировок, чтобы исключить неточности в интерпретации условий разных заданий" if "формули" in behavior_notes else ""}.
"""

    behavior_text = ""
    behavior_list = []
    if "медл" in behavior_notes:
        behavior_list.append("медленно считает")
    if "неув" in behavior_notes:
        behavior_list.append("боится допустить ошибку")
    if "часто" in behavior_notes or "путает" in behavior_notes:
        behavior_list.append("ошибается по невнимательности")
    if behavior_list:
        behavior_text = ", ".join(behavior_list)
        behavior_text = "пока " + behavior_text + ", но"
    else:
        behavior_text = "очень"

    res += f"""
На занятии {student.name} {behavior_text} старается, видно, что хочет понять предмет. Мы приложим все усилия и сведём допускаемые ошибки к минимуму. Выработаем и усилим необходимые навыки для успешного освоения школьной программы и получения высоких отметок.
"""

    if "отвлекается" in behavior_notes:
        res += f"""
Среди прочих нюансов мы также отметили, что вычисления и задачи кажутся {name_dat} скучными. Преподаватель будет нацелен на то, чтобы повысить общий интерес к математике, добавить мотивации заниматься. И покажет, что примеры могут быть увлекательными, особенно когда даются без труда, к чему мы со временем непременно придём.
"""

    res += f"""
В приоритете будут текущие темы, изучаемые в школе. Но также разберём и более ранний материал, чтобы закрыть пробелы из предыдущих классов. Для достижения лучшего результата отлично подойдут занятия с частотой 2—3 раза в неделю.

Таким образом, в ходе регулярной комплексной работы мы с {name_tvor} разберёмся не только с тем, что осталось непонятно в классе на данный момент, но и подтянем «хвосты», что, как показывает практика, ведёт к общему улучшению понимания предмета.

Ждём вас на уроках в нашей школе! :)"""

    return res


class Report:
    def __init__(self, _student: Student, _subject, ):
        self.student = _student
        self.subject = _subject
        self.oge_peresdacha = False
        self.oge_prep = False
        self.ege_prep = False
        self.college = False

    # scenarios:
    # all 5 - занятия 1-2 раза в неделю
    # all 4 and 5 - занятия 1-2 раза в неделю
    # all 1-3 - есть остаточные знания
    # all


