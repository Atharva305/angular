from distutils.log import debug
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello world Atharva Patil")


app = webapp2.WSGIApplication([('/',MainPage)], debug=True)
