

from app.database import Base
from app.database import engine

from app.routes.auth import router as auth_router
from app.routes.dashboard import router as dashboard_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PocketSmart AI"
)


@app.get("/")
def root():

    return {
        "message":
        "PocketSmart AI API Running"
    }


app.include_router(auth_router)

app.include_router(dashboard_router)