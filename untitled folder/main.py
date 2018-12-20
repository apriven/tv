import os
from bottle import (get, post, redirect, request, route, run, static_file, jinja2_view,
                    template, error)
import utils
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
def index():
    sectionTemplate = "./templates/browse.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/search')
def index():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@error(404)
def index():
    print("????")
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", sectionTemplate=sectionTemplate)

# run(host='0.0.0.0', port=os.environ.get('PORT', 5000))


run(host='localhost', port=7002)
