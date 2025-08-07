"""py4web app bootstrap for the place_stories application."""

# Import modules that define actions so they are registered at startup
from . import common  # sets up db, session, etc.
from . import routes
