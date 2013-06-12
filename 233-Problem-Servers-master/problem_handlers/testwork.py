#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#

import base_handler
import math
import random
import json
import logging

class Testwork(base_handler.BaseHandler):
  valid_types = [
    "testwork"    # Description to Components
  ]
  
  def data_for_question(self,question_type):
      num1 = self.generator.randint(0,100)
      num2 = self.generator.randint(0,100)
      answer = (num1+num2) #tag
      description = 'Given ' + str(num1) + ' and  ' + str(num2) + ' what is the sum?'
      return {"description":description, "answer":answer}
    

  def score_student_answer(self,question_type,question_data,student_answer):
      wanted = self.get_description_string(question_data)
      if wanted == student_answer:
        return (100.0, wanted)
      else:
        return (0.0,wanted)
    

  def get_description_string(self,description):
    return "%i" % (description["answer"])
