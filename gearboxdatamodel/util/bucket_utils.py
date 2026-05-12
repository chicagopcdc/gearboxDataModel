from fastapi import HTTPException

from gearboxdatamodel.util import status

def get_bucket_name(config):
    # THE S3_TEST_COMPOSE_BUCKET_NAME is used for compose testing and points to
    # a public S3 bucket containting fake mock data. The fake mock data is not used
    # for match condition or match form logic tests, so use the regular test
    # bucket for testing post requests which actually build the match and form logic and
    # post them to the back end.

    if config.DUMMY_S3:
        return config.S3_TEST_COMPOSE_BUCKET_NAME
    elif config.TESTING_S3:
        return config.S3_TEST_BUCKET_NAME
    else:
        return config.S3_BUCKET_NAME


def get_presigned_url(request, key_name, pu_config, method, config):
    bucket_name = get_bucket_name(config)
    presigned_url = ""
    try:
        presigned_url = request.app.boto_manager.presigned_url(
            bucket_name,
            key_name,
            config.S3_PRESIGNED_URL_EXPIRES,
            pu_config,
            method,
            dummy_s3=config.DUMMY_S3,
        )

        if config.DUMMY_S3:
            start_idx = presigned_url.find("Signature")
            end_idx = presigned_url.find("&", start_idx)
            presigned_url = presigned_url[:start_idx] + presigned_url[end_idx + 1 :]
    except Exception as ex:
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            f"Error creating presigned_url for {bucket_name} {ex}.",
        )

    return presigned_url
