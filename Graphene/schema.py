from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schemadescription
# import schemadescription
# from schemadescription import Student
import models

# class CustomNode(Node):
#     class Meta:
#         name = 'Node'
#     @staticmethod
#     def to_global_id(type, id):
#         return '{}:{}'.format(type, id)
#     @staticmethod
#     def get_node_from_global_id(info, global_id, only_type=None):
#         type, id = global_id.split(':')
#         if only_type:
#             # We assure that the node type that we want to retrieve
#             # is the same that was indicated in the field type
#             assert type == only_type._meta.name, 'Received not compatible node.'
#         if type == 'student':
#             return get_student(id)
#         elif type == 'teacher':
#             return get_teacher(id)
#

class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    teacher = graphene.relay.Node.Field(schemadescription.Teacher)
    teacher_list = SQLAlchemyConnectionField(schemadescription.Teacher)
    student = graphene.relay.Node.Field(schemadescription.Student)
    student_list = SQLAlchemyConnectionField(schemadescription.Student)

schema = graphene.Schema(query=Query)
