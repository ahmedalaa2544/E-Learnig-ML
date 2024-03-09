from flask import Blueprint,  request
from .sentimentAnalysis_controller import sentiment_analysis
my_blueprint = Blueprint('my_blueprint', __name__)

@my_blueprint.route('/sentimentAnalysis', methods=['POST'])

@my_blueprint.route('/my_route')
def route_handler():
    return sentiment_analysis()