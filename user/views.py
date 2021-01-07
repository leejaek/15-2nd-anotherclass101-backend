import json
import boto3
import uuid

from django.views import View
from django.http import JsonResponse

from .models     import User
from .utils      import id_auth
from my_settings import (
                            AWS_ACCESS_KEY_ID,
                            AWS_SECRET_ACCESS_KEY,
                        )


class ProfileView(View):

    @id_auth
    def post(self, request):
        data = json.loads(request.body)

        user = request.user
        name           = data['name']
        nickname       = data['nickname']

        try:
            User.objects.filter(id = user.id).update(
                name          = name,
                nickname      = nickname,
            )
            
            return JsonResponse({'message': "SUCCESS"}, status=201)

        except KeyError as e:
            return JsonResponse({'message': f'KEY_ERROR: =>  {e}'}, status=400)

        except ValueError as e:
            return JsonResponse({'message': f'VALUE_ERROR: =>  {e}'}, status=400)


class ProfileDataView(View):

    @id_auth
    def get(self,request):
        user = request.user

        try:
            result = {
                "name"     : User.objects.get(id = user.id).name,
                "nickname" : User.objects.get(id = user.id).nickname,
                "image"    : User.objects.get(id = user.id).profile_image,
                "email"    : User.objects.get(id = user.id).email,
                "phone"    : User.objects.get(id = user.id).number,
            }

            return JsonResponse({'result': result}, status=200)

        except KeyError as e:
            return JsonResponse({'message': f'KEY_ERROR: =>  {e}'}, status=400)

        except ValueError as e:
            return JsonResponse({'message': f'VALUE_ERROR: =>  {e}'}, status=400)


class ProfileImageView(View):

    s3_client = boto3.client(
        's3',
        aws_access_key_id     = AWS_ACCESS_KEY_ID,
        aws_secret_access_key = AWS_SECRET_ACCESS_KEY
    )

    @id_auth
    def post(self, request):
        user = request.user

        file  = request.FILES['file']

        if file:
            filename = str(uuid.uuid1()).replace('-','')
            self.s3_client.upload_fileobj(
                file,
                'ac101',
                filename,
                ExtraArgs = {
                    'ContentType': 'image/jpeg'
                }
            )
            file_url = f"https://s3.ap-northeast-2.amazonaws.com/ac101/{filename}"

            User.objects.filter(id = user.id).update(
                profile_image = file_url
            )

            return JsonResponse({'message': 'SUCCESS'}, status=200)
