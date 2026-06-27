import pytest

from pages.users_api_page import UsersApi
from utils.logger import logger
import pytest_check as check
#instancio la clase, y la guardo en una variable
api = UsersApi()


def test_get_one_user():
    logger.info("Obteniendo un usuario especifico")
    response = api.get_one_user(1)

    check.equal(
        response.status_code,
        200,
        "STATUS INCORRECTO"


    )

    body = response.json()
    
    check.equal(
        body["id"],
        1,
        "EL ID NO COINCIDE"

    )

def test_get_users():
    logger.info("OBTENIENDO TODOS LOS USUARIOS")
    response = api.get_users()

    check.equal(

        response.status_code,
        200,
        "STATUS INCORRECTO"

    )
    users = response.json()

    check.is_true(
        len(users)>0,
        "NO SE OBTUVIERON USUARIOS"


    )
    check.is_true(
        isinstance(users,list),
        "LA RESPUESTA NO ES UNA LISTA"

    )

def test_create_user(users_data):
    logger.info("CREANDO USUARIO")

    response = api.create_user(
        users_data["name"],
        users_data["username"],
        users_data["email"]

    )
    check.equal(
        response.status_code,
        201,
        "NO SE CREO EL USUARIO"
    )
def test_delete_user():
    logger.info("ELIMINANDO USER")
    user_id_to_delete = 1
    response = api.delete_user(user_id_to_delete)


    check.is_in(
    response.status_code,
    [200, 204],
    "ELIMINACIÓN NO DEVOLVIÓ 200 O 204"
)
