import json


def load_students(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def load_professions(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_student_by_pk(pk, data):
    for item in data:
        if pk == item['pk']:
            return item


def get_profession_by_title(title, data):
    for item in data:
        if title == item['title']:
            return item


def check_fitness(student, profession):
    set_student = set(student["skills"])
    set_profession = set(profession["skills"])

    has_skills = set_student.intersection(set_profession)
    lacks_skills = set_profession.difference(set_student)

    fit_percent = round(len(has_skills) / len(set_profession) * 100)

    dict_result = {
        'has': has_skills,
        'lacks': lacks_skills,
        'fit_percent': fit_percent,
    }

    return dict_result


def show_results(data, name):
    str_has = ', '.join(data['has'])
    str_lack = ', '.join(data['lacks'])
    str_output = f'Пригодность {data["fit_percent"]} \n' \
                 f'{name} знает {str_has} \n' \
                 f'{name} не знает {str_lack}\n'
    return str_output
