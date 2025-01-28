# -*- coding: utf-8 -*-
"""

"""

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json



app =FastAPI()


class result_input(BaseModel):
    opp : int
    teams : int
    venues : int
    

#loading the save model

result_model =joblib.load('winning-result (1)','r')


#create api
@app.post('/results')
def result_data(input_parameters : result_input):
    
    input_data =input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    opps=input_dictionary['opp']
    team =input_dictionary['teams']
    venue =input_dictionary['venues']
    
    
    input_list =[opps,team,venue]
    
    prediction = result_model.predict([input_list])
    
    if prediction[0]==0:
        return "Draw"
    elif prediction[0]==1:
        return "Loss"
    else:
        return "wins"




class team_input(BaseModel):
    opp_pos :float
    opp:int
    team_en :int
    res :int
    venue_d:int
    


#loading the save model

team_model =joblib.load('team_position','r')


#create api
@app.post('/teams')
def team_data(input_parameters : team_input):
    
    input_data =input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    opps=input_dictionary['opp_pos']
    opp_ =input_dictionary['opp']
    teams =input_dictionary['team_en']
    result=input_dictionary['res']
    venue =input_dictionary['venue_d']


    
    
    input_list =[opps,opp_,teams,result,venue]
    
    prediction = team_model.predict([input_list])
    return {"predicted_poss":float( prediction[0])}
     

#opponent position
class opp_input(BaseModel):
    poss :float
    opp:int
    team_en :int
    res :int
    venue_d:int
    


#loading the save model

opp_model =joblib.load('oppositional_position','r')


#create api
@app.post('/opponents')
def opp_data(input_parameters : opp_input):
    
    input_data =input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    poss=input_dictionary['poss']
    opp_ =input_dictionary['opp']
    teams =input_dictionary['team_en']
    result=input_dictionary['res']
    venue =input_dictionary['venue_d']


    
    
    input_list =[poss,opp_,teams,result,venue]
    
    prediction = opp_model.predict([input_list])
    return {"predicted_opps":float( prediction[0])}
     

    
