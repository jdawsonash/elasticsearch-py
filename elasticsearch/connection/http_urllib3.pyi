#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import ssl
from typing import Any, Mapping, Optional, Union

import urllib3  # type: ignore

from .base import Connection

def create_ssl_context(
    cafile: Any = ...,
    capath: Any = ...,
    cadata: Any = ...,
) -> ssl.SSLContext: ...

class Urllib3HttpConnection(Connection):
    pool: urllib3.HTTPConnectionPool
    def __init__(
        self,
        host: str = ...,
        port: Optional[int] = ...,
        url_prefix: str = ...,
        timeout: Optional[Union[float, int]] = ...,
        http_auth: Any = ...,
        use_ssl: bool = ...,
        verify_certs: bool = ...,
        ssl_show_warn: bool = ...,
        ca_certs: Optional[Any] = ...,
        client_cert: Optional[Any] = ...,
        client_key: Optional[Any] = ...,
        ssl_version: Optional[Any] = ...,
        ssl_assert_hostname: Optional[Any] = ...,
        ssl_assert_fingerprint: Optional[Any] = ...,
        maxsize: int = ...,
        headers: Optional[Mapping[str, str]] = ...,
        ssl_context: Optional[Any] = ...,
        http_compress: Optional[bool] = ...,
        cloud_id: Optional[str] = ...,
        api_key: Optional[Any] = ...,
        opaque_id: Optional[str] = ...,
        meta_header: bool = ...,
        **kwargs: Any,
    ) -> None: ...
