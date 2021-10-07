
import os
import unittest
import json
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, TrainingClass, Coach



class GymTestCase(unittest.TestCase):
    """This class represents the gym test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "gym_test"
        self.database_path = "postgresql://rznjnhznkyrokd:464a3ad615c337bc249a2e346c63dd20ef4c304e2a6321bb5418350c0c858406@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d1nui7mnbvq7vc"
        self.t_client = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGRlNTdjNjllYjIwMDcwNGJmY2UzIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNTg4OTIwLCJleHAiOjE2MzM2NzUzMjAsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiXX0.Omdl0vsrahv9RJo9J4IuvXpFH0LZTfSd_AeaMqRyYRFI-Z8g7jEemlVefIBZV0Dykuc1KfBD8QaFqhUvK1ZhK5DpZky2rhwX2vSYh4tz101Anx_TeDhb5BPUCHu06j8AZZXIIhKTafHiQpALJKCSwZTaryHE-9YLc_Gin9JRcAB3LImCCK3SvWO-advF6s8xGYbygJHixjRjlD89LJ4lUPmZfT0EM-t4rhmpDvzdRlAx4kwi0zmr92KaVX3rPTe6WmefzEky60cmn29mRMLBPmbrUtxd4tgY362V86oppnMxgLPgFrMqJC0ov8OuseaxTGqlrcAU3KSujz4qj1JvOw' 
        self.t_prod = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        self.t_managment = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNTg4MTcyLCJleHAiOjE2MzM2NzQ1NzIsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.g-FhdX4Vgb_utuM9oTPTVdmR0l9JjwlNDxT0CrH8czptht3RmolhR5GpOEXxU6762hteKB1L5yd3fRSzpaKwxq-oBEMhhH6lRjIwr8bzSwJEogJRm9VOWGf60KN-_S1dFa37A52vWKjJrJHeF99LsfNlCpCJXk8BHJ8yWCfnB_x1oTt2fnFQ3ubkOLrmntoc-WK8HuQjKhSu80KyeAejfU1hsUWKF6GGCQR3QJgVsd67p6OLSqHnnOj86KJCibmCUs1U9R2G59_Olg_7qHfZ9obOrxZuX2UDDjLoc8XjzBVDo5SerG08IZJUnrk1gSB4memT3dKj9ce2zKfCM_nmFQ'
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    

    def new_trainingClass(self):
        return jsonify({
            'name':'zumba2',
            'coachId':'1',
            'description':'a zumba class',
            'periods':['1','3'],
            'dayes':['sat','wed']
        })
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


    def test_get_trainingClasses_as_user(self):
        res=self.client().get('/TrainingClasses'
        ,headers={'Authorization':'Bearer ' +self.t_client}
        ) #the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['trainingClasses'])
        self.assertTrue(len(data['trainingClasses']))



    def test_401_trainingClass_invalid_header(self):
        res=self.client().get('/TrainingClasses'
        ,headers={'Authorization':'Bearer ' +self.t_prod}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        self.assertEqual(res.status_code,401)
        self.assertEqual(data['code'], 'invalid_header')
        self.assertEqual(data['description'], 'Authorization malformed')
    

    def test_401_delete_unauthorized_access(self):
        res=self.client().delete('/TrainingClasses/5'
        ,headers={'Authorization':'Bearer ' +self.t_client}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        self.assertEqual(res.status_code,403)
        self.assertEqual(data['code'], 'unauthorized')
        self.assertEqual(data['description'], 'Permission not found')

    def test_delete_trainingClass_as_managment(self):
        res1=self.client().get('/TrainingClasses',headers={'Authorization':'Bearer ' +self.t_managment})
        data1=json.loads(res1.data)
        res=self.client().delete('/TrainingClasses/7'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        t_class=TrainingClass.query.filter(TrainingClass.id == 7).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],7)
        self.assertTrue(data['trainingClasses'])
        self.assertEqual(len(data['trainingClasses']) , len(data1['trainingClasses'])-1)
        self.assertEqual(t_class,None)





    def test_404_trainingClass_notFound(self):
        res=self.client().delete('/TrainingClasses/1000'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'not found')



    def test_add_trainingClass_as_managment(self):
        res1=self.client().get('/TrainingClasses',headers={'Authorization':'Bearer ' +self.t_managment}
        )
        data1=json.loads(res1.data)

        res=self.client().post('/TrainingClasses', json={
            'name':'zumba2',
            'coachId':1,
            'description':'a zumba class',
            'periods':['1','3'],
            'dayes':['sat','wed']
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )
        data=json.loads(res.data)
        trainingClass=TrainingClass.query.filter(TrainingClass.id == data['added_class']).one_or_none()

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['added_class'])
        self.assertTrue(len(data['trainingClasses']) == len(data1['trainingClasses'])+1)
        self.assertTrue(trainingClass!=None)
        

    def test_422_if_trainingClass_creation_unprocessable(self):
        res=self.client().post('/TrainingClasses', json={
            'name':'zumba2',
            'coachId':'1',
            'description':'a zumba class',
            'periods':1,
            'dayes':['sat','wed']
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'unprocessable')


    def test_405_if_trainingClass_creation_not_allowed(self):
        res=self.client().post('/TrainingClasses/16', json={
            'name':'zumba2',
            'coachId':'1',
            'description':'a zumba class',
            'periods':['1','3'],
            'dayes':['sat','wed']
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,405)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'method not allowed')


    def test_patch_trainingClass_as_managment(self):

        res=self.client().patch('/TrainingClasses/2', json={ 'periods':['1','3'], 'dayes':['sat','wed']
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        trainingClass=TrainingClass.query.filter(TrainingClass.id == 2).one_or_none()

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['patched'],2)
        self.assertEqual(trainingClass.periods,['1','3'])
        self.assertEqual(trainingClass.dayes,['sat','wed'])
        self.assertTrue(data['trainingClasses'])
        self.assertTrue(trainingClass!=None)
        

    def test_422_if_trainingClass_patching_unprocessable(self):
        res=self.client().patch('/TrainingClasses/2', json={
            'periods':'2,3',
            'dayes':1
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'unprocessable')

        
    # ###############################################################
    def test_get_coaches_by_user(self):
        res=self.client().get('/Coaches'
        ,headers={'Authorization':'Bearer ' +self.t_client}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        print(data)
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['coaches'])
        self.assertTrue(len(data['coaches']))



    def test_delete_coach_as_managment(self):
        res1=self.client().get('/Coaches',headers={'Authorization':'Bearer ' +self.t_managment})
        data1=json.loads(res1.data)

        res=self.client().delete('/Coaches/7'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        coach=Coach.query.filter(Coach.id == 7).one_or_none()
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],7)
        self.assertTrue(data['coaches'])
        self.assertTrue(len(data['coaches']) == len(data1['coaches'])-1)
        self.assertEqual(coach,None)





    def test_404_coach_notFound(self):
        res=self.client().delete('/Coaches/1000'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,404)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'not found')



    def test_add_coach_as_managment(self):
        res1=self.client().get('/Coaches',headers={'Authorization':'Bearer ' +self.t_managment})
        data1=json.loads(res1.data)

        res=self.client().post('/Coaches', json={
            'name':'suha',
            'description':'sweetest coach'}
            ,headers={'Authorization':'Bearer ' +self.t_managment}
            )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        coach=Coach.query.filter(Coach.id == data['added_coach']).one_or_none()

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertTrue(data['added_coach'])
        self.assertTrue(len(data['coaches']) == len(data1['coaches'])+1)
        self.assertTrue(coach!=None)
        

    def test_405_if_coach_creation_unprocessable(self):
        res=self.client().post('/Coaches', json={
            'description':1+3
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,422)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_405_if_coach_creation_not_allowed(self):
        res=self.client().post('/Coaches/16', json={
            'name':'suha',
            'description':'sweetest coach'}
            ,headers={'Authorization':'Bearer ' +self.t_managment}
            )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        self.assertEqual(res.status_code,405)
        self.assertEqual(data['success'],False)
        self.assertEqual(data['message'], 'method not allowed')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()