# attendance/apps.py

from django.apps import AppConfig


class AttendanceConfig(AppConfig):
    name = 'attendance'

    def ready(self):
        import attendance.signals  # 시그널 임포트
