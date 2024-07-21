MDD_ACCESS_STATUS

> The accessibility to the Public of a Media Item

MDD_ACQUISITIONS

> Provides overall information about an acqusition.

MDD_ACQUISITIONS

> NUMBER Y STOCK_CHECK_ID Foreign Key.  Linking Carrier to a particular stock check list NUMBER Y STOCK_CHECK_STATE_ID ID of stock check state.  Can be used for efficient querying and or sorting NUMBER Y STOCK_CHECK_STATE Description of stock check state VARCHAR2 Y STOCK_CHECK_BY Name of user who performed stock check VARCHAR2 Y STOCK_CHECK_DATE Date of most recent stock check DATE Y CONTAINER_LENGTH Length of Carrier (derived from xml metadata) NUMBER Y LOGIN_DATE The date the Carrier was logged into Mediaflex DATE Y LAST_OUT_NAME_ID_FK Foreign Key. Linking to MDD_NAMES NUMBER Y

MDD_ACQ_CATEGORY

> List of TV standards available in the system.

MDD_ACQ_CONTAINERS

> Provides information about the containers in an acqusition.

MDD_ACQ_CONTAINERS.ACQ_CONTAINER_ID to link Acquisition

> Objects and Containers. NUMBER Y OBJECT_DESCRIPTION Description of the Object VARCHAR2 Y PARENT_ID Provides link to acquisition container.  (Superceded by acq_container_id_fk) NUMBER Y OBJECT_TYPE Identifies the Type of the Object NUMBER N MEDIA_ID2_FK Foreign Key.  Links to MDD_MEDIA.MEDIA_ID2 to link Acquisitions and Media VARCHAR2 Y Page 4 of 80 OBJECT_BARCODE Barcode of acquisition object VARCHAR2 Y ACQ_EXTERNAL_REF1 Third party reference for object VARCHAR2 Y MEDIUM Description of object’s medium, eg: Audio, Documentation, Artefact etc. VARCHAR2 Y SUB_MEDIUM Description of object’s sub-medium, eg: Film, Sound Recording etc. VARCHAR2 Y FORM Describes the object’s form, eg: Actuality, Advertisement etc. VARCHAR2 Y OBJECT_FORMAT Physical format of the object, eg: Tape, Disc, Paper etc. VARCHAR2 Y CONTAINER_STATUS_ID ID of the Status of the Container the Object is in NUMBER Y CONTAINER_STATUS_DESC Status of the Container the Object is in VARCHAR2 Y ACCESSION_STATUS Accession Status of Object VARCHAR2 Y QTY_RECEIVED Total number of objects received NUMBER Y QTY_NOT_SELECTED Total number of objects not selected NUMBER Y QTY_REMAINING Total number of objects remaining NUMBER Y QTY_SELECTED Total number of objects selected NUMBER Y QTY_ACCESSIONED Total number of objects accessioned NUMBER Y QTY_AWAITING_ACCESSIONING Total number of objects awaiting accessioning NUMBER Y DATE_EXPECTED Date that the Acquisition Object is expected to be received DATE Y DATE_RECEIVED Date that the Acquisition Object was received DATE Y ARTICLE_LAST_MOVED The date the Article was last moved DATE Y OBJECT_NOTES Notes associated with the Object CLOB Y JOB_ID_FK Foreign Key.  Links to the Job that an Acquisition Object is linked to NUMBER Y TASK_ID_FK Foreign Key.  Links to MDD_TASKS NUMBER Y ARTICLE_BARCODE Barcode of Physical Article VARCHAR2 Y ARTICLE_FILENAME Filename of Digital Article VARCHAR2 Y DISPOSAL_CLASS_NO Disposal Class Number of Article NUMBER Y ARTICLE_EXT_REF1 External Reference 1 number for Article VARCHAR2 Y ARTICLE_EXT_REF2 External Reference 1 number for Article VARCHAR2 Y CREATED_DATE Date Article created DATE Y

MDD_ACQ_OBJECTS

> Provides information about the objects in an acqusition.

MDD_ACQ_TYPES

> Provides information about types of acqusitions.

MDD_ACTION_HISTORY

> No summary available.

MDD_ALT_NAMES

> Provides information about the alternative names linked to a name authority.

MDD_ASPECT_RATIO

> Links a legacy aspect ratio value to its afd details.

