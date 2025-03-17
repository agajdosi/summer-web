import asyncio
import tornado
import random

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        x = random.randint(1,1000000)
        items = ["rouska", "auto", "stetec", "paruka"]
        self.render("main.html", lucky_number=x, items=items)

class UploadHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name")
        self.write(f"Hello {name}!")

class EntryHandler(tornado.web.RequestHandler):
    def get(self, skupina1, skupina2):
        self.write(f"Hello entry numbers! {skupina1} {skupina2}")

async def main():
    app = tornado.web.Application([
        (r"/", MainHandler),
        (r"/upload", UploadHandler),
        (r"/entry/(\d{1,4})/(\w{1,1000})", EntryHandler),
    ])
    app.listen(8888)
    await asyncio.Event().wait()


if __name__ == "__main__":
    asyncio.run(main())