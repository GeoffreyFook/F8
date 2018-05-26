import webapp2
import os


class MainPage(webapp2.RedirectHandler):
    def get(self):
        self.response.write("Hello World")


print(os.environ["HTTP_USER_AGENT"])

app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)
