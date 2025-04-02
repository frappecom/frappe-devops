URLS_ROUTER = "app.urls.AppRouter"

TIME_ZONE = "America/Chicago"

INSTALLED_PACKAGES = [
    "plain.models",
    "plain.tailwind",
    "plain.auth",
    "plain.passwords",
    "plain.sessions",
    "plain.htmx",
    "plain.admin",
    "plain.elements",
    # Local packages
    "app.users",
]

AUTH_USER_MODEL = "users.User"
AUTH_LOGIN_URL = "login"

MIDDLEWARE = [
    "plain.sessions.middleware.SessionMiddleware",
    "plain.auth.middleware.AuthenticationMiddleware",
    "plain.admin.AdminMiddleware",
]
