# Copyright (c) 2012-2022, Mark Peek <mark@peek.org>
# All rights reserved.
#
# See LICENSE file for full license.
#
# *** Do not modify - this file is autogenerated ***


from . import AWSObject, AWSProperty, PropsDictType, Tags
from .validators import boolean


class Database(AWSObject):
    """
    `Database <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-database.html>`__
    """

    resource_type = "AWS::Timestream::Database"

    props: PropsDictType = {
        "DatabaseName": (str, False),
        "KmsKeyId": (str, False),
        "Tags": (Tags, False),
    }


class S3Configuration(AWSProperty):
    """
    `S3Configuration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-s3configuration.html>`__
    """

    props: PropsDictType = {
        "BucketName": (str, True),
        "EncryptionOption": (str, True),
        "KmsKeyId": (str, False),
        "ObjectKeyPrefix": (str, False),
    }


class ErrorReportConfiguration(AWSProperty):
    """
    `ErrorReportConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-errorreportconfiguration.html>`__
    """

    props: PropsDictType = {
        "S3Configuration": (S3Configuration, True),
    }


class SnsConfiguration(AWSProperty):
    """
    `SnsConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-snsconfiguration.html>`__
    """

    props: PropsDictType = {
        "TopicArn": (str, True),
    }


class NotificationConfiguration(AWSProperty):
    """
    `NotificationConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-notificationconfiguration.html>`__
    """

    props: PropsDictType = {
        "SnsConfiguration": (SnsConfiguration, True),
    }


class ScheduleConfiguration(AWSProperty):
    """
    `ScheduleConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-scheduleconfiguration.html>`__
    """

    props: PropsDictType = {
        "ScheduleExpression": (str, True),
    }


class DimensionMapping(AWSProperty):
    """
    `DimensionMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-dimensionmapping.html>`__
    """

    props: PropsDictType = {
        "DimensionValueType": (str, True),
        "Name": (str, True),
    }


class MultiMeasureAttributeMapping(AWSProperty):
    """
    `MultiMeasureAttributeMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasureattributemapping.html>`__
    """

    props: PropsDictType = {
        "MeasureValueType": (str, True),
        "SourceColumn": (str, True),
        "TargetMultiMeasureAttributeName": (str, False),
    }


class MixedMeasureMapping(AWSProperty):
    """
    `MixedMeasureMapping <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-mixedmeasuremapping.html>`__
    """

    props: PropsDictType = {
        "MeasureName": (str, False),
        "MeasureValueType": (str, True),
        "MultiMeasureAttributeMappings": ([MultiMeasureAttributeMapping], False),
        "SourceColumn": (str, False),
        "TargetMeasureName": (str, False),
    }


class MultiMeasureMappings(AWSProperty):
    """
    `MultiMeasureMappings <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-multimeasuremappings.html>`__
    """

    props: PropsDictType = {
        "MultiMeasureAttributeMappings": ([MultiMeasureAttributeMapping], True),
        "TargetMultiMeasureName": (str, False),
    }


class TimestreamConfiguration(AWSProperty):
    """
    `TimestreamConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-timestreamconfiguration.html>`__
    """

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "DimensionMappings": ([DimensionMapping], True),
        "MeasureNameColumn": (str, False),
        "MixedMeasureMappings": ([MixedMeasureMapping], False),
        "MultiMeasureMappings": (MultiMeasureMappings, False),
        "TableName": (str, True),
        "TimeColumn": (str, True),
    }


class TargetConfiguration(AWSProperty):
    """
    `TargetConfiguration <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-scheduledquery-targetconfiguration.html>`__
    """

    props: PropsDictType = {
        "TimestreamConfiguration": (TimestreamConfiguration, True),
    }


class ScheduledQuery(AWSObject):
    """
    `ScheduledQuery <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-scheduledquery.html>`__
    """

    resource_type = "AWS::Timestream::ScheduledQuery"

    props: PropsDictType = {
        "ClientToken": (str, False),
        "ErrorReportConfiguration": (ErrorReportConfiguration, True),
        "KmsKeyId": (str, False),
        "NotificationConfiguration": (NotificationConfiguration, True),
        "QueryString": (str, True),
        "ScheduleConfiguration": (ScheduleConfiguration, True),
        "ScheduledQueryExecutionRoleArn": (str, True),
        "ScheduledQueryName": (str, False),
        "Tags": (Tags, False),
        "TargetConfiguration": (TargetConfiguration, False),
    }


class MagneticStoreRejectedDataLocation(AWSProperty):
    """
    `MagneticStoreRejectedDataLocation <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorerejecteddatalocation.html>`__
    """

    props: PropsDictType = {
        "S3Configuration": (S3Configuration, False),
    }


class MagneticStoreWriteProperties(AWSProperty):
    """
    `MagneticStoreWriteProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-magneticstorewriteproperties.html>`__
    """

    props: PropsDictType = {
        "EnableMagneticStoreWrites": (boolean, True),
        "MagneticStoreRejectedDataLocation": (MagneticStoreRejectedDataLocation, False),
    }


class RetentionProperties(AWSProperty):
    """
    `RetentionProperties <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-retentionproperties.html>`__
    """

    props: PropsDictType = {
        "MagneticStoreRetentionPeriodInDays": (str, False),
        "MemoryStoreRetentionPeriodInHours": (str, False),
    }


class PartitionKey(AWSProperty):
    """
    `PartitionKey <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-partitionkey.html>`__
    """

    props: PropsDictType = {
        "EnforcementInRecord": (str, False),
        "Name": (str, False),
        "Type": (str, True),
    }


class Schema(AWSProperty):
    """
    `Schema <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-timestream-table-schema.html>`__
    """

    props: PropsDictType = {
        "CompositePartitionKey": ([PartitionKey], False),
    }


class Table(AWSObject):
    """
    `Table <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-timestream-table.html>`__
    """

    resource_type = "AWS::Timestream::Table"

    props: PropsDictType = {
        "DatabaseName": (str, True),
        "MagneticStoreWriteProperties": (MagneticStoreWriteProperties, False),
        "RetentionProperties": (RetentionProperties, False),
        "Schema": (Schema, False),
        "TableName": (str, False),
        "Tags": (Tags, False),
    }
