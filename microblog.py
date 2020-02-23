from app import app, db
from app.models import User, Post


#################################
### flask shell ###

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User': User, 'Post':Post}

### Main Part ###

if __name__ == '__main__':
    app.run(debug=True) 