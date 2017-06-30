import connexion
from swagger_server.models.person import Person
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def conn_port_get(port):
    """
    conn_port_get
    Gets all tcp conns. 
    :param port: port num
    :type port: float

    :rtype: List[Person]
    """
    return 'do some magic!'
