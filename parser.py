# итоговый формат: [текст, "(программа Х класса)" без четверти, балл]

# формат 1: (программа Х класса)
# формат 2: , программа Х класса
# формат 3: , Х класс
# формат 4: , курс математики 5—8 класс

import re


def task_string_to_list(task_text):
    # example task string:
    # Задачи по химическому уравнению, 8 (4 четверть) класс:
    program_text_index = task_text.find("программа")
    if program_text_index == -1:
        first_digit_index = re.search(r"\d", task_text).start()
        program_text_index = first_digit_index
    class_end_text_index = task_text.find("класс") + 6
    task_topic = task_text[:program_text_index - 2].lower()
    if "выполнение действий с числами" in task_topic:
        task_topic = task_topic.replace("выполнение действий с числами", "вычисления")
    if task_topic == "решение задач при помощи уравнений":
        task_topic = "составление уравнений для решения задач"

    task_grade_text = task_text[program_text_index: class_end_text_index]
    quarter_text_index = task_grade_text.find("четверт")
    if quarter_text_index != -1:
        quarter_left_bracket = task_grade_text[: quarter_text_index].rfind("(")
        quarter_right_bracket = task_grade_text[quarter_text_index:].find(")") + quarter_text_index
        task_grade_text = task_grade_text[: quarter_left_bracket - 1] + task_grade_text[quarter_right_bracket + 1:]
    task_grade_text = '(' + task_grade_text + ')'
    return task_topic, task_grade_text

