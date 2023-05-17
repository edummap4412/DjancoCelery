
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from project_celery.celeryapp.models import Student, Teacher, Classroom
from project_celery.celeryapp.views import StudentListViewSet


class StudentListViewSetTestCase(TestCase):

    def setUp(self) -> None:
        super(StudentListViewSetTestCase, self).setUp()

        self.factory = APIRequestFactory()

        self.classroom = Classroom.objects.create(
            periodo = 'Noturno'
        )

        self.teacher= Teacher.objects.create(
            firstname='Fulano',
            surname='Siglano',
        )

        classroom_teacher = self.classroom
        classroom_teacher.classes.set(self.teacher.id)
        classroom_teacher.save()

        self.student_list = Student.objects.create(
            firstname='Eduardo',
            surname='Michael',
            age=24,

        )


    def test_create_student(self):
        view = StudentListViewSet.as_view({'post': 'create'})

        data = {
            'firstname': 'Eduardo',
            'surname': 'Michael',
            'age' : 28 ,
            'teacher': 'Albert Einstein'

        }

        request = self.factory.post('student/student_list',data)
        response = view(request)

        print(response)

    def test_get_student(self):
        view = StudentListViewSet.as_view({'get': 'list'})

        request = self.factory.get(f'student_list/{self.student_list.id}')
        response = view(request, student_id=self.student_list.id)

        print(response)
