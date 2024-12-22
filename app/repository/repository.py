import discord
import aiosqlite


class UserRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    async def create_user(self, user: discord.User):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                'INSERT INTO users (id, name) VALUES (?, ?)',
                (user.id, user.name)
            )
            await db.commit()

    async def get_user(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            async with db.execute(
                    'SELECT * FROM users WHERE id = ?',
                    (user_id,)
            ) as cursor:
                return await cursor.fetchone()

    async def update_user(self, user: discord.User):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                'UPDATE users SET name = ? WHERE id = ?',
                (user.name, user.id)
            )
            await db.commit()

    async def delete_user(self, user_id: int):
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute(
                'DELETE FROM users WHERE id = ?',
                (user_id,)
            )
            await db.commit()
