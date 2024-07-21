# Mediaflex Data Dictionary

## 1.  MDD_ACCESS_STATUS*

> The accessibility to the Public of a Media Item.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key.  Unique ID of Access Status |  |
| 2         | STATUS_ID | NUMBER | NO | Unique identifier of the status type |  |
| 3         | ACCESS_STATUS_NAME | VARCHAR2 | NO | Name of status type |  |
| 4         | ACCESS_STATUS_CODE | VARCHAR2 | NO |  |  |
| 5         | MEDIA_ID_FK | NUMBER | NO | Foreign key. Links to MDD_MEDIA |  |
| 6         | DECISION_DATE | DATE | NO | Date of the access status decision |  |
| 7         | MODIFIED_DATE | DATE | NO | Date modified |  |

## 2.  MDD_ACQUISITIONS*

> Provides overall information about an acqusition.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | STOCK_CHECK_ID | NUMBER | YES | Foreign Key.  Linking Carrier to a particular stock check list |  |
| 2         | STOCK_CHECK_STATE_ID | NUMBER | YES | ID of stock check state.  Can be used for efficient querying and or |  |
| 3         | STOCK_CHECK_STATE | VARCHAR2 | YES | Description of stock check state |  |
| 4         | STOCK_CHECK_BY | VARCHAR2 | YES | Name of user who performed stock check |  |
| 5         | STOCK_CHECK_DATE | DATE | YES | Date of most recent stock check |  |
| 6         | CONTAINER_LENGTH | NUMBER | YES | Length of Carrier (derived from xml metadata) |  |
| 7         | LOGIN_DATE | DATE | YES | The date the Carrier was logged into Mediaflex |  |
| 8         | LAST_OUT_NAME_ID_FK | NUMBER | YES | Foreign Key. Linking to MDD_NAMES |  |

## 3.  MDD_ACQ_CATEGORY

> List of TV standards available in the system.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ACQ_ID_FK | NUMBER | NO | Foreign Key.  Joins with the MDD_ACQUISITIONS.ACQ_ID to join an |  |
| 2         | CAT_ID | NUMBER | NO | Primary Key |  |
| 3         | CATEGORY_NAME | VARCHAR2 | NO | Full Category Name |  |
| 4         | CATEGORY_DESCRIPTION | VARCHAR2 | YES | Description of Category |  |

## 4.  MDD_ACQ_CONTAINERS

