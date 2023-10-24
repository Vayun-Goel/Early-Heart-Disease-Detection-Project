from flask import Flask,render_template,request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
app=Flask(__name__)

df=pd.read_csv("/Users/vayungoel/Desktop/ml_flask/CVD_cleaned.csv")
temp=df.to_numpy()
for i in range(len(temp)):
  if(temp[i][10]!="80+"):
    t=(int(temp[i][10][3:])+int(temp[i][10][:2]))/2
    temp[i][10]=t
  else:
    temp[i][10]=int(85)
columns=df.columns
df=pd.DataFrame(temp,columns=columns)
df_new=df[['Age_Category','BMI','Alcohol_Consumption','Fruit_Consumption','Green_Vegetables_Consumption']].copy()
df_filtered = df_new[df_new['BMI'] <= 50]
df_filtered = df_filtered[df_filtered['BMI'] >= 15]
x=df_filtered.to_numpy()
scaler1 = StandardScaler()
scaler1.fit(x)

model=pickle.load(open('/Users/vayungoel/Desktop/ml_flask/model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template('project.html')

@app.route('/products')
def product_review():
    return 'this is a product'

@app.route('/predict',methods=['POST'])
def predict():
    x=[[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]]
    columns1 = ['Exercise', 'Skin_Cancer', 'Other_Cancer','Depression', 'Diabetes', 'Arthritis', 'Sex', 'Smoking_History']
    for i in range(len(columns1)):
       x[0][i]=int(request.form.get(columns1[i]))
    General_Health=int(request.form.get('General_Health'))
    x[0][8+General_Health]=1
    Checkup=int(request.form.get('Checkup'))
    x[0][13+Checkup]=1
    columns2=['Age_Category', 'BMI', 'Alcohol_Consumption', 'Fruit_Consumption','Green_Vegetables_Consumption']
    a=[[0.0,0.0,0.0,0.0,0.0]]
    for i in range(len(columns2)):
       a[0][i]=request.form.get(columns2[i])
    a=scaler1.transform(a)
    for i in range(len(columns2)):
       x[0][18+i]=a[0][i]

    y=model.predict(x)[0]
    if(y==0):
       return render_template("predict_negative.html")
    else:
       return render_template("predict_positive.html")


if __name__ == "__main__":
    app.run(debug=True)