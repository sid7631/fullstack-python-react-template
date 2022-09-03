from asyncio.log import logger
import logging
from flask import Blueprint, request
import logging

api = Blueprint('api', __name__, url_prefix='/api')

logger = logging.getLogger(__name__)

@api.route('/demo', methods=['POST', 'GET'])
def demo():
    if request.method == 'GET':
        return 'demo api', 200
