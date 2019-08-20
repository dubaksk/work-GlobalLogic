from graphene_sqlalchemy import SQLAlchemyObjectType
from models import ModelTeacher, ModelStudent
import graphene


class TeacherAttribute:
    # id = graphene.ID(description="row ID")
    name = graphene.String(description="Name of the Teacher")
    password = graphene.String(description="Password for Login")


class Teacher(SQLAlchemyObjectType, TeacherAttribute):
    """Teacher node."""
    class Meta:
        model = ModelTeacher
        interfaces = (graphene.relay.Node, )


class StudentAttribute:
    admno = graphene.String(description="Student's Admission Number")
    section = graphene.String(description="Section of Student")
    name = graphene.String(description="Name of Student")
    password = graphene.String(description="Password of student")
    teacher_id = graphene.ID(description="Teacher ID")


class Student(SQLAlchemyObjectType, StudentAttribute):
    """Student Node"""
    class Meta:
        model = ModelStudent
        interfaces = (graphene.relay.Node, )






# query {
#   teacherList {
#     edges{
#       node{
#         id
#         name
#       }
#     }
#   }
# }