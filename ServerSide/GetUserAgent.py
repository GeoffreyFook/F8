import webapp2
import os


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write(os.environ["HTTP_USER_AGENT"])


print(os.environ["HTTP_USER_AGENT"])

app = webapp2.WSGIApplication([('/', MainPage), ], debug=True)
