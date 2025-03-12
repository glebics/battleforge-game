# 🏆 BattleForge Game  

## 🔥 Карточная PvP-стратегия с сражениями в реальном времени  

**BattleForge** – это онлайн-игра, в которой игроки собирают отряды из уникальных героев, прокачивают их способности и сражаются друг с другом в режиме реального времени.  

## 🚀 Основные особенности  
- 🎴 **Карточная механика** – собирайте коллекцию персонажей с уникальными навыками.  
- ⚔️ **PvP-бои в реальном времени** – управляйте отрядом, используя WebSocket.  
- 🛡 **Прогрессия и кастомизация** – улучшайте героев, открывайте новые скины.  
- 💬 **Чаты и взаимодействие** – общайтесь с друзьями в игровых чатах.  
- ⚡ **Асинхронная архитектура** – высокопроизводительный backend на **Django 5, DRF, Redis, Celery, WebSockets**.  

## 🛠 Стек технологий  
- **Backend**: Django 5, DRF, Channels, PostgreSQL, Redis, Celery.  
- **Frontend**: React Native (поддержка iOS, Android, Web).  
- **Deployment**: Docker, Docker Compose.  

## 🎯 Цель проекта  
Создать динамичную и увлекательную карточную стратегию, сочетающую глубокую тактику и красочные сражения!  

📌 **Статус**: Активная разработка 🔧  

```
battleforge-game
├─ .env
├─ Dockerfile
├─ README.md
├─ battle
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ consumers.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ routing.py
│  └─ tasks.py
├─ battleforge
│  ├─ __init__.py
│  ├─ asgi.py
│  ├─ celery.py
│  ├─ settings.py
│  ├─ urls.py
│  └─ wsgi.py
├─ chat
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ clans
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ docker-compose.yml
├─ entrypoint.sh
├─ heroes
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ inventory
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tests.py
│  └─ views.py
├─ manage.py
├─ notifications
│  ├─ __init__.py
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  │  └─ __init__.py
│  ├─ models.py
│  ├─ tasks.py
│  ├─ tests.py
│  └─ views.py
├─ requirements.txt
└─ users
   ├─ __init__.py
   ├─ admin.py
   ├─ apps.py
   ├─ migrations
   │  └─ __init__.py
   ├─ models.py
   ├─ serializers.py
   ├─ tests.py
   ├─ urls.py
   └─ views.py

```