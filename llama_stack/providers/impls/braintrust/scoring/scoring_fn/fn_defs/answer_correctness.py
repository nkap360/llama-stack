# Copyright (c) Meta Platforms, Inc. and affiliates.
# All rights reserved.
#
# This source code is licensed under the terms described in the LICENSE file in
# the root directory of this source tree.

from llama_stack.apis.common.type_system import NumberType
from llama_stack.apis.scoring_functions import ScoringFnDef


answer_correctness_fn_def = ScoringFnDef(
    identifier="braintrust::answer-correctness",
    description="Test whether an output is factual, compared to an original (`expected`) value. One of Braintrust LLM basd scorer https://github.com/braintrustdata/autoevals/blob/main/py/autoevals/llm.py",
    parameters=[],
    return_type=NumberType(),
)
