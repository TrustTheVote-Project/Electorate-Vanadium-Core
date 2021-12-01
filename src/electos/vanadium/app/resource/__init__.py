"""Encapsulate shared application resources.

Implementation choices:

- Resources are stored as fields on 'app.state' to allow instance specific
  (instead of global) state.
- Resources are added to 'app.state' in the top-level application setup.
- Accessing 'app.state' in routes requires passing each route a Request.
  Sub-dependencies are used hide direct access to the 'Request', making routes
  directly dependent only on a given resource.

Implementation subtleties:

Doing this in FastAPI without direct access to the classes and without creating
circular dependencies is somewhat arcane.

FastAPI treats shared resources as potentially global, but they don't have to be:
best practice is for routes to access them via dependencies (`fastapi.Depends`).
But making them local to an application instance is tricky without looking them
up by the instance, and the instance is hard to get into other modules without
creating a dependency between the application and the routes.

The solution is storing resources on 'app.state' instead of accessing them
directly. However the only way to access 'app.state' on a per instance basis
appears to be via 'request.app.state', which means a 'Request' parameter to a
route. Since routes usually want specific resource rather than the entire state.
using sub-dependencies to encapsulate the request hides the details and makes it
more obvious what resource a route is actually using.

All of this is not obvious from the FastAPI docs. It requires digging around on
Stack Overflow, numerous GitHub tickets for FastAPI, and looking at several
FastAPI projects that are being shared around as examples of best practice.
"""
