"""Basic py4web routes converted from the Web2py project."""

from py4web import action, request, redirect, URL
from .common import db, session, cache

@action('')
@action('index')
@action.uses(db, session)
def index():
    """Redirect to the Aurelia front-end."""
    return redirect(URL('static/aurelia/index.html'))


@action('get_curr_version')
@action.uses(db, session)
def get_curr_version():
    """Return the current Aurelia version string if available."""
    try:
        with open('static/aurelia/curr_version.txt') as f:
            version = f.read().strip()
    except Exception:
        version = ''
    return dict(version=version)

