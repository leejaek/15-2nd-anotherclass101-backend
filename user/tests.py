import json
import unittest

from django.test    import TestCase, Client
from user.models   import User, UserGrade, PhoneVerification

client = Client()

class ProfileDataTest(TestCase):
    def setUp(self):

        PhoneVerification.objects.create(
            id = 1
        )

        UserGrade.objects.create(
            id=1,
            name='기본',
            description='기본회원입니다'
        )
        User.objects.create(
            id=1,
            name='테스트',
            email='test@naver.com',
            password='asdfasdf',
            nickname='테스트',
            grade_id=1
        )


    def tearDown(self):
        PhoneVerification.objects.all().delete()
        UserGrade.objects.all().delete()
        User.objects.all().delete()

    def test_profiledata(self):
            client = Client()
            response = client.get('/user/profiledata',  content_type='application/json')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(),{
                'message':'SUCCESS','result':{
                    'name':'we',
                    'email' : 'wecode@naver.com',
                    'number' : '01033334444',
                    'image' : 'https://s3.ap-northeast-2.amazonaws.com/ac101/49c40c1c510411ebb06bc4b301cd19f5',
                    'nickname' : 'qqq'
                }
            })
            







