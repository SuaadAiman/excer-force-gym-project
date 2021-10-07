
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
        self.database_path = "postgresql://{}:{}@{}/{}".format('postgres','987654321','localhost:5432', self.database_name)
        self.t_client = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGRlNTdjNjllYjIwMDcwNGJmY2UzIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNTYyMjkzLCJleHAiOjE2MzM2NDg2OTMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiXX0.Y_sk9uNCrKdDfDvA1vVUBmP9g7eQY4Fcbt8cWt02rVHOqSyUZcMiaOS4hcc06jlHbHCn-2847IZiqC6s1JEW8Y2VBzF1mh0MNkLkmc8N45Yp6wcBl0z_3QuVNaHbykuSj3gypQo2CO1pJWIwY506YjGjbdAMRHLe1gT21q70ErR21AQFKjdVrK7GSpSHS7jzefEHRJqRShOcdxg-CjjfF1ftJRqEjZlpB31t5MYGbZo07do_o3imn2-NFc1_Kt2ntyyE3M8v8jEDzgkzTwiLTmm5L6r6MlhKSx8K_ZGn7vAwWBUUOWk_BAnZPDsGewvqQ29p8uSRD8retmWLqtst1w' 
        self.t_prod = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
        self.t_managment = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVHTzN4V0k5TjZ1eld0YkFfV0JSVyJ9.eyJpc3MiOiJodHRwczovL3RoZS1neW0tcHJvamVjdC51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjE1ZGQxOTZmZjg2ZjYwMDZhMzU1MWViIiwiYXVkIjoiZ3ltIiwiaWF0IjoxNjMzNTYyMjQzLCJleHAiOjE2MzM2NDg2NDMsImF6cCI6IjNrOE1zd1VGSEczZXhCZFpwYjZheVcxME1sa1ZsdVp5Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6Q29hY2hlcyIsImRlbGV0ZTpUcmFpbmluZ0NsYXNzZXMiLCJnZXQ6Q29hY2hlcyIsImdldDpUcmFpbmluZ0NsYXNzZXMiLCJwYXRjaDpUcmFpbmluZ0NsYXNzZXMiLCJwb3N0OkNvYWNoZXMiLCJwb3N0OlRyYWluaW5nQ2xhc3NlcyJdfQ.CIQDld6JpwpqT_R-YtFyp-GFl4Evfk2SV9y34hJ83BSJMfBv4fEi9rZMDxf3-XKOoAOOWG9m92ePSSlve3zjlQVZdv9XherM9BvIOKTiFTlvGct24cIwn67JIreJIHp8c5HeoGd39zzu6kJjLilcpaBV3Ez53o3wpTpTCY-eC0032iRcNZ31PSKY8GwJBaTnX2xlWwnqsRKcHZVDHzJPem8_cpjG4v1LgZ9oOkAxm2YzdWabf0zO29-SGpUb-zu-8hskhrawHq2wu0ryZcw-xSji-1ap-XKzoDuVEr8UtlA_62HwBF53jASc7DnOs_IHiHF-r_cYMDtj1iEquKMtWA'
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
        print(data)
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
        res=self.client().delete('/TrainingClasses/18'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        t_class=TrainingClass.query.filter(TrainingClass.id == 18).one_or_none()
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],18)
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

        res=self.client().patch('/TrainingClasses/9', json={ 'periods':['1','3'], 'dayes':['sat','wed']
        }
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)
        trainingClass=TrainingClass.query.filter(TrainingClass.id == 9).one_or_none()

        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['patched'],9)
        self.assertEqual(trainingClass.periods,['1','3'])
        self.assertEqual(trainingClass.dayes,['sat','wed'])
        self.assertTrue(data['trainingClasses'])
        self.assertTrue(trainingClass!=None)
        

    def test_422_if_trainingClass_patching_unprocessable(self):
        res=self.client().patch('/TrainingClasses/9', json={
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

        res=self.client().delete('/Coaches/17'
        ,headers={'Authorization':'Bearer ' +self.t_managment}
        )#the way of sending the header is referenced from https://knowledge.udacity.com/questions/200723
        data=json.loads(res.data)

        coach=Coach.query.filter(Coach.id == 17).one_or_none()
        
        self.assertEqual(res.status_code,200)
        self.assertEqual(data['success'],True)
        self.assertEqual(data['deleted'],17)
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
        print(data)
        print(data)
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