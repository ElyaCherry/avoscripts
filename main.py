# col break - ascii 9
# em dash - ascii 151
# space - ascii 32
# cr lf - ascii 13 10

from report import *

import parser


if __name__ == "__main__":
	name = input("Введите имя (обращение) ученика: ").strip()
	sex = input("Введите пол ученика (м/ж): ").strip()
	gender: str
	if sex[0] == 'м' or sex[0] == 'М':
		gender = "male"
	else:
		gender = "female"
	student = Student(name, gender)
	# actual_grade = int(input("Введите настоящий класс ученика: "))
	# grade = int(input("Введите указанный класс: "))
	# exam_prep = input("Вставьте данные из ячейки о подготовке к экзамену: ")
	# overall_mark = input("Введите общую оценку: ")
	# overall_mark = int(overall_mark) if overall_mark else 0
	behavior_notes = input("Вставьте общие моменты: ")

	solved_test = 'да' == input("Решали ли пробный тест? (Введите \"да\") ").lower()
	if solved_test:
		questions_num = int(input("Сколько заданий решили? "))
		test = []  # формат: [текст, "(программа Х класса)" без четверти, балл]
		print("Скопируйте из таблицы все ячейки решенных заданий и вставьте сюда без изменений")
		input()
		for task in range(questions_num):
			task_text = input()
			task_mark = int(input()[0])
			task_topic, task_grade = parser.task_string_to_list(task_text)

			test.append([task_topic, task_grade, task_mark])
		print(test_text_pattern_1(student, behavior_notes, test))

	else:
		print("Напишите отзыв вручную.")