MDD_AUDIO_FROM_MIS

> Provides information about the audio stored directly against a media item.

MDD_AUTOPURGE_HISTORY

> This view provides information about all active general fileserver and storage device types and autopurge rules associated with each device.

MDD_BOX_CONTAINER_TYPES

> Provides information about a box container type

MDD_BOX_CONTAINER_TYPES

> NUMBER N FORMAT_NAME VARCHAR2 Y FORMAT_SHORTCODE Name of Container Format. VARCHAR2 Y HEIGHT Container height NUMBER Y WIDTH Container width NUMBER Y DEPTH Container depth NUMBER Y WEIGHT Container depth NUMBER Y SHM Container shelf metres in mm NUMBER Y

MDD_CHANNEL_GROUPS

> Lists channels and how they are grouped.

MDD_CODES_ASPECT_RATIO

> Provides details of Aspect Ratios stored in the database.

MDD_CODES_CHANNELS

> No summary available.

MDD_CODES_CULTURAL_STATUS

> List of Cultural Statuses available for use in the system.

MDD_CODES_DEVICES

> No summary available.

MDD_CODES_TASK_TYPES

> This view provides information about a specific task.

MDD_CODES_TEC_DETAILS

> List of tech codes available in the system.

MDD_CODES_TEC_TYPE

> Provides details of tech types and whether they are a condition or a treatment.

MDD_CODES_TVSTD

> No summary available.

MDD_CONTAINERS

> Provides details of carriers.

MDD_CONTAINER_CONDITION_TREAT

> Provides details of conditions and treatments assigned to carriers.

MDD_CONTAINER_FORMATS

> List the carrier formats available in the system.

MDD_CONTAINER_FORMATS

