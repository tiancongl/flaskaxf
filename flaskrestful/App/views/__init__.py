from flask_restful import Api

from App.views.StudentResouce import StudentResouce
#在Init中进行初始化，因为注册路由要api来注册，添加资源，只是也和blue一样需要使用懒加载的方式，
# 当这个需要初始化的时候去app.Init_中去调用懒加载函数，就可以初始化这个api了
api = Api()

def init_api(app):
    api.init_app(app)


api.add_resource(StudentResouce,"/students/",methods = ["POST","GET"])