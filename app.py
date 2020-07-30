import numpy as np
import pickle
from flask import Flask,request,render_template
 
    
app=Flask(__name__ ,template_folder='templates')
model=pickle.load(open('model.pkl','rb'))
    
@app.route('/' )
def home():
    return render_template('index.html')
    
@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method== 'POST':
        Gender=request.form['Gender']
        if Gender=='Male':
            Gender=1
        else:
            Gender=0
            
        Married=request.form['Married']
        if Married=='Yes':
            Married=1
        else:
            Married=0   
            
        Dependents=request.form['Dependents']
        if Dependents=='0':
            Dependents=2
        elif Dependents=='1':
            Dependents=1
        elif Dependents=='2':
            Dependents=3
        else:    
            Dependents=0
            
        Education=request.form['Education']
        if Education=='Graduate':
            Education=1
        else:
            Education=0     
            
        Self_Employed=request.form['Self_Employed']
        if Self_Employed=='Yes':
            Self_Employed=1
        else:
            Self_Employed=0   
         
        ApplicantIncome=float(request.form['ApplicantIncome'])
        CoapplicantIncome=float(request.form['CoapplicantIncome'])
        LoanAmount=float(request.form['LoanAmount'])
        Loan_Amount_Term=float(request.form['Loan_Amount_Term'])
        Credit_History=float(request.form['Credit_History'])
        
            
        Property_Area=request.form['Property_Area']
        if Property_Area=='Rural':
            Property_Area=0 
        elif Property_Area=='Urban':
            Property_Area=1
        else:
            Property_Area=2
            
        feature=[[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]]
        result=model.predict(feature)
        output=result[0]
        
        if output==1:
            answer='Loan Granted'
        else:
            answer='Loan not Granted'
    
        return render_template('index.html',result=answer)
    
if __name__ == "__main__":
    app.run(debug=True)            