from celery import Celery
from celery import Task
from celery.utils.log import get_task_logger

from sqlalchemy.sql import select

from .db import connection
from .db import files

logger = get_task_logger(__name__)

app = Celery(broker='redis://localhost:6379', backend='redis://localhost:16379')


class DBTask(Task):
    _db = None

    @property
    def db(self):
        if self._db is None:
            self._db = connection()
        return self._db


@app.task(base=DBTask)
def create_file(name):
    if isinstance(name, str):
        logger.warning("Is not a str")
    new_file = files.insert().values(name=name)
    create_file.db.execute(new_file)


@app.task(base=DBTask)
def get_files():
    result = list(get_files.db.execute(select([files])))
    print(result)
    logger.info(result)
    logger.info(type(result))
    logger.info(type(result[0]))
    return "OK"
