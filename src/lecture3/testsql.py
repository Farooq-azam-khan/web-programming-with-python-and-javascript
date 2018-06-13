from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


engine = create_engine('sqlite:///test.db')
db = scoped_session(sessionmaker(bind=engine))

def create_table_db():
    db.execute('''
        CREATE TABLE user
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR
        );
    ''')
    db.commit()
    
def inser_db():
    db.execute('''
        INSERT INTO user (name) VALUES ("prison mike");
    '''
    )
    db.commit()

def select_db():
    users = db.execute('''
        SELECT * FROM user;
    ''').fetchall()
    
    for user in users:
        print(f'{user.id} | {user.name}')
    
if __name__ == '__main__':
    # create_table_db()
    inser_db()
    select_db()