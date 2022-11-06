from aiohttp import web
from aiohttp_swagger3 import (
    SwaggerInfo,
    SwaggerDocs,
    SwaggerUiSettings,
    ReDocUiSettings,
    RapiDocUiSettings
)

from client_session import request_sessions
from routes import (
    poke_info_from_id,
	poke_info_from_name,
	poke_infos_from_ids,
	poke_infos_from_names,
	poke_infos_from_offset_limits,
)


app = web.Application()


async def on_startup(app: web.Application):
    await request_sessions.__ainit__()

async def on_shutdown(app: web.Application):
    await request_sessions.__adel__()

app.on_startup.append(on_startup)
app.on_shutdown.append(on_shutdown)

swagger_app = SwaggerDocs(
    app,
    components="components.yaml",
    info=SwaggerInfo(
        title="Poke Info API",
        version="1.0.0",
        description=open("Readme.md").read()
    ),
    swagger_ui_settings=SwaggerUiSettings(path="/swagger"),
    redoc_ui_settings=ReDocUiSettings(path="/redoc"),
    rapidoc_ui_settings=RapiDocUiSettings(path="/rapidoc")
)

swagger_app.add_routes([
    web.get('/pokemon', poke_infos_from_offset_limits, allow_head=False),
    web.get('/pokemon/ids', poke_infos_from_ids, allow_head=False),
    web.get('/pokemon/names', poke_infos_from_names, allow_head=False),
    web.get('/pokemon/id/{poke_id}', poke_info_from_id, allow_head=False),
    web.get('/pokemon/name/{name}', poke_info_from_name, allow_head=False),
])


if __name__ == "__main__":
    web.run_app(app)
