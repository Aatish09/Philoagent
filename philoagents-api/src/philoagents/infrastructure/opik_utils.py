import os

import opik
from loguru import logger
from opik.configurator.configure import OpikConfigurator

from philoagents.config import settings


# def configure() -> None:
#     if settings.COMET_API_KEY and settings.COMET_PROJECT:
#         try:
#             client = OpikConfigurator(api_key=settings.COMET_API_KEY)
#             default_workspace = client._get_default_workspace()
#         except Exception:
#             logger.warning(
#                 "Default workspace not found. Setting workspace to None and enabling interactive mode."
#             )
#             default_workspace = None

#         os.environ["OPIK_PROJECT_NAME"] = settings.COMET_PROJECT

#         try:
#             opik.configure(
#                 api_key=settings.COMET_API_KEY,
#                 workspace=default_workspace,
#                 use_local=False,
#                 force=True,
#             )
#             logger.info(
#                 f"Opik configured successfully using workspace '{default_workspace}'"
#             )
#         except Exception:
#             logger.warning(
#                 "Couldn't configure Opik. There is probably a problem with the COMET_API_KEY or COMET_PROJECT environment variables or with the Opik server."
#             )
#     else:
#         logger.warning(
#             "COMET_API_KEY and COMET_PROJECT are not set. Set them to enable prompt monitoring with Opik (powered by Comet ML)."
#         )
def configure() -> None:
    if settings.COMET_API_KEY and settings.COMET_PROJECT:
        # Use workspace from settings if available
        workspace = settings.COMET_WORKSPACE
        
        # Only try to get default workspace if not provided
        if not workspace:
            try:
                client = OpikConfigurator(api_key=settings.COMET_API_KEY)
                workspace = client._get_default_workspace()
            except Exception:
                logger.warning("Default workspace not found...")
                workspace = None

        # Rest of the configuration remains the same...
        os.environ["OPIK_PROJECT_NAME"] = settings.COMET_PROJECT
        try:
            opik.configure(
                api_key=settings.COMET_API_KEY,
                workspace=workspace,  # Use determined workspace
                use_local=False,
                force=True,
            )
            logger.info(f"Opik configured successfully using workspace '{workspace}'")
        except Exception:
            logger.warning("Couldn't configure Opik...")
    else:
        logger.warning("COMET_API_KEY and COMET_PROJECT are not set...")


def get_dataset(name: str) -> opik.Dataset | None:
    client = opik.Opik()
    try:
        dataset = client.get_dataset(name=name)
    except Exception:
        dataset = None

    return dataset


def create_dataset(name: str, description: str, items: list[dict]) -> opik.Dataset:
    client = opik.Opik()

    client.delete_dataset(name=name)

    dataset = client.create_dataset(name=name, description=description)
    dataset.insert(items)

    return dataset
