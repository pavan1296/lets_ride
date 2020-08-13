from lets_ride.interactors.storages.storage_interface import StorageInterface
from lets_ride.exceptions.exceptions import UserDoesNotExist
from lets_ride.interactors.presenters.presenter_interface import PresenterInterface


class GetShareRideDetailsInteractor:

    def __init__(self, storage: StorageInterface, presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter

    def get_share_ride_details(self, user_ids: int):

        # TODO : check_user_id_exists_in_user
        try:
            share_ride_details  = self._check_user_details_present_in_user(user_ids=user_ids)
            return self.presenter.share_ride_details_response_details(share_ride_details=share_ride_details)
        except UserDoesNotExist:
            self.presenter.invalid_user_given_returns_error_response()

    def _check_user_details_present_in_user(self, user_ids: int):
        user_dtos = self._get_user_dto_in_user(user_ids=user_ids)
        if not user_dtos:
            raise UserDoesNotExist
        user_dtos = storage.get_share_ride_details_dtos(user_ids=user_ids)

    def _get_user_dto_in_user(self, user_ids: int):
        from lets_ride.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_service = service_adapter.user_service.get_user_details(user_ids=user_ids)
        return user_service
