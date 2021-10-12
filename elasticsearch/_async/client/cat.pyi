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

from typing import Any, Collection, MutableMapping, Optional, Tuple, Union

from ._base import NamespacedClient

class CatClient(NamespacedClient):
    async def aliases(
        self,
        *,
        name: Optional[Any] = ...,
        expand_wildcards: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def allocation(
        self,
        *,
        node_id: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def count(
        self,
        *,
        index: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def health(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        ts: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def help(
        self,
        *,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def indices(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        expand_wildcards: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        health: Optional[Any] = ...,
        help: Optional[Any] = ...,
        include_unloaded_segments: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        pri: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def master(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def nodes(
        self,
        *,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        full_id: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        include_unloaded_segments: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def recovery(
        self,
        *,
        index: Optional[Any] = ...,
        active_only: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        detailed: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def shards(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def segments(
        self,
        *,
        index: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def pending_tasks(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def thread_pool(
        self,
        *,
        thread_pool_patterns: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def fielddata(
        self,
        *,
        fields: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def plugins(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        include_bootstrap: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def nodeattrs(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def repositories(
        self,
        *,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def snapshots(
        self,
        *,
        repository: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        ignore_unavailable: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def tasks(
        self,
        *,
        actions: Optional[Any] = ...,
        detailed: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        nodes: Optional[Any] = ...,
        parent_task_id: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def templates(
        self,
        *,
        name: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        local: Optional[Any] = ...,
        master_timeout: Optional[Any] = ...,
        s: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def ml_data_frame_analytics(
        self,
        *,
        id: Optional[Any] = ...,
        allow_no_match: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def ml_datafeeds(
        self,
        *,
        datafeed_id: Optional[Any] = ...,
        allow_no_datafeeds: Optional[Any] = ...,
        allow_no_match: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def ml_jobs(
        self,
        *,
        job_id: Optional[Any] = ...,
        allow_no_jobs: Optional[Any] = ...,
        allow_no_match: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def ml_trained_models(
        self,
        *,
        model_id: Optional[Any] = ...,
        allow_no_match: Optional[Any] = ...,
        bytes: Optional[Any] = ...,
        format: Optional[Any] = ...,
        from_: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        size: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
    async def transforms(
        self,
        *,
        transform_id: Optional[Any] = ...,
        allow_no_match: Optional[Any] = ...,
        format: Optional[Any] = ...,
        from_: Optional[Any] = ...,
        h: Optional[Any] = ...,
        help: Optional[Any] = ...,
        s: Optional[Any] = ...,
        size: Optional[Any] = ...,
        time: Optional[Any] = ...,
        v: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        ignore: Optional[Union[int, Collection[int]]] = ...,
        opaque_id: Optional[str] = ...,
        http_auth: Optional[Union[str, Tuple[str, str]]] = ...,
        api_key: Optional[Union[str, Tuple[str, str]]] = ...,
        params: Optional[MutableMapping[str, Any]] = ...,
        headers: Optional[MutableMapping[str, str]] = ...,
    ) -> Any: ...
