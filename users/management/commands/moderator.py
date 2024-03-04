from django.contrib.auth.models import Group, Permission
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        manager_group = Group.objects.create(name='moderator')

        perm_1 = Permission.objects.get(content_type__app_label='study',
                                        content_type__model='course',
                                        codename='view_course')
        perm_2 = Permission.objects.get(content_type__app_label='study',
                                        content_type__model='course',
                                        codename='change_course')
        perm_3 = Permission.objects.get(content_type__app_label='study',
                                        content_type__model='lesson',
                                        codename='view_lesson')
        perm_4 = Permission.objects.get(content_type__app_label='study',
                                        content_type__model='lesson',
                                        codename='change_lesson')

        manager_group.permissions.add(perm_1)
        manager_group.permissions.add(perm_2)
        manager_group.permissions.add(perm_3)
        manager_group.permissions.add(perm_4)
