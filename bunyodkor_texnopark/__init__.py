try:
    import pymysql
except ImportError:
    pymysql = None

if pymysql is not None:
    # Django 6 checks mysqlclient's version metadata. PyMySQL exposes
    # mysqlclient-compatibility metadata as 1.4.6, so we align it with
    # the minimum version Django expects before installing the shim.
    pymysql.version_info = (2, 2, 1, "final", 0)
    pymysql.__version__ = "2.2.1"
    pymysql.install_as_MySQLdb()
