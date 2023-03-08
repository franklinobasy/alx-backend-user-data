#!/usr/bin/env python3

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    ''' A Class to manage the API authentication.
    '''

    def require_auth(
            self,
            path: str,
            excluded_paths: List[str]
            ) -> bool:
        ''' Required auth
        '''
        if path is None or excluded_paths is None or not excluded_paths:
            return True

        # handle * at end of excluded paths
        if path[-1] == '/':
            path = path[:-1]

        contains_slash = False
        for excluded_path in excluded_paths:
            if excluded_path[-1] == '/':
                excluded_path = excluded_path[:-1]
                contains_slash = True

            if excluded_path.endswith('*'):
                idx_after_last_slash = excluded_path.rfind('/') + 1
                excluded = excluded_path[idx_after_last_slash:-1]

                idx_after_last_slash = path.rfind('/') + 1
                tmp_path = path[idx_after_last_slash:]

                if excluded in tmp_path:
                    return False

            if contains_slash:
                contains_slash = False

        path += '/'

        if path in excluded_paths:
            return False

        return True

    def authorization_header(
            self,
            request=None
            ) -> str:
        '''Auth header
        '''
        if request is None:
            return None

        return request.headers.get('Authorization')

    def current_user(
            self,
            request=None
            ) -> TypeVar('User'):
        ''' Current User
        '''
        request = Flask(__name__)
        return None
