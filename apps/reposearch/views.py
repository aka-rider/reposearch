from http import HTTPStatus
from rest_framework import exceptions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes

from .models import RepoSearch
from .serializers import RepoSearchSerializer
from typing import List, Tuple

import requests
import dateutil.parser


class BadGateway(exceptions.APIException):
    status_code = HTTPStatus.BAD_GATEWAY
    default_detail = 'Upstream service temporarily unavailable, try again later.'
    default_code = 'service_unavailable'


def search_github(q: str):
    """
    Query GitHub API and return the list of found repositeries along with the HTTP status code
    In the case of failure search_github will return non-200 status code
    """
    GITHUB_URL = 'https://api.github.com/search/repositories?q="{}"'
    # route request
    resp = requests.get(GITHUB_URL.format(q))
    if not resp:
        raise BadGateway()
    if resp.status_code != HTTPStatus.OK:
        return Response(None, status=resp.status_code)
    data = resp.json()

    def strptime(tm):
        # native strptime doesn't support timezone information
        return dateutil.parser.isoparse(tm)

    repos = []
    for i in data['items']:
        r = RepoSearch(id=str(i['id']),
                       name=i['name'],
                       description=i['description'],
                       web_url=i['html_url'],
                       created_at=strptime(i['created_at']),
                       updated_at=strptime(i['updated_at']))
        repos.append(r)
    return repos


@api_view(('GET',))
@renderer_classes((JSONRenderer,))
def search(req):
    # retrieve arguments
    q = str(req.GET.get('q')).strip()
    if q == '':
        raise exceptions.ValidationError(
            detail="The mandatory query parameter 'q' is missing",
            code=HTTPStatus.BAD_REQUEST)
    repos = search_github(q)
    serializer = RepoSearchSerializer(repos, many=True)
    return Response(serializer.data, status=HTTPStatus.OK)
