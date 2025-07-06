# place_stories_server

This repository originally hosted a Web2py application.  A basic
[py4web](https://py4web.com) skeleton has been added under the `apps`
directory as a starting point for migrating the project.

## Installation

1. Install the framework and dependencies:
   ```bash
   pip install py4web
   ```
2. From the repository root, run the server:
   ```bash
   py4web run apps --port 8000
   ```
3. Open `http://127.0.0.1:8000/place_stories/` in your browser.

The current py4web app only implements a couple of routes and redirects
to the existing Aurelia front‑end. Additional controllers and models
from the original Web2py project still need to be ported manually.