> NUMBER Y FORMAT Description of Carrier format VARCHAR2 Y LOCATION_FULL Full desciption of location of Carrier VARCHAR2 Y LOCATION_CODE_FULL Location of Carrier VARCHAR2 Y LAST_LIB_LOC Last library location of Carrier VARCHAR2 Y SUGGESTED_LOC_NAME Name of the suggested location of Carrier VARCHAR2 Y OUT_TO VARCHAR2 Y STATUS Value used to determine Carrier status NUMBER Y CONTAINER_STATUS Status of Carrier VARCHAR2 Y FLAG_MASTER Boolean value indicating whether the Carrier is the master NUMBER Y FLAG_SUPPLD Boolean value indicating whether the Carrier was supplied or made NUMBER Y FLAG_JOBCR Boolean value indicating whether the Carrier was created by a job NUMBER Y FLAG_WIPE Boolean value indicating whether the Carrier is to be wiped NUMBER Y FLAG_WIPED Boolean value indicating whether the Carrier has been wiped NUMBER Y FLAG_DEST Boolean value indicating whether the Carrier is to be destroyed NUMBER Y FLAG_DESTYD Boolean value indicating whether the Carrier has been destroyed NUMBER Y FLAG_ONLOAN Boolean value indicating whether the Carrier is on loan NUMBER Y FLAG_RETRNED Boolean value indicating whether the Carrier has been returned NUMBER Y FLAG_MATCHD Boolean value indicating whether the Carrier has been matched NUMBER Y FLAG_UNMATCHD Boolean value indicating whether the Carrier is unmatched NUMBER Y FLAG_IN Boolean value indicating whether the Carrier is in the facility NUMBER Y FLAG_OUT Boolean value indicating whether the Carrier is outside of the facility NUMBER Y FLAG_XOVER Boolean value indicating whether the Carrier has been written over NUMBER Y FLAG_BLANK Boolean value indicating whether the Carrier is blank NUMBER Y FLAG_OUT_INT Boolean value indicating whether the Carrier is on loan internally NUMBER Y FLAG_DAMAGED Boolean value indicating whether the Carrier is damaged NUMBER Y FLAG_ITEM_LIVE Boolean value indicating whether the Carrier is live NUMBER Y FLAG_ATTACH Boolean value indicating whether the Carrier is attached NUMBER Y Page 14 of 80 FLAG_TX_OK Boolean value indicating whether the Carrier is suitable for transmission NUMBER Y FLAG_MODIF Boolean value indicating whether the Carrier has been modified NUMBER Y FLAG_CONTENT_MODIF Boolean value indicating whether the content of the Carrier has been modified NUMBER Y FLAG_TIMELINE_MODIF Boolean value indicating whether the timeline of the Carrier has been modified NUMBER Y FLAG_SH_NEW_CREATE Boolean value indicating whether the Carrier sh new create NUMBER Y FLAG_BLANK_CLI Boolean value indicating whether the Carrier has no owner NUMBER Y FLAG_BLANK_PRE_TTLD Boolean value indicating whether the Carrier is pre-titled blank stock NUMBER Y FLAG_BLANK_ASSND Boolean value indicating whether the Carrier has a blank assnd NUMBER Y FLAG_IMPORT_DATA Boolean value indicating whether the Carrier was imported NUMBER Y FLAG_NEW_ARRV Boolean value indicating whether the Carrier is a new arrival NUMBER Y FLAG_DEL Boolean value indicating whether the Carrier has been deleted NUMBER Y FLAG_ACCEPT Boolean value indicating whether the Carrier has been accepted NUMBER Y FLAG_REJECT Boolean value indicating whether the Carrier has been rejected NUMBER Y FLAG_ITEM_PART Boolean value indicating whether the Carrier is part of an item NUMBER Y FLAG_MISSING Boolean value indicating whether the Carrier is missing NUMBER Y FLAG_FTP_FILE NUMBER Y FLAG_HDR_TC_TRACK_MISSMATCH NUMBER Y FLAG_INVALID_TIMECODE_TRACK NUMBER Y FLAG_UNATTACHED NUMBER Y FLAG_EXTERNALISED NUMBER Y CREATED_BY_LOCATION_ID ID of the location of the user who created the Carrier NUMBER Y CREATED_BY_LOCATION Location of the user who created the Carrier VARCHAR2 Y CREATED_BY_PARENT_LOCATION_I D ID of the parent location of the user who created the Carrier NUMBER Y USER_AREA_ID ID of the area that the user who created the Carrier is in NUMBER Y CREATED_DATE Date the Carrier was created DATE N CREATED_BY Name of the user who created the Carrier VARCHAR2 N MODIFIED_DATE Date the Carrier was last modified DATE Y MODIFIED_BY Name of the user who last modified the Carrier VARCHAR2 Y ATTACHMENT_FILENAMES List of Attachment Filenames. CLOB Y URL_REFERENCES List of URL References. CLOB Y ORIGIN ID of origin of Carrier NUMBER Y TAPE_NUMBER Number of Carrier if media crosses more than one NUMBER Y Page 15 of 80 TOTAL_TAPES Total number of Carriers if media crosses more than one NUMBER Y TAPE_SIZE Size of Carrier NUMBER Y GROUP_NUMBER Foreign Key. Linking Carrier to a group NUMBER Y NOTES Notes associated with a Carrier VARCHAR2 Y ACQ_ID Foreign Key.  Linking Carrier to an acquisition in

MDD_CONTAINER_FORMATS

> NUMBER N FORMAT_NAME VARCHAR2 N FORMAT_SHORTCODE Name of Carrier Format VARCHAR2 Y HEIGHT Carrier height NUMBER Y WIDTH Carrier width NUMBER Y DEPTH Carrier depth NUMBER Y WEIGHT Carrier depth NUMBER Y SHM Carrier shelf metres in mm NUMBER Y

MDD_CONTENT

> Provides information content of a version.

MDD_CONTENT_PURE

> Further information is required re MDD_CONTENT_PURE.

MDD_CREDITS

> Provides information about the credits associated with a version.

MDD_CRS_SERIES_AGENCY

> NUMBER Y RESERVATION_ID_FK Foreign key.  Reservation ID of the Acquisition.  Links to RESERVATION_ID in MDD_SPACE_RESERVATION_ITEMS NUMBER Y ACQ_USER_STATUS User set status for the Acquisition VARCHAR2 Y ACQ_COST Acquisition Cost in $ VARCHAR2 Y

MDD_CRS_SERIES_AGENCY

> Provides information about the credits associated with a version.

MDD_DCTC_BBS_DELIVERY_CUSTOM

> No summary available.

MDD_DCTC_BBS_MRSS_CUSTOM

> No summary available.

MDD_DCTC_BBS_TITLE_CUSTOM

> No summary available.

MDD_DCTC_JOB_CUSTOM

