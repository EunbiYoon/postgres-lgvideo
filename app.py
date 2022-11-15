# CREATE TABLE surveytable (
# 	id serial PRIMARY KEY,
# 	product VARCHAR ( 200 ) NOT NULL,
# 	dealer VARCHAR ( 200 ) NOT NULL,
# 	rating INTEGER NOT NULL,
# 	review TEXT NULL
# );

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Ella135!@localhost/surveydb'
db = SQLAlchemy(app)

class addsurvey(db.Model):
    __tablename__ = 'surveytab3'
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    review = db.Column(db.Text())

    def __init__(self, product, dealer, rating, review):
        self.product = product
        self.dealer = dealer
        self.rating = rating
        self.review = review

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    product = request.form['product']
    dealer = request.form['dealer']
    rating = request.form['rating']
    review = request.form['review']
    print(product, dealer, rating, review)
    
    data = addsurvey(product, dealer, rating, review)
    db.session.add(data)
    db.session.commit()
    return render_template('success.html')

# top loader template render
@app.route('/topnoise')
def topnoise():
    return render_template('tl/noise.html') # do something

@app.route('/topcloth')
def topcloth():  
    return render_template('tl/clothing.html') # do something

@app.route('/topcycle')
def topcycle():         
    return render_template('tl/cycle.html') # do something

@app.route('/topleak')
def topleak():  
    return render_template('tl/leaking.html') # do something

@app.route('/toperror')
def toperror():  
    return render_template('tl/error.html') # do something'

@app.route('/topfill')
def topfill():  
    return render_template('tl/filling.html') # do something

@app.route('/topdrain')
def topdrain():  
    return render_template('tl/drainage.html') # do something

@app.route('/topdispense')
def topdispense():  
    return render_template('tl/dispenser.html') # do something

@app.route('/topdoor')
def topdoor():  
    return render_template('tl/door.html') # do something

@app.route('/toppower')
def toppower():  
    return render_template('tl/power.html') # do something

@app.route('/topsmell')
def topsmell():  
    return render_template('tl/smell.html') # do something

@app.route('/topthinq')
def topthinq():      
    return render_template('tl/thinq.html') # do something


#front loader template render
@app.route('/frontnoise')
def frontnoise():
    return render_template('fl/noise.html') # do something

@app.route('/frontcloth')
def frontcloth():   
    return render_template('fl/clothing.html') # do something

@app.route('/frontcycle')
def frontcycle():         
    return render_template('fl/cycle.html') # do something

@app.route('/fronfleak')
def fronfleak():  
    return render_template('fl/leaking.html') # do something

@app.route('/fronterror')
def fronterror():  
    return render_template('fl/error.html') # do something'

@app.route('/frontfill')
def frontfill():  
    return render_template('fl/filling.html') # do something

@app.route('/frontdrain')
def frontdrain():  
    return render_template('fl/drainage.html') # do something

@app.route('/frontdispense')
def frontdispense():  
    return render_template('fl/dispenser.html') # do something

@app.route('/frontdoor')
def frontdoor():  
    return render_template('fl/door.html') # do something

@app.route('/frontpower')
def frontpower():  
    return render_template('fl/power.html') # do something

@app.route('/frontsmell')
def frontsmell():  
    return render_template('fl/smell.html') # do something

@app.route('/frontthinq')
def frontthinq():      
    return render_template('frontfl/thinq.html') # do something
   

if __name__ == "__main__":
    app.run(debug=True)
