import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    # Lists of dictionaries containing pages that will be added to categories
    python_pages = [{"title": "Official Python Tutorial", "url": "http://docs.python.org/2/tutorial/"},
                    {"title": "How to Think like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/"},
                    {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/"}]

    django_pages = [{"title": "Official Django Tutorial", "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
                    {"title": "Django Rocks", "url": "http://www.djangorocks.com/"},
                    {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/"}]

    other_pages = [{"title": "Bottle", "url": "http://bottlepy.org/docs/dev"},
                    {"title": "Flask", "url": "http://flask.pocoo.org"}]

    # Categories dictionary
    cats = {"Python": {"pages": python_pages},
            "Django": {"pages": django_pages},
            "Other Frameworks": {"pages": other_pages}}

    # Go through the categories dictionary, create the categories and add all of their pages to them
    for cat, cat_data in cats.iteritems():
        c = add_cat(cat)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out all categories and their pages
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

# get_or_create returns a tuple (object, created) where the first element is a reference to the created/fetched object
# and the second element specifies whether a new object was created
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