> Provides a view of custom metadata for a job.

MDD_DCTC_MEDEXTENDED_CUSTOM

> No summary available.

MDD_DCTC_MEDVERSION_CUSTOM

> Provides custom metadata linked to a Digital Media Version

MDD_DCTC_NLS_RUNDOWN_MEDIA

> List of promo and commercial Rundown Media Items.

MDD_DCTC_NLS_VUBIQUITY_PLANNER

> No summary available.

MDD_DCTC_PACKAGE_CUSTOM

> No summary available.

MDD_DCTC_SERIES_CUSTOM

> Provides custom metadata linked to a Title.

MDD_DIGITAL_FILES

> Provides information about Digital Carriers (Files).

MDD_DIGITAL_FILE_LINKS

> No summary available.

MDD_DISPOSAL_RECORDS

> Disposal Records for assessioned carriers

MDD_ENTITY_NATIONALITIES

> Links Entities to their associated nationality(ies)

MDD_GROUPS

> Provides a list of groups that are used to link media

MDD_GROUP_MEDIA

> Links media for certain lists used in the system, eg: Stock Check lists

MDD_HISTORY

> Provides details of History associated with media or a task

MDD_HISTORY_EQUIPMENT

> Links history to associated equipment used

MDD_IBMS_VERSIONS

> No summary available.

MDD_JOB

> Provides details of Jobs created

MDD_JOB_MEDIA

> No summary available.

MDD_JOB_MEDIA

> No summary available.

MDD_JOB_SCHEDULE

> No summary available.

MDD_JOB_SCHEDULE

> No summary available.

MDD_LANG_DATA

> Provides details of Languages available in the system

MDD_LOAN_HEADER

> Provides summary header details for a Loan

MDD_LOAN_HEADER

> NUMBER N MEDIA_ID_FK Foreign Key.  Linking to media item in MDD_MEDIA NUMBER Y CONTAINER_ID_FK NUMBER Y MEDIA_ID1 Media ID1 of Media on Loan VARCHAR2 Y VERSION_ID_FK Foreign Key.  Linking to versions in MDD_VERSIONS NUMBER N BARCODE Barcode of Carrier (if loan is linked to a Carrier) VARCHAR2 Y SERIES_TITLE Title of item VARCHAR2 Y EPISODE_TITLE Episode Title of item VARCHAR2 Y NEXT_TX_DATE Next tranmission date of item DATE N REQUIRED_DATE Date item is required DATE Y RETURN_DATE Date item is due to be returned DATE Y DATE_LOANED Date item was actually loaned DATE Y DATE_RETURNED Date item was actually returned DATE Y STATUS Status of item in Loan VARCHAR2 Y ITEM_TYPE Type of item on Loan, eg: Media or Tape VARCHAR2 Y

MDD_LOAN_ITEMS

> Provides details about individual items within a loan.

MDD_LOCATIONS

> Provides details of Library/Vault Locations.

MDD_LOCATION_USE

> No summary available.

MDD_MEDIA

> No summary available.

MDD_MEDIA

> View to be removed:

MDD_MEDIA

> Provides information about Media items (excluding virtual media items).

MDD_MEDIA_AUDIO

> This view uses new audio tables to provide details of media audio.  This will eventually replace MDD_MEDIA_AUDIO.

MDD_MEDIA_AUDIO_EXTRAS

> No summary available.

MDD_MEDIA_AUDIO_NS

> This view uses new audio tables to provide details of media audio.  This will eventually replace MDD_MEDIA_AUDIO.

MDD_MEDIA_CHANNELS

> View used to link Media to Channels

MDD_MEDIA_CONTNRS_LNK

> View used to link Media and Carriers

MDD_MEDIA_COPY_HISTORY

> View used to link Media Items to any copies created

MDD_MEDIA_CUSTOM_STATUS

> No summary available.

MDD_MEDIA_DISCOVERY

