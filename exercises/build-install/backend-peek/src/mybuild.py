import pathlib
import hatchling
import hatchling.build


def build_wheel(wheel_directory, config_settings=None, metadata_directory=None):
    log_file = pathlib.Path(__file__).parent.parent / "wheel-log.txt"
    text = [
        f"wheel-directory: {wheel_directory}",
        f"ls wheel-directory: {list(pathlib.Path(wheel_directory).iterdir())}",
        f"config_settings: {config_settings}",
        f"metadata_directory: {metadata_directory}",
    ]
    log_file.write_text("\n".join(text))
    return hatchling.build.build_wheel(
        wheel_directory,
        config_settings=config_settings,
        metadata_directory=metadata_directory,
    )


def build_sdist(sdist_directory, config_settings=None):
    log_file = pathlib.Path(__file__).parent.parent / "sdist-log.txt"
    text = [
        f"sdist-directory: {sdist_directory}",
        f"config_settings: {config_settings}",
    ]
    log_file.write_text("\n".join(text))
    return hatchling.build.build_sdist(sdist_directory, config_settings=config_settings)
