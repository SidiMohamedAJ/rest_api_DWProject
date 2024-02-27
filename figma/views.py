from rest_framework.views import APIView
from rest_framework.response import Response
from .models import (Categorie, Course, Instructor,
                     Organization, Subcategorie,
                     Courseinstructor,Courseorganization,
                     Instructororganization)
from .serializers import (
    CategorieSerializer, CourseSerializer, InstructorSerializer,
    OrganizationSerializer, SubcategorieSerializer, CourseOrganizationSerializer,
    CourseInstructorSerializer, InstructorOrganizationSerializer
)

class CategorieListAPIView(APIView):
    def get(self, request):
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)


class CourseListAPIView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

class InstructorListAPIView(APIView):
    def get(self, request):
        instructors = Instructor.objects.all()
        serializer = InstructorSerializer(instructors, many=True)
        return Response(serializer.data)

class OrganizationListAPIView(APIView):
    def get(self, request):
        organizations = Organization.objects.all()
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)

class SubcategorieListAPIView(APIView):
    def get(self, request):
        subcategories = Subcategorie.objects.all()
        serializer = SubcategorieSerializer(subcategories, many=True)
        return Response(serializer.data)

class CourseorganizationListAPIView(APIView):
    def get(self, request):
        course_organizations = Courseorganization.objects.all()
        serializer = CourseOrganizationSerializer(course_organizations, many=True)
        return Response(serializer.data)

class CourseinstructorListAPIView(APIView):
    def get(self, request):
        course_instructors = Courseinstructor.objects.all()
        serializer = CourseInstructorSerializer(course_instructors, many=True)
        return Response(serializer.data)

class InstructororganizationListAPIView(APIView):
    def get(self, request):
        instructor_organizations = Instructororganization.objects.all()
        serializer = InstructorOrganizationSerializer(instructor_organizations, many=True)
        return Response(serializer.data)
