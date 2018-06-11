from flask_restful import Resource, fields, marshal_with

from App.models import Student



#写一个字典把想要传输的数据写在里边，然后放在装饰器中作为装饰器的参数

students_fields={
    "id":fields.Integer,
    "s_name":fields.String,
    "s_age":fields.Integer
}

result_fields={
    "msg":fields.String,
    "status":fields.Integer,
    #NESTed 是级联数据的方法
    #List是将其转换成列表的形式
    "data":fields.List(fields.Nested(students_fields))
}

class StudentResouce(Resource):
#这个装饰器的作用是将数据和字典data中的数据直接映射，记住，data中的数据，必须都包含在result_feilds中
    @marshal_with(result_fields)
    def get(self):
        data = {
            "msg": "ok",
            "status": "200",

        }

        students = Student.query.all()

        data["data"] = students

        return data