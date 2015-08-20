from annoying.decorators import ajax_request
from django.contrib.auth.decorators import login_required
from seed.utils.api import api_endpoint
from django.core.cache import cache

# TODO The API is returning on both a POST and GET. Make sure to authenticate.


@api_endpoint
@ajax_request
@login_required
def get_cleansing_results(request):
    """
    Retrieve the details of the cleansing script.

    TODO: This code is a placeholder and will require the data to be loaded from either disk, redis, or postgres.
    At the moment I think that the data should be loaded from the redis database, since the cleansing is all or nothing,
    and that the cleansing will be running asynchronously.

    """

    import_file_id = request.GET.get('import_file_id')
    ret = cache.get("cleansing_results__%s" % import_file_id)

    return ret


@api_endpoint
@ajax_request
@login_required
def get_progress(request):
    result = {
        'progress_key': 'some_random_key',
        'progress': 50
    }

    return result