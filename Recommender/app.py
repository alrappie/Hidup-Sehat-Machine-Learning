from flask import Flask,request,jsonify
from recommendation import Recommendation

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"

@app.route('/predict',methods=['POST'])
def predict():
    data_user = request.get_data()
    # print(json_)
    model = Recommendation(r'D:\Pemrograman\Python\Project\Hidup-Sehat-Machine-Learning\Recommender\database_konten.json',str(data_user))
    return jsonify({'Recommendation':list(model.recomendations())})
    
if __name__ == '__main__':
    app.run(debug=True)