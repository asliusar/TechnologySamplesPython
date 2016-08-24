from tornado.ioloop import IOLoop
import tornado.web
import tornado.httpserver
import dao
import json

user_dao = dao.UserDao()
car_dao = dao.CarDao()

static_path = "../client"


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("../client/html/index.html")


class GetAllCarHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(car_dao.get_all(), default=lambda o: o.__dict__, sort_keys=True))


class GetCarByIdHandler(tornado.web.RequestHandler):
    def get(self, car_id):
        self.write(car_dao.get_by_id(int(car_id)).to_json())


class GetAllUsersHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps(user_dao.get_all(), default=lambda o: o.__dict__, sort_keys=True))


class GetUsersByIdHandler(tornado.web.RequestHandler):
    def get(self, user_id):
        self.write(user_dao.get_by_id(int(user_id)).to_json())


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler),
            (r"/api/v1/cars", GetAllCarHandler),
            (r"/api/v1/car/(.*)", GetCarByIdHandler),
            (r"/api/v1/users", GetAllUsersHandler),
            (r"/api/v1/user/(.*)", GetUsersByIdHandler),
            (r'/static/(.*)', tornado.web.StaticFileHandler, {'path': static_path}),
        ]
        tornado.web.Application.__init__(self, handlers, debug=True, autoreload=True)


def main():
    dao.generate_data(user_dao, car_dao)

    app = Application()
    app.listen(8090)
    IOLoop.instance().start()


if __name__ == '__main__':
    main()
