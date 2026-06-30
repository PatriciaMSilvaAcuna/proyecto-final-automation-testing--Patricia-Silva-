import pytest

from pages.post_api_page import PostsApi
from utils.logger import logger
import pytest_check as check
#instancio la clase, y la guardo en una variable
api = PostsApi()




def test_get_one_posts():

    logger.info("Obteniendo un posts ")
   

    response = api.get_one_post(1)

    #lo podemos hacer con assert, pero el assert me corta la ejecución
    # assert response.status_code == 200
    # pero necesito que me muestre los fallidos como los ok
    # por ende importamos el modulo check
    check.equal(
        response.status_code,
        200,
        "STATUS INCORRECTO"


    )

    body = response.json()
    check.equal(
        body["id"], # trae el valor del ID
        1, "El ID no COINCIDE"

    )

def test_posts():
    logger.info("Obteniendo TODOS los posteos")
    response = api.get_posts()

    #print(response)

    check.equal(
        response.status_code,
        200,
        "STAATUS INCORRECTO"
    )    

    posts = response.json()
    
    #evaluo si es verdadero, si es mayor a cero
    check.is_true(
        len(posts) > 0,
        "NO SE OBTUVIERON POSTEOS"
    )
    #valido si es una lista, palabra reservada 
    check.is_true(

        #recibe dos valores
        #lo que tengo y que tipo de datos manejo en el argumento
        isinstance(posts, list),
        "LA RESPUESTA NO ES UNA LISTA"

    )

def test_create_posts(posts_data):

    logger.info("CREANDO POSTEOS")
    
    response = api.create_posts(
        posts_data["title"],
        posts_data["body"],
        posts_data["userId"]

    )
    check.equal(
        response.status_code,
        201,
        "NO SE CREO EL POST"
    )


