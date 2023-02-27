from flask import Flask, jsonify, request
from models import get_vacancies

app = Flask(__name__)


@app.route('/get-vacancies-by-query', methods=['POST'])
def get_vacancies_by_query():
    query = request.json['query']
    vacancies = get_vacancies(query)
    response = {
        'vacancies': [],
        'quantity': len(vacancies),
        'query': query,
    }

    for row in vacancies:
        vacancy = {
            'id': row[0],
            'chat_name': row[1],
            'title': row[2],
            'body': row[3],
            'profession': row[4],
            'vacancy': row[5],
            'vacancy_url': row[6],
            'company': row[7],
            'english': row[8],
            'relocation': row[9],
            'job_type': row[10],
            'city': row[11],
            'salary': row[12],
            'experience': row[13],
            'contacts': row[14],
            'time_of_public': str(row[15]),
            'created_at': str(row[16]),
            'agregator_link': row[17],
            'session': row[18],
            'sended_to_agregator': row[19],
            'sub': row[20],
            'tags': row[21],
            'full_tags': row[22],
            'full_anti_tags': row[23],
            'short_session_numbers': row[24],
            'level': row[25],
            'approved': row[26]
        }
        response['vacancies'].append(vacancy)

    return jsonify(response['vacancies'][:10])


if __name__ == '__main__':
    app.run(debug=True)

