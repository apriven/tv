import os
from bottle import (get, post, redirect, request, route, run, static_file, jinja2_view,
                   template, error)
import utils
import json
from functools import partial

view = partial(jinja2_view, template_lookup=['templates'])


# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
   return static_file(filepath, root="./js")

@get("/css/<filepath:re:.*\.css>")
def css(filepath):
   return static_file(filepath, root="./css")

@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
   return static_file(filepath, root="./images")

@route('/')
def index():
   sectionTemplate = "./templates/home.tpl"
   return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def browse():
   sectionTemplate = "./templates/browse.tpl"
   return template("./pages/index.html", version=utils.getVersion(),
                   sectionTemplate=sectionTemplate,
                   sectionData=[json.loads(utils.getJsonFromFile(elem)) for elem in utils.AVAILABE_SHOWS])

@route('/ajax/show/<number>')
def show(number):
   return template("./templates/show.tpl", version=utils.getVersion(),
                   result = json.loads(utils.getJsonFromFile(number)))



@route('/ajax/show/<number>/episode/<ep_number>')
def episode(number, ep_number):
   show = json.loads(utils.getJsonFromFile(number))
   for episode in show["_embedded"]["episodes"]:
       if int(ep_number) == episode["id"]:
           return template("./templates/episode.tpl", version=utils.getVersion(), result=episode)
   return


@route('/search', method="GET")
def search():
   sectionTemplate = "./templates/search.tpl"
   return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@post('/search')
def search_results():
   sectionTemplate = "./templates/search_result.tpl"
   return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@error(404)
def error(error):
   sectionTemplate = "./templates/404.tpl"
   return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})

# run(host='0.0.0.0', port=os.environ.get('PORT', 5000))


run(host='localhost', port=7002)