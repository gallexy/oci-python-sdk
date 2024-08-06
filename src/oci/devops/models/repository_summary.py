# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RepositorySummary(object):
    """
    Summary of the repository.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RepositorySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RepositorySummary.
        :type id: str

        :param name:
            The value to assign to the name property of this RepositorySummary.
        :type name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this RepositorySummary.
        :type compartment_id: str

        :param project_id:
            The value to assign to the project_id property of this RepositorySummary.
        :type project_id: str

        :param parent_repository_id:
            The value to assign to the parent_repository_id property of this RepositorySummary.
        :type parent_repository_id: str

        :param namespace:
            The value to assign to the namespace property of this RepositorySummary.
        :type namespace: str

        :param project_name:
            The value to assign to the project_name property of this RepositorySummary.
        :type project_name: str

        :param description:
            The value to assign to the description property of this RepositorySummary.
        :type description: str

        :param default_branch:
            The value to assign to the default_branch property of this RepositorySummary.
        :type default_branch: str

        :param repository_type:
            The value to assign to the repository_type property of this RepositorySummary.
        :type repository_type: str

        :param ssh_url:
            The value to assign to the ssh_url property of this RepositorySummary.
        :type ssh_url: str

        :param http_url:
            The value to assign to the http_url property of this RepositorySummary.
        :type http_url: str

        :param mirror_repository_config:
            The value to assign to the mirror_repository_config property of this RepositorySummary.
        :type mirror_repository_config: oci.devops.models.MirrorRepositoryConfig

        :param time_created:
            The value to assign to the time_created property of this RepositorySummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this RepositorySummary.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RepositorySummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this RepositorySummary.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this RepositorySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this RepositorySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this RepositorySummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'name': 'str',
            'compartment_id': 'str',
            'project_id': 'str',
            'parent_repository_id': 'str',
            'namespace': 'str',
            'project_name': 'str',
            'description': 'str',
            'default_branch': 'str',
            'repository_type': 'str',
            'ssh_url': 'str',
            'http_url': 'str',
            'mirror_repository_config': 'MirrorRepositoryConfig',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'compartment_id': 'compartmentId',
            'project_id': 'projectId',
            'parent_repository_id': 'parentRepositoryId',
            'namespace': 'namespace',
            'project_name': 'projectName',
            'description': 'description',
            'default_branch': 'defaultBranch',
            'repository_type': 'repositoryType',
            'ssh_url': 'sshUrl',
            'http_url': 'httpUrl',
            'mirror_repository_config': 'mirrorRepositoryConfig',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._name = None
        self._compartment_id = None
        self._project_id = None
        self._parent_repository_id = None
        self._namespace = None
        self._project_name = None
        self._description = None
        self._default_branch = None
        self._repository_type = None
        self._ssh_url = None
        self._http_url = None
        self._mirror_repository_config = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RepositorySummary.
        The OCID of the repository. This value is unique and immutable.


        :return: The id of this RepositorySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RepositorySummary.
        The OCID of the repository. This value is unique and immutable.


        :param id: The id of this RepositorySummary.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this RepositorySummary.
        Name of the repository. Should be unique within the project. This value is mutable.


        :return: The name of this RepositorySummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this RepositorySummary.
        Name of the repository. Should be unique within the project. This value is mutable.


        :param name: The name of this RepositorySummary.
        :type: str
        """
        self._name = name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this RepositorySummary.
        The OCID of the repository's compartment.


        :return: The compartment_id of this RepositorySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this RepositorySummary.
        The OCID of the repository's compartment.


        :param compartment_id: The compartment_id of this RepositorySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def project_id(self):
        """
        **[Required]** Gets the project_id of this RepositorySummary.
        The OCID of the DevOps project containing the repository.


        :return: The project_id of this RepositorySummary.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """
        Sets the project_id of this RepositorySummary.
        The OCID of the DevOps project containing the repository.


        :param project_id: The project_id of this RepositorySummary.
        :type: str
        """
        self._project_id = project_id

    @property
    def parent_repository_id(self):
        """
        Gets the parent_repository_id of this RepositorySummary.
        The OCID of the parent repository.


        :return: The parent_repository_id of this RepositorySummary.
        :rtype: str
        """
        return self._parent_repository_id

    @parent_repository_id.setter
    def parent_repository_id(self, parent_repository_id):
        """
        Sets the parent_repository_id of this RepositorySummary.
        The OCID of the parent repository.


        :param parent_repository_id: The parent_repository_id of this RepositorySummary.
        :type: str
        """
        self._parent_repository_id = parent_repository_id

    @property
    def namespace(self):
        """
        Gets the namespace of this RepositorySummary.
        Tenancy unique namespace.


        :return: The namespace of this RepositorySummary.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this RepositorySummary.
        Tenancy unique namespace.


        :param namespace: The namespace of this RepositorySummary.
        :type: str
        """
        self._namespace = namespace

    @property
    def project_name(self):
        """
        Gets the project_name of this RepositorySummary.
        Unique project name in a namespace.


        :return: The project_name of this RepositorySummary.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """
        Sets the project_name of this RepositorySummary.
        Unique project name in a namespace.


        :param project_name: The project_name of this RepositorySummary.
        :type: str
        """
        self._project_name = project_name

    @property
    def description(self):
        """
        Gets the description of this RepositorySummary.
        Details of the repository. Avoid entering confidential information.


        :return: The description of this RepositorySummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RepositorySummary.
        Details of the repository. Avoid entering confidential information.


        :param description: The description of this RepositorySummary.
        :type: str
        """
        self._description = description

    @property
    def default_branch(self):
        """
        Gets the default_branch of this RepositorySummary.
        The default branch of the repository.


        :return: The default_branch of this RepositorySummary.
        :rtype: str
        """
        return self._default_branch

    @default_branch.setter
    def default_branch(self, default_branch):
        """
        Sets the default_branch of this RepositorySummary.
        The default branch of the repository.


        :param default_branch: The default_branch of this RepositorySummary.
        :type: str
        """
        self._default_branch = default_branch

    @property
    def repository_type(self):
        """
        Gets the repository_type of this RepositorySummary.
        Type of repository. Allowed values:
        `MIRRORED`
        `HOSTED`
        `FORKED`


        :return: The repository_type of this RepositorySummary.
        :rtype: str
        """
        return self._repository_type

    @repository_type.setter
    def repository_type(self, repository_type):
        """
        Sets the repository_type of this RepositorySummary.
        Type of repository. Allowed values:
        `MIRRORED`
        `HOSTED`
        `FORKED`


        :param repository_type: The repository_type of this RepositorySummary.
        :type: str
        """
        self._repository_type = repository_type

    @property
    def ssh_url(self):
        """
        Gets the ssh_url of this RepositorySummary.
        SSH URL that you use to git clone, pull and push.


        :return: The ssh_url of this RepositorySummary.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        """
        Sets the ssh_url of this RepositorySummary.
        SSH URL that you use to git clone, pull and push.


        :param ssh_url: The ssh_url of this RepositorySummary.
        :type: str
        """
        self._ssh_url = ssh_url

    @property
    def http_url(self):
        """
        Gets the http_url of this RepositorySummary.
        HTTP URL that you use to git clone, pull and push.


        :return: The http_url of this RepositorySummary.
        :rtype: str
        """
        return self._http_url

    @http_url.setter
    def http_url(self, http_url):
        """
        Sets the http_url of this RepositorySummary.
        HTTP URL that you use to git clone, pull and push.


        :param http_url: The http_url of this RepositorySummary.
        :type: str
        """
        self._http_url = http_url

    @property
    def mirror_repository_config(self):
        """
        Gets the mirror_repository_config of this RepositorySummary.

        :return: The mirror_repository_config of this RepositorySummary.
        :rtype: oci.devops.models.MirrorRepositoryConfig
        """
        return self._mirror_repository_config

    @mirror_repository_config.setter
    def mirror_repository_config(self, mirror_repository_config):
        """
        Sets the mirror_repository_config of this RepositorySummary.

        :param mirror_repository_config: The mirror_repository_config of this RepositorySummary.
        :type: oci.devops.models.MirrorRepositoryConfig
        """
        self._mirror_repository_config = mirror_repository_config

    @property
    def time_created(self):
        """
        Gets the time_created of this RepositorySummary.
        The time the repository was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_created of this RepositorySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RepositorySummary.
        The time the repository was created. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_created: The time_created of this RepositorySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this RepositorySummary.
        The time the repository was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :return: The time_updated of this RepositorySummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this RepositorySummary.
        The time the repository was updated. Format defined by `RFC3339`__.

        __ https://datatracker.ietf.org/doc/html/rfc3339


        :param time_updated: The time_updated of this RepositorySummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RepositorySummary.
        The current state of the repository.


        :return: The lifecycle_state of this RepositorySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RepositorySummary.
        The current state of the repository.


        :param lifecycle_state: The lifecycle_state of this RepositorySummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this RepositorySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this RepositorySummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this RepositorySummary.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this RepositorySummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this RepositorySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this RepositorySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this RepositorySummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See `Resource Tags`__. Example: `{\"bar-key\": \"value\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this RepositorySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this RepositorySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this RepositorySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this RepositorySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__. Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this RepositorySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this RepositorySummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this RepositorySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this RepositorySummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces. See `Resource Tags`__. Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this RepositorySummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
