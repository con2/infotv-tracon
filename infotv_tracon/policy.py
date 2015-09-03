from infotv.policy import BasePolicy


class TraconPolicy(BasePolicy):
    def get_event_slug(self, request, slug):
        return slug

    def can_edit_slides(self, request):
        return request.user.is_staff

    def can_post_datum(self, request):
        return request.user.is_staff
