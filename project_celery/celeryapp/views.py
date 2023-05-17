from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework import generics


# Part 2
#################################################################
from .serializer import StudentSerializers


class StudentListViewSet(viewsets.ModelViewSet, generics.ListAPIView):
    serializer_class = StudentSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid :
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer.save()
            print(serializer)

            return Response(serializer.data, status.HTTP_201_CREATED)
        except:
            error = {'message': 'Error'}
            return Response(data=error, status=status.HTTP_400_BAD_REQUEST)

    def list(self, student_id, *args, **kwargs):
        serializer = self.serializer_class(student_id=kwargs.get('id'))

        if serializer.is_valid:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        try:
            serializer.save()

            return Response(serializer.data)

        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
