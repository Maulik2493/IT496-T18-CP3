#import library
import uvicorn
from fastapi import FastAPI
from batting_model import batting_model
import numpy as np
import pickle
import pandas as pd

#create the app object
app=FastAPI()
pickle_model=open("model_bat.pkl","rb")
model=pickle.load(pickle_model)
Encoded_list = pd.read_pickle('./Encoded_list.pkl')


# for index , row in Encoded_list.iterrows():
#     print(row['Player'])
#     print(row['Encoded_Player'])



def get_encoded_player(Player):
    for index , row in Encoded_list.iterrows() :
        if(row['Player']==Player):
            return row['Encoded_Player']
    return "None"

def get_encoded_country(Country):
    for index , row in Encoded_list.iterrows():
        if(row['Country']==Country):
            return row['Encoded_Country']
    return "None"

def get_player_country(Player):
    for index , row in Encoded_list.iterrows():
        if(row['Player']==Player):
            return row['Encoded_Country']
    return "None"


#default route
@app.get('/')
def index():
    return{"message":"Hello IDM Students"}

#default route
@app.get('/api-demo')
def index():
    return{"message":"This is demo API"}

#Prediction Function, return the predicted result in JSON
@app.post('/predict')
def predict(data:batting_model):
    # convert data obj to dictionary
    data=dict(data)
    Player = data['Player']
    Opponent = data['Opponent_Country']

    #prediction
    if((get_encoded_player(Player)!="None") & (get_encoded_country(Opponent)!="None") & (get_encoded_country(Opponent)!=get_player_country(Player))):

        runs = model.predict([[get_encoded_player(Player),get_player_country(Player),get_encoded_country(Opponent),1]])
    # print(f'The player {Player} will score {runs} runs against {Opponent}.')
    #return probability

        prediction = f'{Player} will score {int(runs)} runs against {Opponent}'
    else :
        prediction='Invalid Input'
    return {
        'prediction': prediction
    }

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    

#Command to run API server   
#python -m uvicorn main:app --reload