> The following views are being retired and should not be used if they already exist on the database: NOTE: � TransMedia Dynamics Ltd, 2012. All rights reserved. Except as provided below, no part of this document may be reproduced in any material form (including photocopying or storing it in any medium by electronic means) without the prior written permission of TransMedia Dynamics Ltd. except in accordance with the provisions of the (UK) Copyright, Designs and Patents Act 1988. TransMedia Dynamics grants permission to its customers that have entered into a Mediaflex Software Licence Agreement, to make copies of the Data Dictionary as a complete document (including the copyright notice) for their own internal use only. No copies may be published, distributed or made available to third parties whether by paper, electronic or other means without TransMedia Dynamics Ltd. prior written permission. AGREEMENT The Mediaflex data dictionary has been designed to provide Mediaflex clients with a means to extract metadata from the Mediaflex database without the need for additional development. It�s primarily targeted for use by 3rd party reporting tools such as Crystal Reports and Microsoft Excel. Access to the Mediaflex Oracle database is restricted to a series of read only views that not only protect TMD�s Intellectual Property Rights (IPR) but also simplify the complex data structures which Mediaflex is built on. TMD have assumed that anyone using the Data Dictionary has a good understanding of SQL and has access to 3rd party software such as Crystal Reports or Microsoft Excel. This document will be under the sole control of TMD. If you have any suggestions for additions or modifications then please contact: Jo Frost Jo.Frost@tmd.tv or Carlton Smith Carlton.smith@tmd.tv All suggestions should be made in electronic form. INTRODUCTION Page 2 of 80 VIEW DEFINITIONS

MDD_MEDIA_FAULTS

> Provides details of faults for a particular Media item.

MDD_MEDIA_FAULTS view.

> No summary available.

MDD_MEDIA_FAULTS_NS

> Provides details of faults for a particular Media item using the new faults tables.  This will eventually replace the

MDD_MEDIA_FORMATS

> No summary available.

MDD_MEDIA_FORMATS

> No summary available.

MDD_MEDIA_FORMAT_TECH_CODES

> Provides information about all versions stored in the system.

MDD_MEDIA_ITEM_TYPES

> Provides full details of item types for media

MDD_MEDIA_LOCATORS

> This view displays locator metadata for media item

MDD_MEDIA_METADATA

> Provides metadata information about Media items (excluding virtual media items).

MDD_MEDIA_RIGHTS

> Provides details of Rights Agreements

MDD_MEDIA_SEGMENTS

> Provides a view on segment data held at media item level. The durations are displayed as timecode and also as a frame count.

MDD_MEDIA_SIMPLE

> Provides information about Media items (excluding virtual media items).

MDD_MEDIA_USAGE_TYPES

> Provides full details of active media usages.

MDD_MEDIA_VALUATION_MEDIA

> No summary available.

MDD_MEDIA_WITH_VIRTUAL

> Provides information about Media items (including virtual media items).

MDD_MIS_AUDIO

> For internal use only.  Media Audio should be accessed via MDD_MEDIA_AUDIO.

MDD_MOVEMENTS

> Provides details of Carrier or Container Movements.

MDD_NAA_CARRIER_SHM

> Dimentions of NAA Carrier Formats including Shelf Metres.

MDD_NAA_CONTAINER_SHM

> Dimentions of NAA Container Formats including Shelf Metres.

MDD_NAMES

> No summary available.

MDD_NFSA_MEDIA_USAGE_GROUPS

> No summary available.

MDD_PACKAGES

> Provides summary information about individual Packages

MDD_PACKAGES view

> NUMBER N RUNDOWN_ID ID of Rundown. NUMBER N RUNDOWN_MEDIA_ID ID of Rundown Media.  Links to Mediaflex MEDIA_ID2 for promos and commercials VARCHAR2 Y RUNDOWN_ITEM_TYPE Item type of Rundown media VARCHAR2 Y SELECTED_MFX_MEDIA_ID_FK ID of Mediaflex Media that has been selected for the Rundown item. Can be used to link to the MDD_MEDIA view for full details of selected media NUMBER Y Page 22 of 80 MATCHED_MFX_MEDIA_ID ID of Media found to be a match in Mediaflex, ie has MEDIA ID2 that matches the Rundown Media ID NUMBER Y MATCHED_MEDIA_ID2 ID2 of matching Mediaflex media VARCHAR2 Y MATCHED_MEDIA_VERSION_ID1 Version ID1 of matching Mediaflex media VARCHAR2 Y MATCHED_MEDIA_TITLE Title VARCHAR2 Y MATCHED_MEDIA_FILENAME Filename of matching Mediaflex media VARCHAR2 Y MATCHED_MEDIA_FORMAT Format of matching Mediaflex media VARCHAR2 Y MATCHED_MEDIA_LOCATION Location of matching Mediaflex media VARCHAR2 Y DUE_DATE Date media is required per the Valid From date of the Package DATE Y MATCHED_MEDIA_QC_STATUS QC Status of matching Mediaflex media VARCHAR2 Y PACKAGE_VIDEO_STATUS Video Status of the Package VARCHAR2 Y PACKAGE_IMAGE_STATUS Image Status of the Package VARCHAR2 Y PACKAGE_METADATA_STATUS Metadata Status of the Package VARCHAR2 Y RUNDOWN_STATUS Rundown Status NUMBER N TARGET_SCHEDULE_READY Target Schedule Ready status NUMBER Y

