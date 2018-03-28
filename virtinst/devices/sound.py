#
# Copyright 2008-2009, 2013-2014 Red Hat, Inc.
# Cole Robinson <crobinso@redhat.com>
#
# This work is licensed under the GNU GPLv2.
# See the COPYING file in the top-level directory.

from .device import Device
from ..xmlbuilder import XMLProperty


class DeviceSound(Device):
    XML_NAME = "sound"

    MODEL_DEFAULT = "default"
    MODELS = ["es1370", "sb16", "pcspk", "ac97", "ich6", "ich9"]

    model = XMLProperty("./@model",
                        default_cb=lambda s: "es1370",
                        default_name=MODEL_DEFAULT)