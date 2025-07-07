"""Basic py4web routes converted from the Web2py project."""

from py4web import action, request, redirect, URL
from .common import db, session, cache
import uuid

@action('')
@action('/')
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


@action('get_constants')
@action.uses(db, session)
def get_constants():
    """Return various numeric constants used by the frontend.

    The values mirror those defined in the legacy Web2py models so that
    the existing Aurelia application can continue to operate while the
    backend is being ported to py4web.
    """
    return dict(
        story_type=dict(
            STORY4MEMBER=1,
            STORY4EVENT=2,
            STORY4PHOTO=3,
            STORY4TERM=4,
            STORY4MESSAGE=5,
            STORY4HELP=6,
            STORY4FEEDBACK=7,
            STORY4VIDEO=8,
            STORY4DOC=9,
            STORY4AUDIO=10,
            STORY4ARTICLE=12,
            STORY4DOCSEGMENT=14,
        ),
        visibility=dict(
            VIS_NEVER=0,
            VIS_NOT_READY=1,
            VIS_VISIBLE=2,
            VIS_HIGH=3,
        ),
        cause_of_death=dict(
            DC_DIED=0,
            DC_FELL=1,
            DC_KILLED=2,
            DC_MURDERED=3,
        ),
        story_visibility=dict(
            SV_NO_CHANGE=0,
            SV_PUBLIC=1,
            SV_ADMIN=2,
            SV_ARCHIVER=3,
            SV_LOGGEDIN=4,
        ),
        ptp_key=str(uuid.uuid4()),
    )

