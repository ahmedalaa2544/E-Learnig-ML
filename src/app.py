from flask import Flask, render_template
import os
from tensorflow.keras.models import load_model
from modules.sentimentAnalysis.sentimentAnalysis_controller import set_sentiment_analysis_model
from modules.sentimentAnalysis.sentimentAnalysis_router import my_blueprint



app = Flask(__name__)
app.config['PORT'] = os.environ.get('PORT', 3000)
# model= load_model("sentiment_analysis_comments_2.hdf5")

# with app.app_context():
#     set_sentiment_analysis_model(model)

# Register Blueprint
app.register_blueprint(my_blueprint, url_prefix='/model')
@app.route('/')
def render_dummy_page():
    return "ahmed"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))

    app.run(debug=True, port= port)
