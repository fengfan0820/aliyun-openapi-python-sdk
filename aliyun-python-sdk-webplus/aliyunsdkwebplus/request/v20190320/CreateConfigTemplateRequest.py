# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RoaRequest
from aliyunsdkwebplus.endpoint import endpoint_data

class CreateConfigTemplateRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'WebPlus', '2019-03-20', 'CreateConfigTemplate','webx')
		self.set_uri_pattern('/pop/v1/wam/configTemplate')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_OptionSettings(self):
		return self.get_body_params().get('OptionSettings')

	def set_OptionSettings(self,OptionSettings):
		self.add_body_params('OptionSettings', OptionSettings)

	def get_SourceTemplateId(self):
		return self.get_body_params().get('SourceTemplateId')

	def set_SourceTemplateId(self,SourceTemplateId):
		self.add_body_params('SourceTemplateId', SourceTemplateId)

	def get_AppId(self):
		return self.get_body_params().get('AppId')

	def set_AppId(self,AppId):
		self.add_body_params('AppId', AppId)

	def get_StackId(self):
		return self.get_body_params().get('StackId')

	def set_StackId(self,StackId):
		self.add_body_params('StackId', StackId)

	def get_ProfileName(self):
		return self.get_body_params().get('ProfileName')

	def set_ProfileName(self,ProfileName):
		self.add_body_params('ProfileName', ProfileName)

	def get_TemplateName(self):
		return self.get_body_params().get('TemplateName')

	def set_TemplateName(self,TemplateName):
		self.add_body_params('TemplateName', TemplateName)

	def get_SourceEnvId(self):
		return self.get_body_params().get('SourceEnvId')

	def set_SourceEnvId(self,SourceEnvId):
		self.add_body_params('SourceEnvId', SourceEnvId)

	def get_PkgVersionId(self):
		return self.get_body_params().get('PkgVersionId')

	def set_PkgVersionId(self,PkgVersionId):
		self.add_body_params('PkgVersionId', PkgVersionId)

	def get_TemplateDescription(self):
		return self.get_body_params().get('TemplateDescription')

	def set_TemplateDescription(self,TemplateDescription):
		self.add_body_params('TemplateDescription', TemplateDescription)