> Provides information about the containers in an acquisition.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | OBJECT_DESCRIPTION | VARCHAR2 | YES | Description of the Object |  |
| 2         | PARENT_ID | NUMBER | YES | Provides link to acquisition container.  (Superceded by |  |
| 3         | OBJECT_TYPE | NUMBER | NO | Identifies the Type of the Object |  |
| 4         | MEDIA_ID2_FK | VARCHAR2 | YES | Foreign Key.  Links to MDD_MEDIA.MEDIA_ID2 to link Acquisitions |  |
| 5         | OBJECT_BARCODE | VARCHAR2 | YES | Barcode of acquisition object |  |
| 6         | ACQ_EXTERNAL_REF1 | VARCHAR2 | YES | Third party reference for object |  |
| 7         | MEDIUM | VARCHAR2 | YES | Description of object’s medium, eg: Audio, Documentation, Artefact |  |
| 8         | SUB_MEDIUM | VARCHAR2 | YES | Description of object’s sub-medium, eg: Film, Sound Recording etc. |  |
| 9         | FORM | VARCHAR2 | YES | Describes the object’s form, eg: Actuality, Advertisement etc. |  |
| 10         | OBJECT_FORMAT | VARCHAR2 | YES | Physical format of the object, eg: Tape, Disc, Paper etc. |  |
| 11         | CONTAINER_STATUS_ID | NUMBER | YES | ID of the Status of the Container the Object is in |  |
| 12         | CONTAINER_STATUS_DESC | VARCHAR2 | YES | Status of the Container the Object is in |  |
| 13         | ACCESSION_STATUS | VARCHAR2 | YES | Accession Status of Object |  |
| 14         | QTY_RECEIVED | NUMBER | YES | Total number of objects received |  |
| 15         | QTY_NOT_SELECTED | NUMBER | YES | Total number of objects not selected |  |
| 16         | QTY_REMAINING | NUMBER | YES | Total number of objects remaining |  |
| 17         | QTY_SELECTED | NUMBER | YES | Total number of objects selected |  |
| 18         | QTY_ACCESSIONED | NUMBER | YES | Total number of objects accessioned |  |
| 19         | QTY_AWAITING_ACCESSIONING | NUMBER | YES | Total number of objects awaiting accessioning |  |
| 20         | DATE_EXPECTED | DATE | YES | Date that the Acquisition Object is expected to be received |  |
| 21         | DATE_RECEIVED | DATE | YES | Date that the Acquisition Object was received |  |
| 22         | ARTICLE_LAST_MOVED | DATE | YES | The date the Article was last moved |  |
| 23         | OBJECT_NOTES | CLOB | YES | Notes associated with the Object |  |
| 24         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links to the Job that an Acquisition Object is linked to |  |
| 25         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS |  |
| 26         | ARTICLE_BARCODE | VARCHAR2 | YES | Barcode of Physical Article |  |
| 27         | ARTICLE_FILENAME | VARCHAR2 | YES | Filename of Digital Article |  |
| 28         | DISPOSAL_CLASS_NO | NUMBER | YES | Disposal Class Number of Article |  |
| 29         | ARTICLE_EXT_REF1 | VARCHAR2 | YES | External Reference 1 number for Article |  |
| 30         | ARTICLE_EXT_REF2 | VARCHAR2 | YES | External Reference 1 number for Article |  |
| 31         | CREATED_DATE | DATE | YES | Date Article created |  |

## 5.  MDD_ACQ_OBJECTS

> Provides information about the objects in an acqusition.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | OBJECT_ID | NUMBER | NO | Primary Key |  |
| 2         | ACQ_ID | NUMBER | YES | Foreign Key.  Links to MDD_ACQUISITIONS.ACQ_ID to link |  |
| 3         | ACQ_CONTAINER_ID_FK | NUMBER | YES | Foreign Key.  Joins with the |  |

## 6.  MDD_ACQ_TYPES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ACQ_TYPE_ID | NUMBER | NO | Primary Key. Acquisition Type ID |  |
| 2         | ACQ_TYPE_NAME | VARCHAR2 | NO | Acquisition Type Name |  |
| 3         | ACQ_TYPE_CODE | VARCHAR2 | YES | Acquisition Type Code. |  |
| 4         | ACQ_TYPE_CATEGORY | VARCHAR2 | YES | Acquisition Type Category |  |
| 5         | ACQ_TYPE_ELEMENT | VARCHAR2 | YES | Acquisition Type Element |  |

## 7.  MDD_ACTION_HISTORY

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ACTION | VARCHAR2 | YES |  |  |
| 2         | ITEM_TYPE | VARCHAR2 | YES |  |  |
| 3         | USER_NAME | VARCHAR2 | YES |  |  |
| 4         | ITEM_ID | NUMBER | YES |  |  |
| 5         | ITEM_DETAILS | VARCHAR2 | YES |  |  |
| 6         | PC | VARCHAR2 | YES |  |  |
| 7         | LAST_ACCESSED | DATE | YES |  |  |

## 8.  MDD_ALT_NAMES*

> Provides information about the alternative names linked to a name authority.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | NAME_ID_FK | NUMBER | YES | Foreign Key. Provides link to MDD_NAMES |  |
| 2         | ALT_NAME_ID | NUMBER | YES | Primary Key.  ID of Alternative Name |  |
| 3         | ALTERNATIVE_NAME | VARCHAR2 | YES | Alternative Name |  |
| 4         | DATES | VARCHAR2 | YES | Dates Alternative Name used |  |

## 9.  MDD_ASPECT_RATIO

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | LEGACY_VALUE | NUMBER | YES | Primary Key.  Legacy aspect ratio ID. |  |
| 2         | AFD_CODE | VARCHAR2 | YES | AFD code linked to legacy value. |  |
| 3         | DESCRIPTION | NVARCHAR2 | YES | Description of aspect ratio. |  |

## 10.  MDD_AUDIO_FROM_MIS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | YES | Foreign Key.  Linking Audio to Media |  |
| 2         | AU_NM | VARCHAR2 | YES | Track number |  |
| 3         | AU_CONT_ID | VARCHAR2 | YES | Audio content ID.  For internal use only. |  |
| 4         | AUDIO_CONTENT | NVARCHAR2 | YES | Description of audio content, eg: Full Mix |  |
| 5         | AUDIO_CONTENT_TAG | NVARCHAR2 | YES | Code for Audio content |  |
| 6         | AU_LANG_ID | VARCHAR2 | YES | Audio language ID. For internal use only. |  |
| 7         | AUDIO_LANGUAGE | VARCHAR2 | YES | Audio language |  |
| 8         | AUDIO_LANGUAGE_CODE | VARCHAR2 | YES | Code of audio language |  |
| 9         | AU_MS_ID | VARCHAR2 | YES | Mono/Stereo ID.  For internal use only. |  |
| 10         | AU_NR_ID | VARCHAR2 | YES | Noise Reduction ID.  For internal use only. |  |
| 11         | QC_STATUS | VARCHAR2 | YES | Audio QC status |  |
| 12         | LANGUAGE_TAG | VARCHAR2 | YES | SAP |  |
| 13         | LANGUAGE_TAG_DESC | VARCHAR2 | YES | Description of Language Tag |  |
| 14         | LANGUAGE_ISO_CODE | VARCHAR2 | YES | ISO Code for the Language |  |
| 15         | INTERNATIONAL_AUDIO | NUMBER | YES | Indicates whether the track has International Audio or not |  |

## 11.  MDD_AUTOPURGE_HISTORY

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MFX_DEVICE_ID | NUMBER | NO | Unique ID of Mediaflex device. |  |
| 2         | MFX_DEVICE_NAME | VARCHAR2 | NO | Name of Mediaflex device. |  |
| 3         | MFX_DEVICE_CODE | VARCHAR2 | NO | Code of Mediaflex device. |  |
| 4         | MFX_DEVICE_TYPE | VARCHAR2 | YES | Type of Mediaflex device. |  |
| 5         | DEVICE_NOTES | VARCHAR2 | YES | User notes for Mediaflex device. |  |
| 6         | DEVICE_LOCATION | VARCHAR2 | YES | Location that the device points to |  |
| 7         | PURGE_RULE_NAME | VARCHAR2 | YES | Name of the autopurge rule. |  |
| 8         | ACTIVE | NUMBER | YES | Denotes whether or not the autopurge rule is active |  |
| 9         | LOG_ONLY | NUMBER | YES | Denotes if the autopurge rule is set to Log Only. |  |
| 10         | SCHEDULE | VARCHAR2 | YES | Denotes when the autopurge rule is scheduled to run. |  |
| 11         | CREATED_DATE | DATE | YES | Date that the autopurge rule was created. |  |
| 12         | CREATED_BY | VARCHAR2 | YES | User that created the autopurge rule. |  |
| 13         | MODIFIED_DATE | DATE | YES | Date that the autopurge rule was last modified. |  |
| 14         | MODIFIED_BY | VARCHAR2 | YES | User that last modified the autopurge rule. |  |

## 12.  MDD_BOX_CONTAINER_TYPES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | FORMAT_NAME | VARCHAR2 | YES |  |  |
| 2         | FORMAT_SHORTCODE | VARCHAR2 | YES | Name of Container Format. |  |
| 3         | HEIGHT | NUMBER | YES | Container height |  |
| 4         | WIDTH | NUMBER | YES | Container width |  |
| 5         | DEPTH | NUMBER | YES | Container depth |  |
| 6         | WEIGHT | NUMBER | YES | Container depth |  |
| 7         | SHM | NUMBER | YES | Container shelf metres in mm |  |

## 13.  MDD_CHANNEL_GROUPS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | GROUP_ID | NUMBER | YES | Primary Key.  Unique ID of Group |  |
| 2         | GROUP_CODE | VARCHAR2 | YES | Code of Group |  |
| 3         | GROUP_NAME | VARCHAR2 | YES | Name of Group |  |
| 4         | CHANNEL_CODE | VARCHAR2 | YES | Code of Channel in Group |  |
| 5         | ACTIVE | NUMBER | YES | Boolean value indicating whether the Group is active or not |  |

## 14.  MDD_CODES_ASPECT_RATIO

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | AR_ID | NUMBER | NO |  |  |
| 2         | AR_NAME | VARCHAR2 | YES |  |  |
| 3         | AR_CODE | VARCHAR2 | YES |  |  |
| 4         | ACTIVE | NUMBER | NO |  |  |

## 15.  MDD_CODES_CHANNELS*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CHANNEL_ID | NUMBER | NO |  |  |
| 2         | CHANNEL_CODE | VARCHAR2 | NO |  |  |
| 3         | NAME | VARCHAR2 | NO |  |  |
| 4         | PARENT_CHANNEL | VARCHAR2 | YES |  |  |
| 5         | ACTIVE | NUMBER | YES |  |  |
| 6         | PRIORITY | NUMBER | YES |  |  |

## 16.  MDD_CODES_CULTURAL_STATUS*

> List of Cultural Statuses available for use in the system.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CULTURAL_STATUS_ID | NUMBER | NO | Unique ID of the Cultural Status |  |
| 2         | CULTURAL_STATUS_CODE | NVARCHAR2 | YES | Code of Cultural Status |  |
| 3         | CULTURAL_STATUS_NAME | NVARCHAR2 | NO | Name of Cultural Status |  |
| 4         | CULTURAL_STATUS_DESCRIPTION | NVARCHAR2 | YES | Description of Cultural Status |  |
| 5         | ACTIVE | NUMBER | NO | Boolean value indicating whether the Cultural Status is active or not |  |

## 17.  MDD_CODES_DEVICES*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | DEVICE_ID | NUMBER | NO |  |  |
| 2         | DEVICE_NAME | VARCHAR2 | NO |  |  |
| 3         | DEVICE_TYPE | NUMBER | YES |  |  |
| 4         | DEVICE_TYPE_NAME | VARCHAR2 | YES |  |  |
| 5         | DEVICE_PATH | VARCHAR2 | YES |  |  |
| 6         | DEVICE_REF | VARCHAR2 | YES |  |  |
| 7         | CREATED_DATE | DATE | NO |  |  |
| 8         | CREATED_BY | VARCHAR2 | NO |  |  |
| 9         | MODIFIED_DATE | DATE | YES |  |  |
| 10         | MODIFIED_BY | VARCHAR2 | YES |  |  |

## 18.  MDD_CODES_TASK_TYPES*

> This view provides information about a specific task.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_TYPE_ID | NUMBER | YES | Primary Key.  ID can be used to link from MDD_TASKS to get Task |  |
| 2         | TASK_TYPE | VARCHAR2 | YES | Description of Task Type. |  |

## 19.  MDD_CODES_TEC_DETAILS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TEC_NAME_ID | NUMBER | YES | Primary Key.  Unique ID for Technical Condition or Treatment |  |
| 2         | TEC_TYPE_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_CODES_TEC_TYPE |  |
| 3         | TEC_CODE | VARCHAR2 | YES | Code of Technical Condition or Treatment |  |
| 4         | TEC_NAME | VARCHAR2 | YES | Description of Technical Condition or Treatment |  |
| 5         | TYPE | CHAR | YES | Indicates whether this is a Condition or a Treatment |  |
| 6         | ACTIVE | NUMBER | YES | Boolean value indicating whether the Group is active or not |  |

## 20.  MDD_CODES_TEC_TYPE

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TEC_TYPE_ID | NUMBER | YES | Primary Key.  Unique ID of Type |  |
| 2         | TEC_TYPE_NAME | VARCHAR2 | YES | Type of material associated with the Condition or Treatment, eg |  |
| 3         | ACTIVE | NUMBER | YES | Boolean value indicating whether the Group is active or not |  |

## 21.  MDD_CODES_TVSTD

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TVSTD_ID | NUMBER | NO | Primary Key.  Unique ID of TV Standard |  |
| 2         | NAME | NVARCHAR2 | NO | TV Standard name |  |
| 3         | LINES | NUMBER | NO | Lines associated with TV Standard |  |
| 4         | FPS | NUMBER | YES | Frames Per Second |  |
| 5         | DROP_FRAME | NUMBER | NO | Indicates whether this TV Standard uses a Drop Frame |  |
| 6         | CODE | VARCHAR2 | YES | Mediaflex RESTful API code |  |

## 22.  MDD_CONTAINERS*

> Provides details of carriers.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CONTAINER_ID | NUMBER | NO | Primary Key.  Unique ID of Carrier |  |
| 2         | BARCODE | VARCHAR2 | YES | Barcode of Carrier |  |
| 3         | EXT_ID1 | VARCHAR2 | YES | Free text field available to enter second ID if required |  |
| 4         | EXT_ID2 | VARCHAR2 | YES | Free text field available to enter third ID if required |  |
| 5         | CONTAINER_SERIES_TITLE | VARCHAR2 | YES | Series Title associated with Carrier |  |
| 6         | CONTAINER_TITLE | VARCHAR2 | YES | Title associated with Carrier |  |
| 7         | CONTAINER_TYPE | NUMBER | YES | Value that identifies the type of Carrier |  |
| 8         | RETURN_DATE | DATE | YES | Return by Date |  |
| 9         | CONTAINER_TYPE_CODE | VARCHAR2 | YES |  |  |
| 10         | CONTAINER_TYPE_NAME | VARCHAR2 | YES |  |  |
| 11         | CONTAINED_IN | NUMBER | YES | Foreign Key.  Linking to MDD_CONTAINER for a second Carrier that |  |
| 12         | CONTAINER_OWNERS | VARCHAR2 | YES | Identifies the owner(s) of the Carrier |  |
| 13         | FORMAT_ID | NUMBER | YES | Foreign Key.  Linking format to Carrier using |  |

## 23.  MDD_CONTAINER_CONDITION_TREAT*

> Provides details of conditions and treatments assigned to carriers.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CONTAINER_ID | NUMBER | YES | Foreign Key.  Linking the Condition or Treatment to a Container |  |
| 2         | TEC_NAME_ID_FK | NUMBER | YES | Foreign Key.  Linking Container to Tec Code |  |
| 3         | CONDITION_CODE | VARCHAR2 | YES | Code of Technical Condition or Treatment |  |
| 4         | DESCRIPTION | VARCHAR2 | YES | Description of condition or treatment of the carrier. |  |
| 5         | CONDITION_TYPE | VARCHAR2 | YES | Type of material associated with the Condition or Treatment, eg |  |
| 6         | TYPE | CHAR | YES | Indicates whether this is a Condition or a Treatment |  |
| 7         | SEVERITY | NUMBER | YES | Indicates the severity of the condition or treatment. |  |
| 8         | DATE_ENTERED | DATE | YES | Date condition or treatment was selected for the container |  |
| 9         | ENTERED_BY | VARCHAR2 | YES | Name of user who selected the condition or treatment of the carrier. |  |
| 10         | DEPT_ID | NUMBER | YES | ID of the Department of the user who selected the condition or |  |
| 11         | DEPT | VARCHAR2 | YES | Name of the Department of the user who selected the condition or |  |
| 12         | NOTES | VARCHAR2 | YES | Free text notes entered for condition or treatment. |  |

## 24.  MDD_CONTAINER_FORMATS*

> List the carrier formats available in the system.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | FORMAT_NAME | VARCHAR2 | NO |  |  |
| 2         | FORMAT_SHORTCODE | VARCHAR2 | YES | Name of Carrier Format |  |
| 3         | HEIGHT | NUMBER | YES | Carrier height |  |
| 4         | WIDTH | NUMBER | YES | Carrier width |  |
| 5         | DEPTH | NUMBER | YES | Carrier depth |  |
| 6         | WEIGHT | NUMBER | YES | Carrier depth |  |
| 7         | SHM | NUMBER | YES | Carrier shelf metres in mm |  |

## 25.  MDD_CONTENT*

> Provides information content of a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CONTENT_ID | NUMBER | NO | Primary Key.  Unique ID of Content |  |
| 2         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links to MDD_VERSIONS |  |
| 3         | CONTENT_VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links to the Content Version in MDD_VERSIONS |  |
| 4         | CONTENT_VERSION_ID1 | VARCHAR2 | YES | VersionID1 of Content Version |  |
| 5         | VERSION_ID1_FK | VARCHAR2 | YES | Foreign Key. Allows for linking to the VersionID1 field |  |
| 6         | LIST_INDEX | NUMBER | YES | Content index |  |
| 7         | TITLE | VARCHAR2 | YES | Content Title |  |
| 8         | MEDIUM | VARCHAR2 | YES | Content Medium |  |
| 9         | SUB_MEDIUM | VARCHAR2 | YES | Content Sub Medium |  |

## 26.  MDD_CONTENT_PURE*

> Further information is required re MDD_CONTENT_PURE.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CONTENT_ID | NUMBER | NO |  |  |
| 2         | PARENT_VERSION_ID_FK | NUMBER | YES |  |  |
| 3         | LIST_INDEX | NUMBER | YES |  |  |
| 4         | CONTENT_TITLE | VARCHAR2 | YES |  |  |

## 27.  MDD_CREDITS*

> Provides information about the credits associated with a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CREDIT_ID | NUMBER | NO | Primary Key.  Unique ID of Credit |  |
| 2         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_VERSIONS |  |
| 3         | ENTITY_ID_FK | NUMBER | NO | Foreign Key.  Links to the Entity in MDD_NAMES that is related to |  |
| 4         | NAME_ID_FK | NUMBER | NO | Foreign Key.  Links to the Name in MDD_NAMES that is related to |  |
| 5         | FULL_NAME | VARCHAR2 | YES | Full name of the Credit |  |
| 6         | ROLE_ID | NUMBER | YES |  |  |
| 7         | ROLE | VARCHAR2 | YES | Role of the Credit |  |
| 8         | CREATED_BY | VARCHAR2 | YES |  |  |
| 9         | CREATED_DATE | DATE | YES |  |  |
| 10         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 11         | MODIFIED_DATE | DATE | YES |  |  |

## 28.  MDD_CRS_SERIES_AGENCY

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CRS_SERIES_ID_FK | NUMBER | NO | Foreign key link to CRS Series |  |
| 2         | CRS_SERIES_NUMBER | VARCHAR2 | NO | CRS Series Number |  |
| 3         | CRS_SERIES_TITLE | VARCHAR2 | NO | CRS Series Title |  |
| 4         | ENTITY_ID_FK | NUMBER | NO | Foreign Key link to Name Authority Entity |  |
| 5         | AGENCY_CODE | VARCHAR2 | YES | Related Agency Code |  |
| 6         | AGENCY_NAME | VARCHAR2 | YES | Related Agency Name |  |
| 7         | RELATION_TYPE | NUMBER | NO | Relationship Type of Agency |  |
| 8         | SERIES_TYPE | VARCHAR2 | YES | Description of CRS Series Type / Predominant Form |  |

## 29.  MDD_DCTC_BBS_DELIVERY_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | XML_ID | NUMBER | NO |  |  |
| 2         | VERSION_ID_FK | NUMBER | YES |  |  |
| 3         | BBS_NETWORK | VARCHAR2 | YES |  |  |
| 4         | BBS_USEPACKAGE_DATES | VARCHAR2 | YES |  |  |
| 5         | BBS_BUGPRESENTINSOURCE | VARCHAR2 | YES |  |  |
| 6         | BBS_PUBLISHTO_AOL | VARCHAR2 | YES |  |  |
| 7         | BBS_PUBLISHTO_BLINKX | VARCHAR2 | YES |  |  |
| 8         | BBS_PUBLISHTO_COMCAST | VARCHAR2 | YES |  |  |
| 9         | BBS_PUBLISHTO_DISH | VARCHAR2 | YES |  |  |
| 10         | BBS_PUBLISHTO_HULU | VARCHAR2 | YES |  |  |
| 11         | BBS_PUBLISHTO_MSN | VARCHAR2 | YES |  |  |
| 12         | BBS_PUBLISHTO_YAHOO | VARCHAR2 | YES |  |  |
| 13         | BBS_PUBLISHTO_YOUTUBE | VARCHAR2 | YES |  |  |
| 14         | BBS_CATEGORY_AOL | VARCHAR2 | YES |  |  |
| 15         | BBS_CATEGORY_COMCAST | VARCHAR2 | YES |  |  |
| 16         | BBS_CATEGORY_HULU | VARCHAR2 | YES |  |  |
| 17         | BBS_SERIESID_COMCAST | VARCHAR2 | YES |  |  |
| 18         | BBS_ISPUBLIC_YOUTUBE | VARCHAR2 | YES |  |  |

## 30.  MDD_DCTC_BBS_MRSS_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | XML_ID | NUMBER | NO |  |  |
| 2         | BBS_PARTNER | VARCHAR2 | YES |  |  |
| 3         | BBS_NETWORK | VARCHAR2 | YES |  |  |
| 4         | VALID_FROM | VARCHAR2 | YES |  |  |
| 5         | VALID_TO | VARCHAR2 | YES |  |  |
| 6         | MASTER_JOB_ID | VARCHAR2 | YES |  |  |
| 7         | PACKAGE_ID | VARCHAR2 | YES |  |  |
| 8         | PAID | VARCHAR2 | YES |  |  |
| 9         | XML_DATA | VARCHAR2 | YES |  |  |
| 10         | CREATED_DATE | VARCHAR2 | YES |  |  |

## 31.  MDD_DCTC_BBS_TITLE_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | XML_ID | NUMBER | NO |  |  |
| 2         | VERSION_ID_FK | NUMBER | YES |  |  |
| 3         | BBS_SERIES_TITLE | VARCHAR2 | YES |  |  |
| 4         | BBS_SOURCE_SERIES_DESC | VARCHAR2 | YES |  |  |
| 5         | BBS_EPISODE_TITLE | VARCHAR2 | YES |  |  |
| 6         | BBS_EPISODE_SHORT_DESC | VARCHAR2 | YES |  |  |
| 7         | BBS_KEYWORDS | VARCHAR2 | YES |  |  |
| 8         | BBS_USESERIESTITLE_AOL | VARCHAR2 | YES |  |  |
| 9         | BBS_SERIESTITLE_AOL | VARCHAR2 | YES |  |  |
| 10         | BBS_USESRCSERIESDESC_AOL | VARCHAR2 | YES |  |  |
| 11         | BBS_SRCSERIESDESC_AOL | VARCHAR2 | YES |  |  |
| 12         | BBS_USEEPISODETITLE_AOL | VARCHAR2 | YES |  |  |
| 13         | BBS_EPISODETITLE_AOL | VARCHAR2 | YES |  |  |
| 14         | BBS_USEEPSHORTDESC_AOL | VARCHAR2 | YES |  |  |
| 15         | BBS_EPISODESHORTDESC_AOL | VARCHAR2 | YES |  |  |
| 16         | BBS_USEKEYWORDS_AOL | VARCHAR2 | YES |  |  |
| 17         | BBS_KEYWORDS_AOL | VARCHAR2 | YES |  |  |
| 18         | BBS_USESERIESTITLE_BLINKX | VARCHAR2 | YES |  |  |
| 19         | BBS_SERIESTITLE_BLINKX | VARCHAR2 | YES |  |  |
| 20         | BBS_USESRCSERIESDESC_BLINKX | VARCHAR2 | YES |  |  |
| 21         | BBS_SRCSERIESDESC_BLINKX | VARCHAR2 | YES |  |  |
| 22         | BBS_USEEPISODETITLE_BLINKX | VARCHAR2 | YES |  |  |
| 23         | BBS_EPISODETITLE_BLINKX | VARCHAR2 | YES |  |  |
| 24         | BBS_USEEPSHORTDESC_BLINKX | VARCHAR2 | YES |  |  |
| 25         | BBS_EPISODESHORTDESC_BLINKX | VARCHAR2 | YES |  |  |
| 26         | BBS_USEKEYWORDS_BLINKX | VARCHAR2 | YES |  |  |
| 27         | BBS_KEYWORDS_BLINKX | VARCHAR2 | YES |  |  |
| 28         | BBS_USESERIESTITLE_COMCAST | VARCHAR2 | YES |  |  |
| 29         | BBS_SERIESTITLE_COMCAST | VARCHAR2 | YES |  |  |
| 30         | BBS_USESRCSERIESDESC_COMCAS | VARCHAR2 | YES |  |  |
| 31         | BBS_SRCSERIESDESC_COMCAST | VARCHAR2 | YES |  |  |
| 32         | BBS_USEEPISODETITLE_COMCAST | VARCHAR2 | YES |  |  |
| 33         | BBS_EPISODETITLE_COMCAST | VARCHAR2 | YES |  |  |
| 34         | BBS_USEEPSHORTDESC_COMCAST | VARCHAR2 | YES |  |  |
| 35         | BBS_EPISODESHORTDESC_COMCAS | VARCHAR2 | YES |  |  |
| 36         | BBS_USESERIESTITLE_DISH | VARCHAR2 | YES |  |  |
| 37         | BBS_SERIESTITLE_DISH | VARCHAR2 | YES |  |  |
| 38         | BBS_USESRCSERIESDESC_DISH | VARCHAR2 | YES |  |  |
| 39         | BBS_SRCSERIESDESC_DISH | VARCHAR2 | YES |  |  |
| 40         | BBS_USEEPISODETITLE_DISH | VARCHAR2 | YES |  |  |
| 41         | BBS_EPISODETITLE_DISH | VARCHAR2 | YES |  |  |
| 42         | BBS_USEEPSHORTDESC_DISH | VARCHAR2 | YES |  |  |
| 43         | BBS_EPISODESHORTDESC_DISH | VARCHAR2 | YES |  |  |
| 44         | BBS_USESERIESTITLE_HULU | VARCHAR2 | YES |  |  |
| 45         | BBS_SERIESTITLE_HULU | VARCHAR2 | YES |  |  |
| 46         | BBS_USESRCSERIESDESC_HULU | VARCHAR2 | YES |  |  |
| 47         | BBS_SRCSERIESDESC_HULU | VARCHAR2 | YES |  |  |
| 48         | BBS_USEEPISODETITLE_HULU | VARCHAR2 | YES |  |  |
| 49         | BBS_EPISODETITLE_HULU | VARCHAR2 | YES |  |  |
| 50         | BBS_USEEPSHORTDESC_HULU | VARCHAR2 | YES |  |  |
| 51         | BBS_EPISODESHORTDESC_HULU | VARCHAR2 | YES |  |  |
| 52         | BBS_USEKEYWORDS_HULU | VARCHAR2 | YES |  |  |
| 53         | BBS_KEYWORDS_HULU | VARCHAR2 | YES |  |  |
| 54         | BBS_USESERIESTITLE_MSN | VARCHAR2 | YES |  |  |
| 55         | BBS_SERIESTITLE_MSN | VARCHAR2 | YES |  |  |
| 56         | BBS_USESRCSERIESDESC_MSN | VARCHAR2 | YES |  |  |
| 57         | BBS_SRCSERIESDESC_MSN | VARCHAR2 | YES |  |  |
| 58         | BBS_USEEPISODETITLE_MSN | VARCHAR2 | YES |  |  |
| 59         | BBS_EPISODETITLE_MSN | VARCHAR2 | YES |  |  |
| 60         | BBS_USEEPSHORTDESC_MSN | VARCHAR2 | YES |  |  |
| 61         | BBS_EPISODESHORTDESC_MSN | VARCHAR2 | YES |  |  |
| 62         | BBS_USEKEYWORDS_MSN | VARCHAR2 | YES |  |  |
| 63         | BBS_KEYWORDS_MSN | VARCHAR2 | YES |  |  |
| 64         | BBS_USESERIESTITLE_YAHOO | VARCHAR2 | YES |  |  |
| 65         | BBS_SERIESTITLE_YAHOO | VARCHAR2 | YES |  |  |
| 66         | BBS_USESRCSERIESDESC_YAHOO | VARCHAR2 | YES |  |  |
| 67         | BBS_SRCSERIESDESC_YAHOO | VARCHAR2 | YES |  |  |
| 68         | BBS_USEEPISODETITLE_YAHOO | VARCHAR2 | YES |  |  |
| 69         | BBS_EPISODETITLE_YAHOO | VARCHAR2 | YES |  |  |
| 70         | BBS_USEEPSHORTDESC_YAHOO | VARCHAR2 | YES |  |  |
| 71         | BBS_EPISODESHORTDESC_YAHOO | VARCHAR2 | YES |  |  |
| 72         | BBS_USEKEYWORDS_YAHOO | VARCHAR2 | YES |  |  |
| 73         | BBS_KEYWORDS_YAHOO | VARCHAR2 | YES |  |  |
| 74         | BBS_USESERIESTITLE_YOUTUBE | VARCHAR2 | YES |  |  |
| 75         | BBS_SERIESTITLE_YOUTUBE | VARCHAR2 | YES |  |  |
| 76         | BBS_USESRCSERIESDESC_YOUTUB | VARCHAR2 | YES |  |  |
| 77         | BBS_SRCSERIESDESC_YOUTUBE | VARCHAR2 | YES |  |  |
| 78         | BBS_USEEPISODETITLE_YOUTUBE | VARCHAR2 | YES |  |  |
| 79         | BBS_EPISODETITLE_YOUTUBE | VARCHAR2 | YES |  |  |
| 80         | BBS_USEEPSHORTDESC_YOUTUBE | VARCHAR2 | YES |  |  |
| 81         | BBS_EPISODESHORTDESC_YOUTUB | VARCHAR2 | YES |  |  |
| 82         | BBS_USEKEYWORDS_YOUTUBE | VARCHAR2 | YES |  |  |
| 83         | BBS_KEYWORDS_YOUTUBE | VARCHAR2 | YES |  |  |

## 32.  MDD_DCTC_JOB_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Linking custom metadata to related Job in MDD_JOB |  |
| 2         | CHANNEL_STORAGE_LOCATION | VARCHAR2 | YES | Provides details of the Storage Location specified for the job. |  |

## 33.  MDD_DCTC_MEDEXTENDED_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | YES |  |  |
| 2         | NEW_MEDIA_TYPE | VARCHAR2 | YES |  |  |
| 3         | BBS_PUBLISH | VARCHAR2 | YES |  |  |

## 34.  MDD_DCTC_MEDVERSION_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Provides a link to the related Version |  |
| 2         | WEB_SERIES_TITLE | VARCHAR2 | YES | Series Title assigned by the Web Producer |  |
| 3         | WEB_TITLE | VARCHAR2 | YES | Series Title assigned by the Web Producer |  |
| 4         | WEB_SHORT_DESC | VARCHAR2 | YES | Short Description assigned by the Web Producer |  |
| 5         | SOURCE_PAID | VARCHAR2 | YES | PAID ID for source material used to create media item |  |

## 35.  MDD_DCTC_NLS_RUNDOWN_MEDIA

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_ID | NUMBER | NO | ID of Package linked to Rundown.  Can be used to link to |  |

## 36.  MDD_DCTC_NLS_VUBIQUITY_PLANNER

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_ID_FK | NUMBER | NO |  |  |
| 2         | PROVIDER | VARCHAR2 | YES |  |  |
| 3         | PROVIDER_ID | VARCHAR2 | YES |  |  |
| 4         | ASSET_ID | VARCHAR2 | YES |  |  |
| 5         | PACKAGE_ASSET_ID | VARCHAR2 | YES |  |  |
| 6         | TITLE_ASSET_ID | VARCHAR2 | YES |  |  |
| 7         | MOVIE_ASSET_ID | VARCHAR2 | YES |  |  |
| 8         | POSTER_ART_ASSET_ID | VARCHAR2 | YES |  |  |
| 9         | BOX_COVER_ASSET_ID | VARCHAR2 | YES |  |  |
| 10         | PROVIDER_CONTENT_TIER | VARCHAR2 | YES |  |  |
| 11         | VIDEO_FORMAT | VARCHAR2 | YES |  |  |
| 12         | TITLE | VARCHAR2 | YES |  |  |
| 13         | LICENSING_WINDOW_START | VARCHAR2 | YES |  |  |
| 14         | LICENSING_WINDOW_END | VARCHAR2 | YES |  |  |
| 15         | MOVIE_RUN_TIME | VARCHAR2 | YES |  |  |
| 16         | MOVIE_FILE_NAME | VARCHAR2 | YES |  |  |
| 17         | POSTER_ART_FILE_NAME | VARCHAR2 | YES |  |  |
| 18         | BOX_COVER_FILE_NAME | VARCHAR2 | YES |  |  |
| 19         | MANIFEST_ID | VARCHAR2 | YES |  |  |

## 37.  MDD_DCTC_PACKAGE_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_ID_FK | NUMBER | YES |  |  |
| 2         | USNETS_DISTRIBUTION_CHANNEL | VARCHAR2 | YES |  |  |
| 3         | KEYWORDS | VARCHAR2 | YES |  |  |
| 4         | VIDEO_CATEGORY | VARCHAR2 | YES |  |  |

## 38.  MDD_DCTC_SERIES_CUSTOM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PARENT_SERIES_ID_FK | NUMBER | YES | Foreign Key.  Linking custom metadata to PARENT_SERIES_ID_FK |  |
| 2         | PDS_SERIES_NAME | VARCHAR2 | YES | Series Name from PDS |  |

## 39.  MDD_DIGITAL_FILES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | DFILE_ID | NUMBER | NO | Primary Key.  Unique ID of Digital Carrier |  |
| 2         | DTYPE_ID | NUMBER | YES |  |  |
| 3         | DFILE_TYPE | VARCHAR2 | YES | Description of the Material Type eg Physical A/V Material |  |
| 4         | PATH | VARCHAR2 | YES | Full location (on disk) of the Digital Carrier / File |  |
| 5         | FILENAME | VARCHAR2 | YES | Filename of the digital carrier |  |
| 6         | FILE_EXTENSION | VARCHAR2 | YES |  |  |
| 7         | DEVICE_ID | NUMBER | YES | Foreign Key. Unique ID of the Mediaflex Device that this digital |  |
| 8         | DEVICE_NAME | VARCHAR2 | YES | The text desciption of the linked Mediaflex Device |  |
| 9         | FILESIZE | NUMBER | YES | The size (in bytes) of the digital file |  |
| 10         | CREATED | DATE | NO | Date the Digital carrier record was created |  |
| 11         | CREATED_BY | VARCHAR2 | NO | Name of the user who created the Digital Carrier record |  |
| 12         | MODIFIED | DATE | YES | The date of the last change to the Digital Carrier record |  |
| 13         | MODIFIED_BY | VARCHAR2 | YES | Name of the last user who modified the Digital Carrier record |  |
| 14         | SOM_FRAMES | NUMBER | YES | Start of Media stored in frames |  |
| 15         | SOM_TIMECODE | VARCHAR2 | YES | SOM displayed as a timecode |  |
| 16         | EOM_FRAMES | NUMBER | YES | End of Media stored in frames |  |
| 17         | EOM_TIMECODE | VARCHAR2 | YES | EOM displayed as a timecode |  |
| 18         | DURATION_FRAMES | NUMBER | YES | Duration of the media stored as frames |  |
| 19         | DURATION_TIMECODE | VARCHAR2 | YES | Duration of the media displayed as a timecode |  |
| 20         | TV_STANDARD_ID | NUMBER | YES | Foreign Key. Unique ID of the TV Standard for the Media in |  |
| 21         | TV_STANDARD_NAME | NVARCHAR2 | YES | The text description of the TV Standard for the Media |  |
| 22         | MEDIA_FILE_TYPE_ID | NUMBER | YES | Foreign Key. The unique ID of the type of Digital file in |  |
| 23         | MEDIA_FILE_TYPE_NAME | VARCHAR2 | YES | Text Description of the type of Digital File |  |
| 24         | EXT_REF1 | VARCHAR2 | YES | Client specific Identifier |  |
| 25         | EXT_REF2 | VARCHAR2 | YES | Client specific Identifier |  |
| 26         | ORIGINAL_FILENAME | VARCHAR2 | YES | The last name of the file before any renaming workflows |  |
| 27         | DFILE_LINK_GUID | VARCHAR2 | YES | Internal Use ID |  |

## 40.  MDD_DIGITAL_FILE_LINKS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | NO |  |  |
| 2         | DIGITAL_FILE_ID_FK | NUMBER | NO |  |  |
| 3         | MEDIA_ITEM_INDEX | NUMBER | YES |  |  |
| 4         | DIGITAL_FILE_INDEX | NUMBER | YES |  |  |
| 5         | CREATED_DATE | DATE | NO |  |  |
| 6         | CREATED_BY | VARCHAR2 | NO |  |  |
| 7         | MODIFIED_DATE | DATE | YES |  |  |
| 8         | MODIFIED_BY | VARCHAR2 | YES |  |  |

## 41.  MDD_DISPOSAL_RECORDS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | NO | Foreign Key.  Links to MEDIA_ID in MDD_MEDIA |  |
| 2         | DISPOSAL_CLASS_ID | NUMBER | NO | Disposal class ID |  |
| 3         | DISPOSAL_CLASS | NUMBER | YES | Disposal Class |  |
| 4         | DISPOSAL_CLASS_DESCRIPTION | VARCHAR2 | YES | Disposal Class Description |  |
| 5         | DISPOSAL_STATUS_ID | NUMBER | NO | Disposal status ID |  |
| 6         | DISPOSAL_STATUS | VARCHAR2 | YES | Disposal status |  |
| 7         | DISPOSAL_DUE_DATE | DATE | YES | Disposal due date |  |
| 8         | DISPOSAL_ACTION | VARCHAR2 | YES | Disposal action |  |
| 9         | MODIFIED_BY | VARCHAR2 | YES | Person who last modified the Disposal Status |  |
| 10         | MODIFIED_DT | DATE | YES | Date that the media item disposal status was last modified |  |

## 42.  MDD_ENTITY_NATIONALITIES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ENTITY_ID | NUMBER | NO | Foreign Key.  Links to Entity details in MDD_ENTITIES |  |
| 2         | NATIONALITY | VARCHAR2 | YES | Nationality(ies) associated with Entity |  |

## 43.  MDD_GROUPS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | GROUP_ID | NUMBER | NO | Primary Key.  Unique ID of the Group |  |
| 2         | PARENT_ID | NUMBER | YES | Foreign Key.  Links to a parent Group if there is one |  |
| 3         | GROUP_NAME | VARCHAR2 | YES | Name of Group |  |
| 4         | GROUP_DESCRIPTION | VARCHAR2 | YES | Description of Group |  |
| 5         | CREATED_DATE | DATE | NO | Date Group was created |  |
| 6         | CREATED_BY | VARCHAR2 | NO | Name of user who created the group |  |
| 7         | MODIFIED_DATE | DATE | YES | Date Group was modified |  |
| 8         | MODIFIED_BY | VARCHAR2 | YES | Name of user who modified the group |  |
| 9         | IMPORTED_DATE | DATE | YES | Date Items were imported into the group |  |
| 10         | REFRESHED_DATE | DATE | YES | Date the Items in the group were last refreshed |  |
| 11         | GROUP_TYPE_ID | NUMBER | YES | Identifies the type of group |  |
| 12         | LIST_COMPLETED | NUMBER | NO | Locked status of the Group |  |
| 13         | LIST_COMPLETED_DATE | DATE | YES | Date the Group was locked |  |
| 14         | LIST_COMPLETED_BY | VARCHAR2 | YES | Name of the user who lockd the group |  |

## 44.  MDD_GROUP_MEDIA*

> Links media for certain lists used in the system, eg: Stock Check lists

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TAG_ID | NUMBER | NO | Primary Key.  Links to TAG table (internal use only) |  |
| 2         | GROUP_ID_FK | NUMBER | YES | Foreign Key.  Links to group in MDD_GROUPS |  |
| 3         | ITEM_TYPE | NUMBER | YES | Identifies how the item is grouped, eg: 3020 = Carrier |  |
| 4         | ITEM_ID | NUMBER | YES | Foreign Key.  Links to a scondary view depending on the type of |  |
| 5         | TITLE_ID_FK | NUMBER | YES | Foreign Key.  Links to Title in MDD_TITLES |  |
| 6         | CONTAINER_ID_FK | NUMBER | YES | Foreign Key.  Links to container in MDD_CONTAINERS |  |
| 7         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to media in MDD_MEDIA |  |
| 8         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links to version in MDD_VERSIONS |  |
| 9         | JOB_ID_FK | NUMBER | YES |  |  |
| 10         | LOAN_ITEM_ID_FK | NUMBER | YES | Foreign Key.  Links to job in MDD_JOB |  |
| 11         | CREATED_BY | VARCHAR2 | NO | Name of the user who created the group |  |
| 12         | CREATED_DATE | DATE | NO | Date the group was created |  |
| 13         | STATUS | NUMBER | YES | Internal use value used to determine if location matches between |  |
| 14         | STOCK_CHECK_STATUS_ID | NUMBER | YES |  |  |
| 15         | STOCK_CHECK_STATUS | VARCHAR2 | YES | Status of Carriers in a Stock Check Picklist |  |
| 16         | STOCK_CHECK_DATE | DATE | YES | Date the Stock Check status was set |  |
| 17         | STOCK_CHECK_USER | VARCHAR2 | YES | User who performed the stock check |  |

## 45.  MDD_HISTORY

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | HISTORY_ID | NUMBER | NO | Primary Key.  Unique ID of History data |  |
| 2         | HISTORY_TYPE_ID | NUMBER | NO | Internal use key to determine the type of data |  |
| 3         | HISTORY_TYPE | VARCHAR2 | NO | Description of History type |  |
| 4         | HISTORY_TEXT | VARCHAR2 | YES | History Text |  |
| 5         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to Task History is associated with in MDD_TASKS |  |
| 6         | INTEGER1_HEADER | VARCHAR2 | YES | Details captured depending on the type of History |  |
| 7         | PARENT_ID | NUMBER | NO | Foreign Key.  Linking to either Task or Media |  |
| 8         | PARENT_TYPE_ID | NUMBER | NO | Internal use key identifying parent type |  |
| 9         | INTEGER_VALUE1 | NUMBER | YES | Details captured depending on the type of History |  |
| 10         | QC_STATUS | VARCHAR2 | YES | Primary Key.  Links to TAG table (internal use only) |  |
| 11         | INTEGER_VALUE2 | NUMBER | YES | Details captured depending on the type of History |  |
| 12         | STRING_VALUE1 | VARCHAR2 | YES | Details captured depending on the type of History |  |
| 13         | STRING_VALUE2 | VARCHAR2 | YES | Details captured depending on the type of History |  |
| 14         | NOTES | VARCHAR2 | YES | Notes captured |  |
| 15         | CREATED_BY | VARCHAR2 | NO | Name of user who entered the details |  |
| 16         | CREATED_DATE | DATE | NO | Date record was created |  |

## 46.  MDD_HISTORY_EQUIPMENT

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | HISTORY_ID_FK | NUMBER | YES | Foreign Key.  Provides link to History data |  |
| 2         | EQUIPMENT_ORDER | NUMBER | YES | Equipment index |  |
| 3         | EQUIPMENT_NAME | VARCHAR2 | YES | Name of Equipment used |  |
| 4         | EQUIPMENT_ID_FK | VARCHAR2 | YES | Foreign Key.  Internal use key |  |

## 47.  MDD_IBMS_VERSIONS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO |  |  |
| 2         | HOUSE_NUMBER | VARCHAR2 | YES |  |  |
| 3         | FILE_REF | VARCHAR2 | YES |  |  |

## 48.  MDD_JOB*

> Provides details of Jobs created

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | JOB_ID | NUMBER | NO | Primary Key.  Unique ID of Job |  |
| 2         | JOB_NO | VARCHAR2 | YES | Provides full Job number including client prefix |  |
| 3         | CLIENT_REF | VARCHAR2 | YES | Secondary reference for Job |  |
| 4         | JOB_CREATE_DATE | DATE | YES | Date Job was created |  |
| 5         | JOB_CREATED_BY | VARCHAR2 | NO | Name of user who created the job |  |
| 6         | JOB_COMPLETE_BY | DATE | YES | Date Job is due to be completed by |  |
| 7         | JOB_COMPLETED_DATE | DATE | YES | Date Job was actually completed |  |
| 8         | JOB_COMPLETED_DMY | VARCHAR2 | YES | Job completed in groupable format |  |
| 9         | JOB_COMPLETED_MY | VARCHAR2 | YES | Month and year Job was completed |  |
| 10         | JOB_COMPLETED_M_NUM | NUMBER | YES | Month Job was completed in numerical format |  |
| 11         | JOB_COMPLETED_YEAR | VARCHAR2 | YES | Year Job was completed |  |
| 12         | OWNERS | VARCHAR2 | YES | Owner of Job |  |
| 13         | JOB_NOTES | VARCHAR2 | YES |  |  |
| 14         | PRESET_ID | NUMBER | YES |  |  |
| 15         | PRESET_USED | VARCHAR2 | YES | Name of preset used |  |
| 16         | PRESET_DESC | VARCHAR2 | YES | Description of the preset used |  |
| 17         | PRESET_ACTIVE | NUMBER | YES | 0 indicates that the preset is Not Active, 1 indicates that it is active |  |
| 18         | JOB_STATUS_ID | NUMBER | YES | Internal use ID |  |
| 19         | JOB_STATUS | VARCHAR2 | YES | Status of overall Job |  |
| 20         | FAILURE_RESOLVED | NUMBER | YES | Indicates if the Job has been marked as resolved |  |
| 21         | JOB_REQUEST_REFERENCE | VARCHAR2 | YES | External Reference number for Job |  |
| 22         | PARENT_JOB | NUMBER | YES | The ID of the parent job from which this job was raised. |  |

## 49.  MDD_JOB_MEDIA (Replaced By MDD_TASK_MEDIA)*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | JOB_ID | NUMBER | YES |  |  |
| 2         | MEDIA_ID | NUMBER | YES |  |  |
| 3         | SOURCE | NUMBER | YES |  |  |
| 4         | TASK_ID | NUMBER | YES |  |  |
| 5         | TASK_TYPE | NUMBER | YES |  |  |
| 6         | TASK_TYPE_DESC | VARCHAR2 | YES |  |  |
| 7         | ARRIVE_BY | DATE | YES |  |  |
| 8         | DESPATCH_FROM | VARCHAR2 | YES |  |  |
| 9         | DESPATCH_TO | VARCHAR2 | YES |  |  |
| 10         | COMPLETE_BY | DATE | YES |  |  |
| 11         | TASK_STATUS | NUMBER | YES |  |  |
| 12         | TASK_END | DATE | YES |  |  |
| 13         | TASK_OPERATOR | VARCHAR2 | YES |  |  |
| 14         | TASK_TITLE_ID_FK | NUMBER | YES |  |  |
| 15         | TASK_POS | NUMBER | YES |  |  |
| 16         | SCHEDULE_AREA | NUMBER | YES |  |  |
| 17         | CREATED_BY | VARCHAR2 | YES |  |  |

## 50.  MDD_JOB_SCHEDULE (Replaced By MDD_TASK)*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | JOB_NO | NUMBER | YES |  |  |
| 2         | TASK_NO | NUMBER | NO |  |  |
| 3         | CLIENT_CODE | VARCHAR2 | YES |  |  |
| 4         | TASK_POS | NUMBER | YES |  |  |
| 5         | SCHEDULE_AREA | NUMBER | YES |  |  |
| 6         | PRESET_USED | VARCHAR2 | YES |  |  |

## 51.  MDD_LANG_DATA

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key.  Unique ID of Language |  |
| 2         | LANGUAGE_SHORTCODE | VARCHAR2 | NO | Language code |  |
| 3         | LANGUAGE_NAME | VARCHAR2 | YES | Full Language name |  |
| 4         | ISO_CODE | VARCHAR2 | YES | Official ISO Code for Language |  |

## 52.  MDD_LOAN_HEADER*

> Provides summary header details for a Loan

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Linking to media item in MDD_MEDIA |  |
| 2         | CONTAINER_ID_FK | NUMBER | YES |  |  |
| 3         | MEDIA_ID1 | VARCHAR2 | YES | Media ID1 of Media on Loan |  |
| 4         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Linking to versions in MDD_VERSIONS |  |
| 5         | BARCODE | VARCHAR2 | YES | Barcode of Carrier (if loan is linked to a Carrier) |  |
| 6         | SERIES_TITLE | VARCHAR2 | YES | Title of item |  |
| 7         | EPISODE_TITLE | VARCHAR2 | YES | Episode Title of item |  |
| 8         | NEXT_TX_DATE | DATE | NO | Next tranmission date of item |  |
| 9         | REQUIRED_DATE | DATE | YES | Date item is required |  |
| 10         | RETURN_DATE | DATE | YES | Date item is due to be returned |  |
| 11         | DATE_LOANED | DATE | YES | Date item was actually loaned |  |
| 12         | DATE_RETURNED | DATE | YES | Date item was actually returned |  |
| 13         | STATUS | VARCHAR2 | YES | Status of item in Loan |  |
| 14         | ITEM_TYPE | VARCHAR2 | YES | Type of item on Loan, eg: Media or Tape |  |

## 53.  MDD_LOAN_ITEMS*

> Provides details about individual items within a loan.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | LOAN_ITEM_ID | NUMBER | NO |  |  |
| 2         | LOAN_NO | NUMBER | NO | Foreign Key.  Linking Loan Item to Loan Header in |  |

## 54.  MDD_LOCATIONS*

> Provides details of Library/Vault Locations.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | LOCATION_ID | NUMBER | NO | Primary Key. Internal ID of the Location item |  |
| 2         | NAME | VARCHAR2 | YES | Name of Location Item. |  |
| 3         | SHORT_CODE | VARCHAR2 | YES | Short Code of the Location Item.. |  |
| 4         | PARENT_ID_FK | NUMBER | YES | Foreign Key. Link to parent record in this view (MDD_LOCATIONS). |  |
| 5         | LOCATION_TYPE | VARCHAR2 | YES | Type of Location Item (e.g. Shelf/Area/Bay etc.) |  |
| 6         | FULL_LOCATION_NAME | VARCHAR2 | YES | Full Path of the Location Name (Underscore delimited) |  |
| 7         | FULL_LOCATION_CODE | VARCHAR2 | YES | Full Path of the Location Code (Pipe Delimited). |  |
| 8         | LOCATION_BARCODE | NUMBER | YES | Barcode of Location Item. |  |
| 9         | CREATED | DATE | YES | Date the Location Item was created. |  |
| 10         | CREATED_BY | VARCHAR2 | YES | Name of user who created the Location Item. |  |
| 11         | MODIFIED | DATE | YES | Date the Location Item was last modified. |  |
| 12         | MODIFIED_BY | VARCHAR2 | YES | Name of user who last modified the Location Item. |  |
| 13         | AREA_EMAIL | VARCHAR2 | YES | Email address defined for area notification. |  |
| 14         | ACCLIMATISATION_PERIOD | NUMBER | NO | Period of Time indicated for acclimatisation of incomgin/outgoing |  |
| 15         | TEMPERATURE_CLASSIFICATION | VARCHAR2 | YES | Label of Area Temperature configuration |  |
| 16         | AIR_CONDITIONING | VARCHAR2 | YES | Label of Area Air Conditioning. |  |
| 17         | HUMIDITY | NUMBER | YES | Label of Area Humidity levels. |  |
| 18         | HOME_LONG_TERM | VARCHAR2 | YES | Details of whether a location Item is configured as a Home Location |  |
| 19         | BOOKING_READY | VARCHAR2 | YES | Details of whether a loan/booking item should be marked ready in |  |
| 20         | BOOKING_RETURN | VARCHAR2 | YES | Details of whether a loan/booking item should be marked returned |  |
| 21         | CONFIGURED_STORAGE | VARCHAR2 | YES | Details of whether a location item is maked as configured |  |
| 22         | LOCATION_FULL | VARCHAR2 | YES | Details of whether a location item is full (True/False). |  |
| 23         | RETURN_TO_HOME | VARCHAR2 | YES | Details of whether a location item is used to return items to the |  |
| 24         | PREFERRED | VARCHAR2 | YES | Details of whether a location item is a preferred location |  |
| 25         | CUSTOM_FLAGS | VARCHAR2 | YES |  |  |
| 26         | SHELF_WIDTH | NUMBER | YES | Configured width of the shelf (in millimetres). |  |
| 27         | SHELF_HEIGHT | NUMBER | YES | Configured height of the shelf (in millimetres). |  |
| 28         | SHELF_DEPTH | NUMBER | YES | Configured depth of the shelf (in millimetres). |  |
| 29         | PRESET_NAME | VARCHAR2 | YES | Name of the shelf configuration preset if used. |  |
| 30         | CAPACITY_CALCULATION_ID | NUMBER | YES |  |  |
| 31         | CAPACITY_CALCULATION | VARCHAR2 | YES | Details of shelf capacity configuration. |  |
| 32         | MAX_ITEMS | NUMBER | YES | Details of the configured maximum number of items on a shelf. |  |
| 33         | LOC_DELETED | NUMBER | YES | Boolean value indicating whether the Location Item has been |  |
| 34         | LOC_DELETED_BY | VARCHAR2 | YES | Name of the User who marked the Location Item as deleted |  |
| 35         | LOC_DELETED_DT | DATE | YES | Date the Location Item was marked as deleted |  |

## 55.  MDD_LOCATION_USE*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | LOC | NUMBER | NO |  |  |
| 2         | ACTUAL_COUNT | NUMBER | YES |  |  |
| 3         | ACTUAL_VOLUME_USED | NUMBER | YES |  |  |
| 4         | ACTUAL_LENGTH_USED | NUMBER | YES |  |  |
| 5         | LAST_HOME_VOLUME_USED | NUMBER | YES |  |  |
| 6         | LAST_HOME_COUNT | NUMBER | YES |  |  |
| 7         | LAST_HOME_LENGTH_USED | NUMBER | YES |  |  |
| 8         | SUGGESTED_COUNT | NUMBER | YES |  |  |
| 9         | SUGGESTED_VOLUME_USED | NUMBER | YES |  |  |
| 10         | SUGGESTED_LENGTH_USED | NUMBER | YES |  |  |
| 11         | TOTAL_COUNT | NUMBER | YES |  |  |
| 12         | TOTAL_VOLUME_USED | NUMBER | YES |  |  |
| 13         | TOTAL_LENGTH_USED | NUMBER | YES |  |  |

## 56.  MDD_MEDIA*

> Provides information about Media items (excluding virtual media items).

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | NO | Primary Key.  Unique ID of Media item |  |
| 2         | U_TO_TXD | DATE | YES |  |  |
| 3         | U_FRM_TXD | DATE | YES |  |  |
| 4         | SERIES_ID_FK | NUMBER | YES | Foreign Key.  Links Media to Series in MDD_TITLES |  |
| 5         | TITLE_ID_FK | NUMBER | NO | Foreign Key.  Links Media to Title in MDD_TITLES |  |
| 6         | MASTER_VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links Media to master version (where immediate |  |
| 7         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links Media to Version in MDD_VERSIONS |  |
| 8         | ACQ_ID_FK | NUMBER | YES | Foreign Key.  Links Media to Acquisition in MDD_ACQUISITIONS |  |
| 9         | MEDIA_TITLE | VARCHAR2 | YES | Episode title of Media |  |
| 10         | MEDIA_SERIES_TITLE | VARCHAR2 | YES | Title of Media (labeled as Series in Media details screen) |  |
| 11         | MEDIA_ID1 | VARCHAR2 | NO | Client specific Media identifier |  |
| 12         | COMPONENT_NO | VARCHAR2 | YES | n/a for most clients |  |
| 13         | CARRIER_NO | VARCHAR2 | YES | n/a for most clients |  |
| 14         | TV_NUM | NUMBER | YES |  |  |
| 15         | MEDIA_ID2 | VARCHAR2 | YES | Second client specific Media identifier |  |
| 16         | ITEM_TYPE_ID | NUMBER | NO | Foreign Key.  Links to item type in MDD_MEDIA_ITEM_TYPES |  |
| 17         | ITEM_TYPE | VARCHAR2 | YES | Program Type, eg: Promo, Episode etc |  |
| 18         | ITEM_SUB_TYPE_ID | NUMBER | YES |  |  |
| 19         | ITEM_SUB_TYPE | VARCHAR2 | YES |  |  |
| 20         | ITEM_FORMAT_ID | NUMBER | YES |  |  |
| 21         | ITEM_FORMAT | VARCHAR2 | YES | Format of item per configuration tables |  |
| 22         | NFSA_ITEM_TYPE | VARCHAR2 | YES | DO NOT USE!!! |  |
| 23         | OWNERS | VARCHAR2 | NO | Owner(s) of the Media item |  |
| 24         | DESCRIPTION | VARCHAR2 | YES | Description/Notes for Media |  |
| 25         | SERIES_NAME | VARCHAR2 | YES | Title of Media (labeled as Series Name in Media details screen) |  |
| 26         | SERIES_NO | NUMBER | YES | Series number that the Media is associated with |  |
| 27         | SERIES_EPISODE_NO | NUMBER | YES | Episode number that the Media is associated with |  |
| 28         | SERIES_ID1 | VARCHAR2 | YES | Client specific series identifier |  |
| 29         | SERIES_ID2 | VARCHAR2 | YES | Second client specific series identifier |  |
| 30         | PROG_ID1 | VARCHAR2 | YES | Client specific program identifier |  |
| 31         | PROG_ID2 | VARCHAR2 | YES | Second client specific program identifier |  |
| 32         | HOUSE_NUMBER | VARCHAR2 | YES | International ID that has been called House ID, Up Link Number, |  |
| 33         | VERSION_NAME | VARCHAR2 | YES | Name of the version that the Media is associated with |  |
| 34         | VERSION_ID1 | VARCHAR2 | YES | Client specific version identifier |  |
| 35         | VERSION_ID2 | VARCHAR2 | YES | Second client specific version identifier |  |
| 36         | PRODUCTION_YEAR | NUMBER | YES | Year title was produced |  |
| 37         | SOM | NUMBER | NO | Start of Media stored in frames |  |
| 38         | EOM | NUMBER | NO | End of Media stored in frames |  |
| 39         | SOM_TIMECODE | VARCHAR2 | YES | SOM displayed as a timecode. |  |
| 40         | EOM_TIMECODE | VARCHAR2 | YES | EOM displayed as a timecode. |  |
| 41         | CREATED_DATE | DATE | NO | Date Media was created |  |
| 42         | CREATED_BY | VARCHAR2 | NO | Name of user who created Media |  |
| 43         | CREATED_BY_DEPT_ID | NUMBER | YES | Internal use ID |  |
| 44         | CREATED_BY_DEPT | VARCHAR2 | YES | Name of department within which Media was created |  |
| 45         | CREATED_BY_EMAIL | VARCHAR2 | YES | Email address of the person who created the Media |  |
| 46         | MODIFIED_DATE | DATE | YES | Date Media item was last changed |  |
| 47         | MODIFIED_BY | VARCHAR2 | YES | Name of user who last changed the media item |  |
| 48         | STATUS_ID | NUMBER | YES | Internal use ID |  |
| 49         | STATUS_DESC | NVARCHAR2 | YES | Status of program, eg: Restricted |  |
| 50         | RESTRICTION_STATUS | VARCHAR2 | YES | !!  This needs to be checked.  The rule does not appear to be |  |
| 51         | USAGE_ID | NUMBER | YES | Internal use ID |  |
| 52         | USAGE_TYPE | VARCHAR2 | YES | Displays the Usage Type of the Media item, eg:  Access Copy |  |
| 53         | USAGE_SHORTCODE | VARCHAR2 | YES | Shortcode of the usage type |  |
| 54         | MEDIA_STATUS_ID | NUMBER | YES |  |  |
| 55         | MEDIA_STATUS | NVARCHAR2 | YES |  |  |
| 56         | ATTACHMENT_FILENAMES | CLOB | YES | List of Attachment Filenames. |  |
| 57         | URL_REFERENCES | CLOB | YES | List of URL References. |  |
| 58         | PROGRAM_DURATION | NUMBER | YES | Duration of the program in frames |  |
| 59         | DURATION_MILLISECONDS | NUMBER | YES | Duration of the program in milliseconds |  |
| 60         | DURATION_SECONDS | NUMBER | YES |  |  |
| 61         | CALCULATED_DURATION | NUMBER | YES | EOM minus SOM stored in frames |  |
| 62         | DURATION_TIMECODE | VARCHAR2 | YES | Duration displayed as a timecode |  |
| 63         | SLOT_DUR | NUMBER | YES |  |  |
| 64         | ASSESS_STATUS | VARCHAR2 | YES | Status of the latest assessment |  |
| 65         | ASSESS_DATE | DATE | YES |  |  |
| 66         | TV_STD_ID | NUMBER | YES | Internal use ID |  |
| 67         | TV_STD | NVARCHAR2 | YES | Text description of TV Standard for the Media item |  |
| 68         | ASPECT_RATIO_ID | NUMBER | YES | Internal use ID |  |
| 69         | ASPECT_RATIO | VARCHAR2 | YES | Legacy value Aspect ratio of Media item |  |
| 70         | AFD_ID | NUMBER | YES | Foreign key.  For internal use only |  |
| 71         | AFD_DESC | NVARCHAR2 | YES | Active Format Description |  |
| 72         | ASPECT_RATIO_LEGACY_ID | NUMBER | YES | Next tranmission date of item |  |
| 73         | ASPECT_RATIO_LEGACY | NVARCHAR2 | YES | Date item is required |  |
| 74         | AFD_CODE | VARCHAR2 | YES | Date item is due to be returned |  |
| 75         | LANGUAGE_ID | NUMBER | YES | Internal use ID |  |
| 76         | LANGUAGE | VARCHAR2 | YES | Primary Language as displayed on the Media details screen |  |
| 77         | FLAG_1 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 78         | FLAG_2 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 79         | FLAG_3 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 80         | FLAG_4 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 81         | FLAG_5 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 82         | FLAG_6 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 83         | FLAG_7 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 84         | FLAG_8 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 85         | FLAG_9 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 86         | FLAG_10 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 87         | FLAG_11 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 88         | FLAG_12 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 89         | FLAG_13 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 90         | FLAG_14 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 91         | FLAG_15 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 92         | FLAG_16 | NUMBER | YES | Boolean value representing data according to the Flag tab in the |  |
| 93         | CLOSEDCAPTION | VARCHAR2 | YES | Boolean value indicating whether the Media item is Closed |  |
| 94         | SUBTITLES | VARCHAR2 | YES | Boolean value indicating whether the Media item is Subtitled or not |  |
| 95         | COLOR | NUMBER | YES | Internal use ID |  |
| 96         | COLOUR_DESC | NVARCHAR2 | YES |  |  |
| 97         | AU_TRACKS_NUM | NUMBER | YES | DO NOT USE!!  Link to MDD_MEDIA_AUDIO for audio information |  |
| 98         | AU_TRACKS_LANGUAGES | VARCHAR2 | YES | DO NOT USE!!  Link to MDD_MEDIA_AUDIO for audio information |  |
| 99         | AU_TRACKS_CONT | VARCHAR2 | YES | DO NOT USE!!  Link to MDD_MEDIA_AUDIO for audio information |  |
| 100         | AU_TRACKS_MS | VARCHAR2 | YES | DO NOT USE!!  Link to MDD_MEDIA_AUDIO for audio information |  |
| 101         | AU_TRACKS_MODE | VARCHAR2 | YES | DO NOT USE!!  Link to MDD_MEDIA_AUDIO for audio information |  |
| 102         | OS_DIR | VARCHAR2 | YES | Location of digital media |  |
| 103         | OS_FILENAME | VARCHAR2 | YES | Filename of digital media |  |
| 104         | DIGITAL_FILENAME | VARCHAR2 | YES |  |  |
| 105         | PATH | VARCHAR2 | YES | Full path of digital media, including location and filename |  |
| 106         | FILE_SIZE | NUMBER | YES | Size, in bytes, of digital media |  |
| 107         | MEDIA_LOCATION | VARCHAR2 | YES | Physical Location of media |  |
| 108         | DEVICE_ID | NUMBER | YES |  |  |
| 109         | PARENT_ID | NUMBER | YES | DO NOT USE!!!  Replaced by TITLE_ID_FK |  |
| 110         | FILE_NAME | VARCHAR2 | YES | Name of file type, eg Omneon Media Server |  |
| 111         | FILE_TYPE | VARCHAR2 | YES | File type category, eg Video |  |
| 112         | FILE_EXTENSION | VARCHAR2 | YES | Valid extension of file type |  |
| 113         | FILENAME_NO_EXTENSION | VARCHAR2 | YES | Digital Filename with file extension stripped off |  |
| 114         | MEDIA_FORMAT_ID | NUMBER | YES | Internal use ID |  |
| 115         | MEDIA_TYPE | NUMBER | NO | Internal use ID |  |
| 116         | MEDIA_TYPE_DESC | VARCHAR2 | YES | Description of the Material Type eg Physical A/V Material |  |
| 117         | MEDIA_FORMAT_NAME | VARCHAR2 | YES | Format of Media, eg IPV Browse |  |
| 118         | ARCHIVED | NUMBER | YES | Boolean value indicating whether the Media item is archived or not. |  |
| 119         | DELETED | NUMBER | YES | Boolean value indicating whether the Media item has been marked |  |
| 120         | MI_DELETED | NUMBER | YES | Boolean value indicating whether the Media item has been marked |  |
| 121         | DELETED_DATE | DATE | YES | Date the Media was marked as deleted |  |
| 122         | FULL_TECHCODE | VARCHAR2 | YES | Technical category assigned to Media |  |
| 123         | MEDIA_FORMAT_CODE | VARCHAR2 | YES | Format code for Media |  |
| 124         | FLAG_SUPPLIED | NUMBER | YES | Boolean value indicating whether the Media item is supplied or not |  |
| 125         | FLAG_CREATED | NUMBER | YES | Boolean value indicating whether the Media item is created or not |  |
| 126         | ORIGIN | VARCHAR2 | YES | Origin of Media, eg Made |  |
| 127         | A_GRADE | NUMBER | YES | A Grade level of Media item |  |
| 128         | V_GRADE | NUMBER | YES | V Grade level of Media item |  |
| 129         | CRS_SERIES_ID | NUMBER | YES | Internal use key |  |
| 130         | CRS_SERIES_NO | VARCHAR2 | YES | CRS Series Number of Media item |  |
| 131         | CRS_SERIES_TITLE | VARCHAR2 | YES | CRS Series Title of Media item |  |
| 132         | SUITABLE_VOEC | NUMBER | YES | Indicates whether End Credit is OK for V/O or not |  |
| 133         | MEDIA_LINK_ID_FK | NUMBER | YES | Provides a link back to the original source media |  |
| 134         | DIVA_CATEGORY | VARCHAR2 | YES | DIVA category where archive is stored. |  |
| 135         | DIVA_MEDIA_GROUP | VARCHAR2 | YES | DIVA media group where archive is stored. |  |
| 136         | FPS | NVARCHAR2 | YES |  |  |
| 137         | CHECKSUM | VARCHAR2 | YES | CHECKSUM extracted from media file. |  |
| 138         | LAST_TX_DATE | DATE | YES | Contains Last TX Date for Media ONLY if stored directly against |  |
| 139         | ITEM_TYPE_SHORTCODE | VARCHAR2 | YES |  |  |
| 140         | ASSISTED_ASSESS_STATUS | VARCHAR2 | YES | Fail, Pass, or null if no Assisted QC has been performed |  |
| 141         | MEDIA_ID3 | VARCHAR2 | YES |  |  |
| 142         | MEDIA_SHELL | VARCHAR2 | YES | YES (unattached media) or NO (has media attached) |  |
| 143         | IS_ORIGINAL_AUDIO | VARCHAR2 | YES |  |  |

## 57.  MDD_MEDIA_AUDIO*

> This view uses new audio tables to provide details of media audio.  This will eventually replace MDD_MEDIA_AUDIO.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | AUDIO_ID | NUMBER | NO |  |  |
| 2         | MEDIA_ID | NUMBER | YES | Foreign Key.  Linking audio to MDD_MEDIA |  |
| 3         | TRACK_NUMBER | NVARCHAR2 | YES |  |  |
| 4         | AU_NM | NVARCHAR2 | YES | Track number |  |
| 5         | AUDIO_NM | NVARCHAR2 | YES |  |  |
| 6         | AU_CONT_ID | NUMBER | YES | Audio content ID.  For internal use only. |  |
| 7         | AUDIO_CONTENT | NVARCHAR2 | YES | Audio content, eg: Full Mix |  |
| 8         | AUDIO_CONTENT_TAG | NVARCHAR2 | YES | Code for Audio content |  |
| 9         | AU_LANG_ID | NUMBER | YES | Audio language ID. For internal use only. |  |
| 10         | AUDIO_LANGUAGE | VARCHAR2 | YES | Audio language |  |
| 11         | AUDIO_LANGUAGE_CODE | VARCHAR2 | YES | Code for audio language |  |
| 12         | AU_MS_ID | NUMBER | YES | Mono/Stereo ID.  For internal use only. |  |
| 13         | AUDIO_MS | NVARCHAR2 | YES | Details of mono or stereo. |  |
| 14         | AUDIO_MS_CODE | NVARCHAR2 | YES | Code for mono or stereo. |  |
| 15         | AU_NR_ID | NUMBER | YES | Noise Reduction ID.  For internal use only. |  |
| 16         | AUDIO_NR | NUMBER | YES |  |  |
| 17         | QC_STATUS | NUMBER | YES | Audio QC status |  |
| 18         | LANGUAGE_TAG | NUMBER | YES | Language Tag |  |
| 19         | LANGUAGE_TAG_DESC | NVARCHAR2 | YES | Description of Language Tag |  |
| 20         | LANGUAGE_ISO_CODE | VARCHAR2 | YES | ISO Code for the Language |  |
| 21         | INGEST_SELECTED | NUMBER | YES |  |  |
| 22         | PRIMARY_AUDIO | NUMBER | YES | Audio Track with Internal Audio set |  |
| 23         | INTERNATIONAL_AUDIO | NUMBER | YES | Indicates whether the track has International Audio or not |  |
| 24         | AUDIO_QC_PASS | NUMBER | YES | Audio has passed QC |  |
| 25         | AUDIO_QC_FAIL | NUMBER | YES | Audio has failed QC |  |
| 26         | TAG_MATCH | NUMBER | YES |  |  |
| 27         | STACKED | NUMBER | YES | Indicates this audio track has be re-added / re-stacked to the mov, |  |
| 28         | STACKED_DATE | DATE | YES | Date the audio was stacked |  |
| 29         | TRACK_RENAMED | NUMBER | YES | Will be set to true if audio track as been renamed |  |
| 30         | CREATED_DATE | DATE | NO |  |  |
| 31         | CREATED_BY | VARCHAR2 | NO |  |  |
| 32         | MODIFIED_DATE | DATE | YES |  |  |
| 33         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 34         | KHZ | VARCHAR2 | YES |  |  |
| 35         | PEAK | VARCHAR2 | YES |  |  |
| 36         | AVG | VARCHAR2 | YES |  |  |
| 37         | DIP | VARCHAR2 | YES |  |  |
| 38         | LM100_SHORT | VARCHAR2 | YES |  |  |
| 39         | LM100_LONG | VARCHAR2 | YES |  |  |

## 58.  MDD_MEDIA_AUDIO_EXTRAS*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | YES |  |  |
| 2         | TASK_ID_FK | NUMBER | YES |  |  |
| 3         | TRACK_INDEX | NUMBER | YES |  |  |
| 4         | KHZ | VARCHAR2 | YES |  |  |
| 5         | PEAK | VARCHAR2 | YES |  |  |
| 6         | AVG | VARCHAR2 | YES |  |  |
| 7         | DIP | VARCHAR2 | YES |  |  |
| 8         | LM100_SHORT | VARCHAR2 | YES |  |  |
| 9         | LM100_LONG | VARCHAR2 | YES |  |  |

## 59.  MDD_MEDIA_AUDIO_NS*

> This view uses new audio tables to provide details of media audio.  This will eventually replace MDD_MEDIA_AUDIO.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | YES | Foreign Key.  Linking audio to MDD_MEDIA |  |
| 2         | AU_NM | NVARCHAR2 | YES | Track number |  |
| 3         | AU_CONT_ID | NUMBER | YES | Audio content ID.  For internal use only. |  |
| 4         | AUDIO_CONTENT | NVARCHAR2 | YES | Audio content, eg: Full Mix |  |
| 5         | AUDIO_CONTENT_TAG | NVARCHAR2 | YES | Code for Audio content |  |
| 6         | AU_LANG_ID | NUMBER | YES | Audio language ID. For internal use only. |  |
| 7         | AUDIO_LANGUAGE | VARCHAR2 | YES | Audio language |  |
| 8         | AUDIO_LANGUAGE_CODE | VARCHAR2 | YES | Code for audio language |  |
| 9         | AU_MS_ID | NUMBER | YES | Mono/Stereo ID.  For internal use only. |  |
| 10         | AUDIO_MS | NVARCHAR2 | YES | Details of mono or stereo. |  |
| 11         | AUDIO_MS_CODE | NVARCHAR2 | YES | Code for mono or stereo. |  |
| 12         | AU_NR_ID | NUMBER | YES | Noise Reduction ID.  For internal use only. |  |
| 13         | QC_STATUS | NUMBER | YES | Audio QC status |  |
| 14         | LANGUAGE_TAG | NUMBER | YES | Language Tag |  |
| 15         | LANGUAGE_TAG_DESC | NVARCHAR2 | YES | Description of Language Tag |  |
| 16         | LANGUAGE_ISO_CODE | VARCHAR2 | YES | ISO Code for the Language |  |
| 17         | INGEST_SELECTED | NUMBER | YES |  |  |
| 18         | PRIMARY_AUDIO | NUMBER | YES | Audio Track with Internal Audio set |  |
| 19         | INTERNATIONAL_AUDIO | NUMBER | YES | Indicates whether the track has International Audio or not |  |
| 20         | AUDIO_QC_PASS | NUMBER | YES | Audio has passed QC |  |
| 21         | AUDIO_QC_FAIL | NUMBER | YES | Audio has failed QC |  |
| 22         | TAG_MATCH | NUMBER | YES |  |  |
| 23         | STACKED | NUMBER | YES | Indicates this audio track has be re-added / re-stacked to the mov, |  |
| 24         | STACKED_DATE | DATE | YES | Date the audio was stacked |  |
| 25         | TRACK_RENAMED | NUMBER | YES | Will be set to true if audio track as been renamed |  |

## 60.  MDD_MEDIA_CHANNELS*

> View used to link Media to Channels

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Linking to MDD_MEDIA |  |
| 2         | CHANNEL_ID_FK | NUMBER | YES | Foreign Key.  Linking to MDD_CODES_CHANNELS |  |
| 3         | CHANNEL_CODE | VARCHAR2 | YES | Channel code associated with Media and linked Audio |  |

## 61.  MDD_MEDIA_CONTNRS_LNK*

> View used to link Media and Carriers

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | YES | Foreign Key.  Linking to carrier to MDD_MEDIA |  |
| 2         | CONTAINER_ID | NUMBER | NO | Foreign Key.  Linking to media to MDD_CONTAINERS |  |
| 3         | SCAN_LOCATION | VARCHAR2 | YES | Scanned location of carrier |  |

## 62.  MDD_MEDIA_COPY_HISTORY*

> View used to link Media Items to any copies created

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key |  |
| 2         | MEDIA_ID_FK | NUMBER | NO | Foreign key. Copied Media Item Linking to MDD_MEDIA |  |
| 3         | SOURCE_MEDIA_ID_FK | NUMBER | NO | Foreign key. Source Media Item Linking to MDD_MEDIA |  |
| 4         | SOURCE_VERSION_ID_FK | NUMBER | YES | Foreign key. Source Version Linking to MDD_VERSIONS |  |
| 5         | CREATED_DATE | DATE | NO | Date copy history record was created |  |
| 6         | CREATED_BY | VARCHAR2 | NO | Name of user who created copy history record |  |
| 7         | ENTERED_DATE | DATE | YES | Date that copy occured |  |
| 8         | ENTERED_BY | VARCHAR2 | YES | Name of user who created the copy |  |
| 9         | CUT | NUMBER | YES | Sequence number of Media Item on source carrier/file |  |
| 10         | SIDE | VARCHAR2 | YES | Side of source carrier |  |

## 63.  MDD_MEDIA_CUSTOM_STATUS*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | NO | Foreign Key, used to link to Media item |  |
| 2         | STATUS_ID | NUMBER | NO | Custom Media Status ID.  For internal use only. |  |
| 3         | MEDIA_STATUS | VARCHAR2 | YES | Custom Media Status |  |
| 4         | STATUS_TYPE_ID | NUMBER | NO | Custom Media Status Type ID.  For internal use only. |  |
| 5         | MEDIA_STATUS_TYPE | VARCHAR2 | YES | Custom Media Status type |  |

## 64.  MDD_MEDIA_FAULTS*

> Provides details of faults for a particular Media item.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | FAULT_ID | NUMBER | NO | Primary Key.  Unique ID of fault |  |
| 2         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links fault to MDD_MEDIA |  |
| 3         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links fault to MDD_JOB |  |
| 4         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links fault to MDD_TASKS |  |
| 5         | FAULT | VARCHAR2 | YES | Description of the fault |  |
| 6         | FAULT_TYPE | VARCHAR2 | YES | Code of type of fault, eg: V (video) |  |
| 7         | FAULT_INDEX | NUMBER | YES | Index of fault for a task |  |
| 8         | TIMECODE_IN | VARCHAR2 | YES | Timecode of start of fault |  |
| 9         | TIMECODE_OUT | VARCHAR2 | YES | Timecode of end of fault |  |
| 10         | SEVERITY | VARCHAR2 | YES | Severity of the fault |  |
| 11         | DURATION | VARCHAR2 | YES | Duration of the fault |  |
| 12         | SECTORS | VARCHAR2 | YES | Sectors where fault is present |  |
| 13         | NOTES | VARCHAR2 | YES | Fault notes |  |
| 14         | CREATED_DATE | DATE | NO | Date fault entered into system |  |
| 15         | CREATED_BY | VARCHAR2 | NO | Name of user who entered the details of the fault |  |
| 16         | FIXED | VARCHAR2 | YES | Boolean value indicating whether the fault has been fixed or not |  |

## 65.  MDD_MEDIA_FAULTS_NS*

> Provides details of faults for a particular Media item using the new faults tables. This will eventually replace the MDD_MEDIA_FAULTS view.

| Field No. | Field Name    | Data Type | Nullable | Description                            | Sample Data |
|-----------|---------------|-----------|----------|----------------------------------------|-------------|
| 1         | FAULT_ID      | NUMBER    | No       | Primary Key. Unique ID of fault        |             |
| 2         | MEDIA_ID_FK   | NUMBER    | Yes      | Foreign Key. Links fault to MDD_MEDIA  |             |
| 3         | JOB_ID_FK     | NUMBER    | Yes      | Foreign Key. Links fault to MDD_JOB    |             |
| 4         | TASK_ID_FK    | NUMBER    | Yes      | Foreign Key. Links fault to MDD_TASKS  |             |
| 5         | FAULT         | VARCHAR2  | Yes      | Description of the fault               |             |
| 6         | FAULT_TYPE    | VARCHAR2  | Yes      | Code of type of fault, e.g., V (video) |             |
| 7         | FAULT_INDEX   | NUMBER    | Yes      | Index of fault for a task              |             |
| 8         | TIMECODE_IN   | VARCHAR2  | Yes      | Timecode of start of fault             |             |
| 9         | TIMECODE_OUT  | VARCHAR2  | Yes      | Timecode of end of fault               |             |
| 10        | SEVERITY      | VARCHAR2  | Yes      | Severity of the fault                  |             |
| 11        | DURATION      | VARCHAR2  | Yes      | Duration of the fault                  |             |
| 12        | SECTORS       | VARCHAR2  | Yes      | Sectors where fault is present         |             |
| 13        | NOTES         | VARCHAR2  | Yes      | Fault notes                            |             |
| 14        | CREATED_DATE  | DATE      | No       | Date fault entered into system         |             |
| 15        | CREATED_BY    | VARCHAR2  | No       | Name of user who entered the fault     |             |
| 16        | FIXED         | VARCHAR2  | Yes      | Boolean value indicating fault status  |             |


## 66.  MDD_MEDIA_FORMATS (Replaced By MDD_MEDIA)*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_TYPE | NUMBER | YES |  |  |
| 2         | FORMAT_ID | NUMBER | YES |  |  |
| 3         | FORMAT_NAME | VARCHAR2 | YES |  |  |
| 4         | FORMAT_SHORT_CODE | VARCHAR2 | YES |  |  |

## 67.  MDD_MEDIA_FORMAT_TECH_CODES*

> Provides information about all versions stored in the system.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | NO | Foreign Key.  Links to media item in MDD_MEDIA. |  |
| 2         | FORMAT_TECH_CODE_SUB_TYPE | VARCHAR2 | NO | Format Tech Code Sub Type header for media item. |  |
| 3         | FORMAT_TECH_CODE_VALUE | VARCHAR2 | NO | Format Tech Code value. |  |

## 68.  MDD_MEDIA_ITEM_TYPES*

> Provides full details of item types for media

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key.  Unique ID of item type |  |
| 2         | ITEM_TYPE_NAME | VARCHAR2 | YES | Name of item type |  |
| 3         | ITEM_TYPE_DESCRIPTION | VARCHAR2 | YES | Description of item type |  |
| 4         | ITEM_TYPE_SHORTCODE | VARCHAR2 | YES | Two letter short code of item type |  |
| 5         | ITEM_TYPE_SHORTNAME | VARCHAR2 | YES | Short name code of item type |  |
| 6         | ITEM_GROUP | VARCHAR2 | YES | Name of group that item belongs to |  |
| 7         | ITEM_GROUP_ID | NUMBER | YES | ID of group that item belongs to |  |

## 69.  MDD_MEDIA_LOCATORS*

> This view displays locator metadata for media item

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | LOCATOR_ID | NUMBER | YES | Primary Key |  |
| 2         | MEDIA_ID_FK | NUMBER | YES | Foreign Key, used to link to Media item |  |
| 3         | LINKING_GUID | VARCHAR2 | YES |  |  |
| 4         | LOCATOR_TYPE | VARCHAR2 | YES |  |  |
| 5         | IN_TC_TEXT | VARCHAR2 | YES | Timecode IN |  |
| 6         | OUT_TC_TEXT | VARCHAR2 | YES | Timecode OUT |  |
| 7         | NOTES | VARCHAR2 | YES | Operator notes |  |
| 8         | CREATED_BY | VARCHAR2 | YES | Name of user who created the locator |  |
| 9         | CREATED_DATE | DATE | YES | Date locator created |  |
| 10         | MODIFIED_BY | VARCHAR2 | YES | Name of user who modified the locator |  |
| 11         | MODIFIED_DATE | DATE | YES | Date locator modified |  |

## 70.  MDD_MEDIA_METADATA*

> Provides metadata information about Media items (excluding virtual media items).

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | NO |  |  |
| 2         | SERIES_ID_FK | NUMBER | YES |  |  |
| 3         | TITLE_ID_FK | NUMBER | NO |  |  |
| 4         | MASTER_VERSION_ID_FK | NUMBER | NO |  |  |
| 5         | VERSION_ID_FK | NUMBER | NO |  |  |
| 6         | MEDIA_TITLE | VARCHAR2 | YES |  |  |
| 7         | MEDIA_SERIES_TITLE | VARCHAR2 | YES |  |  |
| 8         | MEDIA_ID1 | VARCHAR2 | NO |  |  |
| 9         | MEDIA_ID2 | VARCHAR2 | YES |  |  |
| 10         | ITEM_TYPE_ID | NUMBER | NO |  |  |
| 11         | ITEM_TYPE | VARCHAR2 | YES |  |  |
| 12         | ITEM_SUB_TYPE_ID | NUMBER | YES |  |  |
| 13         | ITEM_SUB_TYPE | VARCHAR2 | YES |  |  |
| 14         | ITEM_TYPE_SHORTCODE | VARCHAR2 | YES |  |  |
| 15         | ITEM_FORMAT_ID | NUMBER | YES |  |  |
| 16         | ITEM_FORMAT | VARCHAR2 | YES |  |  |
| 17         | OWNERS | VARCHAR2 | NO |  |  |
| 18         | DESCRIPTION | VARCHAR2 | YES |  |  |
| 19         | SERIES_NAME | VARCHAR2 | YES |  |  |
| 20         | SERIES_NO | NUMBER | YES |  |  |
| 21         | SERIES_EPISODE_NO | NUMBER | YES |  |  |
| 22         | SERIES_ID1 | VARCHAR2 | YES |  |  |
| 23         | SERIES_ID2 | VARCHAR2 | YES |  |  |
| 24         | PROG_ID1 | VARCHAR2 | YES |  |  |
| 25         | PROG_ID2 | VARCHAR2 | YES |  |  |
| 26         | HOUSE_NUMBER | VARCHAR2 | YES |  |  |
| 27         | VERSION_NAME | VARCHAR2 | YES |  |  |
| 28         | VERSION_ID1 | VARCHAR2 | YES |  |  |
| 29         | VERSION_ID2 | VARCHAR2 | YES |  |  |
| 30         | PRODUCTION_YEAR | NUMBER | YES |  |  |
| 31         | SOM | NUMBER | NO |  |  |
| 32         | EOM | NUMBER | NO |  |  |
| 33         | SOM_TIMECODE | VARCHAR2 | YES |  |  |
| 34         | EOM_TIMECODE | VARCHAR2 | YES |  |  |
| 35         | CREATED_DATE | DATE | NO |  |  |
| 36         | CREATED_BY | VARCHAR2 | NO |  |  |
| 37         | MODIFIED_DATE | DATE | YES |  |  |
| 38         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 39         | USAGE_ID | NUMBER | YES |  |  |
| 40         | USAGE_TYPE | VARCHAR2 | YES |  |  |
| 41         | PROGRAM_DURATION | NUMBER | YES |  |  |
| 42         | DURATION_MILLISECONDS | NUMBER | YES |  |  |
| 43         | DURATION_SECONDS | NUMBER | YES |  |  |
| 44         | CALCULATED_DURATION | NUMBER | YES |  |  |
| 45         | DURATION_TIMECODE | VARCHAR2 | YES |  |  |
| 46         | ASSESS_STATUS | VARCHAR2 | YES |  |  |
| 47         | TV_STD_ID | NUMBER | YES |  |  |
| 48         | TV_STD | NVARCHAR2 | YES |  |  |
| 49         | ASPECT_RATIO_ID | NUMBER | YES |  |  |
| 50         | ASPECT_RATIO | VARCHAR2 | YES |  |  |
| 51         | AFD_ID | NUMBER | YES |  |  |
| 52         | AFD_DESC | NVARCHAR2 | YES |  |  |
| 53         | LANGUAGE_ID | NUMBER | YES |  |  |
| 54         | LANGUAGE | VARCHAR2 | YES |  |  |
| 55         | CLOSEDCAPTION | VARCHAR2 | YES |  |  |
| 56         | SUBTITLES | VARCHAR2 | YES |  |  |
| 57         | COLOR | NUMBER | YES |  |  |
| 58         | COLOUR_DESC | NVARCHAR2 | YES |  |  |
| 59         | MEDIA_LOCATION | VARCHAR2 | YES |  |  |
| 60         | PARENT_ID | NUMBER | YES |  |  |
| 61         | MEDIA_FORMAT | VARCHAR2 | YES |  |  |
| 62         | FILE_TYPE | VARCHAR2 | YES |  |  |
| 63         | MEDIA_FORMAT_ID | NUMBER | YES |  |  |
| 64         | MEDIA_TYPE | NUMBER | NO |  |  |
| 65         | MEDIA_TYPE_DESC | VARCHAR2 | YES |  |  |
| 66         | MEDIA_FORMAT_FULL | VARCHAR2 | YES |  |  |
| 67         | ARCHIVED | NUMBER | YES |  |  |
| 68         | DELETED | NUMBER | YES |  |  |
| 69         | MI_DELETED | NUMBER | YES |  |  |
| 70         | DELETED_DATE | DATE | YES |  |  |
| 71         | MEDIA_FORMAT_CODE | VARCHAR2 | YES |  |  |
| 72         | FLAG_SUPPLIED | NUMBER | YES |  |  |
| 73         | FLAG_CREATED | NUMBER | YES |  |  |
| 74         | ORIGIN | VARCHAR2 | YES |  |  |
| 75         | A_GRADE | NUMBER | YES |  |  |
| 76         | V_GRADE | NUMBER | YES |  |  |
| 77         | SUITABLE_VOEC | NUMBER | YES |  |  |
| 78         | MEDIA_LINK_ID_FK | NUMBER | YES |  |  |
| 79         | MI_LINK_GUID | VARCHAR2 | YES |  |  |
| 80         | DFILE_LINK_GUID | VARCHAR2 | YES |  |  |
| 81         | DIVA_CATEGORY | VARCHAR2 | YES |  |  |
| 82         | DIVA_MEDIA_GROUP | VARCHAR2 | YES |  |  |
| 83         | FPS | NVARCHAR2 | YES |  |  |
| 84         | CHECKSUM | VARCHAR2 | YES |  |  |
| 85         | LAST_TX_DATE | DATE | YES |  |  |
| 86         | ASSISTED_ASSESS_STATUS | VARCHAR2 | YES |  |  |
| 87         | MEDIA_ID3 | VARCHAR2 | YES |  |  |
| 88         | MEDIA_SHELL | VARCHAR2 | YES |  |  |
| 89         | IS_ORIGINAL_AUDIO | VARCHAR2 | YES |  |  |

## 71.  MDD_MEDIA_RIGHTS*

> Provides details of Rights Agreements

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RIGHTS_ID | NUMBER | NO | Primary Key.  Unique ID of Rights Agreement. |  |
| 2         | RIGHTS_HOLDER | NUMBER | YES | Rights Holder. |  |
| 3         | CONTACT | VARCHAR2 | YES | Rights Contact. |  |
| 4         | AGREEMENT_DATE | DATE | YES | Agreement Date. |  |
| 5         | FILE_REF | VARCHAR2 | YES | File Reference. |  |
| 6         | CREATED | DATE | YES | Date when the information got created. |  |
| 7         | CREATED_BY | VARCHAR2 | YES | Name of user who created the information. |  |
| 8         | MEDIA_ID | NUMBER | YES | MEDIA ID. |  |
| 9         | PERMISSION_TYPE | NUMBER | YES | Type of Permission. |  |
| 10         | PERM_TYPE_DESC | VARCHAR2 | YES | Permission type Description |  |
| 11         | START_DATE | DATE | YES | Start Date. |  |
| 12         | END_DATE | DATE | YES | End Date. |  |
| 13         | GEOGRAPHICAL_COVERAGE | NUMBER | YES | Geographical Coverage. |  |
| 14         | GEO_COVERAGE_DESC | VARCHAR2 | YES | Geographic Coverage Description |  |
| 15         | PROJECT_CODE | VARCHAR2 | YES | Project Code |  |
| 16         | PROJECT_CODE_DESC | VARCHAR2 | YES | Project Code Description |  |

## 72.  MDD_MEDIA_SEGMENTS*

> Provides a view on segment data held at media item level. The durations are displayed as timecode and also as a frame count.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | SEGMENT_ID | NUMBER | NO | Primary Key.  Unique ID of the segment. |  |
| 2         | MEDIA_ID | NUMBER | YES | Foreign Key.  Links to media to MDD_MEDIA. |  |
| 3         | SEQUENCE_NO | NUMBER | YES | Sequence number of the segment |  |
| 4         | SEGMENT_NO | NUMBER | YES | Same as SEQUENCE_NO, renamed to clarify use |  |
| 5         | PART_NO | NUMBER | YES | Part number of the segment |  |
| 6         | SEGMENT_TYPE | NUMBER | YES | Internal use ID |  |
| 7         | PART_TYPE_ID | NUMBER | YES |  |  |
| 8         | SEGMENT_TYPE_DESC | NVARCHAR2 | YES | Description of segment type.  (This will only be available if config |  |
| 9         | SEGMENT_TYPE_SHORT | NVARCHAR2 | YES | Short code of Segment Type. |  |
| 10         | SEGMENT_TITLE | VARCHAR2 | YES | Title assigned to segment |  |
| 11         | SOM_FRAMES | NUMBER | YES | Start of Media in frames. |  |
| 12         | SOM | VARCHAR2 | YES | Start of Media displayed as a timecode. |  |
| 13         | EOM_FRAMES | NUMBER | YES | End of Media in frames. |  |
| 14         | EOM | VARCHAR2 | YES | End of Media displayed as a timecode. |  |
| 15         | DURATION_FRAMES | NUMBER | YES | Duration of a segment in frames. |  |
| 16         | DUR | VARCHAR2 | YES | Duration of segment displayed as a timecode. |  |
| 17         | USE_IN_DUR_CALC | NUMBER | YES | Should this segment be used to calculate duration? |  |
| 18         | TX_PART | NUMBER | YES | Is this segment valid for transmission? |  |
| 19         | CREATED_BY | VARCHAR2 | NO |  |  |
| 20         | CREATED_DATE | DATE | NO |  |  |
| 21         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 22         | MODIFIED_DATE | DATE | YES |  |  |

## 73.  MDD_MEDIA_SIMPLE*

> Provides information about Media items (excluding virtual media items).

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | NO | Primary Key.  Unique ID of Media item |  |
| 2         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links Media to Version in MDD_VERSIONS |  |
| 3         | VERSION_NAME | VARCHAR2 | YES | Name of the version that the Media is associated with |  |
| 4         | VERSION_ID1 | VARCHAR2 | YES | Client specific version identifier |  |
| 5         | DIGITAL_FILENAME | VARCHAR2 | YES |  |  |
| 6         | PATH | VARCHAR2 | YES | Full path of digital media, including location and filename |  |
| 7         | DEVICE_ID | NUMBER | YES | Foreign key link to MDD_CODES_DEVICES |  |
| 8         | MEDIA_TYPE | NUMBER | NO | Internal use ID |  |
| 9         | MEDIA_TYPE_DESC | VARCHAR2 | YES | Description of the Material Type eg Physical A/V Material |  |
| 10         | MEDIA_FORMAT_NAME | VARCHAR2 | YES | Format of Media, eg IPV Browse |  |
| 11         | DELETED | NUMBER | YES | Boolean value indicating whether the Media item has been marked |  |

## 74.  MDD_MEDIA_USAGE_TYPES*

> Provides full details of active media usages.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key.  Unique ID of usage type. |  |
| 2         | USAGE_NAME | VARCHAR2 | NO | Name of usage type, eg Core audio. |  |
| 3         | USAGE_DESCRIPTION | VARCHAR2 | YES | Description of usage. |  |
| 4         | USAGE_SHORTCODE | VARCHAR2 | NO | Usage shortcode. |  |

## 75.  MDD_MEDIA_VALUATION_MEDIA*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_FK | NUMBER | NO |  |  |
| 2         | MEDIA_ID1 | VARCHAR2 | NO |  |  |
| 3         | VALUATION_PERIOD_FK | NUMBER | YES |  |  |
| 4         | VALUATION_PERIOD | VARCHAR2 | YES |  |  |
| 5         | USAGE_GROUP_FK | NUMBER | YES |  |  |
| 6         | USAGE_GROUP | VARCHAR2 | YES |  |  |
| 7         | ORIGIN_FK | NUMBER | YES |  |  |
| 8         | ORIGIN | VARCHAR2 | YES |  |  |
| 9         | ACQ_TYPE_ELEMENT_FK | NUMBER | YES |  |  |
| 10         | ACQ_TYPE_ELEMENT | VARCHAR2 | YES |  |  |
| 11         | ITEM_FORMAT_FK | NUMBER | YES |  |  |
| 12         | ITEM_FORMAT | VARCHAR2 | YES |  |  |
| 13         | ITEM_TYPE_FK | NUMBER | YES |  |  |
| 14         | ITEM_TYPE | VARCHAR2 | YES |  |  |
| 15         | VALUATION_FK | VARCHAR2 | YES |  |  |
| 16         | TECH_CODE | VARCHAR2 | YES |  |  |
| 17         | VALUE_BY_BITWISE | NUMBER | YES |  |  |
| 18         | CARRIERS | NUMBER | YES |  |  |
| 19         | FILE_SIZE_BYTES | NUMBER | YES |  |  |
| 20         | CREATED_DT | DATE | NO |  |  |

## 76.  MDD_MEDIA_WITH_VIRTUAL*

> Provides information about Media items (including virtual media items).

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID | NUMBER | NO |  |  |
| 2         | SERIES_ID_FK | NUMBER | YES |  |  |
| 3         | TITLE_ID_FK | NUMBER | NO |  |  |
| 4         | MASTER_VERSION_ID_FK | NUMBER | NO |  |  |
| 5         | VERSION_ID_FK | NUMBER | NO |  |  |
| 6         | ACQ_ID_FK | NUMBER | YES |  |  |
| 7         | MEDIA_TITLE | VARCHAR2 | YES |  |  |
| 8         | MEDIA_SERIES_TITLE | VARCHAR2 | YES |  |  |
| 9         | MEDIA_ID1 | VARCHAR2 | NO |  |  |
| 10         | COMPONENT_NO | VARCHAR2 | YES |  |  |
| 11         | CARRIER_NO | VARCHAR2 | YES |  |  |
| 12         | MEDIA_ID2 | VARCHAR2 | YES |  |  |
| 13         | ITEM_TYPE_ID | NUMBER | NO |  |  |
| 14         | ITEM_TYPE | VARCHAR2 | YES |  |  |
| 15         | ITEM_FORMAT_ID | NUMBER | YES |  |  |
| 16         | ITEM_FORMAT | VARCHAR2 | YES |  |  |
| 17         | NFSA_ITEM_TYPE | VARCHAR2 | YES |  |  |
| 18         | OWNERS | VARCHAR2 | NO |  |  |
| 19         | DESCRIPTION | VARCHAR2 | YES |  |  |
| 20         | SERIES_NAME | VARCHAR2 | YES |  |  |
| 21         | SERIES_NO | NUMBER | YES |  |  |
| 22         | SERIES_EPISODE_NO | NUMBER | YES |  |  |
| 23         | SERIES_ID1 | VARCHAR2 | YES |  |  |
| 24         | SERIES_ID2 | VARCHAR2 | YES |  |  |
| 25         | PROG_ID1 | VARCHAR2 | YES |  |  |
| 26         | PROG_ID2 | VARCHAR2 | YES |  |  |
| 27         | HOUSE_NUMBER | VARCHAR2 | YES |  |  |
| 28         | VERSION_NAME | VARCHAR2 | YES |  |  |
| 29         | VERSION_ID1 | VARCHAR2 | YES |  |  |
| 30         | VERSION_ID2 | VARCHAR2 | YES |  |  |
| 31         | PRODUCTION_YEAR | NUMBER | YES |  |  |
| 32         | SOM | NUMBER | NO |  |  |
| 33         | EOM | NUMBER | NO |  |  |
| 34         | SOM_TIMECODE | VARCHAR2 | YES |  |  |
| 35         | EOM_TIMECODE | VARCHAR2 | YES |  |  |
| 36         | CREATED_DATE | DATE | NO |  |  |
| 37         | CREATED_BY | VARCHAR2 | NO |  |  |
| 38         | CREATED_BY_DEPT_ID | NUMBER | YES |  |  |
| 39         | CREATED_BY_DEPT | VARCHAR2 | YES |  |  |
| 40         | CREATED_BY_EMAIL | VARCHAR2 | YES |  |  |
| 41         | MODIFIED_DATE | DATE | YES |  |  |
| 42         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 43         | STATUS_ID | NUMBER | YES |  |  |
| 44         | STATUS_DESC | NVARCHAR2 | YES |  |  |
| 45         | RESTRICTION_STATUS | VARCHAR2 | YES |  |  |
| 46         | USAGE_ID | NUMBER | YES |  |  |
| 47         | USAGE_TYPE | VARCHAR2 | YES |  |  |
| 48         | USAGE_SHORTCODE | VARCHAR2 | YES |  |  |
| 49         | PROGRAM_DURATION | NUMBER | YES |  |  |
| 50         | DURATION_MILLISECONDS | NUMBER | YES |  |  |
| 51         | CALCULATED_DURATION | NUMBER | YES |  |  |
| 52         | ASSESS_STATUS | VARCHAR2 | YES |  |  |
| 53         | TV_STD_ID | NUMBER | YES |  |  |
| 54         | TV_STD | NVARCHAR2 | YES |  |  |
| 55         | ASPECT_RATIO_ID | NUMBER | YES |  |  |
| 56         | ASPECT_RATIO | VARCHAR2 | YES |  |  |
| 57         | AFD_ID | NUMBER | YES |  |  |
| 58         | AFD_DESC | NVARCHAR2 | YES |  |  |
| 59         | ASPECT_RATIO_LEGACY_ID | NUMBER | YES |  |  |
| 60         | ASPECT_RATIO_LEGACY | NVARCHAR2 | YES |  |  |
| 61         | AFD_CODE | VARCHAR2 | YES |  |  |
| 62         | LANGUAGE_ID | NUMBER | YES |  |  |
| 63         | LANGUAGE | VARCHAR2 | YES |  |  |
| 64         | FLAG_1 | NUMBER | YES |  |  |
| 65         | FLAG_2 | NUMBER | YES |  |  |
| 66         | FLAG_3 | NUMBER | YES |  |  |
| 67         | FLAG_4 | NUMBER | YES |  |  |
| 68         | FLAG_5 | NUMBER | YES |  |  |
| 69         | FLAG_6 | NUMBER | YES |  |  |
| 70         | FLAG_7 | NUMBER | YES |  |  |
| 71         | FLAG_8 | NUMBER | YES |  |  |
| 72         | FLAG_9 | NUMBER | YES |  |  |
| 73         | FLAG_10 | NUMBER | YES |  |  |
| 74         | FLAG_11 | NUMBER | YES |  |  |
| 75         | FLAG_12 | NUMBER | YES |  |  |
| 76         | FLAG_13 | NUMBER | YES |  |  |
| 77         | FLAG_14 | NUMBER | YES |  |  |
| 78         | FLAG_15 | NUMBER | YES |  |  |
| 79         | FLAG_16 | NUMBER | YES |  |  |
| 80         | CLOSEDCAPTION | VARCHAR2 | YES |  |  |
| 81         | SUBTITLES | VARCHAR2 | YES |  |  |
| 82         | COLOR | NUMBER | YES |  |  |
| 83         | COLOUR_DESC | NVARCHAR2 | YES |  |  |
| 84         | AU_TRACKS_NUM | NUMBER | YES |  |  |
| 85         | AU_TRACKS_LANGUAGES | VARCHAR2 | YES |  |  |
| 86         | AU_TRACKS_CONT | VARCHAR2 | YES |  |  |
| 87         | AU_TRACKS_MS | VARCHAR2 | YES |  |  |
| 88         | AU_TRACKS_MODE | VARCHAR2 | YES |  |  |
| 89         | OS_DIR | VARCHAR2 | YES |  |  |
| 90         | OS_FILENAME | VARCHAR2 | YES |  |  |
| 91         | PATH | VARCHAR2 | YES |  |  |
| 92         | FILE_SIZE | NUMBER | YES |  |  |
| 93         | MEDIA_LOCATION | VARCHAR2 | YES |  |  |
| 94         | PARENT_ID | NUMBER | YES |  |  |
| 95         | FILE_NAME | VARCHAR2 | YES |  |  |
| 96         | FILE_TYPE | VARCHAR2 | YES |  |  |
| 97         | FILE_EXTENSION | VARCHAR2 | YES |  |  |
| 98         | MEDIA_FORMAT_ID | NUMBER | YES |  |  |
| 99         | MEDIA_TYPE | NUMBER | NO |  |  |
| 100         | MEDIA_TYPE_DESC | VARCHAR2 | YES |  |  |
| 101         | MEDIA_FORMAT_NAME | VARCHAR2 | YES |  |  |
| 102         | ARCHIVED | NUMBER | YES |  |  |
| 103         | DELETED | NUMBER | YES |  |  |
| 104         | MI_DELETED | NUMBER | YES |  |  |
| 105         | DELETED_DATE | DATE | YES |  |  |
| 106         | FULL_TECHCODE | VARCHAR2 | YES |  |  |
| 107         | MEDIA_FORMAT_CODE | VARCHAR2 | YES |  |  |
| 108         | FLAG_SUPPLIED | NUMBER | YES |  |  |
| 109         | FLAG_CREATED | NUMBER | YES |  |  |
| 110         | ORIGIN | VARCHAR2 | YES |  |  |
| 111         | A_GRADE | NUMBER | YES |  |  |
| 112         | V_GRADE | NUMBER | YES |  |  |
| 113         | CRS_SERIES_ID | NUMBER | YES |  |  |
| 114         | CRS_SERIES_NO | VARCHAR2 | YES |  |  |
| 115         | CRS_SERIES_TITLE | VARCHAR2 | YES |  |  |
| 116         | SUITABLE_VOEC | NUMBER | YES |  |  |
| 117         | MEDIA_LINK_ID_FK | NUMBER | YES |  |  |
| 118         | DIVA_CATEGORY | VARCHAR2 | YES |  |  |
| 119         | DIVA_MEDIA_GROUP | VARCHAR2 | YES |  |  |

## 77.  MDD_MIS_AUDIO

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MIS_ID | NUMBER | YES |  |  |
| 2         | TASK_ID_FK | NUMBER | YES |  |  |
| 3         | TRACK_INDEX | NUMBER | YES |  |  |
| 4         | AU_NM_ID | VARCHAR2 | YES |  |  |
| 5         | AU_CONT_ID | VARCHAR2 | YES |  |  |
| 6         | AU_LANG_ID | VARCHAR2 | YES |  |  |
| 7         | AU_MS_ID | VARCHAR2 | YES |  |  |
| 8         | AU_NR_ID | VARCHAR2 | YES |  |  |
| 9         | KHZ | VARCHAR2 | YES |  |  |
| 10         | PEAK | VARCHAR2 | YES |  |  |
| 11         | AVG | VARCHAR2 | YES |  |  |
| 12         | DIP | VARCHAR2 | YES |  |  |
| 13         | LM100_SHORT | VARCHAR2 | YES |  |  |
| 14         | LM100_LONG | VARCHAR2 | YES |  |  |
| 15         | LANGUAGE_TAG | VARCHAR2 | YES |  |  |

## 78.  MDD_MOVEMENTS*

> Provides details of Carrier or Container Movements.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MOVEMENT_ID | NUMBER | NO | Primary Key. Internal ID of the Movement |  |
| 2         | CONTAINER_ID_FK | NUMBER | YES | Foreign Key. Links to Carrier or Container in MDD_CONTAINERS |  |
| 3         | PREVIOUS_LOCATION_ID_FK | NUMBER | YES | Foreign Key. Links to original location in MDD_LOCATIONS |  |
| 4         | PREVIOUS_LOCATION_NAME | VARCHAR2 | YES | Name of the original location |  |
| 5         | PREVIOUS_ENTITY_ID_FK | NUMBER | YES | Foreign Key. Links to Authorities in MDD_NAMES |  |
| 6         | MOVEMENT_REASON | VARCHAR2 | YES | Description of movement |  |
| 7         | NEW_LOCATION_ID_FK | NUMBER | YES | Foreign Key. Links to new location in MDD_LOCATIONS |  |
| 8         | NEW_LOCATION_NAME | VARCHAR2 | YES | Name of the new location |  |
| 9         | NEW_ENTITY_ID_FK | NUMBER | YES | Foreign Key. Links to Authorities in MDD_NAMES |  |
| 10         | CREATED_DATE | DATE | NO | Date the Carrier or Container was moved |  |
| 11         | CREATED_BY | VARCHAR2 | NO | Name of the User who actioned the move |  |
| 12         | TASK_ID_FK | NUMBER | YES | Foreign Key. Links to the Internal Movement or Despatch task in |  |

## 79.  MDD_NAA_CARRIER_SHM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CARRIER_FORMAT_ID | NUMBER | NO | Foreign Key.  Unique ID of Carrier Format. Linking to |  |

## 80.  MDD_NAA_CONTAINER_SHM

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | CONTAINER_FORMAT_ID | NUMBER | NO | Foreign Key.  Unique ID of Container Format linking to |  |

## 81.  MDD_NAMES*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | NAME_ID | NUMBER | NO |  |  |
| 2         | ENTITY_ID | NUMBER | NO |  |  |
| 3         | FULL_NAME | VARCHAR2 | YES |  |  |
| 4         | FIRSTNAME | VARCHAR2 | YES |  |  |
| 5         | SURNAME_OR_COMPANY_NAME | VARCHAR2 | NO |  |  |
| 6         | CONTACT_ROLE | VARCHAR2 | YES |  |  |
| 7         | CONTACT_FIRSTNAME | VARCHAR2 | YES |  |  |
| 8         | CONTACT_SURNAME_COMPANY_NA | VARCHAR2 | NO |  |  |
| 9         | QUALIFIER | VARCHAR2 | YES |  |  |
| 10         | DATE_OF_BIRTH | DATE | YES |  |  |
| 11         | DATE_OF_DEATH | DATE | YES |  |  |
| 12         | OTHER_NAME | VARCHAR2 | YES |  |  |
| 13         | PREFERRED_NAME | VARCHAR2 | YES |  |  |
| 14         | NAME_TYPE | VARCHAR2 | YES |  |  |
| 15         | GENDER | VARCHAR2 | YES |  |  |
| 16         | DATES | VARCHAR2 | YES |  |  |
| 17         | ADDRESS | VARCHAR2 | YES |  |  |
| 18         | CITY | VARCHAR2 | YES |  |  |
| 19         | STATE | VARCHAR2 | YES |  |  |
| 20         | POSTCODE | VARCHAR2 | YES |  |  |
| 21         | PHONE1 | VARCHAR2 | YES |  |  |
| 22         | PHONE2 | VARCHAR2 | YES |  |  |
| 23         | FAX | VARCHAR2 | YES |  |  |
| 24         | EMAIL1 | VARCHAR2 | YES |  |  |
| 25         | EMAIL2 | VARCHAR2 | YES |  |  |
| 26         | WEB | VARCHAR2 | YES |  |  |
| 27         | FILE_NO | VARCHAR2 | YES |  |  |
| 28         | DELIVER_FAO | VARCHAR2 | YES |  |  |
| 29         | DELIVERY_CONTACT | VARCHAR2 | YES |  |  |
| 30         | DELIVERY_ADDRESS | VARCHAR2 | YES |  |  |
| 31         | DELIVERY_CITY | VARCHAR2 | YES |  |  |
| 32         | DELIVERY_STATE | VARCHAR2 | YES |  |  |
| 33         | DELIVERY_POSTCODE | VARCHAR2 | YES |  |  |
| 34         | CHECKED | DATE | YES |  |  |
| 35         | CHECKED_BY | VARCHAR2 | YES |  |  |
| 36         | DELIVERY_COUNTRY | NUMBER | YES |  |  |
| 37         | CULTURAL_BACKGROUND | VARCHAR2 | YES |  |  |
| 38         | BIOGRAPHY | CLOB | YES |  |  |
| 39         | FULL_BIOGRAPHY | CLOB | YES |  |  |
| 40         | NOTES | CLOB | YES |  |  |
| 41         | CREATED_BY | VARCHAR2 | YES |  |  |
| 42         | CREATED | DATE | YES |  |  |
| 43         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 44         | MODIFIED | DATE | YES |  |  |

## 82.  MDD_NFSA_MEDIA_USAGE_GROUPS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | USAGE_ID | NUMBER | YES |  |  |
| 2         | USAGE_NAME | VARCHAR2 | YES |  |  |
| 3         | USAGE_SHORTCODE | VARCHAR2 | YES |  |  |
| 4         | NFSA_USAGE_GROUP | VARCHAR2 | YES |  |  |

## 83.  MDD_PACKAGES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_ID | NUMBER | NO | Primary Key.  Unique ID of the Package |  |
| 2         | PACKAGE_REQ_ID_FK | NUMBER | YES | Foreign key linking to MDD_PACKAGE_REQUIREMENTS view |  |
| 3         | VALID_FROM | DATE | YES | Date Package is valid from |  |
| 4         | VALID_TO | DATE | YES | Date Package is valid to |  |
| 5         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Provides a link to corresponding version |  |
| 6         | PREP_JOB_ID | NUMBER | YES |  |  |
| 7         | PREP_JOB_STATUS_ID | NUMBER | YES |  |  |
| 8         | PREP_JOB_STATUS | VARCHAR2 | YES |  |  |
| 9         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Provides a link to corresponding job |  |
| 10         | PACKAGE_JOB_NO | VARCHAR2 | YES | Reference to the Job that was raised from the Package |  |
| 11         | PACKAGE_JOB_STATUS_ID | NUMBER | YES |  |  |
| 12         | PACKAGE_JOB_STATUS | VARCHAR2 | YES | Status of the Package Publish Job |  |
| 13         | EXTERNAL_REF | VARCHAR2 | YES | External Reference ID |  |
| 14         | ASSET_ID_CHOICE | VARCHAR2 | YES | Option selected for handling an Asset ID when package is reset |  |
| 15         | USER_ASSET_ID | VARCHAR2 | YES | Custom Asset ID entered when package is reset |  |
| 16         | CREATED_BY | VARCHAR2 | YES | Name of user who created the Package |  |
| 17         | CREATED_DATE | DATE | NO | Date the Package was created |  |
| 18         | CREATED_BY_EMAIL | VARCHAR2 | YES | Email address of user who created the Package |  |
| 19         | MODIFIED_DATE | DATE | YES |  |  |
| 20         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 21         | DELETED | NUMBER | NO | Deleted status of Package.  0 = Not Deleted, 1 = Deleted |  |

## 84.  MDD_PACKAGE_MEDIA

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_ID_FK | NUMBER | NO | Foreign Key.  Provides a link to the Package |  |
| 2         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Provides a link to the media select for the Package |  |
| 3         | MEDIA_TYPE | CHAR | YES | Type of Media selected |  |

## 85.  MDD_PACKAGE_REQUIREMENTS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PACKAGE_REQ_ID | NUMBER | NO | Primary Key.  Unique ID of the Package Requirements |  |
| 2         | NAME | VARCHAR2 | NO | Name of Package Requirement |  |
| 3         | DESCRIPTION | VARCHAR2 | YES | Description of Package Requirement |  |
| 4         | EXTERNAL_ID | VARCHAR2 | YES | External ID associated with Package Requirement |  |

## 86.  MDD_POST_EVENT_NOTES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key. |  |
| 2         | EVENT_NOTES | VARCHAR2 | YES | Event Notes from Make Details of Post task. |  |
| 3         | MEDIA_ID_FK | NUMBER | NO | Foreign key. Links to MDD_MEDIA for full details of associated |  |

## 87.  MDD_PRODUCERS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to task in MDD_TASKS |  |
| 2         | PRODUCER | VARCHAR2 | YES | Name of producer. |  |
| 3         | PRODUCER_TITLE | VARCHAR2 | YES | Title of producer. |  |

## 88.  MDD_PROGRAMS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PROGRAM_ID | NUMBER | YES |  |  |
| 2         | ITEM_TYPE_ID | NUMBER | YES |  |  |
| 3         | SERIES_TITLE | VARCHAR2 | YES |  |  |
| 4         | EPISODE_NUM | NUMBER | YES |  |  |
| 5         | TITLE | VARCHAR2 | YES |  |  |
| 6         | SERIES_FROM_ABS | VARCHAR2 | YES |  |  |
| 7         | PRODUCTION_YEAR | NUMBER | YES |  |  |
| 8         | CREATED_BY | VARCHAR2 | YES |  |  |
| 9         | CREATED_DATE | DATE | YES |  |  |
| 10         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 11         | MODIFIED_DATE | DATE | YES |  |  |
| 12         | VERSION_NAME | VARCHAR2 | YES |  |  |
| 13         | GENRE | VARCHAR2 | YES |  |  |
| 14         | MEDIUM | VARCHAR2 | YES |  |  |
| 15         | SUB_MEDIUM | VARCHAR2 | YES |  |  |
| 16         | FORM | VARCHAR2 | YES |  |  |

## 89.  MDD_PROGRAM_FORM*

> There may be more than one form for a particular program.  This view provides a list of forms per program.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TITLE_OR_VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links to either title (MDD_TITLES) or version |  |
| 2         | FORM | VARCHAR2 | YES | Description of form. |  |

## 90.  MDD_RECORD_LABELS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RECORD_LABEL_ID | NUMBER | YES | Primary Key. Internal ID of the Record Label. |  |
| 2         | RECORD_LABEL_NAME | VARCHAR2 | YES | Name of Record Label. |  |
| 3         | COPYRIGHT_HOLDER_ID_FK | NUMBER | YES | Foreign Key. Links to Copyright Holder details in MDD_NAMES. |  |
| 4         | COPYRIGHT_HOLDER | VARCHAR2 | YES | Name of Copyright Holder. |  |
| 5         | CREATED_BY | NVARCHAR2 | YES | Name of the user who created the Record Label. |  |
| 6         | CREATED_DATE | DATE | YES | Date the Record Label was created. |  |
| 7         | MODIFIED_BY | NVARCHAR2 | YES | Name of the user who last modified the Record Label. |  |
| 8         | MODIFIED_DATE | DATE | YES | Date the Record Label was last modified. |  |

## 91.  MDD_RECORD_LABEL_MEDIA_LINKS*

> Provides details of links between Record Labels and Media Items.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RECORD_LABEL_ID_FK | NUMBER | NO | Foreign Key. Link to Record Label details in MDD_RECORD_LABELS. |  |
| 2         | MEDIA_ID_FK | NUMBER | NO | Foreign Key. Link to Media Item details in MDD_MEDIA. |  |
| 3         | RECORD_LABEL_ID | NUMBER | NO | Record Label ID. |  |
| 4         | VERSION_ID_FK | NUMBER | YES | Foreign Key. Link to Version details in MDD_VERSIONS. |  |
| 5         | CARRIER_NO | NUMBER | YES | Carrier Number of linked Media Item. |  |
| 6         | SIDE_NO | NUMBER | YES | Carrier Side Number of linked Media Item. |  |
| 7         | RELEASE_YEAR | VARCHAR2 | YES | Record Label Release Year. |  |
| 8         | CATALOGUE_NO_PREFIX | VARCHAR2 | YES | Catalogue Number Prefix. |  |
| 9         | CATALOGUE_NO_NUMBER | VARCHAR2 | YES | Catalogue Number. |  |
| 10         | CATALOGUE_NO_SUFFIX | VARCHAR2 | YES | Catalogue Number Suffix. |  |

## 92.  MDD_RELATED_NAMES*

> This view displays other names related to a Name Authority.  It also provides a foreign key allowing a link to the MDD_NAMES view for more details of related name if required.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | NAME_ID_FK | NUMBER | YES | Foreign Key.  Links to the MDD_NAMES view for full details of the |  |
| 2         | RELATED_NAME_ID | NUMBER | YES | Primary Key.  Unique ID of the related name.  This can also be used |  |
| 3         | RELATED_NAME | VARCHAR2 | YES | Full related name (or company name) |  |
| 4         | DATES | VARCHAR2 | YES | Dates that related name are relevant. |  |

## 93.  MDD_RESPONSIBILITIES

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | USER_ID | VARCHAR2 | YES | User logon ID. |  |
| 2         | FIRST_NAME | VARCHAR2 | YES | First name of user. |  |
| 3         | LAST_NAME | VARCHAR2 | YES | Last name of user. |  |
| 4         | ROLE_ID | NUMBER | NO | ID for internal use only. |  |
| 5         | ROLE_NAME | VARCHAR2 | NO | Name of role that has responsibilities assigned. |  |
| 6         | ROLE_DESCRIPTION | VARCHAR2 | YES | Description of the role that has responsibilities assigned. |  |
| 7         | RESPONSIBILITY | VARCHAR2 | YES | Responsibility.  This starts at the highest level and works its way |  |
| 8         | RESPONSIBILITY_DESC | VARCHAR2 | YES | Description of the responsibility |  |
| 9         | PERMISSION | NUMBER | NO | ID for internal use only. |  |
| 10         | ACCESS_TO | CHAR | YES | Indicates if a user has access rights for a particular function where |  |
| 11         | VIEW | CHAR | YES | Indicates if a user has view rights for a particular function where |  |
| 12         | MODIFY | CHAR | YES | Indicates if a user has modify rights for a particular function where |  |
| 13         | DELETE | CHAR | YES | Indicates if a user has delete rights for a particular function where |  |

## 94.  MDD_RESTRICTION_REASONS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RESTRICTION_REASON_ID | NUMBER | NO | Primary Key.  Unique ID of Restriction Reason |  |
| 2         | ACCESS_STATUS_ID_FK | NUMBER | NO | Foreign key. Links to ID in MDD_ACCESS_STATUS |  |
| 3         | RESTRICTION_REASON | VARCHAR2 | NO | Reason of Restriction |  |
| 4         | DATE_MODIFIED | DATE | NO | Date Modified |  |

## 95.  MDD_RIGHTS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RIGHTS_ID | NUMBER | NO | Primary Key.  Unique ID of Rights Agreement. |  |
| 2         | RIGHTS_HOLDER | NUMBER | YES | Rights Holder. |  |
| 3         | CONTACT | VARCHAR2 | YES | Rights Contact. |  |
| 4         | AGREEMENT_DATE | DATE | YES | Agreement Date. |  |
| 5         | FILE_REF | VARCHAR2 | YES | File Reference. |  |
| 6         | CREATED | DATE | YES | Date when the information got created. |  |
| 7         | CREATED_BY | VARCHAR2 | YES | Name of user who created the information. |  |
| 8         | PERMISSION_TYPE | NUMBER | YES | Type of Permission. |  |
| 9         | PERM_TYPE_DESC | VARCHAR2 | YES | Permission type Description |  |
| 10         | START_DATE | DATE | YES | Start Date. |  |
| 11         | END_DATE | DATE | YES | End Date. |  |
| 12         | GEOGRAPHICAL_COVERAGE | NUMBER | YES | Geographical Coverage. |  |
| 13         | GEO_COVERAGE_DESC | VARCHAR2 | YES | Geographic Coverage Description |  |
| 14         | PROJECT_CODE | VARCHAR2 | YES | Project Code |  |
| 15         | PROJECT_CODE_DESC | VARCHAR2 | YES | Project Code Description |  |

## 96.  MDD_SERIES_INDICATORS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | INDICATOR_ID | NUMBER | NO | Primary Key.  Unique ID of Indicator |  |
| 2         | EXTERNAL_ID | NUMBER | YES | Unique identifier assigned to the Indicator by Record Search |  |
| 3         | INDICATOR_NAME | VARCHAR2 | YES | Name of Indicator |  |
| 4         | INDICATOR_DESCRIPTION | VARCHAR2 | YES | Description of Indicator |  |

## 97.  MDD_SERIES_INDICATORS_LNK

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | ID | NUMBER | NO | Primary Key. |  |
| 2         | INDICATOR_ID_FK | NUMBER | NO | Foreign key.  Linking to indicator in MDD_SERIES_INDICATORS |  |
| 3         | SERIES_ID_FK | NUMBER | YES | Foreign key.  Linkiing to series in MDD_TITLES |  |
| 4         | IMPORTED | NUMBER | NO | Flag indicating if Indicator was imported |  |
| 5         | MI_ID_FK | NUMBER | YES | Foregin key.  Linking to media in MDD_MEDIA |  |
| 6         | MEDIA_ID_FK | NUMBER | YES | Foregin key.  Linking to media in MDD_MEDIA. (Replaces MI_ID_FK |  |

## 98.  MDD_SPACE_RESERVATION_ITEMS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RESERVATION_ID | NUMBER | YES | Primary Key.  Reservation ID |  |
| 2         | LOCATION_ID | NUMBER | YES | ID of the location of the reservation item |  |
| 3         | ITEM_COUNT | NUMBER | YES | Number of items in the reservation |  |
| 4         | ITEM_TYPE_ID | NUMBER | YES | ID of the reservation item type |  |
| 5         | ITEM_TYPE_NAME | VARCHAR2 | YES | Friendly name of the item type |  |
| 6         | FORMAT_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_CONTAINERS.FORMAT_ID |  |
| 7         | RESERVATION_LENGTH | NUMBER | YES | Length of the reservation in millimeters. Only non-zero when |  |
| 8         | RESERVATION_NAME | VARCHAR2 | YES | Name of the reservation |  |
| 9         | CREATED_DATE | DATE | NO | Date that the reservation was created |  |

## 99.  MDD_SYNONYMS*

> This view displays synonyms for a Name Authority.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | SYNONYM_ID | NUMBER | NO | Primary Key.  Unique ID of the synonym. |  |
| 2         | NAME_ID_FK | NUMBER | NO | Foreign Key.  Links to the MDD_NAMES view for full details of the |  |
| 3         | SYNONYM_NAME | VARCHAR2 | YES | Synonym name, eg Jim Smith vs James Smith. |  |
| 4         | DATES | VARCHAR2 | YES | Dates that related name are relevant. |  |
| 5         | NAME_TYPE | VARCHAR2 | YES |  |  |

## 100.  MDD_TASKS*

> This view provides information about a specific task.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID | NUMBER | NO | Primary Key.  Unique ID for task. |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links task to MDD_JOB. |  |
| 3         | TASK_TYPE_ID | NUMBER | YES | ID for internal use only. |  |
| 4         | TASK_TYPE | VARCHAR2 | YES | Type of task, eg Ingest. |  |
| 5         | TASK_CLIENT | VARCHAR2 | YES | Client associated with the task. |  |
| 6         | TASK_START_DATE | DATE | YES | Actual start date for the task. |  |
| 7         | TASK_END_DATE | DATE | YES | Actual end date for the task. |  |
| 8         | COMPLETE_BY | DATE | YES | Date task is due to be completed by. |  |
| 9         | TASK_STARTED_BY | VARCHAR2 | YES | Name of the operator who started the task. |  |
| 10         | TASK_COMPLETED_BY | VARCHAR2 | YES | Name of the operator who completed the task. |  |
| 11         | TASK_OPERATOR | VARCHAR2 | YES | Operator assigned to the task.  Obsolete.  Replaced by |  |
| 12         | TASK_OPERATOR_FULL | VARCHAR2 | YES | Full name of operator assigned to the task. |  |
| 13         | CURRENT_OPERATOR_FULL | VARCHAR2 | YES |  |  |
| 14         | TASK_POSITION | NUMBER | YES | Position of task within the job. |  |
| 15         | SCHEDULE_AREA | NUMBER | YES | ID for internal use only. |  |
| 16         | SCHEDULE_AREA_NAME | VARCHAR2 | YES | Name of Schedule Area that task is assigned to. |  |
| 17         | SCHEDULE_AREA_PARENT | VARCHAR2 | YES | Parent Schedule Area that task is assigned to. |  |
| 18         | SCHEDULE_AREA_CODE_FULL | VARCHAR2 | YES | Full Schedule Area codes that task is assigned to. |  |
| 19         | SCHEDULE_AREA_FULL | VARCHAR2 | YES | Full Schedule Area that task is assigned to. |  |
| 20         | CREATED_DATE | DATE | NO | Date task was created. |  |
| 21         | CREATED_BY | VARCHAR2 | NO | Name of user who created the task. |  |
| 22         | CREATED_BY_FULL | VARCHAR2 | YES | Full name of user who created the task. |  |
| 23         | MODIFIED_DATE | DATE | YES | Data task was last modified. |  |
| 24         | MODIFIED_BY | VARCHAR2 | YES | Name of user who last modified the task. |  |
| 25         | MODIFIED_BY_FULL | VARCHAR2 | YES | Full name of user who last modified the task. |  |
| 26         | TASK_STATUS_ID | NUMBER | YES | ID for internal use only. |  |
| 27         | TASK_STATUS | VARCHAR2 | YES | Status of task, eg In progress. |  |
| 28         | EQUIPMENT_USED_ID | VARCHAR2 | YES | Foreign Key.  Links task to MDD_TASK_EQUIPMENT. |  |
| 29         | TASK_NOTES | VARCHAR2 | YES | Notes for task. |  |
| 30         | FULL_NOTES | VARCHAR2 | YES | Full notes for task. |  |
| 31         | JOB_RAISED | NUMBER | YES | ID of the job raised by a Raise Workflow task. |  |
| 32         | FRIENDLY_NAME | VARCHAR2 | YES |  |  |

## 101.  MDD_TASKS_OLD*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID | NUMBER | NO |  |  |
| 2         | PRESET | VARCHAR2 | YES |  |  |
| 3         | COMPLETED_DATE | DATE | YES |  |  |
| 4         | DAY | VARCHAR2 | YES |  |  |
| 5         | MONTH | VARCHAR2 | YES |  |  |
| 6         | YEAR | VARCHAR2 | YES |  |  |
| 7         | TASK_TYPE | NUMBER | YES |  |  |

## 102.  MDD_TASK_CONFIG

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign key link to Task. |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign key link to Job. |  |
| 3         | ITEM_INDEX | NUMBER | YES | ID for internal use only. |  |
| 4         | TASK_TYPE_ID | NUMBER | YES | Unique identifier of task type. |  |
| 5         | TASK_TYPE | VARCHAR2 | YES | Type of task. |  |
| 6         | MOVE_MODE | VARCHAR2 | YES | The mode of move used by a Data Move task. |  |
| 7         | TOOL_TYPE | VARCHAR2 | YES | Type of Digital Tool used. |  |
| 8         | ARRIVE_BY | DATE | YES |  |  |
| 9         | DESPATCH_FROM_LOCATION | VARCHAR2 | YES |  |  |
| 10         | DESPATCH_TO_LOCATION | VARCHAR2 | YES |  |  |
| 11         | DESPATCH_TO_CONTACT | VARCHAR2 | YES | Location to where media is to be dispatched. |  |
| 12         | DESPATCH_TO_CONTACT_FIRST | VARCHAR2 | YES |  |  |
| 13         | DESPATCH_TO_CONTACT_LAST | VARCHAR2 | YES |  |  |
| 14         | DESPATCH_TO_ADDRESS | VARCHAR2 | YES | Address to which media is to be dispatched. |  |
| 15         | DESPATCH_TO_MAIL_CODE | VARCHAR2 | YES | Mail code to which media is to be dispatched. |  |
| 16         | DESPATCH_TO_NA | VARCHAR2 | YES | Name Authority to whom the media is to be dispatched. |  |
| 17         | DESPATCH_TO_NA_ADDRESS | VARCHAR2 | YES | Address of Name Authority to whom the media is to be dispatched. |  |
| 18         | DESPATCH_TO_NA_CITY | VARCHAR2 | YES | City for Name Authority to whom the media is to be dispatched. |  |
| 19         | DESPATCH_TO_NA_STATE | VARCHAR2 | YES | State for Name Authority to whom the media is to be dispatched. |  |
| 20         | DESPATCH_TO_NA_CODE | VARCHAR2 | YES | Post Code of Name Authority to whom the media is to be |  |
| 21         | ENTITY_ID_FK | NUMBER | YES | Foreign key link to Entity. |  |
| 22         | AGENCY_CODE | VARCHAR2 | YES | State for Name Authority to whom the media is to be dispatched. |  |
| 23         | AGENCY_NAME | VARCHAR2 | YES | Post Code of Name Authority to whom the media is to be |  |
| 24         | PROFILE_NAME | VARCHAR2 | YES | Name of Profile used in a Transcode task. |  |

## 103.  MDD_TASK_EQUIPMENT

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS for full details of associated |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_JOB for full details of associated job. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_MEDIA for full details of associated |  |
| 4         | DEVICE_USED | VARCHAR2 | YES | ID of device used. |  |
| 5         | DEVICE_NAME | VARCHAR2 | YES | Name of device used. |  |
| 6         | DEVICE_CODE | VARCHAR2 | YES | Code allocated to device used. |  |
| 7         | FACILITY_ID | VARCHAR2 | YES | ID of facility used. |  |
| 8         | FACILITY_NAME | VARCHAR2 | YES | Name of facility used. |  |

## 104.  MDD_TASK_EQUIPMENT_ID

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | For internal use only. |  |
| 2         | JOB_ID_FK | NUMBER | YES | For internal use only. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | For internal use only. |  |
| 4         | LINE_NO | NUMBER | YES | For internal use only. |  |
| 5         | DEVICE_ID | VARCHAR2 | YES | For internal use only. |  |
| 6         | FACILITY_ID | VARCHAR2 | YES | For internal use only. |  |

## 105.  MDD_TASK_MEDIA*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS for full details of associated |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_JOB for full details of associated job. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_MEDIA for full details of associated |  |
| 4         | CONTAINER_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_CONTAINERS for full details of |  |
| 5         | MEDIA_CLASS | VARCHAR2 | YES | Indicates whether the media is real or virtual at this stage of the |  |
| 6         | SOURCE | NUMBER | YES | Boolean value indicating whether the media is the source media for |  |
| 7         | ARRIVE_BY | DATE | YES | Date media is expected. |  |
| 8         | DESPATCH_FROM | VARCHAR2 | YES | This field is obsolete.  Please use MDD_TASK_CONFIG view for this |  |
| 9         | DESPATCH_TO | VARCHAR2 | YES | This field is obsolete.  Please use MDD_TASK_CONFIG view for this |  |
| 10         | SOURCE_DEST | NUMBER | YES | ID for Internal use only. |  |
| 11         | ITEM_INDEX | NUMBER | YES |  |  |
| 12         | TA_REPORT_ID_FK | NUMBER | YES |  |  |
| 13         | AGENCY_CODE | NUMBER | YES |  |  |
| 14         | AGENCY_NAME | VARCHAR2 | YES |  |  |
| 15         | MEDIA_STATUS_ID | NUMBER | YES | ID for internal use only. |  |
| 16         | MEDIA_STATUS | VARCHAR2 | YES | Indicates the status of the media, eg Ready. |  |
| 17         | DEVICE_PATH | VARCHAR2 | YES |  |  |
| 18         | DEVICE | VARCHAR2 | YES |  |  |

## 106.  MDD_TASK_OUTPUT_MEDIA*

> This view provides information about media associated with a task.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS for full details of associated |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_JOB for full details of associated job. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_MEDIA for full details of associated |  |
| 4         | CONTAINER_ID_FK | VARCHAR2 | YES |  |  |
| 5         | MEDIA_CLASS | VARCHAR2 | YES | Indicates whether the media has been soft deleted or still available. |  |
| 6         | SOURCE | NUMBER | YES | Always set to zero for this view. |  |

## 107.  MDD_TASK_SOURCE_MEDIA*

> This view provides information about media associated with a task.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS for full details of associated |  |
| 2         | JOB_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_JOB for full details of associated job. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_MEDIA for full details of associated |  |
| 4         | CONTAINER_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_CONTAINERS for full details of |  |
| 5         | MEDIA_CLASS | VARCHAR2 | YES | Indicates whether the media is real or virtual at this stage of the |  |
| 6         | SOURCE | NUMBER | YES | Boolean value indicating whether the media is the source media for |  |
| 7         | ARRIVE_BY | DATE | YES | Date media is expected. |  |
| 8         | DESPATCH_FROM | VARCHAR2 | YES | This field is obsolete.  Please use MDD_TASK_CONFIG view for this |  |
| 9         | DESPATCH_TO | VARCHAR2 | YES | This field is obsolete.  Please use MDD_TASK_CONFIG view for this |  |
| 10         | SOURCE_DEST | NUMBER | YES | ID for Internal use only. |  |
| 11         | AGENCY_CODE | NUMBER | YES |  |  |
| 12         | AGENCY_NAME | VARCHAR2 | YES |  |  |
| 13         | MEDIA_STATUS_ID | NUMBER | YES | ID for internal use only. |  |
| 14         | MEDIA_STATUS | VARCHAR2 | YES |  |  |
| 15         | DEVICE_PATH | VARCHAR2 | YES |  |  |
| 16         | DEVICE | VARCHAR2 | YES |  |  |

## 108.  MDD_TASK_TIMELINE

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TASK_TIMELINE_ID | NUMBER | NO | Primary Key.  Unique ID for task timeline entry. |  |
| 2         | TASK_ID_FK | NUMBER | NO | Foreign Key. Links task to MDD_TASKS. |  |
| 3         | JOB_ID_FK | NUMBER | NO | Foreign Key. Links task to MDD_JOB. |  |
| 4         | LOG_ACTION | VARCHAR2 | YES | Description of the action that initiated the logging. |  |
| 5         | NOTES | VARCHAR2 | YES | Log detail. |  |
| 6         | OPERATOR_ID | VARCHAR2 | NO | Name of the operator who initiated the action. |  |
| 7         | TIMESTAMP | DATE | NO | The date and time the action occurred |  |

## 109.  MDD_TASK_VIDEO_MEASUREMENTS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_MEDIA for full details of associated |  |
| 2         | TASK_ID_FK | NUMBER | YES | Foreign Key.  Links to MDD_TASKS for full details of associated |  |
| 3         | VITC | VARCHAR2 | YES | Displays the Virtical Interval TimeCode (VITC) for a piece of media |  |
| 4         | DIGITAL_ERR | VARCHAR2 | YES | Digital error condition of media in the task. |  |
| 5         | LTC | VARCHAR2 | YES | Longitudinal TimeCode (LTC) for a piece of media in the task. |  |
| 6         | DIGITAL_BLANKING | VARCHAR2 | YES | Details of digitial blanking for a piece of media in the task. |  |
| 7         | DIGITAL_CH | VARCHAR2 | YES | Details of digitial channels for a piece of media in the task. |  |
| 8         | PB_PHASE | VARCHAR2 | YES | Details of PB phase for a piece of media in the task. |  |
| 9         | BARS_REF | VARCHAR2 | YES | Bars reference for a piece of media in the task. |  |
| 10         | AUD_REF | VARCHAR2 | YES | Audio reference for a piece of media in the task. |  |

## 110.  MDD_TITLES*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TITLE_ID | NUMBER | NO | Primary Key.  Unique ID of title. |  |
| 2         | TITLE_TYPE | VARCHAR2 | YES |  |  |
| 3         | PARENT_SERIES_ID_FK | NUMBER | YES | Foreign key linking back to TITLE_ID of parent Series. |  |
| 4         | SERIES_TITLE | VARCHAR2 | YES | Series Title. |  |
| 5         | PARENT_SEASON_ID_FK | NUMBER | YES |  |  |
| 6         | SEASON | VARCHAR2 | YES | Season. |  |
| 7         | TITLE | VARCHAR2 | YES | Episode or Standalone Title. |  |
| 8         | ORIGINAL_TITLE | VARCHAR2 | YES |  |  |
| 9         | ITEM_TYPE_ID | NUMBER | NO | Describes the type of Title, eg Series or Episode. |  |
| 10         | EPISODE_NUM | NUMBER | YES | Episode number of title. |  |
| 11         | PRODUCTION_YEAR | NUMBER | YES | Year title was produced. |  |
| 12         | SERIES_TYPE | NUMBER | YES | Internal use only. |  |
| 13         | PROGRAM_ID1 | VARCHAR2 | YES | Client specific primary ID of title. |  |
| 14         | PROGRAM_ID2 | VARCHAR2 | YES | Client specific secondary ID of title. |  |
| 15         | SERIES_ID1 | VARCHAR2 | YES | Client specific primary ID of Series. |  |
| 16         | SERIES_ID2 | VARCHAR2 | YES | Client specific secondary ID of Series. |  |
| 17         | VERSION_ID1 | VARCHAR2 | YES | Client specific primary ID of version. |  |
| 18         | VERSION_ID2 | VARCHAR2 | YES | Client specific secondary ID of version. |  |
| 19         | EXPECTED_DURATION | NUMBER | YES | Expected program duration (in seconds). |  |
| 20         | EXPECTED_ASPECT_RATIO | NUMBER | YES | Expected program aspect ratio. |  |
| 21         | OWNERS | VARCHAR2 | YES | Owner of title. |  |
| 22         | SLOT_DURATION | NUMBER | YES | Slot allocated to title. |  |
| 23         | RUN_TIME_DURATION | NUMBER | YES | Run-time duration of title. |  |
| 24         | COPYRIGHT_STATUS | NUMBER | YES | Title copyright status. |  |
| 25         | COPYRIGHT_STATUS_DESC | NVARCHAR2 | YES | Description of Title copyright status. |  |
| 26         | CULTURAL_STATUS | VARCHAR2 | YES | Internal use only. |  |
| 27         | CULTURAL_STATUS_DESC | VARCHAR2 | YES | Description of Cultural Status of Title. |  |
| 28         | CREATED_BY | VARCHAR2 | NO | Name of user who created the title. |  |
| 29         | CREATED_DATE | DATE | NO | Date the title was created. |  |
| 30         | MODIFIED_BY | VARCHAR2 | YES | Name of user who last modified the title. |  |
| 31         | MODIFIED_DATE | DATE | YES | Date the title was last modified. |  |
| 32         | MEDIUM_ID_FK | NUMBER | YES |  |  |
| 33         | MEDIUM | VARCHAR2 | YES | Medium assigned to title. |  |
| 34         | SUB_MEDIUM_ID_FK | NUMBER | YES |  |  |
| 35         | SUB_MEDIUM | VARCHAR2 | YES | Sub-medium assigned to title. |  |
| 36         | ATTACHMENT_FILENAMES | CLOB | YES | List of Attachment Filenames. |  |
| 37         | URL_REFERENCES | CLOB | YES | List of URL References. |  |
| 38         | DELETED | NUMBER | YES | Date the Title was marked as deleted. |  |
| 39         | DELETED_BY | VARCHAR2 | YES | Identifies the ID of the user that marked the Title as deleted. |  |
| 40         | DELETED_DATE | DATE | YES |  |  |
| 41         | TITLE_PARENTAL_RATING | VARCHAR2 | YES | Parental Rating at the Title level.  This may be different to the |  |
| 42         | TITLE_PARENTAL_SUBRATING | VARCHAR2 | YES | Parental SubRating at the Title level.  This may be different to the |  |

## 111.  MDD_TITLE_GENRE*

> Provides information about the genre of a title.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | TITLE_ID_FK | NUMBER | NO | Foreign_Key.  Links genre to MDD_TITLES. |  |
| 2         | GENRE_ID | NUMBER | YES | Primary Key.  Unique ID of genre. |  |
| 3         | GENRE | VARCHAR2 | YES | Genre description. |  |

## 112.  MDD_TRANSMISSION_SCHEDULE

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | SCHEDULE_ID | NUMBER | NO | Primary Key.  Unique ID of transmision schedule. |  |
| 2         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links transmission schedule to MDD_VERSIONS. |  |
| 3         | MEDIA_ID_FK | NUMBER | YES | Foreign Key.  Links transmission schedule to MDD_MEDIA. |  |
| 4         | NETWORK | VARCHAR2 | YES | Transmission network. |  |
| 5         | TRANSMISSION_DATE | DATE | YES | Transmission date for specific media. |  |
| 6         | TRANSMISSION_START | DATE | YES | Scheduled start of transmission for specific media. |  |
| 7         | TRANSMISSION_END | DATE | YES | Scheduled end of transmission for specific media. |  |
| 8         | TRANSMISSION_SERIES_TITLE | VARCHAR2 | YES | Series or one-off title. |  |
| 9         | TRANSMISSION_TITLE | VARCHAR2 | YES | Episode title |  |
| 10         | PRODUCT_NUMBER | VARCHAR2 | YES | Product number for media on schedule. |  |
| 11         | DURATION_SECONDS | NUMBER | YES | Duration of scheduled transmission (in seconds) |  |
| 12         | QC_STATUS | VARCHAR2 | YES | QC status of scheduled media. |  |

## 113.  MDD_USERS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | USER_ID | VARCHAR2 | YES | Mediaflex user |  |
| 2         | FULL_NAME | VARCHAR2 | YES | Full name of Mediaflex user |  |
| 3         | TITLE | VARCHAR2 | YES | Title of Mediaflex user |  |
| 4         | PHONE | VARCHAR2 | YES | Phone number of Mediaflex user |  |
| 5         | EMAIL | VARCHAR2 | YES |  |  |
| 6         | EXPIRYDATE | DATE | YES | Expiry Date |  |
| 7         | DEPARTMENT | VARCHAR2 | YES | Department of Mediaflex user |  |
| 8         | AREA_SHORT_CODE | VARCHAR2 | YES |  |  |
| 9         | AREA | VARCHAR2 | YES |  |  |
| 10         | DBA_MODE | VARCHAR2 | YES | Indicates whether the user has TMDDBA rights |  |
| 11         | IS_DISABLED | VARCHAR2 | YES |  |  |
| 12         | LAST_MFX_LOGIN_DATE | DATE | YES |  |  |
| 13         | LAST_IMFX_LOGIN_DATE | DATE | YES |  |  |

## 114.  MDD_USER_ACCESS_GROUPS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | USER_ID | VARCHAR2 | YES | Mediaflex User. |  |
| 2         | USER_NAME | VARCHAR2 | YES | Mediaflex User full name. |  |
| 3         | STATUS | VARCHAR2 | YES | Mediaflex User account status. |  |
| 4         | ACCESS_GROUP | VARCHAR2 | YES | Access Groups assigned to user. |  |
| 5         | CREATED | DATE | YES | User account Creation date. |  |
| 6         | IS_IMFX | VARCHAR2 | YES | Indicate with "Y" when item is iMediaflex Access group. |  |

## 115.  MDD_USER_SCHEDULE_RIGHTS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | USER_ID | VARCHAR2 | YES | Mediaflex User |  |
| 2         | SCHEDULE_RIGHTS_ID | VARCHAR2 | YES | ID for internal use only |  |
| 3         | SCHEDULE_RIGHTS | VARCHAR2 | YES | Schedule Rights assigned to user |  |

## 116.  MDD_VERSIONS*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID | NUMBER | NO | Primary Key.  Unique ID of version. |  |
| 2         | ITEM_TYPE_ID | NUMBER | NO | Foreign Key.  Links version to MDD_MEDIA_ITEM_TYPES. |  |
| 3         | TITLE_ID_FK | NUMBER | NO | Foreign Key.  Links version to MDD_TITLES. |  |
| 4         | PARENT_VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links a sub version to its parent in MDD_VERSIONS. |  |
| 5         | MASTER_VERSION_ID_FK | NUMBER | YES |  |  |
| 6         | VERSION_TYPE | CHAR | YES | The Version Type will be SM for Supplier Masters. |  |
| 7         | VERSION_TITLE | VARCHAR2 | YES | Episode title for version. |  |
| 8         | VERSION_SERIES_TITLE | VARCHAR2 | YES | Series or one-off title for version. |  |
| 9         | VERSION_SERIES_NAME | VARCHAR2 | YES | The Series or Season Name for the Version. |  |
| 10         | VERSION_EPISODE | VARCHAR2 | YES | The Episode number for the Version. |  |
| 11         | EPISODE_NUM | NUMBER | YES |  |  |
| 12         | VERSION_ID1 | VARCHAR2 | YES | Client specific primary identifier for version. |  |
| 13         | VERSION_ID2 | VARCHAR2 | YES | Client specific secondary identifier for version. |  |
| 14         | VERSION_PROGRAM_ID1 | VARCHAR2 | YES | Client specific primary identifier for program. |  |
| 15         | VERSION_PROGRAM_ID2 | VARCHAR2 | YES | Client specific secondary identifier for program. |  |
| 16         | HOUSE_NUMBER | VARCHAR2 | YES | Client Version reference number. |  |
| 17         | VERSION_NAME | VARCHAR2 | YES | Name of version. |  |
| 18         | EXPECTED_DURATION | NUMBER | NO | Expected duration of version (in seconds). |  |
| 19         | SLOT_DURATION | NUMBER | YES | Slot duration allocated to version (in seconds). |  |
| 20         | OWNERS | VARCHAR2 | YES | Owner(s) of version. |  |
| 21         | STATUS_ID | NUMBER | YES | ID for internal use only. |  |
| 22         | STATUS | NVARCHAR2 | YES | Status of version, eg Restricted. |  |
| 23         | EXPECTED_FORMAT | NUMBER | YES | Expected format of version. |  |
| 24         | ASPECT_RATIO | NUMBER | YES | Aspect ratio code.  For internal use only. |  |
| 25         | ASPECT_RATIO_NAME | VARCHAR2 | YES | Aspect ratio of version. |  |
| 26         | TV_STD | NVARCHAR2 | YES | TV Standard of version. |  |
| 27         | NEXT_TX_DATE | DATE | YES | Next scheduled transmission date for version. |  |
| 28         | ITV_CAT | VARCHAR2 | YES |  |  |
| 29         | ITV_TYPE | NUMBER | YES |  |  |
| 30         | REF_CODE | VARCHAR2 | YES |  |  |
| 31         | SUB_MEDIUM | VARCHAR2 | YES | Sub-Medium of version. |  |
| 32         | CREATED_BY | VARCHAR2 | NO |  |  |
| 33         | CREATED_DT | DATE | NO | Date version was created. |  |
| 34         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 35         | MODIFIED_DT | DATE | YES | Date version was last modified. |  |
| 36         | COPYRIGHT_STATUS | NUMBER | YES | Version copyright status. |  |
| 37         | COPYRIGHT_STATUS_DESC | NVARCHAR2 | YES | Description of Copyright Status of Version. |  |
| 38         | CULTURAL_STATUS_ID | VARCHAR2 | YES | Version cultural status ID. |  |
| 39         | CULTURAL_STATUS_DESC | VARCHAR2 | YES | Description of Cultual Status of Version. |  |
| 40         | ALTERNATIVE_TITLES | VARCHAR2 | YES | Alternative Titles. |  |
| 41         | ATTACHMENT_FILENAMES | CLOB | YES | List of Attachment Filenames. |  |
| 42         | URL_REFERENCES | CLOB | YES | List of URL References. |  |
| 43         | PRODUCTION_PLACE_TYPE | VARCHAR2 | YES | The Production Place type of Version. |  |
| 44         | PRODUCTION_PLACE | VARCHAR2 | YES | The Production Place of Version. |  |
| 45         | PRODUCTION_COLOUR_ID | NUMBER | YES |  |  |
| 46         | PRODUCTION_COLOUR | NVARCHAR2 | YES | The Production Colour of the Version. |  |
| 47         | PRODUCTION_AUDIO_ID | NUMBER | YES |  |  |
| 48         | PRODUCTION_AUDIO | NVARCHAR2 | YES | The Production Audio of the Version. |  |
| 49         | NOTES | VARCHAR2 | YES | Displays Notes saved against Version. |  |
| 50         | DELETED | NUMBER | YES | Boolean value indicating whether a Version has been marked as |  |
| 51         | DELETED_BY | VARCHAR2 | YES | Identifies the ID of the user that marked the Version as deleted. |  |
| 52         | DELETED_DATE | DATE | YES | Date the Version was marked as deleted. |  |
| 53         | PARENTAL_RATING | VARCHAR2 | YES | Parental rating of item. |  |
| 54         | PARENTAL_SUBRATING | VARCHAR2 | YES | Parental Advisory rule. |  |
| 55         | VERSION_GUID | VARCHAR2 | YES | Unique identifier for Version |  |

## 117.  MDD_VERSION_COUNTRY*

> Provides details of country(ies) assigned to a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links country to MDD_VERSIONS. |  |
| 2         | COUNTRY | VARCHAR2 | YES | Country(ies) associate with a version. |  |

## 118.  MDD_VERSION_LANGUAGE*

> Provides details of language(s) assigned to a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links language(s) to MDD_VERSIONS. |  |
| 2         | LANGUAGE | VARCHAR2 | YES | Language(s) associated with a particular version. |  |
| 3         | ROLE | VARCHAR2 | YES | Language(s) Role associated with a particular version. |  |

## 119.  MDD_VERSION_MATRIX_NUMBER*

> Provides details of Matrix number data linked to a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | MAT_NUM_ID | NUMBER | NO | Primary Key.  Unique ID of Matrix Number |  |
| 2         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links Production to MDD_VERSIONS. |  |
| 3         | MATRIX_PREFIX | VARCHAR2 | YES | Matrix Prefix. |  |
| 4         | MATRIX_NUMBER | VARCHAR2 | YES | Matrix number. |  |
| 5         | MATRIX_SUFFIX | VARCHAR2 | YES | Matrix suffix. |  |
| 6         | CREATED_BY | VARCHAR2 | NO | Name of user who created the information. |  |
| 7         | CREATED_DATE | DATE | NO | Date the information was entered. |  |
| 8         | MODIFIED_BY | VARCHAR2 | YES | Name of user who last modified the information. |  |
| 9         | MODIFIED_DATE | DATE | YES | Date the information was last modified. |  |

## 120.  MDD_VERSION_PLACE

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | NO | Primary Key.  Unique ID of version. |  |
| 2         | VERSION_ID1_FK | VARCHAR2 | YES | Client specific primary identifier for version. |  |
| 3         | PLACE | VARCHAR2 | YES | The Production Place of Version. |  |
| 4         | PLACE_TYPE | VARCHAR2 | YES | The Production Place type of Version. |  |

## 121.  MDD_VERSION_PRODUCTION_DATES*

> Provides details of production dates linked to a version.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | PROD_DATE_ID | NUMBER | NO | Primary Key.  Unique ID of production date. |  |
| 2         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links production date to MDD_VERSIONS. |  |
| 3         | DATE_TYPE_ID | NUMBER | YES | ID for internal use only. |  |
| 4         | DATE_TYPE | VARCHAR2 | YES | Type of Production Date. |  |
| 5         | DATE_FROM | DATE | YES | Date production from. |  |
| 6         | DATE_TO | DATE | YES | Date production to. |  |
| 7         | FROM_DAY | NUMBER | YES | Day production from. |  |
| 8         | FROM_MONTH | NUMBER | YES | Month production from. |  |
| 9         | FROM_YEAR | NUMBER | YES | Year production from. |  |
| 10         | TO_DAY | NUMBER | YES | Day production to. |  |
| 11         | TO_MONTH | NUMBER | YES | Month production to. |  |
| 12         | TO_YEAR | NUMBER | YES | Year production to. |  |
| 13         | CIRCA | NUMBER | YES | Production date circa. |  |
| 14         | NOTES | VARCHAR2 | YES | Notes related to production date. |  |
| 15         | CREATED_BY | NVARCHAR2 | NO | Name of user who created the information. |  |
| 16         | CREATED_DATE | DATE | NO | Date the information was entered. |  |
| 17         | MODIFIED_BY | NVARCHAR2 | YES | Name of user who last modified the information. |  |
| 18         | MODIFIED_DATE | DATE | YES | Date the information was last modified. |  |

## 122.  MDD_VERSION_RELATED*

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | NO | Foreign Key.  Links to MDD_VERSIONS |  |
| 2         | RELATED_VERSION_ID_FK | NUMBER | NO | Related versions ID Foreign Key |  |
| 3         | RELATED_VERSION_ID1 | VARCHAR2 | YES | Related versions ID1 |  |
| 4         | RELATED_VERSION_TITLE | VARCHAR2 | YES | Related versions Title |  |
| 5         | RELATED_VERSION_NAME | VARCHAR2 | YES | Related versions Name |  |

## 123.  MDD_VERSION_RIGHTS*

> Provides details of Rights Agreements

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | RIGHTS_ID | NUMBER | NO | Primary Key.  Unique ID of Rights Agreement. |  |
| 2         | RIGHTS_HOLDER | NUMBER | YES | Rights Holder. |  |
| 3         | CONTACT | VARCHAR2 | YES | Rights Contact. |  |
| 4         | AGREEMENT_DATE | DATE | YES | Agreement Date. |  |
| 5         | FILE_REF | VARCHAR2 | YES | File Reference. |  |
| 6         | CREATED | DATE | YES | Date when the information got created. |  |
| 7         | CREATED_BY | VARCHAR2 | YES | Name of user who created the information. |  |
| 8         | VERSION_ID | NUMBER | YES | Version ID. |  |
| 9         | PERMISSION_TYPE | NUMBER | YES | Type of Permission. |  |
| 10         | PERM_TYPE_DESC | VARCHAR2 | YES | Permission type Description |  |
| 11         | START_DATE | DATE | YES | Start Date. |  |
| 12         | END_DATE | DATE | YES | End Date. |  |
| 13         | GEOGRAPHICAL_COVERAGE | NUMBER | YES | Geographical Coverage. |  |
| 14         | GEO_COVERAGE_DESC | VARCHAR2 | YES | Geographic Coverage Description |  |
| 15         | PROJECT_CODE | VARCHAR2 | YES | Project Code |  |
| 16         | PROJECT_CODE_DESC | VARCHAR2 | YES | Project Code Description |  |

## 124.  MDD_VERSION_SEGMENTS

> No summary available

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | VERSION_ID_FK | NUMBER | YES | Foreign Key.  Links to unique ID of version in MDD_VERSIONS. |  |
| 2         | SEGMENT_NO | NUMBER | YES | Segment number. |  |
| 3         | PART_NO | NUMBER | YES | Part number of the segment. |  |
| 4         | SEGMENT_TYPE | NUMBER | YES | Internal use ID. |  |
| 5         | SEGMENT_TYPE_DESC | NVARCHAR2 | YES | Description of segment type.  (This will only be available if config |  |
| 6         | SEGMENT_TITLE | VARCHAR2 | YES | Title assigned to segment. |  |
| 7         | SOM_FRAMES | NUMBER | YES | Start of Media in frames.. |  |
| 8         | SOM | VARCHAR2 | YES | Start of Media displayed as a timecode.. |  |
| 9         | EOM_FRAMES | NUMBER | YES | End of Media in frames.. |  |
| 10         | EOM | VARCHAR2 | YES | End of Media displayed as a timecode.. |  |
| 11         | DURATION_FRAMES | NUMBER | YES | Duration of a segment in frames.. |  |
| 12         | DUR | VARCHAR2 | YES | Foreign Key.  Duration of segment displayed as a timecode.. |  |
| 13         | USE_IN_DUR_CALC | NUMBER | YES | Indicates if segment should be used to calculate duration. |  |
| 14         | TX_PART | NUMBER | YES | Indicates if this segment is valid for transmission. |  |

## 125.  MDD_XML_METADATA*

> Provides all XML data held in the system.

| Field No. | Field Name            | Data Type | Nullable | Description | Sample Data |
|-----------|-----------------------|-----------|----------|-------------|-------------|
| 1         | XML_ID | NUMBER | NO | Primary Key.  Unique ID of metadata. |  |
| 2         | LINKING_ID_FK | NUMBER | YES | Foreign Key.  Can be used to link to other views for more info. |  |
| 3         | XML_LINK_TYPE | VARCHAR2 | YES | Indicates the type of data that the XML is linked to, eg VERSION, |  |
| 4         | SCHEMA_TYPE | NUMBER | YES | ID for internal use only. |  |
| 5         | XML_TYPE | VARCHAR2 | YES | Description of the XML Schema Type |  |
| 6         | SCHEMA_NAME | VARCHAR2 | YES | Name of the Schema |  |
| 7         | DATA_TYPE | NUMBER | YES | ID for internal use only. |  |
| 8         | CREATED_BY | VARCHAR2 | YES |  |  |
| 9         | CREATED_DATE | DATE | YES |  |  |
| 10         | MODIFIED_BY | VARCHAR2 | YES |  |  |
| 11         | MODIFIED_DATE | DATE | YES |  |  |
| 12         | XML_DATA | XMLTYPE | YES | XML data. |  |
| 13         | OWN_ID | NUMBER | YES | OBSOLETE - This has been replaced by the LINKING_ID_FK field. |  |
| 14         | MEDIA_ID_FK | NUMBER | YES | OBSOLETE - This has been replaced by the LINKING_ID_FK field. |  |
| 15         | VERSION_ID_FK | NUMBER | YES | OBSOLETE - This has been replaced by the LINKING_ID_FK field. |  |