MDD_PACKAGE_MEDIA

> Provides a link between a Package and the media that was selected for it

MDD_PACKAGE_REQUIREMENTS

> Provides summary information about Package Requirements

MDD_POST_EVENT_NOTES

> Provides Event Notes from Make Details of Post tasks.

MDD_PRODUCERS

> Provides a list of producers for a particular task.

MDD_PROGRAMS

> No summary available.

MDD_PROGRAM_FORM

> There may be more than one form for a particular program.  This view provides a list of forms per program.

MDD_RECORD_LABELS

> No summary available.

MDD_RECORD_LABEL_MEDIA_LINKS

> Provides details of links between Record Labels and Media Items.

MDD_RELATED_NAMES

> This view displays other names related to a Name Authority.  It also provides a foreign key allowing a link to the MDD_NAMES view for more details of related name if required.

MDD_RESPONSIBILITIES

> Provides details of responsibilities assigned to a role in the system.

MDD_RESTRICTION_REASONS

> The reason why a Media Item is not accessible to the public

MDD_RIGHTS

> Provides details of Rights Agreements

MDD_SERIES_INDICATORS

> No summary available.

MDD_SERIES_INDICATORS_LNK

> No summary available.

MDD_SPACE_RESERVATION_ITEMS

> Provides overall information about a space reservation item

MDD_SYNONYMS

> This view displays synonyms for a Name Authority.

MDD_TASKS

> No summary available.

MDD_TASKS

> NUMBER Y Page 55 of 80

MDD_TASKS

> This view provides information about a specific task.

MDD_TASKS_OLD

> No summary available.

MDD_TASK_CONFIG

> Provides Task configuration details.

MDD_TASK_EQUIPMENT

> This view provides information about equipment and/or facilities used in a task.

MDD_TASK_EQUIPMENT_ID

> This view is for internal use only.  Use MDD_TASK_EQUIPMENT for details of equipment used in a task.

MDD_TASK_MEDIA

> No summary available.

MDD_TASK_MEDIA

> This view provides information about media associated with a task.

MDD_TASK_OUTPUT_MEDIA

> This view provides information about media associated with a task.

MDD_TASK_SOURCE_MEDIA

> This view provides information about media associated with a task.

MDD_TASK_TIMELINE

> This view provides information about actions associated with a task.

MDD_TASK_VIDEO_MEASUREMENTS

> This view provides information about the video measurements noted for a media item in a task.

MDD_TITLES

> No summary available.

MDD_TITLE_GENRE

> Provides information about the genre of a title.

MDD_TRANSMISSION_SCHEDULE

> Provides information about the transmissions scheduled for a version or media item.

MDD_USERS

> Provides information about Mediaflex users.

MDD_USER_ACCESS_GROUPS

> Provides information about the Schedule Rights for each user.

MDD_USER_SCHEDULE_RIGHTS

> Provides information about the Schedule Rights for each user.

MDD_VERSIONS

> No summary available.

MDD_VERSION_COUNTRY

> Provides details of country(ies) assigned to a version.

MDD_VERSION_LANGUAGE

> Provides details of language(s) assigned to a version.

MDD_VERSION_MATRIX_NUMBER

> Provides details of Matrix number data linked to a version.

MDD_VERSION_PLACE

> No summary available.

MDD_VERSION_PRODUCTION_DATES

> Provides details of production dates linked to a version.

MDD_VERSION_RELATED

> No summary available.

MDD_VERSION_RIGHTS

> Provides details of Rights Agreements

MDD_VERSION_SEGMENTS

> Segment details assigned to Version.

MDD_XML_METADATA

> Provides all XML data held in the system.

