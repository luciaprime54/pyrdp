#
# This file is part of the PyRDP project.
# Copyright (C) 2022 GoSecure Inc.
# Licensed under the GPLv3 or later.
#

# Disable line-too-long lints.
# flake8: noqa

from enum import IntEnum


class NtStatusSeverity(IntEnum):
    """
    [MS-ERREF]: Windows Error Codes
    https://msdn.microsoft.com/en-us/library/cc231199.aspx
    [MS-ERREF]: NTSTATUS
    https://msdn.microsoft.com/en-us/library/cc231200.aspx
    """
    STATUS_SEVERITY_SUCCESS = 0x0
    STATUS_SEVERITY_INFORMATIONAL = 0x1
    STATUS_SEVERITY_WARNING = 0x2
    STATUS_SEVERITY_ERROR = 0x3


class NTSTATUS(IntEnum):
    """
    [MS-ERREF]: Windows Error Codes
    https://learn.microsoft.com/en-us/openspecs/windows_protocols/ms-erref/87fba13e-bf06-450e-83b1-9241dc81e781
    """

    # Various RDP clients can return other error codes.
    # Instead of listing every Windows Error code,
    # we just list the ones we care about, and create a 'catch-all' value
    @classmethod
    def _missing_(cls, value):
        """
        Handle a missing Windows error code by dynamically creating it
        :param value: The error code
        """
        other = NTSTATUS(0x00000000)
        other._name_ = "STATUS_PYRDP_FAILURE"
        other._value_ = value
        return other

    STATUS_SUCCESS       = 0x00000000
    STATUS_NO_MORE_FILES = 0x80000006
    STATUS_NO_SUCH_FILE  = 0xC000000F
    STATUS_ACCESS_DENIED = 0xC0000022
