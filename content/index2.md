title: How to write Static Site Generators?
date: 06 March 2019
slug: index2
summary: A static website generator combines a markup language, such as Markdown or reStructuredText, with a templating engine such as Jinja, to produce HTML files. The HTML files can be hosted and served by a web server or content delivery network (CDN) without any additional dependencies such as a WSGI server.

###Why are static site generators useful?
Static content files such as HTML, CSS and JavaScript can be served from a content delivery network (CDN) for high scale and low cost. If a statically generated website is hit by high concurrent traffic it will be easily served by the CDN without dropped connections.

For example, when Full Stack Python was on the top of Hacker News for a weekend, GitHub Pages was used as a CDN to serve the site and didn't have any issues even with close to 400 concurrent connections at a time, as shown in the following Google Analytics screenshot captured during that traffic burst.
###How do static website generators work?
Static site generators allow a user to create HTML files by writing in a markup language and coding template files. The static site generator then combines the markup language and templates to produce HTML. The output HTML does not need to be maintained by hand because it is regenerated every time the markup or templates are modified.

For example, as shown in the diagram below, the Pelican static site generator can take in reStructuredText files and Jinja2 template files as input then combine them to output a set of static HTML files.

###Python implementations
Numerous static website generators exist in many different languages. The ones listed here are primarily coded in Python.

+ Pelican is a commonly used Python static website generator which is used to create Full Stack Python. The primary templating engine is Jinja and Markdown, reStructuredText and AsciiDoc are supported with the default configuration.

+ Lektor is a static content management system and site generator that can deploy its output to any webserver. It uses Jinja2 as its template engine.

+ MkDocs uses a YAML configuration file to take Markdown files and an optional theme to output a documentation site. The templating engine is Jinja, but a user doesn't have to create her own templates unless a custom site is desired at which point it might make more sense to use a different static site generator instead.

+ mynt (source code) is built to create blogs and uses Jinja to generate HTML pages.

+ Nikola (source code) takes in reStructuredText, Markdown or Jupyter (IPython) Notebooks and combines the files with Mako or Jinja2 templates to output static sites. It is compatible with both Python 2.7 and 3.3+. Python 2.7 will be dropped in early 2016 while Python 3.3+ will continue to be supported.

+ Acrylamid (source code) uses incremental builds to generate static sites faster than recreating every page after each change is made to the input files.

+ Hyde (source code) started out as a Python rewrite of the popular Ruby-based Jekyll static site generator. Today the project has moved past those "clone Jekyll" origins. Hyde supports Jinja as well as other templating languages and places more emphasis on metadata within the markup files to instruct the generator how to produce the output files. Check out the Hyde-powered websites page to see live examples created with Hyde.

+ Grow SDK (source code) uses projects, known as pods, which contain a specific file and directory structure so the site can be generated. The project remains in the "experimental" phase.

+ Complexity (source code) is a site generator for users who like to work in HTML. It uses HTML for templating but has some functionality from Jinja for inheritance. Works with Python 2.6+, 3.3+ and PyPy.

+ Cactus (source code) uses the Django templating engine that was originally built with front-end designers in mind. It works with both Python 2.x and 3.x.