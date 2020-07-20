"""
A Basic Flask API for creating,reading,upadting and deleting (CRUD)
movie info
"""

#importing Flask and other required libraries
from flask import Flask,jsonify,abort,make_response,request

#creating a Flask app instance
app = Flask(__name__)

movies=[    {
        'id':1,
        'name':'titanic',
        'genre':'romance',
        'rating':9,
        'director':'james cameron',
        'year':1997

    }
]



#read
@app.route('/movies/list',methods=['GET'])
def movie_list():
    return jsonify({'movies':movies})

@app.route('/movies/<int:m_id>',methods=['GET'])
def get_movie(m_id):
    movie=[movie for movie in movies if movie['id']==m_id]
    if len(movie)==0:
        abort(404)
    return jsonify(movie)

#create
@app.route('/movies/list',methods=['POST'])
def add_movie():
    if not request.json or not 'name' in request.json:
        abort(400)
    movie={
        'id': movies[-1]['id']+1,
        'name': request.json['name'],
        'genre': request.json['genre'],
        'rating': request.json['rating'],
        'director': request.json['director'],
        'year': request.json['year']
    }
    movies.append(movie)
    return jsonify({'movie':movie}),201

#update
@app.route('/movies/<int:m_id>',methods=['PUT'])
def upadte_movie(m_id):
    movie=[movie for movie in movies if movie['id']==m_id]
    if len(movie) == 0:
        abort(404)
    if not request.json:
        abort(400)

    movie[0]['name']=request.json.get('name',movie[0]['name'])
    movie[0]['genre'] = request.json.get('genre', movie[0]['genre'])
    movie[0]['rating'] = request.json.get('rating', movie[0]['rating'])
    movie[0]['director'] = request.json.get('director', movie[0]['director'])
    movie[0]['year'] = request.json.get('year', movie[0]['year'])
    return (jsonify({'movie':movie[0]}))

#delete
@app.route('/movies/<int:m_id>',methods=['DELETE'])
def delete_movie(m_id):
    movie=[movie for movie in movies if movie['id']==m_id]
    if len(movie)==0:
        abort(404)
    movies.remove(movie[0])
    return jsonify({'movies':movies})

#error handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)



if __name__ == '__main__':
    app.run(debug=True)