import pytest

from afni_test_utils.tools import run_cmd
from unittest.mock import MagicMock
import platform
from afnipy import lib_system_check as SC


@pytest.mark.slow
def test_with_afni_system_check(data):
    cmd = "afni_system_check.py -check_all"
    run_cmd(data, cmd)


def test_with_afni_system_check_with_dist_deprecated(data, monkeypatch):
    with monkeypatch.context() as m:
        if hasattr(platform, "dist"):
            m.setattr(
                platform,
                "dist",
                MagicMock(
                    side_effect=AttributeError("'platform' has no attribute 'dist'")
                ),
            )
        if hasattr(platform, "linux_distribution"):
            m.setattr(
                platform,
                "linux_distribution",
                MagicMock(
                    side_effect=ValueError(
                        "Non-specific error to force execution of except clause"
                    )
                ),
            )

        sinfo = SC.SysInfo()
        sinfo.show_general_sys_info()
