from flask import Flask,request,jsonify
from recommendation import Recommendation

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    data_user = request.get_json(force=True)
    text = data_user['text']
    model = Recommendation(r'D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\Recommender\dataset\database_konten_fixed.json',str(text))
    # model = Recommendation(r'app/api/data/database_blog.json',str(data_user))
    recommendations = list(model.recomendations().itertuples(index=False, name=None))
    recommendation_list = [{'key': rec[0], 'title': rec[1]} for rec in recommendations]
    return {'Recommendation': recommendation_list}
    # print(hasil.to_json(orient='records'))

    # return jsonify({'Recommendation':list(hasil)})
    
if __name__ == '__main__':
    app.run(debug=True)