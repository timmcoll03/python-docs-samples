#!/usr/bin/env python

# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

import pytest

import undeploy_model
import vision_object_detection_deploy_model_node_count

PROJECT_ID = os.environ['GCLOUD_PROJECT']
MODEL_ID = 'IOD6143103405779845120'


@pytest.mark.slow
def test_deploy_undeploy_model_with_node_count(capsys):
    undeploy_model.undeploy_model(PROJECT_ID, MODEL_ID)
    out, _ = capsys.readouterr()
    assert 'Model undeployment finished.' in out

    vision_object_detection_deploy_model_node_count.\
        deploy_model_with_node_count(PROJECT_ID, MODEL_ID)
    out, _ = capsys.readouterr()
    assert 'Model deployment finished.' in out