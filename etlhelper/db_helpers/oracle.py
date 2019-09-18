"""
Database helper for Oracle
"""
from etlhelper.db_helpers.db_helper import DbHelper


class OracleDbHelper(DbHelper):
    """
    Oracle DB helper class
    """
    def __init__(self):
        super().__init__()
        try:
            import cx_Oracle
            self.sql_exceptions = (cx_Oracle.DatabaseError)
            self._connect_func = cx_Oracle.connect
            self.connect_exceptions = (cx_Oracle.DatabaseError)
        except ImportError:
            print("The cxOracle drivers were not found. See setup guide for more information.")
            # TODO: More helpul information.

    def get_connection_string(self, db_params, password_variable):
        """
        Return a connection string
        :param db_params: DbParams
        :param password: str, password
        :return: str
        """
        # Prepare connection string
        password = self.get_password(password_variable)
        return (f'{db_params.username}/{password}@'
                f'{db_params.host}:{db_params.port}/{db_params.dbname}')

    def get_sqlalchemy_connection_string(self, db_params, password_variable):
        """
        Returns connection string for sql alchemy type connections
        """
        password = self.get_password(password_variable)

        return (f'oracle://{db_params.username}:{password}@'
                f'{db_params.host}:{db_params.port}/{db_params.dbname}')