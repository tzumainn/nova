# Copyright (c) 2011 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_log import log as logging
from oslo_serialization import jsonutils
import six

from nova.scheduler import filters
from nova.scheduler.filters import extra_specs_ops

LOG = logging.getLogger(__name__)


class OESIFilter(filters.BaseHostFilter):
    """Filter used specifically for OESI."""

    # Instance type and host capabilities do not change within a request
    run_filter_once_per_request = True

    RUN_ON_REBUILD = False

    def host_passes(self, host_state, spec_obj):
        ironic_node_properties = host_state.ironic_node.properties
        return ironic_node_properties.get("available", "") == '*'
