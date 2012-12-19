import model
#from gwhiz.model import meta
from gwhiz.model import *


print meta.Session.query(model.Composer).all()
print meta.Session.query(model.Publication).slice(1,5).all()

from sqlalchemy.sql import text
from sqlalchemy.sql import select

from sqlalchemy.sql.expression import func
