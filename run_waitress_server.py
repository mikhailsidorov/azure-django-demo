import os
import sys
from waitress import serve  
sys.path.insert(0, './demo')
from demo.wsgi import application

serve(application, host="0.0.0.0", port=os.environ["PORT"])