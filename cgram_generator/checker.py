from logging import getLogger

from cgram_generator import models, errors

logger = getLogger(__name__)


def check_dependencies(api: models.CGramAPI):
    registered_types: list[str] = [model.name for model in api.types]
    for model in api.types:
        for dependency in model.dependencies:
            if dependency not in registered_types:
                raise errors.UnknownDependencyError(model.name, dependency)
        logger.debug(
            "Type '%s' depends on %s",
            model.name,
            ", ".join(model.dependencies) or "nothing",
        )
    logger.info("All dependencies are valid")
