import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

from models import setup_db, Coach , TrainingClass
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)



  @app.route('/')
  def get_home():

    greeting = "Welcome to the Excer Force Gym" 

    return greeting



  #This endpoint return all the training classes information in the database 
  #It requires a get:TrainingClasses permission which the manager and client both has
  @app.route('/TrainingClasses'  , methods=['GET'])
  @requires_auth('get:TrainingClasses')
  def get_TrainingClass(jwt):

    trainingClasses=TrainingClass.query.all()
    trainingClasses_list=[]
    for t_class in trainingClasses:
        trainingClasses_list.append(
            t_class.format())

    return jsonify({
        "success": True, 
        "trainingClasses": trainingClasses_list
    })


  #This endpoint add a training class into the database it requiers a name, description, coach id to associte 
  # with the class, periods and dayes the class will be had
  # it returns the added class id and all the classes information in the database
  #It requires a post:TrainingClasses permission which the manager has
  @app.route('/TrainingClasses'  ,methods=['POST'])
  @requires_auth('post:TrainingClasses')
  def add_TrainingClass(jwt):
    body = dict (request.json)
    name_gotten=body.get('name',None)
    description_gotten=body.get('description',None)
    periods_gotten=body.get('periods',None)
    dayes_gotten=body.get('dayes',None)
    coachId_gotten=body.get('coachId',None)

    print(type(periods_gotten))

    #check if the id of the coach is valid error 404 
    coach=Coach.query.filter_by(id=coachId_gotten).one_or_none()
    if coach is None:
      abort(404)

    try:
        trainingClass= TrainingClass(
          name = name_gotten, 
          coachId = coachId_gotten,
          description = description_gotten,
          periods = periods_gotten,
          dayes = dayes_gotten
        )
        trainingClass.insert()

        trainingClasses=TrainingClass.query.all()
        trainingClasses_list=[]
        for t_class in trainingClasses:
          trainingClasses_list.append(
            t_class.format())
        
        return jsonify(
        {'success': True,
        'added_class': trainingClass.id,
        'trainingClasses': trainingClasses_list
        })
    except:
        abort(422)


  #This endpoint deletes a training class with a specified id 
  #it returns the id of the deleted class and a list of all the classe in the database
  #It requires a delete:TrainingClasses permission which the manager has
  @app.route('/TrainingClasses/<class_id>'  ,methods=['DELETE'])
  @requires_auth('delete:TrainingClasses')
  def delete_TrainingClass(jwt,class_id):

      if(request.method != 'DELETE'):
        abort(405)

      trainingClass=TrainingClass.query.filter_by(id=class_id).one_or_none()
    
      if trainingClass is None:
        abort(404)
      else:
        trainingClass.delete()

      trainingClasses=TrainingClass.query.all()
      trainingClasses_list=[]
      for t_class in trainingClasses:
          trainingClasses_list.append(
            t_class.format())

      return jsonify({
      'success': True,
      'deleted': trainingClass.id,
      'trainingClasses': trainingClasses_list
      })


  #this endpoint updates the periodes and dayes of a training class specified by an id
  #it returns the id of the updated class and a list of all the classe in the database
  #It requires a patch:TrainingClasses permission which the manager has
  @app.route('/TrainingClasses/<class_id>'  ,methods=['PATCH'])
  @requires_auth('patch:TrainingClasses')
  def update_TrainingClass(jwt,class_id):

    if class_id is None:
        abort(404)

    body = request.get_json()
    periods_gotten=body.get('periods',None)
    dayes_gotten=body.get('dayes',None)

    trainingClass=TrainingClass.query.filter_by(id=class_id).one_or_none()
    try:
      trainingClass.periods=periods_gotten
      trainingClass.dayes=dayes_gotten
      trainingClass.update()
    except:
      abort(422)
    
    trainingClasses=TrainingClass.query.all()
    trainingClasses_list=[]
    for t_class in trainingClasses:
          trainingClasses_list.append(t_class.format())


    return jsonify({
      'success': True,
      'patched': trainingClass.id,
      'trainingClasses': trainingClasses_list
      })

  '''
  Coach

  '''
  #This endpoint return all the coaches information in the database 
  ##It requires a get:Coaches permission which the manager and client both has
  @app.route('/Coaches'  ,methods=['GET'])
  @requires_auth('get:Coaches')
  def get_Coach(jwt):
    coaches=Coach.query.all()
    Coaches_list=[]
    for coach in coaches:
        Coaches_list.append(
            coach.format())

    return jsonify({
        "success": True, 
        "coaches": Coaches_list
    })



  # This endpoint add a coach into the database it requiers a name and a description of the coach
  # It returns the added coach id and all the coaches information in the database
  ##It requires a post:Coaches permission which the client has
  @app.route('/Coaches' , methods=['POST'])
  @requires_auth('post:Coaches')
  def add_Coach(jwt):

    body = dict(request.json)
    name_gotten=body.get("name",None)
    description_gotten=body.get("description",None)
    if name_gotten == None:
      abort(422)

    try:
        coach= Coach(name = name_gotten, description = description_gotten)
        coach.insert()
        coaches=Coach.query.all()
        coaches_list=[]
        for t_coach in coaches:
          coaches_list.append( t_coach.format())
        print(111111111)
        return jsonify(
        {'success': True,
        'added_coach': coach.id,
        'coaches': coaches_list
        })
    except:
        abort(422)


  #This endpoint deletes a coach with a specified id 
  #it returns the id of the deleted coach and a list of all the coaches in the database
  #It requires a delete:Coaches permission which the client has
  @app.route('/Coaches/<coach_id>' , methods=['DELETE'])
  @requires_auth('delete:Coaches')
  def delete_Coach(jwt,coach_id):

    if(request.method != 'DELETE'):
        abort(405)
    coach=Coach.query.filter_by(id=coach_id).one_or_none()
    traingingClass=TrainingClass.query.filter_by(coachId=coach_id).one_or_none()

    if coach is None:
        abort(404)
    else:
      if traingingClass is not None:
        traingingClass.delete()
      coach.delete()

    coaches=Coach.query.all()
    coaches_list=[]
    for t_coach in coaches:
       coaches_list.append(t_coach.format())

    return jsonify({
      'success': True,
      'deleted': coach.id,
      'coaches': coaches_list
      })


  #Error handelers

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False, 
      "error": 404,
      "message": "not found"
      }), 404

  @app.errorhandler(405)
  def method_not_allowed(error):
    return jsonify({
      "success": False, 
      "error": 405,
      "message": "method not allowed"
      }), 405

  #https://knowledge.udacity.com/questions/336564
  @app.errorhandler(AuthError)
  def handle_auth_error(ex):
    """
    Receive the raised authorization error and propagates it as response
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

  return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)