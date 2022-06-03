from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject
from mock import Mock
from dotenv import load_dotenv


class Tools:
    def __init__(self, tool: str):
        self.tool = tool
        print(tool)


class Service:
    def __init__(self, tools: Tools):
        self.tools = tools


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    tools = providers.Singleton(
        Tools,
        tool=config.tool,
    )

    service = providers.Factory(
        Service,
        tools=tools,
    )


@inject
def main(service: Service = Provide[Container.service]):
    ...


if __name__ == "__main__":
    load_dotenv()
    container = Container()
    container.config.tool.from_env("tool", required=True)
    container.wire(modules=[__name__])

    main()

    with container.tools.override(Mock()):
        main()
