from celery import shared_task


@shared_task
def send_notification(user_id, message):
    # Логика отправки уведомления
    print(f"Отправлено уведомление пользователю {user_id}: {message}")
    return f"Notification sent to {user_id}"
