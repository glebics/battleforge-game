from celery import shared_task


@shared_task
def process_battle_results(battle_id):
    # Логика обработки результатов боя
    print(f"Обрабатываем результаты боя {battle_id}")
    return f"Battle {battle_id} processed"
