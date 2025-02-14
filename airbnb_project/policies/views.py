from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
import logging

from listings.listing_models import Listing
from policies.services.business_licence_client import BusinessLicenceClient

# Set up logger for this module
logger = logging.getLogger(__name__)


@require_http_methods(["GET"])
def evaluate_policies(request):
    """
       Django view to initiate the policy evaluation
       """
    try:
        logger.info("Processing Listings....")
        print('xxxxxxxxxxxxx')
        for listing in Listing.objects.all():
            print(listing)
            business_licences_number = listing.registration_number
            status = BusinessLicenceClient().get_licence_status(business_licences_number)
            print(status)
            print('--------------')
        return HttpResponse("Evaluating Policies started 2", status=202)
    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Failed to start policy evaluation process: {str(e)}")
        return HttpResponse("Failed to start policy evaluation process", status=500)
