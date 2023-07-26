import time

from flask import Flask,render_template,request
from flask_cors import CORS,cross_origin
from scraper import extractVideoDetails

app = Flask(__name__)


@app.route('/',methods=['GET'])
@cross_origin()
def render():
    return render_template("index.html")

@app.route('/scrap',methods=['GET','POST'])
@cross_origin()
def scrap():
    if request.method == 'POST':
        request_url = request.form['content']
        video_url = request_url
        videoDetails = extractVideoDetails(video_url)
        print(videoDetails)
        return render_template('results.html',videos=videoDetails)


if __name__ =='__main__':
    app.run(debug=True)