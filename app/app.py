from flask import Flask, jsonify, request
import requests
import json

app = Flask(__name__)


def get_vacancies_by_query_flask(query):
    url = "http://1118013-cw00061.tw1.ru:5000/get-vacancies-by-query"
    data = {"query": query}
    response = requests.post(url, json=data)
    try:
        vacancies_data = response.json()
    except json.JSONDecodeError:
        vacancies_data = {}
    return vacancies_data.get('vacancies', [])



@app.route('/get-vacancies-by-query', methods=['POST'])
def get_vacancies_by_query():

    request_data = request.get_json()


    query = "WHERE 1=1"
    if 'profession' in request_data and request_data['profession']:
        query += f" AND profession IN {tuple(request_data['profession'])}"
    if 'direction' in request_data and request_data['direction']:
        query += f" AND direction IN {tuple(request_data['direction'])}"
    if 'specialization' in request_data and request_data['specialization']:
        query += f" AND specialization IN {tuple(request_data['specialization'])}"
    if 'city' in request_data and request_data['city']:
        query += f" AND city IN {tuple(request_data['city'])}"
    if 'salary' in request_data and request_data['salary']:
        query += f" AND salary IN {tuple(request_data['salary'])}"
    if 'experience' in request_data and request_data['experience']:
        query += f" AND experience IN {tuple(request_data['experience'])}"
    if 'english' in request_data and request_data['english']:
        query += f" AND english IN {tuple(request_data['english'])}"
    if 'relocation' in request_data and request_data['relocation']:
        query += f" AND relocation IN {tuple(request_data['relocation'])}"
    if 'job_type' in request_data and request_data['job_type']:
        query += f" AND job_type IN {tuple(request_data['job_type'])}"
    if 'tags' in request_data and request_data['tags']:
        query += f" AND tags IN {tuple(request_data['tags'])}"
    if 'full_tags' in request_data and request_data['full_tags']:
        query += f" AND full_tags IN {tuple(request_data['full_tags'])}"
    if 'full_anti_tags' in request_data and request_data['full_anti_tags']:
        query += f" AND full_anti_tags IN {tuple(request_data['full_anti_tags'])}"
    if 'level' in request_data and request_data['level']:
        query += f" AND level IN {tuple(request_data['level'])}"
    if 'approved' in request_data and request_data['approved']:
        query += f" AND approved IN {tuple(request_data['approved'])}"


    vacancies_data = get_vacancies_by_query_flask(query)


    response_data = {
        "vacancies": vacancies_data
    }
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)

