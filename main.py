#col break - ascii 9
#em dash - ascii 151
#space - ascii 32
# cr lf - ascii 13 10


from collections import defaultdict


pattern_1 = """Здравствуйте!

По итогам пробного занятия увидели, что [] молодец, отлично справляется с _, но заметили и некоторые пробелы, которые нужно закрыть.

Бывают ошибки при работе с _. Более пристального внимания требуют _.

Самые актуальные для освоения темы – _. В школе, возможно, не хватило практики, нужно повторить.

На занятии [] пока _, но старается, видно, что хочет понять предмет. Мы приложим все усилия и сведём допускаемые ошибки к минимуму. Отработаем и усилим необходимые навыки для успешного освоения школьной программы и получения высоких отметок.

В приоритете будут текущие темы, изучаемые в школе. Но также разберём и более ранний материал, чтобы закрыть пробелы из предыдущих классов. Для достижения лучшего результата отлично подойдут занятия с частотой 2—3 раза в неделю.

Таким образом, в ходе регулярной комплексной работы мы с [] разберёмся не только с тем, что осталось непонятно в классе на данный момент, но и подтянем "хвосты", что, как показывает практика, ведёт к общему улучшению понимания предмета.

Ждём Вас на уроках в нашей школе! :)"""



def test_text_pattern_1(student_name, behavior_notes, test: list):
	test_dict = defaultdict(list)
	for i in test:
		test_dict[i[2]].append([i[0], i[1]])

	res = f"""Здравствуйте!

По итогам пробного занятия увидели, что {student_name} молодец, отлично справляется с {', '.join([i[0] + ' ' + i[1] for i in test_dict[5]])}, но заметили и некоторые пробелы, которые нужно закрыть.

Бывают ошибки при работе с {', '.join([i[0] + ' ' + i[1] for i in test_dict[4]])}. Более пристального внимания требуют {', '.join([i[0] + ' ' + i[1] for i in test_dict[3]])}.

Самые актуальные для освоения темы – {', '.join([i[0] + ' ' + i[1] for i in (test_dict[2] + test_dict[1])])}. В школе, возможно, не хватило практики, нужно повторить.

На занятии {student_name} пока {behavior_notes}, но старается, видно, что хочет понять предмет. Мы приложим все усилия и сведём допускаемые ошибки к минимуму. Отработаем и усилим необходимые навыки для успешного освоения школьной программы и получения высоких отметок.
"""

	if "отвлекается" in behavior_notes:
		res += f"""
Среди прочих нюансов мы также отметили, что вычисления и задачи кажутся {student_name} скучными. Преподаватель будет нацелен на то, чтобы повысить общий интерес к математике, добавить мотивации заниматься. И покажет, что примеры могут быть увлекательными, особенно когда даются без труда, к чему мы со временем непременно придём.
"""
	res += f"""
С началом учебного года в приоритете будут текущие темы, изучаемые в школе. Но также разберём и более ранний материал, чтобы закрыть пробелы из предыдущих классов. Для достижения лучшего результата отлично подойдут занятия с частотой 2—3 раза в неделю.

Таким образом, в ходе регулярной комплексной работы мы с {student_name} разберёмся не только с тем, что осталось непонятно в классе на данный момент, но и подтянем "хвосты", что, как показывает практика, ведёт к общему улучшению понимания предмета.

Ждём Вас на уроках в нашей школе! :)"""


	return res




if __name__=="__main__":
	name = input("Введите имя (обращение) ученика: ").strip()
	sex = input("Введите пол ученика (м/ж): ").strip()
	gender: str
	if sex[0] == 'м' or sex[0] == 'М':
		gender = "male"
	else:
		gender = "female"
	actual_grade = int(input("Введите настоящий класс ученика: "))
	grade = int(input("Введите указанный класс: "))
	exam_prep = input("Вставьте данные из ячейке о подготовке к экзамену: ")
	overall_mark = input("Введите общую оценку: ")
	overall_mark = int(overall_mark) if overall_mark else 0
	behavior_notes = input("Вставьте общие моменты: ")
	comments = input("Вставьте комментарии: ")

	solved_test = 'да' == input("Решали ли пробный тест? ").lower()
	if solved_test:
		questions_num = int(input("Сколько заданий решили? "))
		test = []  # [текст, "(программа Х класса)" без четверти, балл]
		input()
		for task in range(questions_num):
			task_text = input()
			task_mark = int(input()[0])
			program_text_index = task_text.find("программа")
			class_end_text_index = task_text.find("класса") + 6
			task_topic = task_text[:program_text_index - 2].lower()
			if "выполнение действий с числами" in task_topic:
				task_topic = task_topic.replace("выполнение действий с числами", "вычисления")
			if task_topic == "решение задач при помощи уравнений":
				task_topic = "составление уравнений для решения задач"

			task_grade = task_text[program_text_index : class_end_text_index]
			quarter_text_index = task_grade.find("четверт")
			if quarter_text_index != -1:
				quarter_left_bracket = task_grade[: quarter_text_index].rfind("(")
				quarter_right_bracket = task_grade[quarter_text_index :].find(")") + quarter_text_index
				task_grade = task_grade[: quarter_left_bracket - 1] + task_grade[quarter_right_bracket + 1 :]
			task_grade = '(' + task_grade +')'

			test.append([task_topic, task_grade, task_mark])
		print(test_text_pattern_1(name, behavior_notes, test))