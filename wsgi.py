from app.main import app
from app.main import celery

if __name__ == '__main__':

	app.run(debug=True)
