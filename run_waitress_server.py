import os
import sys
from waitress import serve
sys.path.insert(0, './demo')
from demo.wsgi import application

port = os.environ.get('PORT') or 8000
serve(application, host="0.0.0.0", port=port)
