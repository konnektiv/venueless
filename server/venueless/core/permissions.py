from enum import Enum


class Permission(Enum):
    WORLD_VIEW = "world:view"
    WORLD_UPDATE = "world:update"
    WORLD_ANNOUNCE = "world:announce"
    WORLD_SECRETS = "world:secrets"
    WORLD_API = "world:api"
    WORLD_ROOMS_CREATE = "world:rooms.create"
    ROOM_ANNOUNCE = "room:announce"
    ROOM_VIEW = "room:view"
    ROOM_UPDATE = "room:update"
    ROOM_DELETE = "room:delete"
    ROOM_CHAT_READ = "room:chat.read"
    ROOM_CHAT_JOIN = "room:chat.join"
    ROOM_CHAT_SEND = "room:chat.send"
    ROOM_INVITE = "room:invite"
    ROOM_CHAT_MODERATE = "room:chat.moderate"
    ROOM_BBB_JOIN = "room:bbb.join"
    ROOM_BBB_MODERATE = "room:bbb.moderate"