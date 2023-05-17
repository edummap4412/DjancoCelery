from rest_framework import serializers
from project_celery.celeryapp.models import Student


class StudentSerializers(serializers.ModelSerializer):

    firstname = serializers.CharField(max_length=100)
    surname = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    classroom = serializers.IntegerField()
    teacher = serializers.CharField(max_length=100)

    class meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['firstname']

    def create(self, validated_data):

        try:
            return Student.objects.create(**validated_data)

        except:
            return ValueError('Objeto nao pode ser criado')

    def update(self, instance, validated_data):

        try :
            instance.name = validated_data.get('name', instance.name)
            instance.surname = validated_data.get('surname', instance.surname)
            instance.age = validated_data.get('age', instance.age)
            instance.classroom = validated_data.get('classroom', instance.classroom)
            instance.teacher = validated_data.get('teacher', instance.teacher)

            instance.save()

            return instance

        except:
            return ValueError('Errorr atuallizar os caampos')




