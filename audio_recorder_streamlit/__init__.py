import json
import os
from pathlib import Path
from typing import Optional

import streamlit.components.v1 as components

_RELEASE = bool(os.environ.get("RELEASE", "True"))

if _RELEASE:
    build_dir = Path(__file__).parent.absolute() / "frontend" / "build"
    _audio_recorder_ui = components.declare_component(
        "audio_recorder_ui", path=build_dir
    )
else:
    _audio_recorder_ui = components.declare_component(
        "audio_recorder_ui",
        url="http://localhost:3001",
    )


def audio_recorder_ui(
    neutral_color: str = "#303030",
    recording_color: str = "#de1212",
    icon_name: str = "microphone",
    icon_size: str = "3x",
    get_status_url: str = "http://localhost:8594/get_recording_state",
    polling_interval: int = 600,
    status: str = None,
    key: Optional[str] = None,
) -> Optional[bytes]:
    """Create a new instance of "audio_recorder_ui".

    Parameters
    ----------
    neutral_color: str
        Color of the recorder icon while stopped.
    recording_color: str
        Color of the recorder icon while recording.
    icon_name: str
        Font Awesome solid icon name
        (https://fontawesome.com/search?o=r&s=solid)
    icon_size: str
        Size of the icon (https://fontawesome.com/docs/web/style/size)
    key: str or None
        An optional key that uniquely identifies this component. If this is
        None, and the component's arguments are changed, the component will be
        re-mounted in the Streamlit frontend and lose its current state.

    Returns
    -------
    Optional[bool]
        Returns True if the audio recorder ui was successfully showing up, False otherwise.

    """

    status = _audio_recorder_ui(
        neutral_color=neutral_color,
        recording_color=recording_color,
        icon_name=icon_name,
        icon_size=icon_size,
        get_status_url=get_status_url,
        polling_interval=polling_interval,
        status=status,
        key=key,
    )

    return status
